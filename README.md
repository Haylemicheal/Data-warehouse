
## Overview
A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. The company is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. 

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
- .github/workflows- Contains yml configration file of github acyion
- .dvc: Data versioning related configration and files
- .travis.yml: Contains config file for travis ci/cd 

## Author

- [Haylemicheal Berihun](https://www.linkedin.com/in/haylemicheal-berihun-a20320aa)
- 10academy team
