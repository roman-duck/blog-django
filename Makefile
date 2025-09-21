PYTHON ?= python
MANAGE = $(PYTHON) manage.py

run:
	@$(MANAGE) runserver

migrate:
	@$(MANAGE) migrate

migrations:
	@$(MANAGE) makemigrations

superuser:
	@$(MANAGE) createsuperuser

shell:
	@$(MANAGE) shell
