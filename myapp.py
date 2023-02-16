import requests
import json
URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id = None):
    
    # data = {}
    # if id is not None:
    #     data = {'id': id}
    # json_data = json.dumps(data)
    r = requests.get(URL,verify=False)
    data = r.json()
    print(data)

get_data()