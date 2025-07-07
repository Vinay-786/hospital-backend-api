# Setting up the project locally

This project uses uv package manager (rust btw) to manage its dependencies and env but pip should work just fine.

## Before you creating virtual env and install dependencies, snip up a postgresql instance using docker

### Creating a postgres docker
```bash
  sudo docker run --name healthcare \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=passwd \
  -e POSTGRES_DB=healthcare \
  -p 5432:5432 \
  -d postgres
```

### You can poke around the same docker instance's tables and schema for debug purpose like this
```bash
  sudo docker exec -it healthcare psql -U admin -d healthcare
```

### create an .env file in the root directory of the django-project (healthcarebackend)
- Add the credentials

DB_NAME=healthcare
DB_USER=admin
DB_PASSWORD=passwd
DB_HOST=localhost
DB_PORT=5432


## setting up using uv
- Make sure you've installed uv
- Create a virtual env using <code> uv venv </code>
- Source the venv using <code> source ./.venv/bin/activate </code>
- To install dependencies run <code> uv pip install -r pyproject.toml </code>


## setting up using pip
- Make sure you've installed pip and venv
- Create a virutal env using <code> python3 -m venv .venv </code>
- Source the venv using <code> source ./.venv/bin/activate </code>
- To install dependencies run <code>pip install -r pyproject.toml </code>

## cd into the root directory (healthcarebackend ) and run:
```bash
  python manage.py runserver
```
