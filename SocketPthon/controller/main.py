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
from threading import Thread
import webbrowser
import json
import os

from UnModel import UnModel

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.server = WebsocketServer(9999)
        self.server.set_fn_new_client(new_client) #définition de la fonction pour l arrivé d un nouveau client
        self.server.set_fn_message_received(rxMessage) #Définition de la fonction pour l arrivé d un nouveau message
        self.server.set_fn_client_left(clientLeft) #définition de la fonction pour la déconnexion d'un client
    
# Thread de server
    def run(self):
        self.server.run_forever()

'''        
OverLoad des fonctions de webSocket
'''
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
Envoie d "Object"
'''
def sendObject(object,messageType):
    global wsIHM
    dict={}
    dict["messageType"] = messageType
    dict["object"] = object
    objJson = json.dumps(dict)
    serv.server.send_message(wsIHM, objJson)

'''
Fonction de routage des message entrants
'''    
def ihmRouting(message, server):
#     objDict = ast.literal_eval(message) //pour compatibilité avec Android
    objDict = json.loads(message)
    func = switch[objDict["sendType"]]
    func(message, server)

def doLogin(message, server):
    global unModel
#     obj = ast.literal_eval(message) //pour compatibilité avec Android
#     print message //aucune idée pourquoi mais il faut mettre cela pour que ça fonctionne avec Android!!?
    obj = json.loads(message)
    objLogin = obj["object"]
    unModel.nom = objLogin["name"]
    unModel.prenom = objLogin["firstname"]
    #Ack client
    dict={}
    dict["messageType"]="ackLogin"
    objJson = json.dumps(dict)
    server.send_message(wsIHM, objJson)
    
if __name__ == "__main__":
# Fixation du point de lecture de fichier
    os.chdir('/')#Obligation de donner le chemin du fichier avec le QPython
# routage des messages receptionnes    
    switch={
        "login":doLogin
    }
# Initialisation des models
    unModel = UnModel()
    
# ouverture du client web
#     os.system("where /R c:\\ chrome.exe")# pour appeler une commande DOS "WHERE" afin de trouver le chemin de l'exe de Chrome. pour la gestion des sorties: https://stackoverflow.com/questions/3791465/python-os-system-for-command-line-call-linux-not-returning-what-it-should
    webbrowser.register("ff", None, webbrowser.BackgroundBrowser("C:\\Program Files\\Firefox Developer Edition\\firefox.exe"))
    b = webbrowser.get('ff')
    b.open('file://'+os.path.realpath("../../../Code/Angular/index.html"))

#     webbrowser.open('file://'+os.path.realpath("../../../Angular/index.html"))

# lancement du thread serveur
    serv = Server()
    serv.start()