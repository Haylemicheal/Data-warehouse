{{ config(materialized='view') }}

with source_data as (

    select * from vehicles where traveled_distance>450

)

select *
from source_data