# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

in_text = 'абв абв вот пытаюсь делать дз и абв абв абв тяжело доходит абв'

def del_some_words(out_text):
    out_text = list(filter(lambda x: 'абв' not in x, in_text.split()))
    return " ".join(out_text)

out_text = del_some_words(in_text)
print(in_text)
print(out_text)
