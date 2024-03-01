# para uso de expresiones regulares
import re

# para agregar colores
from colorama import Fore 

# hacer peticiones http a la pagina web
import requests

# website = "https://app.hapi.trade/"
website = "https://app.hapi.trade/asset/NVDA"
result = requests.get(website)
#convertir a texto
content = result.text

patron = r"total[\W-]*"
matches = re.findall(patron, str(content))
print(matches)