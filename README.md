# COVID-19 Vaccine Booking
This repository helps you to book the slot  for getting a COVID-19 vaccine in India from COWIN portal by sending you the SMS whenever a booking is available.

## Prerequisite:
You need to have a Twilio account. Its pretty easy to create one. Once you create a trial account, it gives 15$ to use, which is more than sufficient for this task. Just keep the SID and Auth token and a phone number (which you get free in Twilio)

![twilio](https://user-images.githubusercontent.com/30747497/118460031-f22c7f80-b719-11eb-8022-e2f64c4c717b.png)


## How to run the Script:
### 1. Download the code or copy paste the script in some text file and name it as cowin_scrape.py and note its path.
Lets say C:\Users\tseth\Documents\cowin_scripts\cowin_scrape.py
  - Update the SID, auth token, pincodes you want to scrape, to: and from: phone numbers. Your from: phone number will be the one shown in the Twilio dashboard and To: is your own   number where you want to send the sms.

### 2. Create a Windows task scheduler 
- create a new task as cowin_scheduler and update the user/group to SYSTEM (else you will get black screen popup whenever the script runs).
- Then go to Conditions and uncheck the "Start the task only if the computer is on AC power".
- Go to trigger, select a time to start the task and add 1 minute in "Repeat task every:":
  #### If you are on MAC or Ubuntu:
  then run a crontab instead of task scheduler; its similar to that.
  crontab -e
  In the vim editor, type i for insert, then write the following:
  */1 * * * * C:\Users\tseth\Documents\cowin_scripts\cowin_script.py >> C:\Users\tseth\Documents\cowin_scripts\cowin_script_log.txt 2>&1

And thats all. You have your COWIN notifier running. Whenever it finds any slot, you will get and SMS similar to this:

