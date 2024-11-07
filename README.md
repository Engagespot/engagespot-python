This is the official Python library for communicating with Engagespot REST API. Send multi-channel notifications from your python app.

# Installation

```
pip install engagespot
```

# Prerequisites
You need Engagespot API KEY and API SECRET from your [dashboard](https://console.engagespot.co) to get started. If you don't have one, just get one for free.

# Creating or updating a user

Before you can send a notification, you should create the user (recipient) profile in Engagespot.

```python
from engagespot import Engagespot

client = Engagespot(api_key="ENGAGESPOT_API_KEY", api_secret="ENGAGESPOT_API_SECRET", data_region="us")

user_profile = {
    "name" : "Python User",
    "email" : "python@engagespot.co",
    "phoneNumber": "+1620000000"
}

response = client.create_or_update_user("user-identifier");
```

<i>`data_region` can be either `us` or `eu` depending on your workspace data region</i>

# Triggering a workflow

The easiest way to send notifications in Engagespot is by creating message workflows in [Engagespot console](https://console.engagespot.co) and trigger it using this Python library.

```python
from engagespot import Engagespot

client = Engagespot(api_key="ENGAGESPOT_API_KEY", api_secret="ENGAGESPOT_API_SECRET")

send_request = {
    "notification": {
        "workflow":{
            "identifier":"welcome-message-workflow"
        }
    },
    "sendTo":{
        "recipients": ["user-identifier"]
    }
}
    
response = client.send(send_request)
```

Refer [Engagespot REST API Docs](https://docs.engagespot.co/docs/rest-api) to get the list of all supported parameters.


# Detailed Guide
Read [Engagespot docs](https://docs.engagespot.co/docs/introduction/quick-start) to learn how to build and send notification workflows.