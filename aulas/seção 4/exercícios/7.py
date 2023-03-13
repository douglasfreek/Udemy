"""
Fahrenheit para Celsius -> fórmula: C = 5.0*(F-32.0)/9.0
"""

while True:
    try:
        far = float(input('Digite a temperatura em F: '))
    except:
        print('erro : digite um valor válido')
    else:
        celsius = (5.0 * (far - 32.0)) / 9.0
        print(f'{far} Fahrenheit convertido para Celsius é igual a {celsius:.0f}º')
        break
