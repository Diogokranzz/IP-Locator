# Localizador de IP com IA e Mapa Interativo

Este projeto permite que você localize geograficamente um endereço IP (aproximadamente) e visualize a localização em um mapa interativo.  Ele utiliza as seguintes tecnologias:

*   **geocoder:**  Para obter as coordenadas (latitude e longitude) a partir do endereço IP.
*   **folium:**  Para gerar o mapa interativo com marcadores e visualizações.
*   **ipywidgets:** (Opcional, mas recomendado) Para criar uma interface gráfica interativa dentro de ambientes como Jupyter Notebook e Google Colab, permitindo que o usuário insira o IP diretamente.
*   **IPython.display:** (Junto com ipywidgets) Para exibir o mapa e os widgets dentro do ambiente interativo.
*   **Animações CSS:** Para dar um toque visual mais interessante ao título e ao marcador do mapa.

## Funcionalidades

*   **Localização aproximada:**  Obtém a cidade, estado/região, país, latitude e longitude a partir de um endereço IP.
*   **Mapa interativo:**  Exibe a localização em um mapa usando a biblioteca Folium.
*   **Marcador animado:**  Um marcador personalizado no mapa com um ícone e animação.
*   **Círculo de imprecisão:**  Um círculo ao redor do marcador indica a área aproximada da localização.
*   **Interface gráfica (opcional):**  Se usado em um ambiente compatível (Jupyter, Colab), oferece campos de entrada e botões interativos.
*   **Tratamento de erros:**  Lida com casos em que o IP é inválido ou a localização não pode ser encontrada.
*   **Título animado:** Um título com animações CSS chama a atenção do usuário.

## Pré-requisitos

*   Python 3.6 ou superior.
*   Bibliotecas Python:
    *   `geocoder`
    *   `folium`
    *   `ipywidgets` (opcional, mas recomendado)

## Instalação das Bibliotecas

Você pode instalar as bibliotecas necessárias usando o `pip`:

```bash
pip install geocoder folium ipywidgets
```

## Uso

### Em um Jupyter Notebook ou Google Colab

```python
import geocoder
import folium

# Exemplo de uso
ip_address = '192.168.1.1'  # Substitua pelo IP que você deseja localizar
location = geocoder.ip(ip_address)

# Cria o mapa
m = folium.Map(location=[location.lat, location.lng], zoom_start=15)

# Adiciona um marcador ao mapa
folium.Marker(location=[location.lat, location.lng], popup=location.city).add_to(m)
```

### Em um Ambiente Python Simples

```python
import geocoder
import folium

# Exemplo de uso
ip_address = '192.168.1.1'  # Substitua pelo IP que você deseja localizar

# Obtém a localização do IP
location = geocoder.ip(ip_address)

# Cria o mapa
m = folium.Map(location=[location.lat, location.lng], zoom_start=15)

# Adiciona um marcador ao mapa
folium.Marker(location=[location.lat, location.lng], popup=location.city).add_to(m)
```

## Contribuições

Sinta-se à vontade para contribuir com este projeto. Você pode abrir um problema ou enviar um pull request.#   I P - L o c a t o r  
 