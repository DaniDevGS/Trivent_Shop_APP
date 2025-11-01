import requests
import logging

# Configuración de logging (opcional, pero buena práctica)
logger = logging.getLogger(__name__)

# Función auxiliar para obtener la tasa de cambio (sin cambios)
def get_exchange_rate():
    """Obtiene la tasa de cambio de USD a VES desde la API."""
    # Nota: Tu clave API es visible en el código. Considera usar variables de entorno.
    API_URL = "https://v6.exchangerate-api.com/v6/37de8ccc33411893bb7d71ba/latest/USD"
    try:
        response = requests.get(API_URL, timeout=5) # timeout para evitar bloqueos
        response.raise_for_status() # Lanza un error para códigos de estado HTTP incorrectos (4xx o 5xx)
        data = response.json()
        
        # La tasa de USD a VES (Bolívar Soberano) está en el diccionario 'conversion_rates'
        if 'conversion_rates' in data and 'VES' in data['conversion_rates']:
            # *** ESTA LÍNEA RETORNA EL PRECIO DEL BOLÍVAR (VES por USD) ***
            return data['conversion_rates']['VES']
        else:
            logger.error("La respuesta de la API no contiene la tasa de VES.")
            return None # Retorna None si el formato no es el esperado

    except requests.exceptions.RequestException as e:
        logger.error(f"Error al conectar con la API de cambio: {e}")
        return None # Retorna None en caso de cualquier error de conexión
    