import allure
import pytest
import requests

import test_1_booking_token
import test_2_booking_create


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Partial Update Booking with Token')
@allure.description('Test to verify response when partially updating a booking with token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send PATCH request to partially update a booking'):
        response = requests.patch(
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

    with allure.step('Verify totalprice is present in response'):
        assert 'totalprice' in response_data, "'totalprice' key not found in response"

    with allure.step('Verify depositpaid is present in response'):
        assert 'depositpaid' in response_data, "'depositpaid' key not found in response"

    with allure.step('Verify bookingdates is present in response'):
        assert 'bookingdates' in response_data, "'bookingdates' key not found in response"

    with allure.step('Verify checkin date is present in bookingdates'):
        assert 'checkin' in response_data['bookingdates'], "'checkin' key not found in 'bookingdates'"

    with allure.step('Verify checkout date is present in bookingdates'):
        assert 'checkout' in response_data['bookingdates'], "'checkout' key not found in 'bookingdates'"

    with allure.step('Verify additionalneeds is present in response'):
        assert 'additionalneeds' in response_data, "'additionalneeds' key not found in response"


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Negative Partial Update Booking with Invalid Token')
@allure.description('Test to verify response when partially updating a booking with an invalid token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_booking():
    body = {
        "firstname": "Celine",
        "lastname": "Dion"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token=123dvfvsf'}

    with allure.step('Send PATCH request with invalid token to partially update a booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Negative Partial Update Booking without Token')
@allure.description('Test to verify response when partially updating a booking without providing a token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_without_token_booking():
    body = {
        "firstname": "Sally",
        "lastname": "Hansen"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send PATCH request without token to partially update a booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, 'Expected status code 403, but got {response.status_code}'


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Partial Update Booking with Basic Authorization')
@allure.description('Test to verify response when partially updating a booking with basic authorization instead of using a token')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_booking_with_basic_authorization():
    body = {
        "firstname": "Kim",
        "lastname": "Kardashian"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }
    with allure.step('Send PATCH request with authorization basic to partially update a booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

