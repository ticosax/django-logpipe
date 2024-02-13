# Create the .po and .mo files used for i18n
.PHONY: translations
translations:
	cd src/logpipe && \
	django-admin makemessages -a && \
	django-admin compilemessages

.PHONY: install_precommit
install_precommit:
	pre-commit install

.PHONY: test_precommit
test_precommit: install_precommit
	pre-commit run --all-files

.PHONY: docs_serve
docs_serve:
	DJANGO_SETTINGS_MODULE=sandbox.settings poetry run mkdocs serve --strict

.PHONY: docs_build
docs_build:
	DJANGO_SETTINGS_MODULE=sandbox.settings poetry run mkdocs build --strict

docs: docs_build
	rm -rf public/ && \
	mkdir -p public/ && \
	cp -r build/mkdocs/* public/
