import requests
from dotenv import load_dotenv
import os
import argparse

load_dotenv()
api_key = os.getenv('API_KEY')


def get_github_data(username):
    
    
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.github+json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json()
        for event in events:
            print(f"{event['type']} at {event['created_at']}")
    else:
        print(f"Failed to fetch data: {response.status_code}")
parser = argparse.ArgumentParser(description='Retrieve Github User activity')
parser.add_argument('username', type=str, help='Github username')

args = parser.parse_args()
get_github_data(args.username)

        
