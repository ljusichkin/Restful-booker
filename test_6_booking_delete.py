import allure
import requests
import pytest

import test_1_booking_token
import test_2_booking_create


@allure.feature('Booking Feature')
@allure.suite('Delete Booking Suite')
@allure.title('Test Delete Booking by ID with Valid Token')
@allure.description('Test to delete a booking by ID using a valid token and verify the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id_valid_token():
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send DELETE request to delete a booking by ID using a valid token'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'


# # Note: After deletion by ID with a valid token, this test is expected to fail
# # because the resource has been successfully removed. Ensure that the test accounts
# # for this scenario and validates the appropriate error response or status.
# # Recommendation: Comment out the test_delete_booking_by_id_valid_token function
# # and re-run the test suite to ensure that the rest of the tests function correctly.
@allure.feature('Booking Feature')
@allure.suite('Delete Booking Suite')
@allure.title('Test Delete Booking with Basic Authorization')
@allure.description('Test to delete a booking delete using Basic Authorization and expects a status code of 201 for successful deletion.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id_basic_auth():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }

    with allure.step('Send DELETE request to delete a booking by ID using Basic Authorization'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'


@allure.feature('Booking Feature')
@allure.suite('Delete Booking Suite')
@allure.title('Test Delete Booking by ID with Error Status Code')
@allure.description('This test is intentionally designed to verify handling of an error status code (403) when attempting to delete a booking.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_with_incorrect_response_status_code():
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send DELETE request to delete a booking by ID'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f' Expected status code 200, but got {response.status_code}'
