"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from levelupapi.models import Game

from levelupreports.views.helpers import dict_fetch_all


class UserEventList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
            select e.date, e.time, u.first_name || " " || u.last_name full_name, ga.title, g.id as gamer_id
            FROM levelupapi_event e
            JOIN levelupapi_eventgamer eg ON e.id = eg.event_id
            JOIN levelupapi_gamer g ON eg.gamer_id = g.id
            JOIN auth_user u on u.id = g.user_id
            JOIN levelupapi_game ga ON e.game_id = g.id
            """)

            dataset = dict_fetch_all(db_cursor)

            events_with_gamer = []

            for row in dataset:
                event = {
                    'game_title': row['title'],
                    'date': row['date'],
                    'time': row['time'],
                }


                user_dict = next(
                    (user_event for user_event in events_with_gamer
                    if user_event['gamer_id'] == row['gamer_id']
                    ),
                    None
                )

                if user_dict is not None:
                    user_dict['events'].append(event)
                else: 
                    events_with_gamer.append({
                        'gamer_id': row['gamer_id'],
                        'full_name': row['full_name'],
                        'events': [event]
                    })
            template = 'users/events_with_gamer.html'

            context = {
                'user_events': events_with_gamer
            }

            return render(request, template, context)
