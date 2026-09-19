def text_to_numbers(text):
    numbers = []
    for char in text.lower():
        if char == ' ':
            numbers.append(99)
        elif 'a' <= char <= 'z':
            numbers.append(ord(char) - 97 + 10)
    return numbers

def numbers_to_text(numbers):
    chars = []
    for num in numbers:
        if num == 99:
            chars.append(' ')
        elif 10 <= num <= 35:
            chars.append(chr(num - 10 + 97))
    return ''.join(chars)

texto_original = "Hello World"
vetor_numeros = text_to_numbers(texto_original)
texto_decodificado = numbers_to_text(vetor_numeros)

print("Original:", texto_original)
print("Vetor:", vetor_numeros)
print("Decodificado:", texto_decodificado)