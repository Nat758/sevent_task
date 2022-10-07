# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких 
# форматах.


from unicodedata import name
from controller import work_with_ponebook


if name == 'main':
    work_with_ponebook()