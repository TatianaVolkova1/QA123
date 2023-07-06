import requests
from config import *

def test_get_users(get_users):
    assert get_users.status_code == 200, 'Error: wrong status code'
    req = get_users.json()
    assert(req['data'][0]['last_name']) == 'Lawson'

def test_get_user():
    r = requests.get(url_get_user)
    assert r.status_code == 200
    req = r.json()
    assert(req['data']['first_name']) == 'Janet'

def test_post_user():
    r = requests.post(url=url_create_user, data=params_create_user)
    assert r.status_code == 201


def test_get_list_resource():
    r = requests.get(url_get_list_resource)
    assert r.status_code == 200, 'Error: wrong status code'
    req = r.json()
    assert(req['data'][2]['name']) == 'true red'

def test_get_user_not_found():
    r = requests.get(url_get_user_not_found)
    assert r.status_code == 404, 'Error: wrong status code'
    req = r.json()
    assert not req

def test_get_resource_not_found():
    r = requests.get(url_get_resource_not_found)
    assert r.status_code == 404, 'Error: wrong status code'
    req = r.json()
    assert not req
