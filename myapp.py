import requests 
import json
URL ="http://127.0.0.1:8000/bkapi/"


def get_data(id=None):
    data ={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    r= requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

get_data() #Enter Id values to get particular id otherwise it retrives the all records
'''
'''
#Field Level Validation
def post_data():
    data={
        'name':'The Guide',
        'desc':'The novel is based on Malgudi',
        'author':'R. K. Narayan',
        'price': 205
    }
    json_data = json.dumps(data)
    r= requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

post_data()
'''
'''
#Object  level Validation
def post_data():
    data={
        'name':'jinni',
        'roll':5,
        'city':'Rajpur'
    }
    json_data = json.dumps(data)
    r= requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

post_data()
'''

#Validators
def post_data():
    data={
        'name':'godan',
        'desc':'socio-economic deprivation',
        'author':'narayan',
        'price':98
    }
    json_data = json.dumps(data)
    r= requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

#post_data()

'''

post_data():
    data={
        'name':'The Guide',
        'desc':'The novel is based on Malgudi',
        'author':'R. K. Narayan',
        'price': 205
    }
    json_data = json.dumps(data)
    r= requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

#post_data()

'''
def update_data():
    data={
        'id':1,
        'price':107,
        
    }
    json_data = json.dumps(data)
    r= requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

#update_data()

def delete_data():
    data={'id':5 }
    json_data = json.dumps(data)
    r= requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

#delete_data()