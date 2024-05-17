### Entity Relationship / Schema:

![schema](https://github.com/artc95/dbtBigQuery/blob/inventory_dashboard/diagrams/schema.png?raw=true)

### Architecture:

![architecture](https://github.com/artc95/dbtBigQuery/blob/inventory_dashboard/diagrams/architecture.png?raw=true)


### Setup to run locally (using dbt Core)
- Create virtual environment and activate it
```
python3 -m venv <name of virtual environment> # create a virtual environment
e.g. python3 -m venv dbtBigQuery_venv
```

- **NOTE:** This project uses BigQuery as data warehouse. See [setup instructions](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup) for other data warehouses.

- Install project `requirements.txt` into virtual environment:
    - in `requirements.txt`, replace `dbt-postgres` adapter package if not using Postgres
```
python3 -m pip install -r requirements.txt # install the project's requirements
# if above doesn't work, run without python3 -m...
pip install -r requirements.txt
```

- Setup `profiles.yml` to connect to data warehouse
    - DO NOT VERSION CONTROL SENSITIVE INFO! see [`profiles.yml` best practices](https://docs.getdbt.com/docs/core/connect-data-platform/connection-profiles)
    - if not using Postgres, see [setup instructions](https://docs.getdbt.com/docs/core/connect-data-platform/postgres-setup) for other data warehouses

- (optional) Run `dbt debug`, expect final message `All checks passed!` 
    - ref: (dbt-labs/jaffle-shop)[https://github.com/dbt-labs/jaffle-shop/tree/main] project, project skeleton from results of "initialize project" in dbt Cloud

### Using the starter project

Try running the following commands:
- dbt run
- dbt test
