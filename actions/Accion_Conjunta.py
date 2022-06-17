
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

class ActionConjunta(Action):
    """Esta accion se encarga de seleccionar la respuesta determinada al intent detectado por rasa, acorde a la persona que interpreta el asistente"""

    def name(self) -> Text:
        return "accion_conjunta"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        ultimo_intent =  tracker.latest_message['intent'].get('name')

        entidad = self.getEntidades(tracker, "nombres")
        animacion = self.getEntidades(tracker, "animacionConjunta")

        data = {
            "Accion_Conjunta": {
                "avatarA": entidad[0],
                "avatarB": entidad[1],
                "animacion": animacion[0]
            },
        }
        print(ultimo_intent)   
        
        json_object = json.dumps(data , indent = 4)

        with open("F:\\Unity\dr-director-microlearning\Assets\Resources\CustomActions\cajerodemo2.json", 'w') as outfile:
            outfile.write(json_object)

        dispatcher.utter_message(text= "Director dice cargar las acciones de vuelta")
        dispatcher.utter_message(text= "Estoy en eso!")

        return []

    def getEntidades(self, tracker, entity):
        entidades = []
        for i in tracker.latest_message['entities']:
               
            if i['entity'] == entity:
                entidades.append(i['value'])
        return entidades
    
    





   