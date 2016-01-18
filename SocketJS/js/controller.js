var app = angular.module('uneApp', []);

app.controller("uneFonctionCtrl", function ($scope, $rootScope,WebSocketService) {
	
//Mise en place du Socket
	$rootScope.ws = new SocketManager.SocketManager($scope,$rootScope);
	
	$scope.foo = [
	              {username: "rbeck", content:"bienvenue"},
	              {username: "sthomas", content:"WTF"}]
	
	//WebSocketService.sendPseudo("kiki","gris");//TODO ne fonctionne pas... voir avec le dépo entier et manque la partie réception "rxRouting" du projet dans son intégralité
});

app.factory("Post", function(){
	var factory = {
		posts : false,
		getPosts : function(){
			return factory.posts;
		},
		getPost : function(id){
			var post = {};
			angular.forEach(factory.posts,function(){});
			return post;
		}
	};
	return factory;
})

var SocketManager = {
	ws:{},
	
	SocketManager: function (scope,rootScope/*,partyStartService*/){
//        this.ws = new WebSocket("ws://localhost:9000/startserver");
		this.ws = new WebSocket("ws://echo.websocket.org");
        
        this.ws.onopen = function(){
        	console.log("Socket has been opened!");
        };
        
    	this.ws.onmessage = function(message) {
    	    var messageObj = JSON.parse(message.data);
    	    
//  console.log("Received data from websocket: ", messageObj);
    	    rxTools.rxRouting(scope,rootScope,messageObj);
    	};
        
        return this.ws;
    }
	
};
//TODO @ICI: vidéo n°7 à 0:02:00 pour commencer à tester "$http" et "$q"