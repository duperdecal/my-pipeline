{{ config(materialized='table', alias='gold_layer') }}

select sys_id, 
cust_key,
first_name,
last_name,
marriage,
gender,
cast(create_date::date-interval '2 years' as date) as create_date
from (select 
row_number() over(partition by sys_id order by sys_id) rn,
*
from {{ ref('staging') }})t
where rn = 1 and first_name is not null and gender is not null