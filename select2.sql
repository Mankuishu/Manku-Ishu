SELECT e.*, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department = d.department_id;
