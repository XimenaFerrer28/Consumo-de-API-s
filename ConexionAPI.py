import requests
#Script para conectar a una API
# Función para obtener datos de la API de usuarios
def get_users():
    url = "https://fakerapi.it/api/v1/users"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener datos de la API de usuarios")
        return None

# Función para obtener datos de la API de productos
def get_products():
    url = "https://fakerapi.it/api/v1/products"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener datos de la API de productos")
        return None

# Función para obtener datos de la API de texto
def get_text():
    url = "https://fakerapi.it/api/v1/texts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener datos de la API de texto")
        return None

# Ejemplo de uso de las funciones
def main():
    # Obtener datos de la API de usuarios
    users_data = get_users()
    if users_data:
        print("Datos de usuarios:")
        print(users_data)

    # Obtener datos de la API de productos
    products_data = get_products()
    if products_data:
        print("\nDatos de productos:")
        print(products_data)

    # Obtener datos de la API de texto
    text_data = get_text()
    if text_data:
        print("\nDatos de texto:")
        print(text_data)

if __name__ == "__main__":
    main()