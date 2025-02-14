import geocoder
import folium
# Remova as importações de ipywidgets e IPython.display:
# import ipywidgets as widgets
# from ipywidgets import Layout
# from IPython.display import HTML, display

def gerar_pagina_html(ip_address):  # Função para criar a página completa
    try:
        g = geocoder.ip(ip_address)
        if not g.ok:
            return "<p>Não foi possível obter a localização.</p>"

        m = folium.Map(location=g.latlng, zoom_start=13)
        folium.Marker(
            g.latlng,
            popup=f"Localização de {ip_address}",
            tooltip=f"{g.city}, {g.state}",
            icon=folium.Icon(color="red", icon="info-sign", prefix='fa', spin=True)
        ).add_to(m)
        folium.Circle(
            radius=1000,
            location=g.latlng,
            popup="Área aproximada",
            color="crimson",
            fill=True,
            fill_color="crimson",
            fill_opacity=0.2
        ).add_to(m)

        map_html = m._repr_html_()  # Obtém o HTML do mapa

        # Monta a página HTML completa, incluindo o título animado
        html_completo = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Localizador de IP</title>
            <style>
                /* CSS do título animado (copie do código original) */
                @keyframes color-change {{
                  0% {{ color: #3498db; }}
                  50% {{ color: #e74c3c; }}
                  100% {{ color: #3498db; }}
                }}
                @keyframes pulse {{
                  0% {{ transform: scale(1); }}
                  50% {{ transform: scale(1.05); }}
                  100% {{ transform: scale(1); }}
                }}
            </style>
        </head>
        <body>
            <div style="background-color:#f0f0f0;padding:10px;border-radius:5px;text-align:center;">
              <h1 style="color:#3498db; animation: color-change 3s infinite;">Localizador de IP com IA</h1>
              <p style="color:#2ecc71; animation: pulse 2s infinite;">Descubra a localização de qualquer endereço IP!</p>
            </div>
            {map_html}  <!-- Insere o mapa aqui -->
        </body>
        </html>
        """
        return html_completo

    except Exception as e:
        return f"<p>Erro: {e}</p>"

if __name__ == "__main__":
    ip = input("Digite o endereço IP: ")  # Obtém o IP do usuário
    html = gerar_pagina_html(ip)      # Gera a página

    with open("mapa.html", "w", encoding="utf-8") as f:  # Salva em um arquivo
        f.write(html)
    print("Mapa gerado e salvo em mapa.html")