%sql
SHOW DATABASES LIKE "sbp*";

SHOW TABLES IN sbp_b900_public_work;

CREATE TABLE sbp_b900_public_work.test_persons_databricks (
  id int,
  name string,
  age int,
  favColor string
);

SHOW GRANT ON sbp_b900_public_work.test_persons_databricks;

ALTER TABLE sbp_b900_public_work.test_persons_databricks owner to `AAD-GRP-bdap-sbx-dl-b900-public-contributor`;

INSERT INTO sbp_b900_public_work.ttest_persons_databricks VALUES
  (1, "Alice Hammond", 38, "Blue"),
  (2, "Joy Meyer", 20, "Red"),
  (3, "Frieda Schmidt", 59, "Blue"),
  (4, "Dong Seok", 44, "Blue"),
  (5, "Camila Castillo", 32, "Green"),
  (6, "Alba Cantu", 27, "Red");
  
SELECT * FROM sbp_b900_public_work.test_persons_databricks;

SELECT 
  favColor, 
  COUNT(*), 
  AVG(age) 
FROM 
  sbp_b900_public_work.test_persons_databricks
GROUP BY
  favColor;

DROP TABLE sbp_b900_public_work.test_persons_databricks;