from engagespot import Engagespot


client = Engagespot(api_key="y57uye3rxiqmt350r5shi", api_secret="2o1dqq5s5hqda7o7mrlr38j6hcfi34i3637dcjiehje8011")

send_request = {
    "notification": {
        "title":"Test from Python library🔥"
    },
    "recipients":["uid_123456"]
}
    
#response = client.send(send_request)

user_profile = {
    "name" : "Python User",
    "email" : "python@engagespot.co"
}

user_response = client.create_or_update_user("pythonuser2");

print(user_response);