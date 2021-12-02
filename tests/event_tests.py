import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from levelupapi.models import GameType, Game, Event, Gamer

# class EventTests(APITestCase):
#     def setUp(self):
#         """
#         Create a new Gamer, collect the auth Token, and create a sample GameType
#         """
#         # Define the URL path for registering a Gamer
#         url = '/register'

#         # Define the Gamer properties
#         gamer = {
#             "username": "steve",
#             "password": "Admin8*",
#             "email": "steve@stevebrownlee.com",
#             "address": "100 Infinity Way",
#             "phone_number": "555-1212",
#             "first_name": "Steve",
#             "last_name": "Brownlee",
#             "bio": "Love those gamez!!"
#         }

#         # Initiate POST request and capture the response
#         response = self.client.post(url, gamer, format='json')

#         # Store the TOKEN from the response data
#         self.token = Token.objects.get(pk=response.data['token'])

#         # Use the TOKEN to authenticate the requests
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         # Assert that the response status code is 201 (CREATED)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # SEED THE DATABASE WITH A GAMETYPE
#         # This is necessary because the API does not
#         # expose a /gametypes URL path for creating GameTypes

#         # Create a new instance of GameType
#         game_type = GameType()
#         game_type.label = "Board game"
#         game_type.save()
#         game = Game.objects.create(
#             game_type=game_type,
#             title="Monopoloy",
#             maker="Hasboro",
#             gamer_id=1,
#             number_of_players=5,
#             skill_level=2
#         )

#         # Save the GameType to the testing database

#     def test_create_event(self):
#         """
#         Ensure we can create (POST) a new Game.
#         """

#         # Define the URL path for creating a new Game
#         url = "/events"

#         # Define the Game properties
#         event = {
#             "date": "2021-12-23",
#             "time": "12:30:00",
#             "description": "Game Day",
#             "gameId": self.game.id,
#         }

#         # Initiate POST request and capture the response
#         response = self.client.post(url, event, format='json')

#         # Assert that the response status code is 201 (CREATED)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # Assert that the values are correct
#         self.assertIsNotNone(response.data['id'], event.id)
#         self.assertEqual(response.data["organizer"]['id'], event.organizer.id)
#         self.assertEqual(response.data["date"], event["date"])
#         self.assertEqual(response.data["time"], event["time"])
#         self.assertEqual(response.data["description"], event["description"])

#     def test_get_event(self):
#         """
#         Ensure we can GET an existing game.
#         """

#         game_type = GameType()
#         game_type.label = "Board game"
#         game_type.save()

#         game = Game.objects.create(
#             game_type=game_type,
#             title="Monopoloy",
#             maker="Hasboro",
#             gamer_id=1,
#             number_of_players=5,
#             skill_level=2
#         )

#         event = Event.objects.create(
#             organizer_id=1,
#             game=game,
#             time="12:30:00",
#             date="2021-12-23",
#             description="game night"
#         )
#         url = f'/events/{event.id}'
#         response = self.client.get(url)

#         # Assert that the response status code is 200 (OK)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Assert that the values are correct
#         self.assertEqual(response.data['id'], event.id)
#         self.assertEqual(response.data["organizer"]['id'], event.organizer.id)
#         self.assertEqual(response.data["date"], event.date)
#         self.assertEqual(response.data["time"], event.time)
#         self.assertEqual(response.data["description"], event.description)
#     def test_change_event(self):
#         """
#         Ensure we can change an existing game.
#         """

#         # Create a new instance of Event
#         event = Event()
#         event.game_id = 1
#         event.description = "Not Sorry!"
#         event.date = "2021-12-22"
#         event.time = "12:30:00"
#         event.organizer = 1

#         # Save the Game to the testing database
#         event.save()

#         # Define the URL path for updating an existing Game
#         url = f'/events/{event.id}'

#         # Define NEW Game properties
#         new_event = {
#             "gameId": 1,
#             "description": "I'm Sorry!",
#             "date": "2021-12-25",
#             "time": "12:30:00",
#             "organizer": 1
#         }

#         # Initiate PUT request and capture the response
#         response = self.client.put(url, new_event, format="json")

#         # Assert that the response status code is 204 (NO CONTENT)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         # Initiate GET request and capture the response
#         response = self.client.get(url)

