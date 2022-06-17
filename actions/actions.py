# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

class ActionGuardarAccion(Action):
    
    def name(self) -> Text:
        return "action_guardar_accion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            intent = str(tracker.latest_message['intent'].get('name'))
            boton = str(tracker.get_slot("boton"))
            nombre = tracker.get_slot("nombres")
            ubicacion = tracker.get_slot("ubicacion")
            animacion_solitaria = tracker.get_slot("animacion_solitaria")
        
            if(intent == "apretar_boton"):
                dictionary = {
                        "Accion_ReproducirAnimacion": {
                            "avatar": nombre,
                            "animacion": "PresionarBoton2"
                        },
                        "Accion Cajero": {
                            "cajero": "cajero",
                            "operacion": "apretar_boton",
                            "boton": boton
                        } }
                        

            elif(intent == "hablar"):

                text = str(tracker.latest_message['text'])
                text = text.split('"')
                print(text)
                dictionary = { 
                            "Accion_Hablar": {
                                "avatar": nombre,
                                "texto" : text[1],
                                "modo": "1"
                            } }

            json_object = json.dumps(dictionary, indent = 4)

            with open("F:\\Unity\dr-director-microlearning\Assets\Resources\CustomActions\cajerodemo2.json", 'w') as outfile:
                    outfile.write(json_object)
            dispatcher.utter_message(text= "Director dice cargar las acciones de vuelta")
            dispatcher.utter_message(text= "Estoy en eso!")

            return[]
