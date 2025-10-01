select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sys_id
from "airflow"."analytics"."gold_layer"
where sys_id is null



      
    ) dbt_internal_test