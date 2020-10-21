# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from random import randrange
import datetime

class ActionUtterName(Action):

    def name(self) -> Text:
        return "action_utter_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	name = tracker.get_slot("user_name")

    	if name is not None:
    		possible = [
    			"Don't worry, I will remember your name " + (name),
    			"I know your name " + name
    		]
    		message = possible[randrange(len(possible))]
    	else:
    		possible = [
    			"I don't know your name! Can you tell me your name?",
    			"You have never told me your name"
    		]
    		message = possible[randrange(len(possible))]

    	dispatcher.utter_message(text=message)


    	return []

class ActionAcknowledgeCompany(Action):

    def name(self) -> Text:
        return "action_acknowledge_company"


    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = ""
        company = tracker.get_slot("company")

        date = tracker.get_slot("DATE")

        if company is None:
            company = tracker.get_slot("ORG")

        listed = ["google", "microsoft"]

        if company.lower() not in listed:
            message = "Please select a company from the given list"

        else:

            possible = [
                "I could not find the date when the price has to be predicted, can you specify the number of days from now for which the price has to be predicted?"
            ]

            message = possible[randrange(len(possible))]

        dispatcher.utter_message(text=message)


        return []

class ActionPredictPrice(Action):

    def name(self) -> Text:
        return "action_predict_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = ""
        company = tracker.get_slot("company")

        days_later = tracker.get_slot("days_later")


        if company is not None and days_later is not None:

            message = "2000 Rs"

        dispatcher.utter_message(text=message)


        return []
