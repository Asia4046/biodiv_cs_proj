# BIODIVERSITY ZOO MANAGEMENT SYSTEM USING Python & MySQL
## Setup
This readme assumes that mysql has already been installed in your system and the root user with password has been initalized.

### Initialize connection to the database:

- In main.py:
```python
    dataBase = mysql.connector.connect(
    host = "localhost",
    user = "username", # Enter the configured username (most probably root)
    passwd = "passwd", # Enter the configured password
    )
```

