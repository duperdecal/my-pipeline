select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    sys_id as unique_field,
    count(*) as n_records

from "airflow"."analytics"."gold_layer"
where sys_id is not null
group by sys_id
having count(*) > 1



      
    ) dbt_internal_test