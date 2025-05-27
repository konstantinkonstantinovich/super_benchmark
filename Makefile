# Define variables
DOCKER_COMPOSE = docker compose

.PHONY: setup
setup: ## Set up env file, pre commit hook and build Docker containers
	cp .env.example .env
	pip install pre-commit
	pre-commit install
	$(DOCKER_COMPOSE) build

.PHONY: run
run: ## Server startup
	$(DOCKER_COMPOSE) up

.PHONY: help
help: ## Show list of commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
