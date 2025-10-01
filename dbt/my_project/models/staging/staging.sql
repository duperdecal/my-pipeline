{{config( materialized = 'table', alias= "silver_layer") }}

select 
cst_id::bigint as sys_id,
trim(cst_key) as cust_key,
trim(cst_firstname) as first_name,
trim(cst_lastname) as last_name,
case when cst_marital_status = 'M' then '1' else '0'::boolean
end as marriage,
cst_gndr as gender,
cst_create_date::date as create_date
from {{ source('raw','raw_data')}}
where cst_id is not null and cst_key is not null