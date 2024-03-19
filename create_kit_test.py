import data
import sender_stand_request

# Переменные для проверки большого кол-ва символов
large511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
large512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


# Генерация набора для тестов
def get_kit_body(name):
    correct_kit_body = data.kit_body.copy()
    correct_kit_body["name"] = name
    return correct_kit_body


# Функция для позитивной проверки
def positive_assertion(name):
    kit_body_positive = get_kit_body(name)
    kit_body_positive_response = sender_stand_request.post_new_kit(kit_body_positive)
    assert kit_body_positive_response.json()["name"] == name
    assert kit_body_positive_response.status_code == 201


# Функция для негативной проверки
def negative_assertion(name):
    kit_body_negative = get_kit_body(name)
    kit_body_negative_response = sender_stand_request.post_new_kit(kit_body_negative)
    assert kit_body_negative_response.status_code == 400

# Функция для негативной проверки, когда тело запроса пустое
def negative_assertion_no_name(kit_body):
    kit_no_name = sender_stand_request.post_new_kit(kit_body)
    assert kit_no_name.status_code == 400

# Тест.1 Допустимое количество символов (1) ++
def test_kit_1_in_name_get_success_response():
    positive_assertion("a")

# Тест.2 Допустимое количество символов (511) ++
def test_kit_511_in_name_get_success_response():
    positive_assertion(large511)

# Тест.3 Количество символов меньше допустимого (0) +-
def test_kit_0_in_name_get_error_response():
    negative_assertion("")

# Тест.4 Количество символов больше допустимого (512) +-
def test_kit_512_in_name_get_error_response():
    negative_assertion(large512)

# Тест.5 Разрешены английские буквы: (QWErty) ++
def test_kit_eng_in_name_get_success_response():
    positive_assertion("QWErty")

# Тест.6 Разрешены русские буквы: (Мария) ++
def test_kit_rus_in_name_get_success_response():
    positive_assertion("Мария")

# Тест.7 Разрешены спецсимволы: ("№%@",) ++
def test_kit_spec_in_name_get_success_response():
    positive_assertion("\"№%@\",")

# Тест.8 Разрешены пробелы: ( Человек и КО ) ++
def test_kit_space_in_name_get_success_response():
    positive_assertion(" Человек и КО ")

# Тест.9 Разрешены цифры: (123) ++
def test_kit_num_in_name_get_success_response():
    positive_assertion("123")

# Тест.10 Параметр не передан в запросе +-
def test_kit_type_no_name_get_error_response():
    correct_kit_body_no_name = data.kit_body.copy()
    correct_kit_body_no_name.pop("name")
    negative_assertion_no_name(correct_kit_body_no_name)

# Тест.11 Передан другой тип параметра (123) +-
def test_kit_type_in_name_get_error_response():
    negative_assertion(123)