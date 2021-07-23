from django.test import TestCase
from statuses.models import Status
from django.contrib.auth.models import User
from .models import Task


class TasksTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='Zde6v45rGBYx2LGx',
        )
        self.client.force_login(self.user)
        User.objects.create_user(
            username='user2',
            password='Zde6v45rGBYx2LGx',
        )
        Status.objects.create(name='New')
        Status.objects.create(name='InProgress')
        Task.objects.create(
            name='Task',
            description='Task',
            status=Status.objects.get(name='New'),
            executor=User.objects.get(username='user2'),
            creator=self.user,
        )

    def test_create(self):
        response = self.client.post('/tasks/create/', {
            'name': 'Task2',
            'description': 'Task2',
            'status': Status.objects.get(name='New').id,
            'executor': User.objects.get(username='user2').id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="Task2"))
        self.assertTrue(Task.objects.filter(status=1))

    def test_update(self):
        response = self.client.post('/tasks/1/update/', {
            'name': 'Task3',
            'description': 'Task3',
            'status': Status.objects.get(name='InProgress').id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="Task3"))
        self.assertTrue(Task.objects.filter(status=2))

    def test_delete(self):
        response = self.client.post('/tasks/1/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
