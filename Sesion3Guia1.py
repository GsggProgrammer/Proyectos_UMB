# DATOS DE ENTRADA

numero = input("Ingrese el número a convertir: ").upper()  # metodo upper para pasar a mayuscula las posibles letras hexadecimales y que cumplan con el string de digitos validos
base_M = int(input("Ingrese la base M de origen (entre 2 y 16): ")) # esta base ingresada tiene que cumplir con los digitos ingresados en el numero a convertir para posteriormente pasar a decimal
base_N = int(input("Ingrese la base N de destino (entre 2 y 16): ")) # estando convertido a decimal el numero desde la base anterior, pasamos a la base que solicite el usuario aqui
# finalmente pasamos a binario e imprimimos el mensaje cumpliendo con las normas ASCII

# VALIDACIONES PERTINENTES

# Validación de rangos de base
val_base1 = 2 <= base_M <= 16
val_base2 = 2 <= base_N <= 16

# String con los digitos validos para un numero hasta hexadecimal
digitos_validos = "0123456789ABCDEF"

# Verificar que todos los caracteres del número están dentro de los dígitos válidos para la base M
verificacion_exitosa = True

for caracter in numero:
    if caracter not in digitos_validos[:base_M]:
        verificacion_exitosa = False
        break

if not (val_base1 and val_base2):
    print("Error: Las bases deben estar entre 2 y 16.")
    exit()
elif not verificacion_exitosa:
    print(f"Error: El número contiene dígitos no válidos para la base {base_M}.")
    exit()
else:
    print("Verificación exitosa. Procediendo con la conversión...")

# DATOS DE SALIDA

# Convertir de base M a decimal
potencia = 0 # se inicializa en 0 ya que en conversion de bases se sabe que la primera potencia es la base elevado a la 0
decimal = 0  # se inicializa la variable que acumula el valor decimal final del numero convertido
for i in range(len(numero) - 1, -1, -1): # este bucle recorre el largo del numero de derecha a izquierda, el -1 permite que sea asi y esto hasta el indice 0
    valor = digitos_validos.index(numero[i]) # usamos el metodo index() que es la forma mas facil de recorrer un string para buscar la posicion del caracter actual en el string de digitos validos y darle el valor numerico en base decimal
    decimal += valor * (base_M ** potencia) # Multiplica el valor numérico del dígito por la base elevada a la potencia actual y suma ese resultado a la variable acumuladora 'decimal'
    potencia += 1 # aumenta la variable de potencia inicializada en 0 para el siguiente digito a recorrer

print(f"Número en base 10: {decimal}")

# Convertir de decimal a base N
if decimal == 0: # verifica que el numero decimal
    numero_baseN = "0" # se agrega 0 en este caso porque independientemente de la base, 0 sigue siendo 0
else: # caso contrario empezamos a convertir
    numero_baseN = "" # se inicializa una cadena vacia donde se ira construyendo el numero convertido
    decimal_temporal = decimal # creamos una copia del numero decimal original para no hacer modificaciones sobre la variable original 'decimal'
    while decimal_temporal > 0: # este bucle se ejecuta hasta que el decimal sea 0
        residuo = decimal_temporal % base_N # el residuo que se extrae aca representa un nuevo digito de la base final
        numero_baseN = digitos_validos[residuo] + numero_baseN # se toma el caracter correspondiente al valor del residuo y se agrega a la izquierda del resultado porque el residuo representa el ultimo digito
        decimal_temporal = decimal_temporal // base_N # hacemos uso del operador aritmetico // para dividir sin dejar residuo (solo tomando el entero)

print(f"Número en base {base_N}: {numero_baseN}")

# Convertir a binario
binario = bin(decimal)[2:]  # hacemos uso del metodo bin que convierte un decimal a un binario automaticamente y le quito los primeros dos caracteres que imprime: '0b'
print(f"Número en binario: {binario}") # no nos vaya a bajar puntos por usar el metodo bin() profe JAJAJA

# Asegurar múltiplos de 1 byte
while len(binario) % 8 != 0: # Verificamos si la longitud del número binario resultante no es múltiplo de 8 (la logica es que el residuo tiene que ser diferente de 0 para comprobar que no sea multiplo de 8)
    binario = "0" + binario # Agregamos un 0 a la izquierda del numero binario de forma que se rellena de ceros hasta que el numero tenga 8, 16, 24, 32 bits, etc.

# Convertir a ASCII (de byte en byte o de 8 bits en 8 bits)
mensaje = "" # Inicializamos el mensaje como una cadena vacia donde se iran agregando los caracteres al convertir a ASCII
for i in range(0, len(binario), 8): # Creamos un bucle simple en el que se recorre el numero binario de 8 bits en 8 bits
    byte = binario[i:i + 8] # Separamos cada 8 bits desde la posicion i
    caracter = chr(int(byte, 2)) # convierte la variable byte (la cual guarda una cadena binaria de 8 caracteres o bits) a su valor decimal para finalmente usar el metodo chr() que convierte ese numero decimal a el caracter ASCII que corresponda
    mensaje += caracter # Se suma el caracter a la cadena vacia inicializada anteriormente y se repite el bucle hasta que no se detecten grupos de 8 bits necesarios para crear un caracter

print(f"Mensaje ASCII: {mensaje}")






    