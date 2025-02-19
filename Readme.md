# Localizador de IP com IA e Mapa Interativo

Este projeto permite localizar geograficamente um endereço IP (de forma aproximada) e visualizar a localização em um mapa interativo.

## Tecnologias Utilizadas

*   **geocoder:** Para obter as coordenadas (latitude e longitude) a partir do endereço IP.
*   **folium:** Para gerar o mapa interativo com marcadores e visualizações.
*   **ipywidgets:** (Opcional, mas recomendado) Para criar uma interface gráfica interativa em ambientes como Jupyter Notebook e Google Colab, permitindo a inserção direta do IP.
*   **IPython.display:** (Usado com ipywidgets) Para exibir o mapa e os widgets dentro do ambiente interativo.
*   **Animações CSS:** Para um visual mais atraente no título e no marcador do mapa.

## Funcionalidades

*   **Localização aproximada:** Obtém cidade, estado/região, país, latitude e longitude a partir de um endereço IP.
*   **Mapa interativo:** Exibe a localização em um mapa, utilizando a biblioteca Folium.
*   **Marcador animado:** Marcador personalizado no mapa com ícone e animação.
*   **Círculo de imprecisão:** Um círculo ao redor do marcador indica a área aproximada da localização.
*   **Interface gráfica (opcional):** Em ambientes compatíveis (Jupyter, Colab), oferece campos de entrada e botões interativos.
*   **Tratamento de erros:** Lida com IPs inválidos ou localizações não encontradas.
*   **Título animado:** Título com animações CSS para maior destaque.

## Pré-requisitos

*   Python 3.6 ou superior.
*   Bibliotecas Python:
    *   geocoder
    *   folium
    *   ipywidgets (opcional, mas altamente recomendado)

## Instalação das Bibliotecas

Instale as bibliotecas necessárias com `pip`:

```bash
pip install geocoder folium ipywidgets
