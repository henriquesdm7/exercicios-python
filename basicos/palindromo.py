import string
import unicodedata

def teste_palindromo(text_to_test):
    # Changes the text to lowercase
    text_to_test = text_to_test.lower()
    # Removes all accents
    text_to_test = unicodedata.normalize('NFKD', text_to_test).encode('ASCII', 'ignore').decode('ASCII')
    # Removes all punctuation
    text_to_test = text_to_test.translate(str.maketrans('', '', string.punctuation))
    # Removes all whitespaces
    text_to_test = text_to_test.replace(' ', '')
    new_word = ""

    for letter in reversed(text_to_test):
        new_word += letter

    if (new_word == text_to_test):
        return True
    else:
        return False

# text = "Socorram-me, subi no ônibus em Marrocos" # Palindromo
text = "Ana" # Palindromo
text = "texto não-palíndromo" # Não-palindromo

function_response = teste_palindromo(text)

if (function_response):
    print(f"\n{'-'*50}\nO texto '{text}' é um palíndromo.\n{'-'*50}\n")
else:
    print(f"\n{'-'*50}\nO texto '{text}' não é um palíndromo.\n{'-'*50}\n")