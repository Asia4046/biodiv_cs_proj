# BIODIVERSITY ZOO MANAGEMENT SYSTEM USING Python & MySQL
## Setup
This readme assumes that mysql has already been installed in your system and the root user with password has been initalized.

### Initialize connection to the database:

In main.py:
```python
    dataBase = mysql.connector.connect(
    host = "localhost",
    user = "username", # Enter the configured username (most probably root)
    passwd = "passwd", # Enter the configured password
    )
```
## Usage
### fetch_where() funtion:
```python
    fetch_where(field, op, payload)
```
This program corresponds to this SQL code
```sql
    SELECT * FROM ZOOMANAGE WHERE "field" "op" "payload"
``` 
for example if i want to display all records whose zoo count is more than 200 then,
```python
    fetch_where("ZOO_COUNT", ">", "200")
```
i.e
```sql
    SELECT * FROM ZOOMANAGE WHERE ZOO_COUNT > 200
```

