import requests

base_urls = {
    'us': 'https://api.engagespot.co/v3',
    'eu': 'https://api-eu.engagespot.co/v3'
}

class Engagespot(object):
    def __init__(self,
                 base_url="https://api.engagespot.co/v3",
                 api_key=None,
                 api_secret=None,
                 data_region="us"
                 ) -> None:
        if base_url:
            self.base_url = base_url

        if data_region:
            self.base_url = base_urls[data_region]
        
        if api_key:
            self.api_key = api_key
        else:
            raise ValueError('api_key is required')
        
        if api_secret:
            self.api_secret = api_secret
        else:
            raise ValueError('api_secret is required')

    def send(self,send_request):

        headers = {
            "Content-Type": "application/json",
            "X-ENGAGESPOT-API-KEY": self.api_key,
            "X-ENGAGESPOT-API-SECRET": self.api_secret
        }

        try:
            response = requests.post(self.base_url+"/notifications", headers = headers, json = send_request)
        except Exception as ex:
            error = ex.__str__()
            return {
                "success": False,
                "message": error,
            }
        else:
            response_code = response.status_code
            if response_code == 202:
                return {
                    "success": True,
                    "message": response.json()
                }
            else:
                return {
                    "success": False,
                    "message": response.json()
                }
            
    def create_or_update_user(self, identifier, profile=None):

        if identifier == None:
            raise ValueError('identifier is required')

        headers = {
            "Content-Type": "application/json",
            "X-ENGAGESPOT-API-KEY": self.api_key,
            "X-ENGAGESPOT-API-SECRET": self.api_secret
        }

        try:
            url = self.base_url+"/users/"+identifier;
            response = requests.put(url, headers=headers, json=profile)
        except Exception as ex:
            error = ex.__str__()
            return {
                "success": False,
                "message": error,
            }
        else:
            response_code = response.status_code
            if response_code == 200:
                return {
                    "success": True,
                    "message": response.json()
                }
            else:
                return {
                    "success": False,
                    "message": response.json()
                }


