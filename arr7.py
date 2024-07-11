def remove_smileys(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+2] == ":-" and (text[i+2] == ")" or text[i+2] == "("):
            # Пропускаем символы, входящие в состав смайлика
            i += 3
        else:
            # Добавляем символ в результирующую строку
            result += text[i]
            i += 1
    return result

text = "я работаю в Гугле :-)))"
print(remove_smileys(text))