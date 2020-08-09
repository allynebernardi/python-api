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
    }'
```
```
heroku login
```
``` 
heroku git:remote --app berry-python-api
```
```
heroku run pip freeze
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