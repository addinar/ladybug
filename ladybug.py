import requests
from openai import OpenAI
import os
import json

class Ladybug:
    def __init__(self):
        self.google_key = 'AIzaSyDG6M9ROdWak3ml8YGeoHKdgR_ZAi81zgg'
        self.open_ai_key = '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'

    def run_task(self):
        print("Hi! I'm a ladybug, your travel assistant. Enter your origin, destination, and preferred mode of travel.\n")
        origin = input("Origin: ")
        print('\n')
        destination = input("Destination: ")
        print('\n')
        print('Fetching response...')
        response = self.answer_query(origin, destination)
        print('\n')
        print(response)

    def get_route(self, origin, destination):
        origin = origin.replace(" ", "+")
        origin = origin.replace(",", "%2C")
        destination = destination.replace(" ", "+")
        destination = destination.replace(" ", "%2C")
        key = self.google_key
        url = f'https://maps.googleapis.com/maps/api/directions/json?destination={destination}&origin={origin}&key={key}'
        response = requests.get(url)
        data = response.json()
        data = json.dumps(data)
        return data

    def answer_query(self, origin, destination):
        route = self.get_route(origin, destination)
        os.environ["OPENAI_API_KEY"] = self.open_ai_key

        # self.get_updated_data()
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Provide the best driving, public transit, and walking routes."
                },
                {
                    "role": "system",
                    "content": route
                }
            ],
            model="gpt-3.5-turbo-0125",
        )
        response = chat_completion.choices[0].message.content
        return response
