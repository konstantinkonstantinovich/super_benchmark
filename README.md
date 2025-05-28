# super_benchmark

## Getting started
These instructions are valid for Mac or Linux.

You need to install following software:
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

After docker and docker compose installed:
* To launch project run `make setup`
* Edit `.env`, set the values you need
* Run the server `make run`
* `make help` - list of all commands

## Tests
To run the tests, use the following command
```bash
make test
```

## Project resources
Health check http://0.0.0.0:8000/healthcheck
API docs http://0.0.0.0:8000/docs
