This is the official Python library for communicating with Engagespot REST API. Send multi-channel notifications from your node app.

# Installation

```
pip install engagespot-python
```

# Prerequisites
You need Engagespot API KEY and API SECRET from your [dashboard](https://portal.engagespot.co) to get started. If you don't have one, just get one for free.

# Sending a notification

```python
from engagespot import Engagespot


client = Engagespot(api_key="ENGAGESPOT_API_KEY", api_secret="ENGAGESPOT_API_SECRET")

send_request = {
    "notification": {
        "title":"Test from Python library🔥"
    },
    "recipients":["uid_123456"]
}
    
response = client.send(send_request)
```

Refer [Engagespot REST API Docs](https://documentation.engagespot.co/docs/rest-api) to get the list of all supported parameters.

# Creating or updating a user

```python
user_profile = {
    "name" : "Python User",
    "email" : "python@engagespot.co"
}

response = client.create_or_update_user("pythonuser2");
```