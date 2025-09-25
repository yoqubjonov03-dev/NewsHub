from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from blok_app.models import Task, Comment

class CommentTest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='user', password='adminroot')
        self.staff_user=User.objects.create_user(username='admin', password='adminroot')
        self.task = Task.objects.create(user=self.user, title='Qabullar boshlandi',
                                         description='oliy talimga qabullar boshlandi')
        self.comment = Comment.objects.create(title=self.task, content='zor habar', rating=5)
        self.comment2 = Comment.objects.create(title=self.task, content='yahshi', rating=4)

    def test_comment_list(self):
        url = reverse('comment-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_comment_create(self):
        url = reverse('comment-list')

        data  = {
            'title':self.task.id ,
            'content':'zor habar',
            'rating': 4
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_delete(self):
        url = reverse('comment-detail', args=[self.comment2.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)







