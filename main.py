from configparser import ConfigParser
import argparse

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def _get_api_key():
    config = ConfigParser
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

def read_user_cli_args():
    parser = argparse.ArgumentParser(
    description="gets weather and temperature information for a city"
    )
    parser.add_argument(
    "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
    "-i",
    "--imperial",
    action="store_true",
    help="display the temperature in imperial units",
    )
    return parser.parse_args()
# ...

if __name__ == "__main__":
    user_args = read_user_cli_args()
    print(user_args.city, user_args.imperial)

