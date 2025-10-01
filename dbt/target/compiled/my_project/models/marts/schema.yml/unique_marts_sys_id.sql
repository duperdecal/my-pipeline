
    
    

select
    sys_id as unique_field,
    count(*) as n_records

from "airflow"."analytics"."gold_layer"
where sys_id is not null
group by sys_id
having count(*) > 1


