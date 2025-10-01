select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select cust_key
from "airflow"."analytics"."silver_layer"
where cust_key is null



      
    ) dbt_internal_test