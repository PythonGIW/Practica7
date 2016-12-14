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

    return template('find_user.tpl', result = data)
    #print data0
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&food=hotdog
        
        
@get('/find_users_or')
def find_users_or():
    # http://localhost:8080/find_users_or?name=Luz&surname=Corral
    #pass
	Persona.objects( Q(name='Luz') | Q(surname='Corral') ) 
               
@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    pass


@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Irlanda
    pass
    
    
@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    pass
    
    
@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    pass

    
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
