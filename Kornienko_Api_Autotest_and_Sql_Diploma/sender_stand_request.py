import configuration
import requests
import data


def post_new_user(body):  # запрос на создание нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


# запрос на создание нового набора
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers)