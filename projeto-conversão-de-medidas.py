# Criar um programa em Python que faça a conversão de unidades de medida, como quilômetros para milhas, Celsius para Fahrenheit ou gramas para onças.
from time import sleep
print('\033[34mBEM VINDO AO SEU PROGRAMA DE CONVERSÃO DE MEDIDAS!\033[0m')
print('De início deixaremos você escolher que tipo de medida você quer converter: METRAGEM, TEMPERATURA, PESAGEM, IMC')
print('-' * 100)
print('\033[32mEscolha 1 para converter medidas de metragem, escolha 2 para converter unidades de temperatura, escolha 3 para converter medidas de pesagem, escolha 4 para calcular IMC!\033[0m')
escolhaInicio = int(input('\033[31mDigite aqui... \033[0m'))
if escolhaInicio == 1:
  print('\033[33mVocê escolheu a convversão de medidas de metragem, a seguir você poderá escolher as unidades para converter!\033[0m')
  sleep(2)
  print('1 para converter quilômetros, 2 para converter centímetros e 3 para converter metros')
  conversao = int(input('\033[31mDigite a sua escolha... \033[0m'))
  sleep(2)
  if conversao == 1:
    print('\033[34mVocê escolheu a conversão de quilômetros.\033[0m')
    sleep(1.5)
    km = float(input('\033[31mDigite a quilometragem a ser convertida... \033[0m'))
    cm = km * 1000000
    m = km * 1000
    print(f'\033[32mA metragem {km}km tem {m} metros e {cm} centímetros.\033[0m')
  elif conversao == 2:
    print('\033[34mVocê escolheu a conversão de centímetros.\033[0m')
    sleep(1.5)
    cm = float(input('\033[31mDigite a medida em centímetros que deseja converter... \033[0m'))
    m = cm / 100
    km = cm / 1000000
    print(f'\033[32mA medida {cm} centímetros tem {m} metros e {km} quilômetros.\033[0m')
  elif conversao == 3:
    print('\033[34mVocê escolheu a conversão de metros.\033[0m')
    sleep(1.5)
    m = float(input('\033[31mDigite a sua medida em metros que deseja converter... \033[0m'))
    cm = m * 100
    km = m / 1000
    print(f'\033[32mA medida {m} metros tem {cm} centímetros e {km} quilômetros.\033[0m')
elif escolhaInicio == 2:
  print('\033[33mVocê escolheu a conversão de temperatura, a seguri você poderá escolhar qual a unidade de medida queira converter.\033[0m')
  sleep(2)
  print('1 para converter Celsius, 2 para converter Fahrenheit ou 3 para converter Kelvin.')
  convTemp = int(input('\033[31mDigite a sua escolha... \033[0m'))
  sleep(2)
  if convTemp == 1:
    print('\033[34mVocê escolheu a conversão de Celsius para Fahrenheit e Kelvin.\033[0m')
    sleep(1.5)
    c = float(input('\033[31mDigite a temperatura em Celsius... \033[0m'))
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f'\033[32mA temperatura {c}° Celsius convertida equivale a {f}° Fahrenheit e {k}° Kelvin.\033[0m')
  elif convTemp == 2:
    print('\033[34mVocê escolheu a conversão de Fahrenheit para Celsius e Kelvin.\033[0m')
    sleep(1.5)
    f = float(input('\033[31mDigite a temperatura em Fahrenheit... \033[m'))
    c = (f - 32) * 5 / 9
    k = (f - 32) * 5 / 9 + 273.15
    print(f'\033[32mA temperatua {f}° Fahrenheit equivale a {c}° Celsius e {k}° Kelvin.\033[0m')
  elif convTemp == 3:
    print('\033[34mVocê escolheu a conversão de Kelvin para Celsius e Fahrenheit.\033[0m')
    sleep(1.5)
    k = float(input('\033[31mDigite a temperatura em Kelvin... \033[m'))
    c = k - 273.15
    f = (k - 273.15) * 9 / 5 + 32
    print(f'\033[32mA temperatura {k}° Kelvin convertida equivale a {c}° Celsius e {f}° Fahrenheit.\033[0m')
elif escolhaInicio == 3:
  print('\033[33mVocê escolheu a conversão de pesos, quilos para libras e libras para quilos, a seguir você poderá escolher as opções.\033[0m')
  sleep(2)
  print('1 para converter quilos para libras ou 2 para converter libras para quilos.')
  convPeso = int(input('\033[31mDigite sua escolha... \033[0m'))
  sleep(2)
  if convPeso == 1:
    print('033[34mVocê escolheu a conversão de quilos para libras033[0m')
    sleep(1.5)
    q = float(input('\033[31mDigite o peso em quilos para converter... \033[0m'))
    l = q * 2.205
    print(f'\033[32mConvertendo {q} quilos para libras o equivalente é {l:.2f} libras.\033[0m')
  elif convPeso == 2:
    print('\033[34mVocê escolheu a conversão de libras para quilos.\033[0m')
    sleep(1.5)
    l = float(input('\033[31mDigite o peso em libras para converter... \033[0m'))
    q = l / 2.205
    print(f'\033[32mConvertendo {l} libras para quilops é equivalente a {q:.2f} quilos.\033[0m')
elif escolhaInicio == 4:
  print('\033[33mVocê escolheu o calculo de IMC!\033[0m')
  sleep(2)
  peso = float(input('\033[31mDigite o peso... \033[0m'))
  sleep(1)
  altura = float(input('\033[31mDigite a altura em metros... \033[0m'))
  imc = peso / altura**2
  sleep(2)
  if imc < 18.5:
    print(f'\033[32mO seu IMC é {imc:.2f}. Após o calculo do seu IMC(Índice de Massa Corpórea) vemos que você está abaixo do peso ideal.\033[0m')
  elif imc > 18.5 and imc <= 25 :
      print(f'\033[32mO seu IMC é {imc:.2f}. Após o calculo do seu IMC(Índice de Massa Corpórea) vemos que você está no peso ideal.\033[0m')
  elif imc > 25 and imc <= 30 :
      print(f'\033[32mO seu IMC é {imc:.2f}. Após o calculo do seu IMC(Índice de Massa Corpórea) vemos que você está com sobrepeso.\033[0m')
  elif imc > 30 and imc <= 40 :
      print(f'\033[32mO seu IMC é {imc:.2f}. Após o calculo do seu IMC(Índice de Massa Corpórea) vemos que você está com obesidade.\033[0m')
  elif imc > 40 :
      print(f'\033[32mO seu IMC é {imc:.2f}. Após o calculo do seu IMC(Índice de Massa Corpórea) vemos que você está obesidade mórbida.\033[0m')
else:
  print('Digite um valor válido para escolher uma das opções.')