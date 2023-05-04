import requests
from datetime import datetime

PIX_USER = 
PIX_TOKEN = 

GRAPH_ID = "walktracker1"
GRAPH_NAME = "Walk_Tracker"
GRAPH_UNIT = "meter"
GRAPH_TYPE = "int"
GRAPH_COLOR = "ichou"

TODAY = datetime.today().strftime("%Y%m%d")
PIX_ENDPOINT = "https://pixe.la"
PIX_USER_ENDPOINT = f"{PIX_ENDPOINT}/v1/users"
graph_url = f"{PIX_USER_ENDPOINT}/{PIX_USER}/graphs"
my_graph_url = f"{graph_url}/{GRAPH_ID}"
my_graph_update_url = f"{my_graph_url}/{TODAY}"
user_params = {
    "token": PIX_TOKEN,
    "username": PIX_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# 1 create a user
# response =requests.post(url=PIX_USER_ENDPOINT, json=user_params)
# print(response.text)

# 2create the graph
graph_param = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": GRAPH_UNIT,
    "type": GRAPH_TYPE,
    "color": GRAPH_COLOR,
}
graph_header = {
    "X-USER-TOKEN": PIX_TOKEN
}

# response=requests.post(url=graph_url, json=graph_param, headers=graph_header)
# print(response.text)

# 
pixel_param = {
    "quantity": "130",
}
response = requests.put(url=my_graph_update_url, json=pixel_param, headers=graph_header)
print(response.text)

# delete value
response = requests.delete(url=my_graph_update_url, headers=graph_header)
print(response.text)
