# python-api

**Setup:**

```python user.py run```

**POST:**
```localhost:8000/users```

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
python3 -m venv env
```
```
source env/bin/activate
```
```
pip freeze > requirements.txt
```
```
gunicorn app:app
```
```
git push heroku master
```
```
heroku logs --tail --app berry-python-api
```

https://berry-python-api.herokuapp.com/