https://www.1point3acres.com/bbs/thread-540456-1-1.html
```
SQL题
1. write a query to return the top10 customer          
2. customer rev by product in 2019 Sum &left join
3. # of customer by month by product 同上，稍微有点记不清了
```

    

1. top10 customer  Top 10 or Dense_Rank()  

table t1:
id | val | 
1  |  10
2  |  7
3  |  18
4  |  5
...

Method A: DENSE_RANK()
http://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/       
# Write your MySQL query statement below
 
SELECT
    val,
    DENSE_RANK() OVER (
        ORDER BY val
    ) my_rank
FROM
    t1
LIMIT 10
;

Method B: ORDER BY()
# Write your MySQL query statement below    
 
SELECT
    val,
FROM
    t1
ORDER BY 1 DESC
LIMIT 10
;



