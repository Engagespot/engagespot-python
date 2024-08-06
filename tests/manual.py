from engagespot import Engagespot


client = Engagespot(api_key="ecnp1p3pqpgdh4mb5n0j6", api_secret="7gpdsngf968a9ngh9jfot2je66eh8c7f132933a038e491a")

send_request = {
    "notification": {
        "workflow":{
            "identifier":"plan-expiry-notification"
        }
    },
    "sendTo":{
        "recipients": ["user-001"]
    }
}
    
response = client.send(send_request)

user_profile = {
    "name" : "Python User",
    "email" : "python@engagespot.co"
}

user_response = client.create_or_update_user("pythonuser2",profile=user_profile);

print(user_response);