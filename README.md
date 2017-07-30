# govhack2017
# initial

# create virtual environement
py -3 -m venv evac_srv
cd  evac_srv

# activate environement
Scripts\activate

# intstall dependencies
pip install -r requirements.txt

python db_create.py
python db_migrate.py

# init db
python db_explore.py 

# run local server
run.bat

# apis

# evacuation areas

http://localhost:5000/evac/api/v1.0/areas
http://localhost:5000/evac/api/v1.0/areas/{1}

# evacuation residential properties
# see note below re Linz dataset 

http://localhost:5000/evac/api/v1.0/addresses   	GET
http://localhost:5000/evac/api/v1.0/addresses/{1} 	GET
http://localhost:5000/evac/api/v1.0/addresses/{1} 	PUT

# rescue teams
http://localhost:5000/evac/api/v1.0/teams/{1} 		GET
http://localhost:5000/evac/api/v1.0/teams       	GET

# rescue team members
http://localhost:5000/evac/api/v1.0/members/{1} 	GET
http://localhost:5000/evac/api/v1.0/members 		GET

# rescue team member status
http://localhost:5000/evac/api/v1.0/statuses/{1} 	GET
http://localhost:5000/evac/api/v1.0/statuses/{1} 	PUT
http://localhost:5000/evac/api/v1.0/statuses GET

# Linz
# Linz dataset api could be used to generate residential properties of concern
url = http://api.data.linz.govt.nz/api/vectorQuery.json?key=61bf92e441344799b334f95ca0361518&layer=3353&x=172.4396117&y=-43.7139295&max_results=50&radius=10000

#Linz dataset api could be used to generate residential properties of concern

response = requests.get(url)
response_json = response.json()

features = response_json['vectorQuery']['layers']['3353']['features']

for i in features:
    address = {'address': i['properties']['full_address'], 
    'long': i['properties']['gd2000_xcoord'],
    'lat': i['properties']['gd2000_ycoord']
    }
    pprint(address)
	
{'address': '2 Spackman Avenue, Springston',
 'lat': -43.71401601,
 'long': 172.43955632}
{'address': '4 Spackman Avenue, Springston',
 'lat': -43.71437053,
 'long': 172.43949394}
{'address': '10 Spackman Avenue, Springston',
 'lat': -43.71477526,
 'long': 172.43950916}
{'address': '11 Spackman Avenue, Springston',
 'lat': -43.71487111,
 'long': 172.4395335}
{'address': '12 Spackman Avenue, Springston',
 'lat': -43.71494719,
 'long': 172.43955632}
{'address': '13 Spackman Avenue, Springston',
 'lat': -43.71503088,
 'long': 172.43955024}
{'address': '2 Selwyn Lake Road, Leeston',
 'lat': -43.71337845,
 'long': 172.4381393}
{'address': '15 Spackman Avenue, Springston',
 'lat': -43.71520433,
 'long': 172.4395761}
{'address': '16 Spackman Avenue, Springston',
 'lat': -43.71528193,
 'long': 172.43958828}
{'address': '17 Spackman Avenue, Springston',
 'lat': -43.71538083,
 'long': 172.43962632}


