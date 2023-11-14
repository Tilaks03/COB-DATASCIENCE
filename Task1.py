import pandas as pd
import requests

# Define the API endpoint
api_url = 'https://randomuser.me/api/'

# Number of records to fetch
num_records = 10

# Make a request to the Random User Generator API
response = requests.get(f'{api_url}?results={num_records}')

if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Extract relevant information from the JSON response
    users = data['results']
    user_list = []

    for user in users:
        user_data = {
            'Name': f"{user['name']['first']} {user['name']['last']}",
            'Gender': user['gender'],
            'Email': user['email'],
            'Phone': user['phone'],
            'City': user['location']['city'],
            'Country': user['location']['country'],
        }
        user_list.append(user_data)

    # Create a DataFrame with the extracted information
    user_df = pd.DataFrame(user_list)

    # Save the DataFrame to a CSV file
    user_df.to_csv('random_users.csv', index=False)

    print('CSV file created successfully.')
else:
    print(f'Error: Unable to fetch data from Random User Generator API. Status code: {response.status_code}')
