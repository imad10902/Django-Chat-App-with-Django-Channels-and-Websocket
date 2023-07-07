from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
from datetime import datetime, timedelta

CAL_ID = config("CAL_ID") #loading id from env file
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "./google-credentials.json"


def test_calendar(request):
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = googleapiclient.discovery.build("calendar", "v3", credentials=credentials)

    # CREATING A NEW EVENT
    if request.method == "POST":
        # Extracting the details from the form data
        event_title = request.POST.get("event_title")
        location = request.POST.get("location")
        start_date = request.POST.get("start_date")
        start_time = request.POST.get("start_time")
        doctor_first_name = request.POST.get("doctor_first_name")
        speciality = request.POST.get("speciality")
        doctor_email = request.POST.get("doctor_email")
        start_datetime = datetime.strptime(
            f"{start_date} {start_time}", "%Y-%m-%d %H:%M"
        )
        end_datetime = start_datetime + timedelta(minutes=45)
        end_date_str = end_datetime.date().isoformat()
        end_time_str = end_datetime.time().isoformat()
        # Creating a new event
        new_event = {
            "summary": event_title,
            "location": location,
            "start": {"date": start_date},
            "end": {"date": end_date_str},
            "attendees": {"email": doctor_email},
            "sendNotifications": True,
            "transparency": "transparent",
            "extendedProperties": {
                "private": {
                    "speciality": speciality,
                    "doctor_first_name": doctor_first_name,
                    "start_time": start_time,
                    "end_time": end_time_str,
                }
            },
        }

        service.events().insert(calendarId=CAL_ID, body=new_event).execute()

    # GETTING ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get("items", [])

    return events
