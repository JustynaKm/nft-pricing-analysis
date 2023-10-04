import json
import os
import requests
import time


# Store your OpenSea API key in a .env file or export it in your shell
api_key = "5ca8b27583284af0bf3c733a5b131fff"

def call_api(url, params):
    """Retrieve event data"""
    headers = {"X-API-KEY": api_key}
    response = requests.get(url=url, params=params, headers=headers)


    if response.status_code != 200:
        print(f'API request failed with status code: {response.status_code}')
        print(f'Response content: {response.content}')
        raise Exception('API response: {}'.format(response.status_code))
    return response



def write_to_json_file(fn: str, data: str) -> None:
    with open(fn, 'wb') as f:
        f.write(data)

def create_event_params(token_id: str) -> dict:
    """Create query parameters for events request"""
    return {
        "token_id": token_id,
        "asset_contract_address": "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
        "limit": 100,
        "event_type": "successful"
    }

def process_many(token_ids: list, files: list, base_url: str) -> None:
    for id in token_ids:
        fn = f'events_data/events_data_{id}.json'
        if not fn in files:
            resp = call_api(base_url, params=create_event_params(token_id=id))
            data = resp.content
            write_to_json_file(fn=fn, data=data)
            print(f'Processed {fn}!')
    print("Done")

events_url = "https://api.opensea.io/api/v1/events"
files = [f'events_data/{f}' for f in os.listdir('./events_data')]
token_ids = [f'{i}' for i in range(0, 100)]
process_many(token_ids=token_ids, files=files, base_url=events_url)
