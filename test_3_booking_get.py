import allure
import pytest
import requests

import test_2_booking_create


@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Test Getting all Bookings')
@allure.description('This test retrieves all bookings and checks the response status and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Send request to get all bookings'):
        response = requests.get("https://restful-booker.herokuapp.com/booking")

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    with allure.step('Verify the response contains a non-empty list'):
        assert len(response.json()) > 0, 'The list should not be empty'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )


@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Test Getting Booking by ID')
@allure.description('This test retrieves a booking by ID and checks the response status and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_id():
    with allure.step('Send request to get booking by ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "firstname"'):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step('Verify the response contains "lastname"'):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"

    with allure.step('Verify the response contains "totalprice"'):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step('Verify the response contains "depositpaid"'):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step('Verify the response contains "bookingdates"'):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step('Verify the response contains "checkin"'):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step('Verify the response contains "checkout"'):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step('Verify the response contains "additionalneeds"'):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step('Verify the value of "depositpaid" is boolean'):
        assert response_data['depositpaid'] is True or response_data['depositpaid'] is False, 'ERRORRR depositpaid'

    with allure.step('Verify the value of "totalprice" is a number'):
        assert isinstance(response_data['totalprice'], (int, float)), 'Total price should be a number'

    with allure.step('Validate deposit paid status'):
        assert response_data['depositpaid'] in [True, False], 'ERROR DEPOSIT PAID'

    with allure.step('Validate total price type'):
        assert isinstance(response_data['totalprice'], (int, float)), 'Error total price type'


@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Verify Booking Retrieval by Query Name')
@allure.description('This test verifies that bookings can be retrieved using a combination of first and last name query parameters.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_query_name():
    firstname = 'Lusine'
    lastname = 'Avetisyan'

    with allure.step("Sending GET request to retrieve booking"):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking?firstname={firstname}&lastname={lastname}')

    with allure.step("Checking response status code"):
        assert response.status_code == 200, f'Request failed: Expected status code 200, got {response.status_code}'

    with allure.step("Verifying the response contains bookings"):
        assert len(response.json()) != 0, 'No bookings found for the given name.'


@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Verify Booking Retrieval by Check-in and Check-out Dates')
@allure.description('This test verifies that bookings can be retrieved using specific check-in and check-out date query parameters.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_query_date():
    checkin = "2023-03-13"
    checkout = "2024-04-13"

    with allure.step("Send GET request to retrieve bookings by date"):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking?checkin={checkin}&checkout={checkout}')

    with allure.step("Check if the response status code is 200"):
        assert response.status_code == 200, f'Request failed: Expected status code 200, got {response.status_code}'

    with allure.step("Verify the response contains bookings"):
        assert len(response.json()) != 0, 'No bookings found for the given dates.'

