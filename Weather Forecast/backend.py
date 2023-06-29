import requests
def get_data(city,days):
    cnt=8*days
    result=[]
    API_KEY="98337e825a8cb737d049f67d4724b168"
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
    response=requests.get(url)
    contact=response.json()
    lat=contact[0]['lat']
    lon=contact[0]['lon']
    url=f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&cnt={cnt}&appid={API_KEY}"
    response=requests.get(url)
    raw_data=response.json()
    temps=raw_data['list']
    return temps
#http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=98337e825a8cb737d049f67d4724b168

get_data("Mathura",3)