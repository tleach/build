.PHONY: dev-env clean test nose-tests pyvows-tests env all update


export gcenv := local

all: env

env: env/.requirements

dev-env: env env/.dev_requirements

env/.requirements: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install -Ur requirements.txt
	touch env/.requirements

env/.dev_requirements: dev_requirements.txt
	. env/bin/activate; pip install -Ur dev_requirements.txt
	touch env/.dev_requirements

update: clean env

clear-test-results:
	rm -rf ./test-results
	mkdir -p ./test-results
	
nose-tests: dev-env clear-test-results
	. env/bin/activate; nosetests --with-xunit --xunit-file=./test-results/TEST-python.xml -e test

pyvows-tests: dev-env clear-test-results
	. env/bin/activate; pyvows test -x -f ./test-results/TEST-pyvows.xml

clean:
	rm -f env/.requirements
	rm -f env/.dev_requirements

test: nose-tests pyvows-tests

