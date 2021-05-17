import requests
import json
from twilio.rest import Client
import datetime

client = Client("AC4a****************************94",
          "a8f**********************18") #Twilio SID and Auth Token
pincodes = ["133001", "134003"]
next_date = (datetime.datetime.today().date() + 
                     datetime.timedelta(1)).strftime("%d-%m-%y")
cowin_base_url = "https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode="

for each_pincode in pincodes:
    cowin_url = cowin_base_url + \
                each_pincode + \
                    "&date=" + \
                    next_date
    cowin_response = requests.get(cowin_url)
    cowin_json = 
    json.loads(cowin_response. \
                content.decode('utf8'). \
                replace("'", '"'))
    for each_center in cowin_json.get('centers'):
        for each_session in each_center.get('sessions'):
            if int(each_session.get('available_capacity')) > 0:
                client.messages.create(to="+91*******596",
                                        from_="+16*******65",                                             
                                        body= script_name +                    
                                        each_session.get('vaccine').upper() +
                                        " Vaccine is available at " +
                                        each_center.get('name') + 
                                                        " on " +
                                        each_session.get('date') + 
                                                " for age above " +
                                          str(each_session.get('min_age_limit')) +
                                          ". Slots available: " +    
                                          str(each_session.get('slots')) +
                                                      ". Only " + 
                                         str(each_session.get('available_capacity')) +                      
                                         " bookings left. Book now and get Vaccinated !!")
