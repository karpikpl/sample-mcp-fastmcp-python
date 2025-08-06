from dataclasses import dataclass
from typing import List

"""
Weather API Data Models

This module contains dataclasses for parsing weather API responses.
The data models represent weather information including current conditions,
forecasts, and location data. All temperature values are provided in both
Celsius and Fahrenheit. Percentages range from 0-100. Times are in local
time zone of the queried location.

Main usage:
    from weather_models import dict_to_weather_data
    weather = dict_to_weather_data(api_response)
    current_temp = weather.current_condition[0].temp_C
"""


@dataclass
class WeatherDescription:
    """Weather condition description like 'Sunny', 'Cloudy', 'Rainy'"""
    value: str  # Human-readable weather description


@dataclass
class WeatherIcon:
    """Weather icon URL for visual representation"""
    value: str  # URL to weather icon image


@dataclass
class CurrentCondition:
    """Current weather conditions at the location"""
    FeelsLikeC: str  # Feels like temperature in Celsius
    FeelsLikeF: str  # Feels like temperature in Fahrenheit
    cloudcover: str  # Cloud coverage percentage (0-100)
    humidity: str  # Humidity percentage (0-100)
    localObsDateTime: str  # Local observation date and time
    observation_time: str  # Time of weather observation
    precipInches: str  # Precipitation amount in inches
    precipMM: str  # Precipitation amount in millimeters
    pressure: str  # Atmospheric pressure in hPa/mbar
    pressureInches: str  # Atmospheric pressure in inches of mercury
    temp_C: str  # Current temperature in Celsius
    temp_F: str  # Current temperature in Fahrenheit
    uvIndex: str  # UV index (0-11+ scale)
    visibility: str  # Visibility in kilometers
    visibilityMiles: str  # Visibility in miles
    weatherCode: str  # Numeric weather code for conditions
    weatherDesc: List[WeatherDescription]  # List of weather descriptions
    weatherIconUrl: List[WeatherIcon]  # List of weather icon URLs
    winddir16Point: str  # Wind direction in 16-point compass (e.g., 'NNE', 'SW')
    winddirDegree: str  # Wind direction in degrees (0-360)
    windspeedKmph: str  # Wind speed in kilometers per hour
    windspeedMiles: str  # Wind speed in miles per hour


@dataclass
class AreaName:
    """Geographic area name"""
    value: str  # Name of the area/city (e.g., 'London', 'New York')


@dataclass
class Country:
    """Country information"""
    value: str  # Country name (e.g., 'United Kingdom', 'United States')


@dataclass
class Region:
    """Regional/state information"""
    value: str  # Region, state, or province name


@dataclass
class WeatherUrl:
    """URL for detailed weather information"""
    value: str  # URL to weather service page for this location


@dataclass
class NearestArea:
    """Information about the nearest geographic location"""
    areaName: List[AreaName]  # List of area names (usually one item)
    country: List[Country]  # List of country info (usually one item)
    latitude: str  # Latitude coordinate as decimal degrees
    longitude: str  # Longitude coordinate as decimal degrees
    population: str  # Population of the area
    region: List[Region]  # List of region info (usually one item)
    weatherUrl: List[WeatherUrl]  # List of weather URLs (usually one item)


@dataclass
class Request:
    """Weather API request information"""
    query: str  # Original query (e.g., 'London' or 'Lat 51.51 and Lon -0.13')
    type: str  # Query type ('City', 'LatLon', etc.)


@dataclass
class Astronomy:
    """Astronomical information for the day"""
    moon_illumination: str  # Moon illumination percentage (0-100)
    moon_phase: str  # Moon phase name (e.g., 'Waxing Gibbous', 'Full Moon')
    moonrise: str  # Moonrise time (e.g., '07:44 PM')
    moonset: str  # Moonset time (e.g., '01:26 AM')
    sunrise: str  # Sunrise time (e.g., '05:32 AM')
    sunset: str  # Sunset time (e.g., '08:39 PM')


