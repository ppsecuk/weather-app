# Weather app

A python-based application which retrieves weather data from external API, stores it in Amazon S3 and then shows within HTML page.


## Variables

| Variable              | Description                                          | Type   |
|-----------------------|------------------------------------------------------|--------|
| LOCATION              | Array of weather locations                           | array |
| API_KEY               | openweathermap.org API key                           | string |
| AWS_KEY_ID            | AWS KEY ID                                           | string |
| AWS_SECRET_ACCESS_KEY | AWS secret access key                                | string |

## Endpoints

http://weather-info-bucket.s3-website.eu-north-1.amazonaws.com/ to view a HTML table with weather information.

## RUN

### Local

```shell
python3 -u main.py
```

### Docker 

Run following command to build docker image

```shell
docker build -t weather-app . 
```

Run following command to run docker app

```shell
docker run weather-app
```