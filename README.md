# aaa-python-04

## issue-01
Дана функция, кодирующая строку в соответсвии с таблицей азбуки Морзе

```python
# полный код в файле morse.py
def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    """
```

Запуск: `python -m doctest -v morse.py`

Вывод: `python -m doctest -v morse.py > result_1.txt`

Результат: `result_1.txt`


## issue-02
Дана функция, декодирующая строку из азбуки Морзе в английский

```python
# полный код в файле morse.py
def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
```

Запуск: `python -m pytest -v morse_test.py`

Вывод: `python -m pytest -v morse_test.py > result_2.txt`

Результат: `result_2.txt`

## issue-03
Дана функция, кодирующая значение в бинарное представление на основе порядкового номера первого встречаемого элемента

```python
# полный код в файле one_hot_encoder.py
def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
```


Запуск: `python -m unittest -v one_hot_encoder_unittest.py`

Вывод: `python -m unittest -v one_hot_encoder_unittest.py 2> result_3.txt`

Результат: `result_3.txt`

## issue-04
Дана функция, кодирующая значение в бинарное представление на основе порядкового номера первого встречаемго элемента\

```python
# полный код в файле one_hot_encoder.py
def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
```

Запуск: `python -m pytest -v one_hot_encoder_test.py`

Вывод: `python -m pytest -v one_hot_encoder_test.py > result_4.txt`

Результат: `result_4.txt`

## issue-05
Дана функция, возвращающая текущий год. Дату и время получаем из API-worldclock

```python
# полный код в файле what_is_year_now.py
def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
```

Запуск: `python -m unittest -v what_is_year_now_unittest.py`

Вывод: `python -m unittest -v what_is_year_now_unittest.py 2> result_5.txt`

Результат: `result_5.txt`

Директория отчета о покрытии кода тестами: `htmlcov/`
