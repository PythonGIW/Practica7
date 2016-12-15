# -*- coding: utf-8 -*-

"""
Autores: 
Alberto Marquez
Álvaro Asenjo
Juan Jose Montiel 
Declaramos que esta solución
es fruto exclusivamente de nuestro trabajo personal. No hemos sido
ayudados por ninguna otra persona ni hemos obtenido la solución de
fuentes externas, y tampoco hemos compartido nuestra solución con
nadie. Declaramos además que no hemos realizado de manera desho-
nesta ninguna otra actividad que pueda mejorar nuestros resultados
ni perjudicar los resultados de los demás.

"""

from bottle import get, run, template, error, static_file, request,response,redirect
from pymongo import MongoClient

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['usuarios']
 
@get('/find_user')
def find_user():
    username = request.query['username']
    data = c.find({'_id':username})
    return template('find_user.tpl', result = data)
        

@get('/find_users')
def find_users():
    params = request.query_string
    listaP = params.split("&")
    keys = []
    values = []
    for param in listaP:
        p = param.split("=")
        if(p[0] == "name" or p[0] == "surname" or p[0] == "birthday"):
            if(p[0] == "birthday"):
                keys.append("birthdate")
            else:
                keys.append(p[0])
            values.append(p[1])
        else:
            print "Error"
            return template('find_user.tpl', result = data)
            break
    print keys
    print values
    if(len(keys) == 1):
        data = c.find({keys[0]:values[0]})
    elif (len(keys) == 2):
        data = c.find({keys[0]:values[0], keys[1]:values[1]})
    elif (len(keys) == 3):
        data = c.find({keys[0]:values[0], keys[1]:values[1], keys[2]:values[2]})

    return template('find_users.tpl', result = data)
        
        
@get('/find_users_or')
def find_users_or():
    params = request.query_string
    listaP = params.split("&")
    keys = []
    values = []
    for param in listaP:
        p = param.split("=")
        if(p[0] == "name" or p[0] == "surname" or p[0] == "birthday"):
            if(p[0] == "birthday"):
                keys.append("birthdate")
            else:
                keys.append(p[0])
            values.append(p[1])
        else:
            print "Error"
            return template('find_user.tpl', result = data)
            break
    print keys
    print values
    if (len(keys) == 2):
        data = c.find({ '$or': [ { keys[0]: values[0] }, { keys[1]:values[1] } ] }) 
    elif (len(keys) == 3):
        data = c.find({ '$or': [ { keys[0]: values[0] }, { keys[1]:values[1] }, { keys[2]:values[2] }  ] })
    return template('find_users.tpl', result = data)
@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    # db.users.find({gustos: {$all: ["p2p", "musica"]}})

    like = request.query['like']
    data = c.find({'likes': {'$all': [like]}})
        
    return template('find_users.tpl', result = data)
    


@get('/find_country')
def find_country():
    country = request.query['country']
    data = c.find({'address.country': country})
        
    return template('find_users.tpl', result = data)
    
    
@get('/find_email_birthdate')
def email_birthdate():
    desde = request.query['from']
    hasta = request.query['to']
    data = c.find({'birthdate': {'$gte':desde, '$lte':hasta}})
        
    return template('find_users.tpl', result = data)
    
    
@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    country = request.query['country']
    likes = request.query['likes']
    limit = request.query['limit']

    data = c.find({'adress.country': country, 'likes': {'$all': [likes]}}).limit(limit)
        
    return template('find_users.tpl', result = data)

    
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
