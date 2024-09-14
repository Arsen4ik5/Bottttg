import requests
import json

# Define the API endpoints for each social network
telegram_api = "https://api.telegram.org/botYOUR_BOT_TOKEN/getChat"
vk_api = "https://api.vk.com/method/users.get"
email_api = "https://emailsearch.io/api/v1/search"

# Define the phone number to search for
phone_number = "+71234567890"

# Function to get data from Telegram API
def get_telegram_data(phone_number):
    params = {"chat_id": phone_number}
    response = requests.get(telegram_api, params=params)
    data = json.loads(response.text)
    if data["ok"]:
        return data["result"]
    else:
        return None

# Function to get data from VK API
def get_vk_data(phone_number):
    params = {"user_ids": phone_number, "fields": "city,region,address"}
    response = requests.get(vk_api, params=params)
    data = json.loads(response.text)
    if data["response"]:
        return data["response"][0]
    else:
        return None

# Function to get data from email search API
def get_email_data(phone_number):
    params = {"phone": phone_number}
    response = requests.get(email_api, params=params)
    data = json.loads(response.text)
    if data["results"]:
        return data["results"][0]
    else:
        return None

# Main function to retrieve and extract data
def get_person_data(phone_number):
    telegram_data = get_telegram_data(phone_number)
    vk_data = get_vk_data(phone_number)
    email_data = get_email_data(phone_number)

    # Extract useful data from the responses
    city = None
    region = None
    address = None
    coordinates = None
    full_name = None
    email = None
    telegram_id = None
    vk_id = None

    if telegram_data:
        city = telegram_data["city"]
        region = telegram_data["region"]
        address = telegram_data["address"]
        coordinates = (telegram_data["latitude"], telegram_data["longitude"])
        full_name = telegram_data["full_name"]

    if vk_data:
        city = vk_data["city"]
        region = vk_data["region"]
        address = vk_data["address"]
        coordinates = (vk_data["latitude"], vk_data["longitude"])
        full_name = vk_data["first_name"] + " " + vk_data["last_name"]

    if email_data:
        email = email_data["email"]
        full_name = email_data["name"]

    # Print the extracted data
    print("City:", city)
    print("Region:", region)
    print("Address:", address)
    print("Coordinates:", coordinates)
    print("Full Name:", full_name)
    print("Email:", email)
    print("Telegram ID:", telegram_id)
    print("VK ID:", vk_id)

# Call the main function with the phone number
get_person_data(phone_number)
