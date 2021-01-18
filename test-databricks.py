# Databricks notebook source
# MAGIC %sql
# MAGIC --Comment 
# MAGIC SHOW DATABASES LIKE "sbp*";

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN sbp_b900_public_work;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE sbp_b900_public_work.test_persons_databricks (
# MAGIC   id int,
# MAGIC   name string,
# MAGIC   age int,
# MAGIC   favColor string
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW GRANT ON sbp_b900_public_work.test_persons_databricks;
# MAGIC ALTER TABLE sbp_b900_public_work.test_persons_databricks owner to `AAD-GRP-bdap-sbx-dl-b900-public-contributor`;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sbp_b900_public_work.ttest_persons_databricks VALUES
# MAGIC   (1, "Alice Hammond", 38, "Blue"),
# MAGIC   (2, "Joy Meyer", 20, "Red"),
# MAGIC   (3, "Frieda Schmidt", 59, "Blue"),
# MAGIC   (4, "Dong Seok", 44, "Blue"),
# MAGIC   (5, "Camila Castillo", 32, "Green"),
# MAGIC   (6, "Alba Cantu", 27, "Red");  
# MAGIC SELECT * FROM sbp_b900_public_work.test_persons_databricks;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   favColor, 
# MAGIC   COUNT(*), 
# MAGIC   AVG(age) 
# MAGIC FROM 
# MAGIC   sbp_b900_public_work.test_persons_databricks
# MAGIC GROUP BY
# MAGIC   favColor;
# MAGIC   

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE sbp_b900_public_work.test_persons_databricks;