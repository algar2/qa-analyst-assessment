"""
Alfonso Garcia
19 October 2025

Take-Home Assignment Part 2: Basic API Testing

The following file consists of simple automated tests for the target API, 
JSONPlaceholder, covering basic GET and POST requests, as well as error handling

"""

import requests


ENDPOINT = "https://jsonplaceholder.typicode.com"

class TestJSONPlaceholderAPI:

    def test_fetch_user_successfully(self):
        """
        Method for fetching a user and validating the response's structure: id,
        name, email all exist 

        Test endpoint: 'GET /users/1'
        """
        response = requests.get(ENDPOINT + "/users/1")
        data = response.json()

        # Check if request was successful
        assert response.status_code == 200, f"Unexpected status code {response.status_code}"

        # Check if required fields exist as keys in response
        assert "id" in data, "'id' is not found in JSON response"
        assert "name" in data, "'name' is not found in JSON response"
        assert "email" in data, "'email' is not found in JSON response"


    def test_create_new_post(self):
        """
        Method for creating a new post and verifying its creation. 
        Test endpoint: 'POST /posts'
        """

        # Creating a sample payload 
        payload = {
            "userId": 11,
            "id": 101,
            "title": "test title",
            "body": "test body"
        }

        create_task_response = requests.post(ENDPOINT + '/posts', json=payload)
        # Post successfully created 
        assert create_task_response.status_code == 201

        data = create_task_response.json()

        # Validating that created post contains sent JSON data
        assert data['userId'] == payload['userId']
        assert data['id'] == payload['id']
        assert data['title'] == payload['title']
        assert data['body'] == payload['body']
        


    def test_handle_nonexistent_user(self):
        """
        Method for testing for 404 response for non-existent resource
        Validates 404 status code and has an appropriate response 
        """
        # Attempting to fetch user information 
        get_response = requests.get(ENDPOINT + '/users/999')
        status_code = get_response.status_code

        # If does not exist, code should be 404 
        assert status_code == 404, f"Expected 404, got {status_code} instead."
        print("User 999 does not exist")


    