@dataclass
class HourlyWeather:
    """Detailed weather information for a specific hour"""
    DewPointC: str  # Dew point in Celsius
    DewPointF: str  # Dew point in Fahrenheit
    FeelsLikeC: str  # Feels like temperature in Celsius
    FeelsLikeF: str  # Feels like temperature in Fahrenheit
    HeatIndexC: str  # Heat index in Celsius
    HeatIndexF: str  # Heat index in Fahrenheit
    WindChillC: str  # Wind chill in Celsius
    WindChillF: str  # Wind chill in Fahrenheit
    WindGustKmph: str  # Wind gust speed in km/h
    WindGustMiles: str  # Wind gust speed in mph
    chanceoffog: str  # Chance of fog percentage (0-100)
    chanceoffrost: str  # Chance of frost percentage (0-100)
    chanceofhightemp: str  # Chance of high temperature percentage (0-100)
    chanceofovercast: str  # Chance of overcast conditions percentage (0-100)
    chanceofrain: str  # Chance of rain percentage (0-100)
    chanceofremdry: str  # Chance of remaining dry percentage (0-100)
    chanceofsnow: str  # Chance of snow percentage (0-100)
    chanceofsunshine: str  # Chance of sunshine percentage (0-100)
    chanceofthunder: str  # Chance of thunder percentage (0-100)
    chanceofwindy: str  # Chance of windy conditions percentage (0-100)
    cloudcover: str  # Cloud coverage percentage (0-100)
    diffRad: str  # Diffuse solar radiation
    humidity: str  # Humidity percentage (0-100)
    precipInches: str  # Precipitation in inches
    precipMM: str  # Precipitation in millimeters
    pressure: str  # Atmospheric pressure in hPa/mbar
    pressureInches: str  # Atmospheric pressure in inches of mercury
    shortRad: str  # Short-wave solar radiation
    tempC: str  # Temperature in Celsius
    tempF: str  # Temperature in Fahrenheit
    time: str  # Time in HHMM format (e.g., '0', '300', '600' for 00:00, 03:00, 06:00)
    uvIndex: str  # UV index (0-11+ scale)
    visibility: str  # Visibility in kilometers
    visibilityMiles: str  # Visibility in miles
    weatherCode: str  # Numeric weather code
    weatherDesc: List[WeatherDescription]  # Weather condition descriptions
    weatherIconUrl: List[WeatherIcon]  # Weather icon URLs
    winddir16Point: str  # Wind direction in 16-point compass
    winddirDegree: str  # Wind direction in degrees (0-360)
    windspeedKmph: str  # Wind speed in km/h
    windspeedMiles: str  # Wind speed in mph


@dataclass
class DailyWeather:
    """Weather forecast for a single day"""
    astronomy: List[Astronomy]  # Astronomical data (sunrise, sunset, moon phases)
    avgtempC: str  # Average temperature for the day in Celsius
    avgtempF: str  # Average temperature for the day in Fahrenheit
    date: str  # Date in YYYY-MM-DD format
    hourly: List[HourlyWeather]  # Hourly weather data for the day (usually 8 entries, every 3 hours)
    maxtempC: str  # Maximum temperature for the day in Celsius
    maxtempF: str  # Maximum temperature for the day in Fahrenheit
    mintempC: str  # Minimum temperature for the day in Celsius
    mintempF: str  # Minimum temperature for the day in Fahrenheit
    sunHour: str  # Hours of sunshine for the day
    totalSnow_cm: str  # Total snowfall for the day in centimeters
    uvIndex: str  # UV index for the day (0-11+ scale)


@dataclass
class WeatherData:
    """Complete weather API response containing current conditions and forecasts"""
    current_condition: List[CurrentCondition]  # Current weather conditions (usually one item)
    nearest_area: List[NearestArea]  # Nearest location information (usually one item)
    request: List[Request]  # Original request information (usually one item)
    weather: List[DailyWeather]  # Daily weather forecasts (usually 3-7 days)


