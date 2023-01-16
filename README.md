# ChatGPT Case Study

### Installation:

Clone the repository and activate your virtual environment:

```
pip install -r requirements.txt
```

To apply migrations

```
python manange.py migrate
python manange.py makemigrations
```

To create mongodb database with docker run:

```
docker run -d  --name mongodb  -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongo -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

To run:
```
python manage.py runserver
Go to browser and paste "http://127.0.0.1:8000/" in search bar
```

Test video:


https://user-images.githubusercontent.com/77622078/212668221-cb48c7d4-a792-4383-b921-c7c1afa15a21.mp4




To check mongodb database run commands:
```
mongosh 
```

To get list of all databases
```
show databases 
```

To use database "chat_app"
```
use chat_app
```

To get all collections of selected database
```
show collections
```

To find data of collection "chat_app_chat"
```
db.chat_app_chat.find()
```

