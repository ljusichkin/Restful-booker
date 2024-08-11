import allure
import pytest
import requests

my_token = None


@allure.feature('Booking Feature')
@allure.suite('Create Token Booking Suite')
@allure.title('Test Booking Token Creation')
@allure.description('Test to create authentication token for booking API.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_booking_create_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create token'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/auth',
            json=body,
            headers=headers
        )

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify "token" is present in response'):
        assert 'token' in response.json(), 'Token not found in response JSON'

    with allure.step('Verify "token" length is greater than zero'):
        assert len(response.json().get('token', '')) > 0, 'Token not generated or empty'

    global my_token
    my_token = response.json().get('token')