# Helper functions to convert from dict to dataclass
# These functions parse the raw API response into typed dataclass objects
def dict_to_weather_description(data: dict) -> WeatherDescription:
    return WeatherDescription(value=data["value"])


def dict_to_weather_icon(data: dict) -> WeatherIcon:
    return WeatherIcon(value=data["value"])


def dict_to_current_condition(data: dict) -> CurrentCondition:
    return CurrentCondition(
        FeelsLikeC=data["FeelsLikeC"],
        FeelsLikeF=data["FeelsLikeF"],
        cloudcover=data["cloudcover"],
        humidity=data["humidity"],
        localObsDateTime=data["localObsDateTime"],
        observation_time=data["observation_time"],
        precipInches=data["precipInches"],
        precipMM=data["precipMM"],
        pressure=data["pressure"],
        pressureInches=data["pressureInches"],
        temp_C=data["temp_C"],
        temp_F=data["temp_F"],
        uvIndex=data["uvIndex"],
        visibility=data["visibility"],
        visibilityMiles=data["visibilityMiles"],
        weatherCode=data["weatherCode"],
        weatherDesc=[dict_to_weather_description(desc) for desc in data["weatherDesc"]],
        weatherIconUrl=[dict_to_weather_icon(icon) for icon in data["weatherIconUrl"]],
        winddir16Point=data["winddir16Point"],
        winddirDegree=data["winddirDegree"],
        windspeedKmph=data["windspeedKmph"],
        windspeedMiles=data["windspeedMiles"]
    )


def dict_to_area_name(data: dict) -> AreaName:
    return AreaName(value=data["value"])


def dict_to_country(data: dict) -> Country:
    return Country(value=data["value"])


def dict_to_region(data: dict) -> Region:
    return Region(value=data["value"])


def dict_to_weather_url(data: dict) -> WeatherUrl:
    return WeatherUrl(value=data["value"])


def dict_to_nearest_area(data: dict) -> NearestArea:
    return NearestArea(
        areaName=[dict_to_area_name(area) for area in data["areaName"]],
        country=[dict_to_country(country) for country in data["country"]],
        latitude=data["latitude"],
        longitude=data["longitude"],
        population=data["population"],
        region=[dict_to_region(region) for region in data["region"]],
        weatherUrl=[dict_to_weather_url(url) for url in data["weatherUrl"]]
    )


def dict_to_request(data: dict) -> Request:
    return Request(
        query=data["query"],
        type=data["type"]
    )


def dict_to_astronomy(data: dict) -> Astronomy:
    return Astronomy(
        moon_illumination=data["moon_illumination"],
        moon_phase=data["moon_phase"],
        moonrise=data["moonrise"],
        moonset=data["moonset"],
        sunrise=data["sunrise"],
        sunset=data["sunset"]
    )


