# python-api

**Setup:**

```python user.py run```

**POST:**
```localhost:5000/users```

**Payload:**
```
   {
        "name": "aniela",
        "email": "bla"
    }
```
```
heroku login
```
``` 
heroku git:remote --app berry-python-api
```
```
pip freeze > requirements.txt

```
```
pipenv install
```
```
virtualenv venv
```
```
git push heroku master
```
```
heroku logs --tail --app berry-python-api
```

https://berry-python-api.herokuapp.com/


## Database
```
docker run --name db -e POSTGRES_USER=postgress -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=apiDB -d -p5432:5432 postgres
```