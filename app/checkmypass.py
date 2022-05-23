import requests
import hashlib

# password = 'password123'
# hash_pass = 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
hash_pass_ini = 'CBFDA'  # first 5 chars from hashed password


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the api and try again!')
    print(response)
    # print(response.text)
    return response


def pwned_api_check(password):
    # check password if it exists in api response
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password


# request_api_data(hash_pass_ini)
print(pwned_api_check(hash_pass_ini))
