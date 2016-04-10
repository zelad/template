#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
Created on 15 janv. 2016

@author: Kiki
@note: inspiration WebSocket ici: https://pypi.python.org/pypi/websocket-server/0.4
@note: ou: https://github.com/Pithikos/python-websocket-server
@note: test le 29/01 pour changement de map dossier de GitH
'''
from websocket_server import WebsocketServer
import json

from UnModel import UnModel

global switch
global UnModel

def new_client(client, server):
    global wsIHM
    wsIHM = client
    print "client connecte"
# ex de broadcast:
    tx2All(); 
    
def rxMessage(client, server, message):
#     print message
    ihmRouting(message, server)
    
def clientLeft(client, server):
    print "le client:"
    print client
    print "est partie"
    
def tx2All():
    pass
#     server.send_message_to_all("Hello tous")
'''
Fonction de routage des message entrants
'''    
def ihmRouting(message, server):
#     objDict = ast.literal_eval(message) //pour compatibilité avec Android
    objDict = json.loads(message)
    func = switch[objDict["sendType"]]
    func(message, server)

def doLogin(message, server):
    global UnModel
#     obj = ast.literal_eval(message) //pour compatibilité avec Android
#     print message //aucune idée pourquoi mais il faut mettre cela pour que ça fonctionne avec Android!!?
    obj = json.loads(message)
    objLogin = obj["object"]
    UnModel.nom = objLogin["name"]
    UnModel.prenom = objLogin["firstname"]
    #Ack client
    dict={}
    dict["messageType"]="ackLogin"
    objJson = json.dumps(dict)
    server.send_message(wsIHM, objJson)
    
if __name__ == "__main__":
# routage des messages receptionnes    
    switch={
        "login":doLogin
    }
# Initialisation des models
    unModel = UnModel()
# Connexion au client web
    server = WebsocketServer(9999)
    server.set_fn_new_client(new_client) #définition de la fonction pour l arrivé d un nouveau client
    server.set_fn_message_received(rxMessage) #Définition de la fonction pour l arrivé d un nouveau message
    server.set_fn_client_left(clientLeft) #définition de la fonction pour la déconnexion d'un client
    
    server.run_forever()