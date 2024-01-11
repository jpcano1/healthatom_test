## **Healthatom Technical Test**

## **Project Structure**

```
.
|-- dev
|   `-- tools.sh
|-- docker-compose.yml
|-- Dockerfile
|-- Makefile
|-- poetry.lock
|-- poetry.toml
|-- pyproject.toml
|-- README.md
|-- setup.cfg
|-- src
|   |-- app
|   |   |-- client.py
|   |   |-- database
|   |   |   |-- db.py
|   |   |   |-- __init__.py
|   |   |   `-- operations.py
|   |   |-- __init__.py
|   |   `-- models
|   |       |-- db_models.py
|   |       |-- __init__.py
|   |       `-- schemas.py
|   |-- __init__.py
|   `-- main.py
`-- tests
    |-- app
    |   |-- __init__.py
    |   `-- test_client.py
    |-- conftest.py
    |-- __init__.py
    `-- test_main.py
```

## **Local Setup**

### Build project using poetry.
- **Don't forget to set the variables in the .env file!**
- For this you must have poetry installed, version 1.6.1
- Execute `poetry install`
- Deploy PostgreSQL database with command `docker-compose up -d postgres`
- Execute commands with Makefile! Just use this one `make retrieve_currency CURRENCY=USD`
or you can change the currency value by `EUR`.
- Enjoy!

## **Run with docker**
- **Don't forget to set the variables in the .env.local file!**
- Run by executing the command `docker-compose up`
- You can change the currency values in the docker-compose.yml file
- Enjoy!

## **Disclaimer**
- **API USED**: [Banco Central de Chile](https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx)

