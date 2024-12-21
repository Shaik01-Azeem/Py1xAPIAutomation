from src.constants.api_constants import BASE_URL, APIConstants, base_url

def test_crud():
    print(BASE_URL)

    url_direct = base_url()
    print(url_direct)

    url_class = APIConstants.base_url()
    print(url_class)
