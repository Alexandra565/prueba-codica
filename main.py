# By Tatiana Alexandra Betancurth Paiba

# Importar la librería freecurrencyapi
import freecurrencyapi

# Petición a la API
client = freecurrencyapi.Client('fca_live_zJu1Ox8MKr9cE4A2pLthcbCvosQblpwu0Q6XMc4A')

# Dicciónario de tasas de cambio
rates = {}

# Historial de conversiones
history = []

# Funcion para obtener las tasas de cambio
def get_rates():
  result = client.latest()['data']
  for key in result:
    rates[key] = result[key]

get_rates()

# Función para mostrar la lista de monedas
def currency_list():
  result = client.latest()['data']
  print("\nLista de monedas:")
  for key in result:
    print(key)

# Función para mostrar las tasas de cambio
def rate_list():
  result = client.latest()['data']
  print("\nTasas de cambio:")
  for key in result:
    print(f"{key}: {result[key]}")

# Función para convertir monedas
def convert():
  source = input("Ingrese moneda origen: ")
  target = input("Ingrese moneda destino: ")
  amount = input("Ingrese cantidad: ")
  rate_source = rates[source.upper()]
  rate_target = rates[target.upper()]
  result = float(amount) * rate_target / rate_source
  history.append(f"{amount} {source.upper()} -> {result} {target.upper()}")
  print(f"\nEl resultado de la conversión es: {result} {target.upper()}")

# Función para mostrar el historial de conversiones
def show_history():
  for item in history:
    print("\nHistorial de conversiones:")
    print(item)

# Función para mostrar el menú
def menu():
  while True:
    print("\nMenú")
    print("1. Mostrar lista de monedas")
    print("2. Mostrar tasas de cambio")
    print("3. Establecer una moneda o dos monedas para convertir")
    print("4. Ver historial de conversiones")
    print("5. Salir\n")
    choice = int(input("Ingresa la opción : "))
    if choice == 1:
      currency_list()
    elif choice == 2:
      rate_list()
    elif choice == 3:
      convert()
    elif choice == 4:
      show_history()
    elif choice == 5:
      break
    else:
      print("Opción no válida")

menu()