VIRTUALENV=virtualenv
PEP8=pep8

.PHONY: clear test

.env: requirements.txt
	rm -fr $@ && $(VIRTUALENV) $@ && \
	. $@/bin/activate && \
	pip install -r $^ && \
	deactivate

.testenv: requirements.txt requirements_test.txt
	rm -fr $@ && $(VIRTUALENV) $@ && \
	. $@/bin/activate && \
	pip install -r $(word 1,$^) && pip install -r $(word 2,$^) && \
	deactivate

test: .testenv 
	. $^/bin/activate && $(PEP8) src --max-line-length=109 && deactivate
	. $^/bin/activate && PYTHONPATH=src py.test --cov=src --ds=growbots.settings -v && deactivate

clear:
	find . -name "*.pyc" -delete
	rm -fr .env .testenv

	
