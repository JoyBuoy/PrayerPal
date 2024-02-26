import requests
from datetime import datetime
from playsound import playsound
import pyttsx3
import time

method = 2  # Islamic Society of North America (ISNA)


def get_prayer_times(year, month, day, latitude, longitude, method=2):
    base_url = f"http://api.aladhan.com/v1/calendar/{year}/{month}"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "method": method
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])[day - 1]  # Adjust day index
    else:
        print("Failed to fetch data.")
        return None


def get_current_location():
    response = requests.get('https://ipinfo.io/json')
    data = response.json()
    coordinates = data.get('loc', '').split(',')
    latitude, longitude = map(float, coordinates)
    return latitude, longitude


def check_prayer_times(prayer_data):
    fajr_time = prayer_data['timings']['Fajr'].split()[0]
    zuhr_time = prayer_data['timings']['Dhuhr'].split()[0]
    asr_time = prayer_data['timings']['Asr'].split()[0]
    maghrib_time = prayer_data['timings']['Maghrib'].split()[0]
    isha_time = prayer_data['timings']['Isha'].split()[0]

    # Converting the time strings to datetime objects inorder to compare, since they are of different datatypes.
    fajr_datetime = datetime.strptime(fajr_time, "%H:%M")
    zuhr_datetime = datetime.strptime(zuhr_time, "%H:%M")
    asr_datetime = datetime.strptime(asr_time, "%H:%M")
    maghrib_datetime = datetime.strptime(maghrib_time, "%H:%M")
    isha_datetime = datetime.strptime(isha_time, "%H:%M")

    # Get the current system time
    current_time = datetime.now().time()

    # Play Azan at prayer times
    if current_time.hour == fajr_datetime.hour and current_time.minute == fajr_datetime.minute:
        engine.say("Its time for Fajr")
        engine.runAndWait()
        play_fajr_azan()
        time.sleep(240)
    elif current_time.hour == zuhr_datetime.hour and current_time.minute == zuhr_datetime.minute:
        engine.say("Its time for Zuhar")
        engine.runAndWait()
        play_azan()
        time.sleep(240)
    elif current_time.hour == asr_datetime.hour and current_time.minute == asr_datetime.minute:
        engine.say("Its time for Asar")
        engine.runAndWait()
        play_azan()
        time.sleep(240)
    elif current_time.hour == maghrib_datetime.hour and current_time.minute == maghrib_datetime.minute:
        engine.say("Its time for Maghrib")
        engine.runAndWait()
        play_azan()
        time.sleep(240)
    elif current_time.hour == isha_datetime.hour and current_time.minute == isha_datetime.minute:
        engine.say("Its time for Isha")
        engine.runAndWait()
        play_azan()
        time.sleep(240)


def play_azan():
    playsound("azan.mp3")


def play_fajr_azan():
    playsound("fajr_azan_mishary_rashid.mp3")


if __name__ == "__main__":
    engine = pyttsx3.init()

    while True:
        # Get current system date
        current_date = datetime.now()

        # Extract year, month, and day
        year = current_date.year
        month = current_date.month
        day = current_date.day

        # Determining the current location
        location = get_current_location()
        if location:
            latitude = location[0]
            longitude = location[1]

        method = 2  # Islamic Society of North America (ISNA)
        prayer_data = get_prayer_times(year, month, day, latitude, longitude, method)

        if prayer_data:
            check_prayer_times(prayer_data)

        else:
            print("Failed to fetch prayer times.")

        # Sleep for 30 seconds before checking again
        time.sleep(30)

        # Check location and API every 24 hours
        if current_date.hour == 0 and current_date.minute == 0:
            location = get_current_location()
            if location:
                latitude = location[0]
                longitude = location[1]

            prayer_data = get_prayer_times(year, month, day, latitude, longitude, method)

            if prayer_data:
                check_prayer_times(prayer_data)

            else:
                print("Failed to fetch prayer times.")
