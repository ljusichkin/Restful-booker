import allure
import pytest
import requests

import test_1_booking_token
import test_2_booking_create


@allure.feature('Booking Feature')
@allure.suite('Update Booking Suite')
@allure.title('Test Update Booking')
@allure.description('Test to update a booking and verify the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send PUT request to update a booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
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

    response_data = response.json()

    with allure.step('Verify firstname is updated correctly'):
        assert body['firstname'] == response_data[
            'firstname'], f"Expected firstname to be {body['firstname']}, but got {response_data['firstname']}"

    with allure.step('Verify lastname is updated correctly'):
        assert body['lastname'] == response_data[
            'lastname'], f"Expected lastname to be {body['lastname']}, but got {response_data['lastname']}"

    with allure.step('Verify totalprice is updated correctly'):
        assert body['totalprice'] == response_data[
            'totalprice'], f"Expected totalprice to be {body['totalprice']}, but got {response_data['totalprice']}"

    with allure.step('Verify depositpaid is updated correctly'):
        assert body['depositpaid'] == response_data[
            'depositpaid'], f"Expected depositpaid to be {body['depositpaid']}, but got {response_data['depositpaid']}"

    with allure.step('Verify checkin date is updated correctly'):
        assert body['bookingdates']['checkin'] == response_data['bookingdates'][
            'checkin'], f"Expected checkin to be {body['bookingdates']['checkin']}, but got {response_data['bookingdates']['checkin']}"

    with allure.step('Verify checkout date is updated correctly'):
        assert body['bookingdates']['checkout'] == response_data['bookingdates'][
            'checkout'], f"Expected checkout to be {body['bookingdates']['checkout']}, but got {response_data['bookingdates']['checkout']}"

    with allure.step('Verify additionalneeds is updated correctly'):
        assert body['additionalneeds'] == response_data[
            'additionalneeds'], f"Expected additionalneeds to be {body['additionalneeds']}, but got {response_data['additionalneeds']}"


@allure.feature('Booking Feature')
@allure.suite('Update Booking Suite')
@allure.title('Test Negative Update Booking')
@allure.description('Test to verify response when updating a booking with an invalid token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token=1231786qweiy'}

    with allure.step('Send PUT request with invalid token to update a booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'