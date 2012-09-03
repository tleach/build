import re

def read_reqs():
    """Reads requirements from requirements.txt

    This method reads the list of dependencies from the local requirements.txt file
    (if present) and returns these as a list suitable to be supplied to setup.py's
    install_requires parameter. 
    """
    try:
        f = open('requirements.txt').readlines()
        reqs = []
        for line in f:
            # Return anything which is an interupted line of non-whitespace chars
            if re.match(r"\S+$", line):
                reqs.append(line.strip())

            # If we find any urls, extract the egg info and include
            elif re.search(r'git\+ssh', line):
                reqs.append(line.strip().split('#')[1].split('=')[1])
                

        return reqs
    except IOError:
        # File does not exist, return an empty list
        return []

def read_dep_links():
    """Reads dependency links from requirements.txt

    This method reads the list of dependencies from the local requirements.txt file
    (if present) and returns a list of URLS which can be supplied to setup.py's 
    dependency_links argument to be used to satisfy eg dependencies."""
    try:
        f = open('requirements.txt').readlines()
        reqs = []
        for line in f:
            if re.search(r'git\+ssh', line):
                reqs.append(line.strip().lstrip('-e').lstrip() + '-dev')
                
        return reqs
    except IOError:
        # File does not exist, return an empty list
        return []
