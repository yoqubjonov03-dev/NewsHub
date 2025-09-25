from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from blok_app.models import Task, Comment
from django.contrib.auth.models import User

class TaskTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='dilshod', password='adminroot')
        self.staff_user = User.objects.create_user(username='admin', password='adminroot', is_staff=True)

        self.task1 = Task.objects.create(user=self.user, title='Qabullar boshlandi',
                                         description='oliy talimga qabullar boshlandi')
        self.task2 = Task.objects.create(user=self.staff_user, title='rivojlannish davri',
                                         description='2025- yil ozbekiston koplash sohalarda yangliklar amalga oshirdi')

        Comment.objects.create(title=self.task2, content='bu yahshi', rating=4,)
        Comment.objects.create(title=self.task2, content='ozgarish bor', rating=5)
        Comment.objects.create(title=self.task1, content='hamaga omad', rating=3)

    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_task_list_create(self):
        url = reverse('task-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'user': self.user.id,
            'title': 'scscccd',
            'description': 'sdcksdbskbd'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_filter_maxmin_rating(self):
        url = reverse('task-list') + f"?filter_min_rating=4&filter_max_rating=5"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail_updete(self):
        url = reverse('task-detail', args=[self.task1.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'user': self.user.id,
            'title': 'scscccd',
            'description': 'sdcksdbskbd'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail_delete(self):
        url=reverse('task-detail', args=[self.task1.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_permission(self):
        url = reverse('task-detail', args=[self.task2.id])
        self.client.force_authenticate(self.user)
        data = {
            'user': self.staff_user.id,
            'title': 'scscccd',
            'description': 'sdcksdbskbd'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)






