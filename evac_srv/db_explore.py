import json
import logging
import logging.config

def add_teams():
    for i in ['South Selwyn A', 'South Selwyn B', 'South Selwyn C']:
        o = models.Team(name=i)
        db.session.add(o)
        db.session.commit()
        print('added', o)

def add_areas():
    t = models.Team.query.get(1)
    for i in ['South Selwyn']:
        o = models.Area(name=i, team=t)
        db.session.add(o)
        db.session.commit()
        print('added', (o, t))

def add_members():
    members = [{'email': 'bruce@evac.com', 'mobile': '021029182739654', 'name': 'Bruce'},
     {'email': 'sarah@evac.com', 'mobile': '021029871692453', 'name': 'Sarah'},
     {'email': 'stuart@evac.com', 'mobile': '021029832476951', 'name': 'Stuart'},
     {'email': 'darrin@evac.com', 'mobile': '021029679348152', 'name': 'Darrin'},
     {'email': 'farid@evac.com', 'mobile': '021029173849526', 'name': 'Farid'}]

    t = models.Team.query.get(1)
    for m in members:
        o = models.Member(name=m['name'], email=m['email'], mobile=m['mobile'], team=t)
        db.session.add(o)
        db.session.commit()
        print('added', (o, t))

    
def add_member_statuses():
    members = models.Member.query.all()
    lat = -43.71392
    long =  172.43961
    for m in members:
        o = models.MemberStatus(status='in the field', lat=lat, long=long, timestamp=datetime.utcnow(), member=m)
        db.session.add(o)
        db.session.commit()
        print('added', (o, m))


def add_addresses():
    a = models.Area.query.get(1)
    addresses = [{
      'address': '1 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7139295,
      'long': 172.4396117,
      'status': 'To Check'},
     {'address': '3 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.71406349999999,
      'long': 172.4395881,
      'status': 'To Check'},
     {'address': '5 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7140985,
      'long': 172.4395741,
      'status': 'To Check'},
     {'address': '7 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7144172,
      'long': 172.4395923,
      'status': 'To Check'},
     {'address': '9 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7144919,
      'long': 172.4395928,
      'status': 'To Check'},
     {'address': '11 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7146906,
      'long': 172.4395302,
      'status': 'To Check'},
     {'address': '13 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7149391,
      'long': 172.4395503,
      'status': 'To Check'},
     {'address': '15 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7150076,
      'long': 172.4395757,
      'status': 'To Check'},
     {'address': '17 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7153345,
      'long': 172.439573,
      'status': 'To Check'},
     {'address': '19 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7153757,
      'long': 172.4395822,
      'status': 'To Check'},
     {'address': '21 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.715567,
      'long': 172.4396661,
      'status': 'To Check'},
     {'address': '23 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7157032,
      'long': 172.4397368,
      'status': 'To Check'},
     {'address': '25 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.71579149999999,
      'long': 172.4397496,
      'status': 'To Check'},
     {'address': '27 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7160567,
      'long': 172.4396889,
      'status': 'To Check'},
     {'address': '29 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7163397,
      'long': 172.4397719,
      'status': 'To Check'},
     {'address': '31 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7164806,
      'long': 172.4398761,
      'status': 'To Check'},
     {'address': '33 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7166317,
      'long': 172.4396476,
      'status': 'To Check'},
     {'address': '35 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.71685309999999,
      'long': 172.4398354,
      'status': 'To Check'},
     {'address': '37 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7170342,
      'long': 172.4398772,
      'status': 'To Check'},
     {'address': '39 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7171846,
      'long': 172.4398895,
      'status': 'To Check'},
     {'address': '41 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7173699,
      'long': 172.4398853,
      'status': 'To Check'},
     {'address': '43 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7174977,
      'long': 172.4398816,
      'status': 'To Check'},
     {'address': '45 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.7176957,
      'long': 172.4398649,
      'status': 'To Check'},
     {'address': '47 Spackman Ave, Springston 7674, New Zealand',
      'checked_by': '',
      'datetime': None,
      'lat': -43.71776939999999,
      'long': 172.4398556,
      'status': 'To Check'}]

    for i in addresses:
        o = models.Address(name=i['address'], status=i['status'], lat=i['lat'], long=i['long'], timestamp=datetime.utcnow(), area=a)
        db.session.add(o)
        db.session.commit()
        print('added', (o, a))

def get_teams():
    items = models.Team.query.all()
    for i in items:
        print(i)

def get_areas():
    items = models.Area.query.all()
    for i in items:
        print(i)
        
def get_members():
    items = models.Member.query.all()
    for i in items:
        print(i, i.email, i.mobile)

def get_member_statuses():
    items = models.MemberStatus.query.all()
    for i in items:
        #if 'farid' in i.member.name.lower():
            #i.status = 'finshed for the day'
            #db.session.commit()
            
        print(i.status, i.member)



def get_addresses():
    items = models.Address.query.all()
    for i in items:
        print(i, i.name)
   
        
def main():
    #add_teams()
    #add_areas()
    #add_members()
    #add_member_statuses()
    #add_addresses()

    get_teams()
    get_areas()
    get_members()
    get_member_statuses()
    get_addresses()
    
if __name__ == '__main__':
    import os, sys
    from datetime import datetime
    from pprint import pprint

    
    from evac import db, models


    logging.basicConfig(level="INFO")
    logger = logging.getLogger(__name__)
    main()

    
