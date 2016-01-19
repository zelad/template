/**
  * Fonction d'orientation de message entrant
  */
var rxTools = {
//Orientation du message reçu
//    rxRouting : function (scope,rootScope,data/*,PartyStartService*/){
	rxRouting : function (scope,rootScope,data){
        var mType = data.messageType;
        
        switch(mType) {
            case "accueil":
                alert(data.message);
                break;
            
            case "broadCastEndR":
//console.info("[Test:] Blason de fin de tour recu: ",data.blasonColor);
				blasonManager.majAffichEndRound(scope, data);
            	break;
				
            default:
                alert("Type de message inconnue!");
            	console.info("ORNI: ",data);
        }
    }
        
};