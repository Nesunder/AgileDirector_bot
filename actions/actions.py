# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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
            f = open("F:\\Unity\dr-director-microlearning\Assets\Resources\CustomActions\cajerodemo2.json", 'w')

            if(intent == "apretar_boton"):
                f.write('{"Accion_ReproducirAnimacion": {\n')
                f.write('   "avatar":' + '"' + nombre + '",\n')
                f.write('   "animacion": "PresionarBoton2" \n')
                f.write(" },\n")
                f.write('"Accion_Cajero": {\n')
                f.write('   "cajero": "cajero",\n')
                f.write('   "operacion": "apretar_boton", \n')
                f.write('   "boton":' + '"'+ boton + '"\n')
                f.write(" }}")
                f.close()
            elif(intent == "moverAvatar"):
                f.write('{"Accion_MoverAvatar": {\n')
                f.write('   "avatar":' + '"' + nombre + '",\n')
                f.write('   "ubicacion":' + '"' + ubicacion + '"\n')
                f.write(" }}")
                f.close()
            else:
                f.write('{"Accion_ReproducirAnimacion": {\n')
                f.write('   "avatar":' + '"' + nombre + '",\n')
                f.write('   "animacion":' + '"' + animacion_solitaria + '"\n')
                f.write(" }}")
                f.close()

            dispatcher.utter_message(text= "Director dice  cargar las acciones de vuelta")

            return[]
