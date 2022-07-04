import requests


def test_register_successful():
    data = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }
    response = requests.post('https://reqres.in/api/register', data=data)

    assert response.status_code == 200, f'Wrong status code ({response.status_code}). Status code 200 expected'

    response_json = response.json()
    assert "id" in response_json, f"JSON doesn't have key: 'id'"
    assert response_json['id'] == 4, f"User id is {response_json['id']}. Id 4 is expected!"
