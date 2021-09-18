install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

compile:
	pip-compile requirements.in

compile-dev:
	pip-compile requirements-dev.in

upgrade:
	pip-compile --upgrade requirements.in

upgrade-dev:
	pip-compile --upgrade requirements-dev.in
