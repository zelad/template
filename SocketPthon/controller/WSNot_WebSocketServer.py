#!/usr/bin/env python
from websocket_server import WebsocketServer
from threading import Thread
import json


class Server(Thread):

    def __init__(self, log, port = 9999):
        # Init the thread
        Thread.__init__(self)
        # Save important data
        self.log = log
        # Create a new WebSocket Server on a specific port
        self.server = WebsocketServer(port)
        # Handle when there is a new client
        self.server.set_fn_new_client(self.new_client)
        # Handle when a client lefts
        self.server.set_fn_client_left(self.clientLeft)
        # Empty list of connected client
        self.wsIHM = []

    def run(self):
        # Inform user
        self.log.info("WebServer online OK")
        # Only run the WebSocket Server
        self.server.run_forever()

    def new_client(self, client, server):
        self.wsIHM.append(client)
        self.log.info("New connected Client : {}".format(str(client)))

    def clientLeft(self, client, server):
        self.log.info("Connected Client has left: {}".format(str(client)))
        # Remove the client from the list only if it is present
        if client in self.wsIHM:
            self.wsIHM.remove(client)

    def broadCast(self, messageType, object):
        # Test is there are any connected clients
        if len(self.wsIHM) == 0:
            self.log.info("No connected client. Nothing to do")
            return
        #
        dict={}
        dict["messageType"] = messageType
        dict["object"] = object
        objJson = json.dumps(dict)
        self.log.info("send_message_to_all:'{}'".format(objJson))
        self.server.send_message_to_all(objJson)

    def updateValue(self, idPage, idElmt, value):
        '''
            Update Value
            can broadcast to all clients, one modification done by one
            @param idPage: id page 
            @param idElmt: id of the element to modify
            @param value: modified value :
                            - int
                            - int
							- int
							- int
        '''
        dict={}
        dict["idPage"] = idPage
        dict["idElmt"] = idElmt
        dict["value"] = value
        self.broadCast("bcUpdtValue", dict)
