from evac import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Team {}>'.format(self.name)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    mobile = db.Column(db.String(22), unique=True)
    #statuses = db.relationship('MemberStatus', backref='member', lazy='dynamic')
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('members', lazy='dynamic'))
    
    def __init__(self, name, email, mobile, team):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.team = team
        
    def __repr__(self):
        return '<Member {} >'.format(self.name)
    
class MemberStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String(300))
    lat = db.Column(db.Numeric(2,5))
    long = db.Column(db.Numeric(3,5))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    member = db.relationship('Member', backref=db.backref('memberstatuses', lazy='dynamic'))

    def __init__(self, status, lat, long, member, timestamp=None):
        self.status = status
        self.lat = lat
        self.long = long
        self.member = member
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
        return '<MemberStatus {}>'.format(self.status)
    

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('areas', lazy='dynamic'))
  
    def __init__(self, name, team):
        self.name = name
        self.team = team
        
    def __repr__(self):
        return '<Area {} >'.format(self.name)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    status = db.Column(db.String(300))
    lat = db.Column(db.Numeric(2,5))
    long = db.Column(db.Numeric(3,5))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    area = db.relationship('Area', backref=db.backref('addresses', lazy='dynamic'))
    timestamp = db.Column(db.DateTime)
    def __init__(self, name, status, lat, long, timestamp, area):
        self.name = name
        self.status = status
        self.lat = lat
        self.long = long
        self.area = area
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp
        
    def __repr__(self):
        return '<Address {} >'.format(self.name)

