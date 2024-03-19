import configuration
import data
import requests


# Этап.1 Создание пользователя
def post_new_user(user_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json = user_body,
	                     headers = data.headers)


# Этап.2 Получение токена авторизации пользователя
def get_new_user_token():
	response = post_new_user(data.user_body)
	return response.json().get("authToken")


# Этап.3 Создание набора под пользователем
def post_new_kit(kit_body):
	data.headers["Authorization"] += get_new_user_token()
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
	                     json = kit_body,
	                     headers = data.headers)