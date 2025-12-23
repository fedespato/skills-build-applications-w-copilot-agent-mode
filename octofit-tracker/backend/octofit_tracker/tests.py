from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(email="test@example.com", name="Test User", team=team)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team Alpha")
        self.assertEqual(team.name, "Team Alpha")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team Beta")
        user = User.objects.create(email="user2@example.com", name="User Two", team=team)
        activity = Activity.objects.create(user=user, type="Run", duration=30)
        self.assertEqual(activity.type, "Run")
        self.assertEqual(activity.duration, 30)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        team = Team.objects.create(name="Team Gamma")
        user = User.objects.create(email="user3@example.com", name="User Three", team=team)
        entry = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(entry.points, 100)
