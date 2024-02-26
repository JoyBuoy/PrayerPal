<h1>PrayerPal-Your-Personal-Prayer-Time-Announcer</h1>

<h1>Description</h1>
Never miss a prayer again with PrayerPal, your personal prayer time announcer! This Python script automatically fetches prayer times based on your location, announces them with text-to-speech, and plays customizable Azan audio files.

<h2>Features</h2>

- **Automatic Alerts:** Get notified with spoken messages and the soothing sound of the Azan (call to prayer) at each prayer time.
  
- **Customizable:** Easily switch between calculation methods to suit your preferences.
  
- **Location-Based:** Utilizes the IP Geolocation API to fetch your current location automatically.
  
- **Daily Updates:** The script runs in the background, updating prayer times every day at midnight.

<h2>Requirements</h2>

    Python 3.x
    requests library
    playsound library
    pyttsx3 library

<h1>Installation</h1>
<h2>Clone the repository</h2>

    git clone https://github.com/JoyBuoy/PrayerPal-Your-Personal-Prayer-Time-Announcer.git


<h2>Install the required libraries</h2>

Place your azan.mp3 and fajr_azan_mishary_rashid.mp3 files in the same directory as the script.


    pip install requests playsound pyttsx3
    


<h2>Usage</h2>
Run the script:

    python prayer_time_notifier.py

  The script will fetch the current location based on your IP address and then fetch the prayer times using the AlAdhan API.

  At the specified prayer times, the script will notify you with a spoken message and play the Azan.

  The script will continue to run and check the prayer times every 30 seconds. Additionally, it will update the location and prayer times from the API every day at midnight.

<h2>Customization</h2>

  You can change the method used for calculation by modifying the method variable in the script.
  To use different audio files for Azan, replace azan.mp3 and fajr_azan_mishary_rashid.mp3 with your desired audio files.

<h2>Credits</h2>

  This script uses the AlAdhan API to fetch prayer times.
  Azan audio files are provided by Mishary Rashid Alafasy.

<h1>Author</h1>
Mohammed Akram
