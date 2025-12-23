from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Solo inserta datos de prueba (no borrar nada)
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        ironman = app_models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        spiderman = app_models.User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel)
        batman = app_models.User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = app_models.User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=spiderman, type='cycle', duration=45)
        app_models.Activity.objects.create(user=batman, type='swim', duration=60)
        app_models.Activity.objects.create(user=superman, type='run', duration=50)

        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        app_models.Leaderboard.objects.create(user=ironman, points=100)
        app_models.Leaderboard.objects.create(user=spiderman, points=90)
        app_models.Leaderboard.objects.create(user=batman, points=95)
        app_models.Leaderboard.objects.create(user=superman, points=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
