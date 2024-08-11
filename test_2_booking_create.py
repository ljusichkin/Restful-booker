import pytest
import requests
import allure

my_bookingid = 0


@allure.feature('Booking Feature')
@allure.suite('Create Booking Suite')
@allure.title('Test Create Booking')
@allure.description('Test to create a booking and verify the response.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking():
    body = {
        "firstname": "Lusine",
        "lastname": "Avetisyan",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-09-09",
            "checkout": "2023-09-16"
        },
        "additionalneeds": "All Inclusive"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a booking'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
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

    with allure.step('Verify "bookingid" is present in response'):
        assert 'bookingid' in response_data, 'Booking ID not found in response'

    with allure.step('Verify "booking" is present in response'):
        assert "booking" in response_data, "'booking' field not found in response data"

    response_booking = response_data['booking']

    with allure.step('Verify "firstname" is correct'):
        assert 'firstname' in response_booking, 'First name not found in booking'
        assert response_booking['firstname'] == body['firstname'], f"Expected firstname to be {body['firstname']} but got '{response_booking['firstname']}'"

    with allure.step('Verify "lastname" is correct'):
        assert 'lastname' in response_booking, "'lastname' key not found in response"
        assert response_booking['lastname'] == body['lastname'], f"Expected lastname to be {body['lastname']} but got '{response_booking['lastname']}'"

    with allure.step('Verify "totalprice" is correct'):
        assert 'totalprice' in response_booking, "'totalprice' key not found in response"
        assert response_booking['totalprice'] == body['totalprice'], f"Expected totalprice to be {body['totalprice']} but got '{response_booking['totalprice']}'"

    with allure.step('Verify "depositpaid" is correct'):
        assert 'depositpaid' in response_booking, "'depositpaid' key not found in response"
        assert response_booking['depositpaid'] == body['depositpaid'], f"Expected depositpaid to be {body['depositpaid']} but got '{response_booking['depositpaid']}'"

    with allure.step('Verify "bookingdates" is correct'):
        assert 'bookingdates' in response_booking, "'bookingdates' key not found in response"
        assert 'checkin' in response_booking['bookingdates'], "'checkin' key not found in 'bookingdates'"
        assert response_booking['bookingdates']['checkin'] == body['bookingdates']['checkin'], f"Expected checkin to be {body['bookingdates']['checkin']} but got '{response_booking['bookingdates']['checkin']}'"
        assert 'checkout' in response_booking['bookingdates'], "'checkout' key not found in 'bookingdates'"
        assert response_booking['bookingdates']['checkout'] == body['bookingdates']['checkout'], f"Expected checkout to be {body['bookingdates']['checkout']} but got '{response_booking['bookingdates']['checkout']}'"

    with allure.step('Verify "additionalneeds" is correct'):
        assert 'additionalneeds' in response_booking, "'additionalneeds' key not found in response"
        assert response_booking['additionalneeds'] == body['additionalneeds'], f"Expected additionalneeds to be {body['additionalneeds']} but got '{response_booking['additionalneeds']}'"

    with allure.step('Attach response text for debugging'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

    global my_bookingid
    my_bookingid = response_data['bookingid']