#         # Assert that the response status code is 200 (OK)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Assert that the values are correct
#         self.assertEqual(response.data["organizer"]['id'], self.token.user_id)
#         self.assertEqual(response.data["game_id"], new_event['gameId'])
#         self.assertEqual(response.data["description"], new_event['description'])
#         self.assertEqual(
#             response.data["date"], new_event['date'])
#         self.assertEqual(
#             response.data["time"], new_event['time'])

#     def test_delete_event(self):
#         """
#         Ensure we can delete an existing game.
#         """

#         # Create a new instance of Game
#         event = Event()
#         event.game_id = 1
#         event.description = "Not Sorry!"
#         event.date = "2021-12-22"
#         event.time = "12:30:00"
#         event.organizer_id = 1

#         # Save the Game to the testing database
#         event.save()

#         # Define the URL path for deleting an existing event
#         url = f'/events/{event.id}'

#         # Initiate DELETE request and capture the response
#         response = self.client.delete(url)

#         # Assert that the response status code is 204 (NO CONTENT)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         # Initiate GET request and capture the response
#         response = self.client.get(url)

#         # Assert that the response status code is 404 (NOT FOUND)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EventTests(APITestCase):
    def setUp(self):
        # TODO: Set up database with logged in user and game
        url = '/register'

        # Define the Gamer properties
        gamer = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, gamer, format='json')

        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])

        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        game_type = GameType()
        game_type.label = "Board game"

        # Save the GameType to the testing database
        game_type.save()
        self.game = Game.objects.create(
            game_type=game_type,
            title="Monopoly",
            maker="Hasbro",
            gamer_id=1,
            number_of_players=5,
            skill_level=2
        )
        

    def test_retrieve(self):
        # TODO: Test the event retrieve method
        event = Event.objects.create(
            organizer_id=1,
            game=self.game,
            time="12:30:00",
            date="2021-12-23",
            description="Game night"
        )
        url = f'/events/{event.id}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], event.id)
        self.assertEqual(response.data['date'], event.date)
        self.assertEqual(response.data['time'], event.time)
        self.assertEqual(response.data['description'], event.description)
        self.assertEqual(response.data['organizer']['id'], event.organizer.id)

    def test_create(self):
        # TODO: Test the event create method
        event = {
            "date": "2021-12-23",
            "time": "12:30:00",
            "description": "Game Day",
            "gameId": self.game.id
        }
        response = self.client.post('/events', event, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])
        self.assertEqual(response.data['date'], event['date'])
        self.assertEqual(response.data['time'], event['time'])
        self.assertEqual(response.data['description'], event['description'])
        self.assertEqual(response.data['organizer']['id'], 1)

    def test_delete(self):
        # TODO: Test the event delete method
        event = Event.objects.create(
            organizer_id=1,
            game=self.game,
            time="12:30:00",
            date="2021-12-23",
            description="Game night"
        )

        response = self.client.delete(f'/events/{event.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(f'/events/{event.id}')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        # TODO: Test the event update method
        event = Event.objects.create(
            organizer_id=1,
            game=self.game,
            time="12:30:00",
            date="2021-12-23",
            description="Game night"
        )

        event_dict = {
            'id': event.id,
            'gameId': event.game.id,
            'time': event.time,
            'date': "2021-12-27",
            'description': event.description
        }

        response = self.client.put(f'/events/{event.id}', event_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        event_updated = Event.objects.get(pk=event.id)
        self.assertEqual(event_updated.date.strftime('%Y-%m-%d'), event_dict['date'])

    def test_joining_event(self):
        # TODO: Test joining an event method
        event = Event.objects.create(
            organizer_id=1,
            game=self.game,
            time="12:30:00",
            date="2021-12-23",
            description="Game night"
        )
        # Assert that no one is in the event list, the length should be 0
        self.assertEqual(len(event.attendees.all()), 0)

        response = self.client.post(f'/events/{event.id}/signup')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # After the post runs assert that the attendees length is 1
        self.assertEqual(len(event.attendees.all()), 1)

    def test_leaving_events(self):
        event = Event.objects.create(
            organizer_id=1,
            game=self.game,
            time="12:30:00",
            date="2021-12-23",
            description="Game night"
        )
        # Add a gamer to the attendees
        gamer = Gamer.objects.get(pk=1)
        event.attendees.add(gamer)

        response = self.client.delete(f'/events/{event.id}/signup')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(event.attendees.all()), 0)