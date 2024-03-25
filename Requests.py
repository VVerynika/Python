import pytest
import requests

def create_booking(name, surname):
    url = "https://restful-booker.herokuapp.com/booking"
    data = {
        "firstname": name,
        "lastname": surname,
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-02-23",
            "checkout": "2024-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, json=data)
    return response.json()


def get_booking_by_id(id_):
    url = f"https://restful-booker.herokuapp.com/booking/{id_}"
    response = requests.get(url)
    return response.json()


# user = create_id()
# id_ = user['userid']
# get_user_by_id(id_)
@pytest.fixture
def token():
    url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, json=data)
    return response.json()['token']


# print(create_token())
# print(response.json())
# create_token()

def test_create_booking():
    name = 'Mike'
    surname = 'Simpson'

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']

    new_booking = get_booking_by_id(id_)

    assert new_booking['firstname'] == name
    assert new_booking['lastname'] == surname


def test_create_and_patch(token):
    name = 'Mike'
    surname = 'Simpson'
    new_name = 'John'
    new_surname = 'Smith'

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']

    url = f"https://restful-booker.herokuapp.com/booking/{id_}"

    headers = {'Cookie': f'token={token}'}
    new_data = {
        "firstname": new_name,
        "lastname": new_surname
    }
    response = requests.patch(url, headers=headers, json=new_data)
    result = response.json()

    assert result['firstname'] == new_name
    assert result['lastname'] == new_surname