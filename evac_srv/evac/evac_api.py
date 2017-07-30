import os
import logging
from datetime import datetime

from flask import request, jsonify

from evac import app
from evac import db
from evac import models


logger = logging.getLogger(__name__)

@app.route('/evac/api/v1.0/areas/<int:id>', methods=['GET'])
def get_area(id):
    i = models.Area.query.get(id)
    return jsonify({'area': {'id': i.id,
                        'name': i.name,
                        'team':
                            { 'id': i.team.id,
                              'name': i.team.name
                            },
                        }
                    })

@app.route('/evac/api/v1.0/areas', methods=['GET'])
def get_areas():
    results = []  
    items = models.Area.query.all()
    for i in items:
        results.append({'id': i.id,
                        'name': i.name,
                        'team':
                            { 'id': i.team.id,
                              'name': i.team.name
                            },
                        })
      
    return jsonify({'areas': results})

@app.route('/evac/api/v1.0/addresses/<int:id>', methods=['GET'])
def get_address(id):
    i = models.Address.query.get(id)
    return jsonify({'address': {'id': i.id,
                        'name': i.name,
                        'area':
                            { 'id': i.area.id,
                              'name': i.area.name
                            },
                        }
                    })


@app.route('/evac/api/v1.0/addresses/<int:id>', methods=['PUT'])
def update_address_status(id):
    status=request.form['status']
    i = models.Address.query.get(id)
    i.status = status
    db.session.commit()

    return ('', 200)

@app.route('/evac/api/v1.0/addresses', methods=['GET'])
def get_addresses():
    results = []  
    items = models.Address.query.all()
    for i in items:
        results.append({'id': i.id,
                        'name': i.name,
                        'area':
                            { 'id': i.area.id,
                              'name': i.area.name
                            },
                        })
      
    return jsonify({'addresses': results})


@app.route('/evac/api/v1.0/teams/<int:id>', methods=['GET'])
def get_team(id):
    i = models.Team.query.get(id)
    return jsonify({'team': {'id': i.id,
                        'name': i.name
                        }
                    })

@app.route('/evac/api/v1.0/teams', methods=['GET'])
def get_teams():
    results = []
    items = models.Team.query.all()
    for i in items:
        results.append({'id': i.id,
                        'name': i.name
                        })
        
    return jsonify({'teams': results})

@app.route('/evac/api/v1.0/members/<int:id>', methods=['GET'])
def get_member(id):
    i = models.Member.query.get(id)
    return jsonify({'member': {'id': i.id,
                        'name': i.name,
                        'team':
                            { 'id': i.team.id,
                              'name': i.team.name
                            },
                        }
                    })

@app.route('/evac/api/v1.0/members', methods=['GET'])
def get_members():
    results = []  
    items = models.Member.query.all()
    for i in items:
        results.append({'id': i.id,
                        'name': i.name,
                        'team':
                            { 'id': i.team.id,
                              'name': i.team.name
                            },
                        })
      
    return jsonify({'members': results})

@app.route('/evac/api/v1.0/statuses/<int:id>', methods=['GET'])
def get_status(id):
    i = models.MemberStatus.query.get(id)
    return jsonify({'member_status': {'id': i.id,
                        'status': i.status,
                        'lat': float(i.lat),
                        'long': float(i.long),
                        'datatime': i.timestamp,
                        'member':
                            { 'id': i.member.id,
                              'name': i.member.name
                            },
                        }
                    })

@app.route('/evac/api/v1.0/statuses/<int:id>', methods=['PUT'])
def update_status(id):
    lat=request.form['lat']
    long=request.form['long']
    status=request.form['status']
    i = models.MemberStatus.query.get(id)
    i.status = status
    i.lat = lat
    i.long = long
    db.session.commit()

    return ('', 200)

@app.route('/evac/api/v1.0/statuses', methods=['GET'])
def get_statuses():
    results = []  
    items = models.MemberStatus.query.all()
    for i in items:
        results.append({'id': i.id,
                        'status': i.status,
                        'lat': float(i.lat),
                        'long': float(i.long),
                        'datatime': i.timestamp,
                        'member':
                            { 'id': i.member.id,
                              'name': i.member.name
                            },
                        })
      
    return jsonify({'statuses': results})
