SELECT 
    a.name,
    SUM(o.total_amt_usd) AS fatturato
FROM orders o
JOIN accounts a 
ON o.account_id = a.id
GROUP BY a.name
ORDER BY fatturato DESC;
