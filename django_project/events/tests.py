from rest_framework.test import APITestCase
from rest_framework import status
from events.models import Event

class EventCRUDTestCase(APITestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            description="This is a test event.",
            country="USA",
            region="New York",
            address="123 Main St",
            start_date="2024-12-15",
            end_date="2024-12-16",
            start_time="12:00:00",  
            end_time="14:00:00"    
        )
        self.valid_data = {
            "title": "New Test Event",
            "description": "A valid event description.",
            "country": "USA",
            "region": "Los Angeles",
            "address": "456 Elm St",
            "start_date": "2024-12-20",
            "end_date": "2024-12-21",
            "start_time": "10:00:00",  
            "end_time": "12:00:00"    
        }


    def test_list_events(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.event.title)

    def test_retrieve_event(self):
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.event.title)

    def test_create_event(self):
        response = self.client.post('/api/events/', data=self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.last().title, "New Test Event")


    def test_update_event(self):
        updated_data = {
            "title": "Updated Event",
            "description": "Updated description.",
            "country": "USA",
            "region": "Chicago",
            "address": "789 Oak St",
            "start_date": "2024-12-22",
            "end_date": "2024-12-23"
        }
        response = self.client.put(f'/api/events/{self.event.id}/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, "Updated Event")
        self.assertEqual(self.event.region, "Chicago")

    def test_delete_event(self):
        response = self.client.delete(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)

from django.test import TestCase
from unittest.mock import patch
from events.models import Event
from events.utils import sync_events_with_local_database

from django.test import TestCase
from unittest.mock import patch
from events.models import Event
from events.utils import sync_events_with_local_database

class SyncEventsTestCase(TestCase):  # Тест синхронизации данных с внешним API

    @patch('events.utils.fetch_events_from_api')
    def test_sync_events(self, mock_fetch_events):
        mock_fetch_events.return_value = [
            {
                "id": 1,
                "title": "API Event 1",
                "description": "Description for API Event 1",
                "country": "USA",
                "region": "California",
                "address": "123 API St",
                "start_date": "2024-12-15",
                "end_date": "2024-12-16",
                "start_time": "12:00:00",  
                "end_time": "14:00:00"     
            },
            {
                "id": 2,
                "title": "API Event 2",
                "description": "Description for API Event 2",
                "country": "USA",
                "region": "Nevada",
                "address": "456 API St",
                "start_date": "2024-12-20",
                "end_date": "2024-12-21",
                "start_time": "10:00:00",  
                "end_time": "12:00:00"     
            }
        ]

        sync_events_with_local_database()

        self.assertEqual(Event.objects.count(), 2)

        event1 = Event.objects.get(id=1)
        event2 = Event.objects.get(id=2)

        self.assertEqual(event1.title, "API Event 1")
        self.assertEqual(event2.region, "Nevada")
