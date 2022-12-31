# Akaraike-API
-------

## Introduction

Akaraike-API is an app designed to assist developers create passwords using different character combination, check password strength and check against the database for week passwords.


## Getting Started

### Pre-requisites and Local Development
- Developers who wish to contribute to this project should have Python3, pip and node installed on their local machines. Here is a link to download Python3 `www.python.org/downloads`.

- Install *pipenv* by running ```pip install --user pipenv``` on your terminal or command line
- When installed run ```pipenv install``` in the Akaraike folder to install dependencies.

- To run the application run the following commands:
    ```
    export FLASK_APP=app.py
    export FLASK_DEBUG=True
    flask run
    ```
The application is run on `http://127.0.0.1:5000/`


## API Reference
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`. 
- Authentication: This application does require authentication and uses JSON Web Token (JWT).

### Error Handling

Akaraike-API uses conventional HTTP response code to indicate success and failure of an API request, errors are returned as JSON objects in the format

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

Here are some status codes;
- 200 - Ok - Everything works as expected.
- 400 - Bad Request - The request was not accepted which may be due to wrong or unaccepted request.
- 401 - Unauthorized - The client request has not been completed because it lacks valid authentication credentials for the requested resource
- 404 - Not Found - The requested resource does not exist.
- 405 - Method not Allowed - This can occure when the wrong method is used on a resource.
- 422 - Unprocessable - This can occur when the request cannot be processed.

### Endpoint Library

### `GET '/'`

  -Returns a success key of true
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/`
```
{
    "success": True
}
```

### `POST '/register'`


  -Endpoint is used to create new users in the database.
  
  -Body should contain an email(string), username(string) and password(string).
  
  -Returns a success key of true and message
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/register -X POST -H "Content-Type: application/json" -d '{"first_name": "Eiyzy","last_name": "Eusy","email": "test005@test.com","username": "Bee5","password": "test5"}'`

```
{
    "message": "okyouna created",
    "success": true
}
```

### `POST '/login'`

  -Body should contain a username(string) and password(string)

  -Returns a success key of true and message of login successful
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/login -X POST -H "Content-Type: application/json" -d '{"username": "Bee5","password": "test5" }'`

```
{
    "message": "Login successful",
    "success": true
}
```

### `GET '/alpha'`

  -Used to generate password with uppercase and lowercase characters

  -Returns a success key of true, the generated password and password strength 
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/alpha

```
{
    "password": "PLrqLENdulpSAzutLPRquuBwDTAaqAQpofDcQ",
    "strength score": 6,
    "success": true
}
```

### `GET '/alphanumeric'`

  -Used to generate password with uppercase, lowercase and numeric characters

  -Returns a success key of true, the generated password and password strength 
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/alphanumeric

```
{
    "password": "QzzG69gIz5HU648F6Fzy31DGQv6GWtRfgR7",
    "strength score": 8,
    "success": true
}
```

### `GET '/alphanumx'`

  -Used to generate password with uppercase, lowercase, numeric and special characters

  -Returns a success key of true, the generated password and password strength 
  
  -Request arguments: None
  
  
Example: `curl http://127.0.0.1:5000/alphanumx

```
{
    "password": "\\30xCx)FC6UA",
    "strength score": 10,
    "success": true
}
```


### Authors
- Celestine Okonkwo

### Acknowledgment
