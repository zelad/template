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

def new_client(client, server):
    print "client connecte"
# ex de broadcast:
    tx2All(); 
    
def rxMessage(client, server, message):
    print message
    
def clientLeft(client, server):
    print "le client:"
    print client
    print "est partie"
    
def tx2All():
    server.send_message_to_all("Hello tous")
    
if __name__ == "__main__":
    server = WebsocketServer(9999)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(rxMessage)
    server.set_fn_client_left(clientLeft)
    
    server.run_forever()