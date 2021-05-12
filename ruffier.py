# Модуль для расчета результатов

# Здесь должен быть твой код




txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая.
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
Обратитесь к врачу!''')
txt_res.append('''средняя.
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')



def test(P1, P2, P3, age):
    if age < 7:
        return (txt_index + "0", txt_nodata) # тайна сия не для теста сего
    else:
        r_index = ruffier_index(P1, P2, P3) # расчет
        result = txt_res[ruffier_result(r_index, neud_level(age))] # интерпретация, перевод числового уровня подготовки в текстовые данные
        return (txt_index + str(r_index), txt_workheart + result) # возвращаем кортеж из двух строк для вывода человеку

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4 # это не будет выполняться, если мы уже вернули ответ "неуд"
    if r_index >= level:
        return 1
    level = level - 5 # аналогично, попадаем сюда, если уровень как минимум "уд"
    if r_index >= level:
        return 2
    level = level - 5.5 # следующий уровень
    if r_index >= level:
        return 3
    return 4 # здесь оказались, если индекс меньше всех промежуточных уровней, т.е. тестируемый крут.

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2 # каждые 2 года разницы от 7 лет превращаются в единицу - вплоть до 15 лет
    result = 21 - norm_age * 1.5 # умножаем каждые 2 года разницы на 1.5, так распределены уровни в таблице
    return result

def ruffier_index(P1, P2, P3):
    return (4 * (P1+P2+P3) - 200) / 10


























