import requests
def get_data(place,forcast_days):
    api_key="c059a49da4e1f5b4c6a4ed68faf468c8"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forcast_days
    filtered_data=filtered_data[:nr_values]
    return filtered_data
if __name__=="__main__":
    get_data(place,forcast_days)