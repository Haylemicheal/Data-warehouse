
## Overview
A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. The company is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. 
![Project design diagram](https://www.google.com/url?sa=i&url=https%3A%2F%2Fturbofuture.com%2Fmisc%2FTraffic-Data-Pipeline-And-Warehouse&psig=AOvVaw0z3AvrEQGUel3PSpkA9JIV&ust=1664122768836000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJD6_dDqrfoCFQAAAAAdAAAAABAD)
The data warehouse take into account future needs, organise data such that a number of downstream projects query the data efficiently. I use the Extract Load Transform (ELT) framework using DBT. The ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis. 




## Objectives

Building data warehouse techstack
- Consisting of
    
    - A “data warehouse” (PostgresQL)
    - An orchestration service (Airflow)
    - An ELT tool (dbt)
    - A reporting environment (redash)
- Set it up locally using 
    - Fully dockerized 

##  Dataset
- [Data(pNEUMA dataset )](https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330)
## Project Structure
- data: Contains the dataset
- dbt: Contains dbt related files
- airflow: contains airflow related files
- scripts: Contains script codes
- logs: contains log files
- tests: Unit test files
## Installation

    1. Clone the repository
```bash
  $ git clone https://github.com/Haylemicheal/Data-warehouse
```
    2. Navigate to the directory
```bash
  $ cd Data-warehouse
```
### Run Airflow
    1. Navigate to the airflow folder
```bash
  $ cd airflow
```
    2. Run the airflow
```bash
  $ docker-compose up airflow-init 
  $ docker-compose up
```
    3. View the dashboard
```bash
  $ localhost:8080
```
### Run dbt
    1. Navigate to the dbt folder
```bash
  $ cd dbt_traffic
```
    2. Run the dbt
```bash
  $ dbt init
  $ dbt run 
  $ dbt docs generate
  $ dbt docs serve --port=port number
```
    3. View the dashboard
```bash
  $ localhost:port number
```
### Run Redash
    1. Navigate to the redash folder
```bash
  $ cd redash
```
    2. Run the redash
```bash
  $ docker-compose up
```
    3. View the dashboard
```bash
  $ localhost:port number
```
### Sample visualization from Redash
![Fastest Vehicles Table](https://github.com/Haylemicheal/Data-warehouse/blob/main/images/fastvehicle%20table.png)
![Fastest Vehicles Bar graph](https://github.com/Haylemicheal/Data-warehouse/blob/main/images/fast%20vehicles%20bar.png)
![Distribution of the Vehicles table](https://github.com/Haylemicheal/Data-warehouse/blob/main/images/dist_table.png)
![Distribution of the Vehicles piechart](https://github.com/Haylemicheal/Data-warehouse/blob/main/images/piechart.png)
    
## Author

- [Haylemicheal Berihun](https://www.linkedin.com/in/haylemicheal-berihun-a20320aa)
- 10academy team
