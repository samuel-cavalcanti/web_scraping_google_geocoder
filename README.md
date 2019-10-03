# web scraping google geocoder

## Requisitos 
python selenium version: __3.141.0-1__  
BeautifulSoup version: __4.8.0-1__  
Obs: Foi testado usando python 3.7   
Verifique se possui o web driver Chrome instalado também !!  
A instalação do web driver varia de acordo com a sua distribuição gnu/linux.

## Exemplo de uso:   
```python

from google_geocoder import Geocoder

def test():
    address_list = ["Unidade Básica de Saúde do Centro", "Unidade Básica do Conjunto Cônego Monte",
                    "Posto de saúde do DNR"]
    geo = Geocoder()
    for address in cycle(address_list):
        location_gps = geo.geocoding(address)
        print(location_gps)


if __name__ == '__main__':
    test()

```  

Em resumo a classe Geocoder só possui um método publico chamado: __geocoding__ a qual recebe um endereço (string) e retora uma uma lista que são as coordenadas latitude e longitude respectivamente.  