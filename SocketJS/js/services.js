/**
 * 
 */
app.factory('WebSocketService',['$q','$rootScope',
                                                     function($q, $rootScope) {
	// Nous retournons cet objet pour toutes les injection de notre service
    var Service = {};
    // Garde toutes les requÃªtes en attente ici, jusqu'à  ce qu'elles obtiennent une réponse
    var callbacks = {};
    // Crée un unique "callback ID" pour tracer/lier les requÃªtes et les réponses
    var currentCallbackId = 0;

    
    function sendRequest(request) {
      var defer = $q.defer();
      var callbackId = getCallbackId();
      callbacks[callbackId] = {
        time: new Date(),
        cb:defer
      };
      request.callback_id = callbackId;
//console.log('Sending request', request);
      $rootScope.ws.send(JSON.stringify(request));
      return defer.promise;
    }

    // Ceci crée un nouveau "callback ID" pour la requÃªt
    function getCallbackId() {
      currentCallbackId += 1;
      if(currentCallbackId > 10000) {
        currentCallbackId = 0;
      }
      return currentCallbackId;
    }
    
    // Fonction de tranmission "general"
    Service.sendObject = function(sendID,object){
    	
        var request = {
            sendType: sendID
        };
        request.object = object;//Pour ajouter un parametre Ã  l objet "request"
        
        var promise = sendRequest(request);
        return promise;
    };
    
/**
 * une erreur pour tester la réponse du serveur...
 */
    Service.sendError = function() {
      var request = {
        type: "une betise..."
      };
      // Stocké dans une variable pour plus de clarté sur ce que "sendRequest retourne
      var promise = sendRequest(request); 
      return promise;
    };

    return Service;
}]);