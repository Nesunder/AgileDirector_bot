
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

class ActionSentarse(Action):
    """Esta accion se encarga de seleccionar la respuesta determinada al intent detectado por rasa, acorde a la persona que interpreta el asistente"""

    def name(self) -> Text:
        return "accion_sentarse"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        ultimo_intent =  tracker.latest_message['intent'].get('name')

        entidad = self.getEntidades(tracker, "nombres")
        asientos = self.getEntidades(tracker, "asiento")

        data = {
            "Accion_Sentarse": {
                "avatar": entidad[0],
                "objeto" : asientos[0]
            },
        }
        print(ultimo_intent)   
        



        dispatcher.utter_message(json_message = data)

        return []

    def getEntidades(self, tracker, entity):
        entidades = []
        for i in tracker.latest_message['entities']:
               
            if i['entity'] == entity:
                entidades.append(i['value'])
        return entidades
    
    





   