import requests
from src.utils import s3
from src.config import secrets

location = ["Tallinn", "London", "Prague"]
for x in location:
    apiKey = secrets.API_KEY
    location = x
    filename = f"datasets/weather-in-{location}.html"
    chunk_size = 100
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&mode=html")

    # Generate a file
    with open(filename,'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

    # Upload to S3
    s3.upload_file(f"datasets/weather-in-{location}.html", "weather-info-bucket")