#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
Created on 15 janv. 2016

@author: Kiki
@note: inspiration WebSocket ici: 
'''
from websocket_server import WebsocketServer

def new_client(client, server):
    print "client connecte"

def new_message(client, server, message):
    print message
    
server = WebsocketServer(9999)
server.set_fn_new_client(new_client)
server.set_fn_message_received(new_message)
server.run_forever()

if __name__ == "__main__":
    pass