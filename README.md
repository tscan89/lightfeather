# Coding Challenge

## Install:

You can use a virtual environment (conda, venv, virtualenvwrapper, etc):
```
mkvirtualenv lightfeather
```

Pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running code

### Spin up webserver
```
python manage.py runserver 23456
```

### Example Request
Use an API tool (such as postman) or CURL
```
curl -d '{"shift":2, "message":"poop"}' -H "Content-Type: application/json" -X POST http://localhost:23456/api/encode
```

### Example Response
```
{"EncodedMessage":"rqqr"}
```


