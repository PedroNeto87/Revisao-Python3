frase = 'Curso em Video Python'
print(frase)
print('='*20)
print('Fatimaneto de String')
print('=' * 20)
print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('=' * 24)
print('Transformação de String')
print('=' * 24)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase_strip = '  Curso em Video Python   '
print(frase_strip.strip())
print('=' * 7)
print('Divisão')
print('=' * 7)
print(frase.split())
print('=' * 7)
print('Junção')
print('=' * 7)
frase_nova = ['Curso', 'em', 'Video']
print(" ".join(frase_nova))