def dict_to_hourly_weather(data: dict) -> HourlyWeather:
    return HourlyWeather(
        DewPointC=data["DewPointC"],
        DewPointF=data["DewPointF"],
        FeelsLikeC=data["FeelsLikeC"],
        FeelsLikeF=data["FeelsLikeF"],
        HeatIndexC=data["HeatIndexC"],
        HeatIndexF=data["HeatIndexF"],
        WindChillC=data["WindChillC"],
        WindChillF=data["WindChillF"],
        WindGustKmph=data["WindGustKmph"],
        WindGustMiles=data["WindGustMiles"],
        chanceoffog=data["chanceoffog"],
        chanceoffrost=data["chanceoffrost"],
        chanceofhightemp=data["chanceofhightemp"],
        chanceofovercast=data["chanceofovercast"],
        chanceofrain=data["chanceofrain"],
        chanceofremdry=data["chanceofremdry"],
        chanceofsnow=data["chanceofsnow"],
        chanceofsunshine=data["chanceofsunshine"],
        chanceofthunder=data["chanceofthunder"],
        chanceofwindy=data["chanceofwindy"],
        cloudcover=data["cloudcover"],
        diffRad=data["diffRad"],
        humidity=data["humidity"],
        precipInches=data["precipInches"],
        precipMM=data["precipMM"],
        pressure=data["pressure"],
        pressureInches=data["pressureInches"],
        shortRad=data["shortRad"],
        tempC=data["tempC"],
        tempF=data["tempF"],
        time=data["time"],
        uvIndex=data["uvIndex"],
        visibility=data["visibility"],
        visibilityMiles=data["visibilityMiles"],
        weatherCode=data["weatherCode"],
        weatherDesc=[dict_to_weather_description(desc) for desc in data["weatherDesc"]],
        weatherIconUrl=[dict_to_weather_icon(icon) for icon in data["weatherIconUrl"]],
        winddir16Point=data["winddir16Point"],
        winddirDegree=data["winddirDegree"],
        windspeedKmph=data["windspeedKmph"],
        windspeedMiles=data["windspeedMiles"]
    )


def dict_to_daily_weather(data: dict) -> DailyWeather:
    return DailyWeather(
        astronomy=[dict_to_astronomy(astro) for astro in data["astronomy"]],
        avgtempC=data["avgtempC"],
        avgtempF=data["avgtempF"],
        date=data["date"],
        hourly=[dict_to_hourly_weather(hour) for hour in data["hourly"]],
        maxtempC=data["maxtempC"],
        maxtempF=data["maxtempF"],
        mintempC=data["mintempC"],
        mintempF=data["mintempF"],
        sunHour=data["sunHour"],
        totalSnow_cm=data["totalSnow_cm"],
        uvIndex=data["uvIndex"]
    )


def dict_to_weather_data(data: dict) -> WeatherData:
    """Convert a weather API response dictionary to WeatherData dataclass."""
    return WeatherData(
        current_condition=[dict_to_current_condition(cc) for cc in data["current_condition"]],
        nearest_area=[dict_to_nearest_area(area) for area in data["nearest_area"]],
        request=[dict_to_request(req) for req in data["request"]],
        weather=[dict_to_daily_weather(day) for day in data["weather"]]
    )


# Example usage:
if __name__ == "__main__":
    # Example of how to use with your weather data
    sample_data = {
        'current_condition': [{'FeelsLikeC': '23', 'FeelsLikeF': '74', 'cloudcover': '0', 'humidity': '36', 'localObsDateTime': '2025-08-06 02:58 PM', 'observation_time': '01:58 PM', 'precipInches': '0.0', 'precipMM': '0.0', 'pressure': '1022', 'pressureInches': '30', 'temp_C': '23', 'temp_F': '73', 'uvIndex': '5', 'visibility': '10', 'visibilityMiles': '6', 'weatherCode': '113', 'weatherDesc': [{'value': 'Sunny'}], 'weatherIconUrl': [{'value': ''}], 'winddir16Point': 'WSW', 'winddirDegree': '241', 'windspeedKmph': '9', 'windspeedMiles': '6'}],
        'nearest_area': [{'areaName': [{'value': 'London'}], 'country': [{'value': 'United Kingdom'}], 'latitude': '51.517', 'longitude': '-0.106', 'population': '7421228', 'region': [{'value': 'City of London Greater London'}], 'weatherUrl': [{'value': ''}]}],
        'request': [{'query': 'Lat 51.51 and Lon -0.13', 'type': 'LatLon'}],
        'weather': []  # Simplified for example
    }
    
    # Convert to dataclass
    weather = dict_to_weather_data(sample_data)
    print(f"Current temperature: {weather.current_condition[0].temp_C}°C")
    print(f"Location: {weather.nearest_area[0].areaName[0].value}")
