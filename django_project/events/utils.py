import requests
from .models import Event

API_URL = "https://themyda-beta-fde0af2b66f6.herokuapp.com/api/v1/events/"

def fetch_events_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []

def sync_events_with_local_database():
    events = fetch_events_from_api()
    for event_data in events:
        Event.objects.update_or_create(
            id=event_data['id'],
            defaults={
                'title': event_data['title'],
                'slug': event_data.get('slug'),
                'description': event_data.get('description', ''),
                'contact_phone': event_data.get('contact_phone'),
                'start_time': event_data['start_time'],
                'end_time': event_data.get('end_time'),
                'start_date': event_data['start_date'],
                'end_date': event_data.get('end_date'),
                'timelines': event_data.get('timelines'),
                'max_people_numbers': event_data.get('max_people_numbers'),
                'country': event_data['country'],
                'region': event_data['region'],
                'address': event_data['address'],
                'coordinates': event_data.get('coordinates'),
                'is_customized': event_data.get('is_customized'),
                'order_number': event_data.get('order_number'),
                'type': event_data.get('type'),
                'is_featured': event_data.get('is_featured', False),
                'in_draft': event_data.get('in_draft', False),
                'owner': event_data.get('owner', ''),
                'meta_data': event_data.get('meta_data'),
                'category': event_data.get('category', []),
                'followers': event_data.get('followers'),
            }
        )
