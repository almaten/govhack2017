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


