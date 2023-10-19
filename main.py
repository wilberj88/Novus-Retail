import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit_echarts import st_echarts
import plotly.figure_factory as ff
import altair as alt
import datetime
import plotly.graph_objects as go
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import urllib, json
import folium
from streamlit_folium import st_folium

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Retail", page_icon="🛒")

st.title('Novus Retail 🛒 Automated Cycle')

st.header("Mandos (5) ⚙️ & Atentos (2)🤖")
st.subheader("Demand, Competence, Stock, Sales & Optimal Ubications 🎯")
st.subheader("New Sales & Confirmn, Welcoming & Support Clients")


colored_header(
    label="Mando 1: Demanda en Tiendas",
    description="Ventas Históricas y Proyectadas, por categorías, productos, horarios y precios",
    color_name="violet-70",
)

colored_header(
    label="Mando 2: Competencia 15km a la redonda",
    description="Productos y precios por categorías",
    color_name="violet-70",
)

colored_header(
    label="Mando 3: Inventario Óptimo en Tiendas",
    description="Vencimientos, Rotación y Rentabilidad",
    color_name="violet-70",
)

colored_header(
    label="Mando 4: Ubicaciones Óptimas de Nuevas Tiendas",
    description="Demanda Proyectada, Competencia Circundante y Desbalance de Mercado",
    color_name="violet-70",
)

colored_header(
    label="Mando 5: Promociones Recomendadas por Tiendas",
    description="Por mes, hora, clima y perfil de usuarios / Combo 5",
    color_name="violet-70",
)


colored_header(
    label="Atento 1: Atención de Clientela",
    description="Recepción, atención, venta y acompañamiento",
    color_name="violet-70",
)

colored_header(
    label="Atento 2: Generador de Nuevas Ventas",
    description="Estrategia de comercialización por día y hora con nuevos y ex clientes",
    color_name="violet-70",
)
    
col4, col5 = st.columns(2)
with col4:
    fig1 = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Fuente1", "Fuente2", "Fuente 3", "Online", "Offline", "Ingresos Totales"],
        color = "blue"
      ),
      link = dict(
        source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
        target = [3, 4, 3, 5, 5],
        value = [8, 4, 5, 13, 4]
    ))])
  
    fig1.update_layout(title_text="Ingresos 2023", font_size=10)
    st.plotly_chart(fig1, theme="streamlit")

with col5:
    fig1 = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Egresos Totales", "Necesidades", "Gastos", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
        color = "red"
      ),
      link = dict(
        source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
        target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        value = [44, 44, 44, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
    ))])
  
    fig1.update_layout(title_text="Egresos 2023", font_size=10)
    st.plotly_chart(fig1, theme="streamlit")

col6, col7 = st.columns(2)
with col6:
    option = {
        "title": {"text": "Eficacia de la Campaña", "subtext": "Porcentaje Conversión(%)"},
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            }
        },
        "legend": {"data": ["Contactados", "Interesados", "Persuadidos", "Comprometidos", "Votantes"]},
        "series": [
            {
                "name": "Contactados",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "label": {"formatter": "{b}%"},
                "labelLine": {"show": False},
                "itemStyle": {"opacity": 0.7},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                },
                "data": [
                    {"value": 60, "name": "Persuadidos"},
                    {"value": 40, "name": "Comprometidos"},
                    {"value": 20, "name": "Votantes"},
                    {"value": 80, "name": "Interesados"},
                    {"value": 100, "name": "Contactados"},
                ],
            },
            {
                "name": "Margen",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "maxSize": "80%",
                "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                },
                "data": [
                    {"value": 30, "name": "Persuadidos"},
                    {"value": 10, "name": "Comprometidos"},
                    {"value": 5, "name": "Votantes"},
                    {"value": 50, "name": "Interesados"},
                    {"value": 80, "name": "Contactados"},
                ],
                "z": 100,
            },
        ],
    }
    st_echarts(option, height="500px")    

with col7:
    option = {
        "legend": {},
        "tooltip": {"trigger": "axis", "showContent": False},
        "dataset": {
            "source": [
                ["product", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                ["Conservador", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ["Verde", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ["Polo", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ["Liberal", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
            ]
        },
        "xAxis": {"type": "category"},
        "yAxis": {"gridIndex": 0},
        "grid": {"top": "55%"},
        "series": [
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "pie",
                "id": "pie",
                "radius": "30%",
                "center": ["50%", "25%"],
                "emphasis": {"focus": "data"},
                "label": {"formatter": "{b}: {@2012} ({d}%)"},
                "encode": {"itemName": "product", "value": "Junio", "tooltip": "Junio"},
            },
        ],
    }
    st_echarts(option, height="500px", key="echarts")




zona_1 = pd.DataFrame({
   'lon':[10.473583, 10.474139, 10.478472, 10.468500, 10.469667, 10.474139],
   'lat':[-73.248639, -73.25125, -73.245361, -73.247278, -73.238056, -73.25125],
   'name':['PV1 COL. Nacional Loperena', 'PV2 ESC Bellas Artes', 'PV3 UDES', 'PV4 COL Prudencia Daza', 'PV5 COL SantoDomingo', 'PV6 COL Parroquial El Carmelo'],
   'value':[7588, 4933,3771, 2735, 5666, 57]
}, dtype=str)


st.write('')
colored_header(
    label="Georreferenciación de Top 3 Zonas de Mayores Gastos en 2023",
    description="Por hora y tipo",
    color_name="violet-70",
)

# center on Liberty Bell, add marker
m = folium.Map(location=[10.4735, -73.2486], zoom_start=13)
n = folium.Map(location=[10.45358, -73.26678], zoom_start=13)
l = folium.Map(location=[10.44664, -73.30750], zoom_start=13)

#zona1
folium.Marker(
    [10.47358, -73.248639], popup="Z1 PV1 PV1 COL Nacional Loperena 3de10K", tooltip="Z1 PV1 PV1 COL Nacional Loperena. 3K de 8K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474139, -73.25125], popup="Z1 PV2 PV2 ESC Bellas Artes. 2K de 5K", tooltip="Z2 PV2 PV2 ESC Bellas Artes. 2K de 5K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.478472, -73.245361], popup="Z1 PV3 PV3 UDES. 1,5K de 4K", tooltip="Z1 PV3 PV3 UDES. 1,5K de 4K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.468500, -73.247278], popup="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", tooltip="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.469667, -73.238056], popup="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", tooltip="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474130, -73.251115], popup="PV6 COL Parroquial El Carmelo (Nuevo 2023)", tooltip="PV6 COL Parroquial El Carmelo", icon=folium.Icon(icon='cloud')
).add_to(m)
#zona2
folium.Marker(
    [10.46006, -73.22889], popup="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", tooltip="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.46322, -73.23575], popup="Z2 PV2 PV8 I.E. Manuel Germán Cuello. 2K de 4K", tooltip="Z2 PV1 PV8 I.E. Manuel Germán Cuello. 2K de 4K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45389, -73.24211], popup="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", tooltip="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45100, -73.23672], popup="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", tooltip="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", icon=folium.Icon(icon='flag')
).add_to(m)
#zona3
folium.Marker(
    [10.44578, -73.25128], popup="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", tooltip="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.44950, -73.25075], popup="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", tooltip="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.45131, -73.25711], popup="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", tooltip="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.45714, -73.25153], popup="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", tooltip="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.43650, -73.25356], popup="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", tooltip="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", icon=folium.Icon(icon='star')
).add_to(n)
#zona4
folium.Marker(
    [10.45358, -73.26678], popup="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", tooltip="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.45892, -73.25958], popup="Z4 PV2 PV21 COL Nacionalizado UPAR. 3,5K de 8K", tooltip="Z4 PV2 PV21 COL Nacionalizado UPAR 8K. 3,5K de 8K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.46157, -73.26789], popup="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", tooltip="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.46661, -73.25814], popup="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", tooltip="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.44381, -73.27533], popup="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", tooltip="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", icon=folium.Icon(icon='info-sign')
).add_to(m)
#zona5
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", tooltip="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", tooltip="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47928, -73.27719], popup="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", tooltip="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47842, -73.29089], popup="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", tooltip="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.48606, -73.28081], popup="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", tooltip="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
#zona6
folium.Marker(
    [10.48044, -73.24781], popup="Z6 PV1 PV33 COL. Pablo Sexto 5K", tooltip="Z6 PV1 PV33 COL. Pablo Sexto 5K", color='red'
).add_to(m)
folium.Marker(
    [10.48181, -73.25644], popup="Z6 PV2 PV34 CONC.San Joaquin 4K", tooltip="Z6 PV2 PV34 CONC.San Joaquin 4K", color='red'
).add_to(l)
folium.Marker(
    [10.49319, -73.26533], popup="Z6 PV3 PV35 COL. Sagrada Familia 3K", tooltip="Z6 PV3 PV35 COL. Sagrada Familia 3K", color='red'
).add_to(l)
#zona7
folium.Marker(
    [10.47475, -73.25969], popup="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", tooltip="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", color='red'
).add_to(l)
#zona8
folium.Marker(
    [10.46442, -73.25625], popup="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", tooltip="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", color='red'
).add_to(l)
folium.Marker(
    [10.44664, -73.30750], popup="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", tooltip="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", color='red'
).add_to(l)

colA, colB, colC = st.columns(3)
with colA:
    st_data = st_folium(m, width=300)
with colB:
    st_data = st_folium(n, width=300)
with colC:
    st_data = st_folium(l, width=300)

colored_header(
    label="Alarmas Financieras 2023",
    description="Por intensidad y categoría",
    color_name="violet-70",
)

col1, col2, col3 = st.columns(3)
with col1:
  acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 50, "name": "Liquidez"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col2:
  acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 85, "name": "Endeudamiento"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col3:
  acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 20, "name": "Solvencia"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)

st.write("---")

colored_header(
    label="Plan Financiero 2024",
    description="Fuentes y Usos",
    color_name="violet-70",
)
url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

fig.update_layout(title_text="Proyección Financiera 2024<br>Modelación por <a href='https://www.novussolutions.io'>Novus Mando</a>",
                  font_size=10)
st.plotly_chart(fig, theme="streamlit")

random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
my_grid = grid(2, 3, 4, vertical_align="bottom")
# Row 1:
my_grid.dataframe(random_df, use_container_width=True)
my_grid.line_chart(random_df, use_container_width=True)
# Row 2:
my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
my_grid.text_input("Your name")
my_grid.button("Send", use_container_width=True)
# Row 3:
my_grid.button("Example 1", use_container_width=True)
my_grid.button("Example 2", use_container_width=True)
my_grid.button("Example 3", use_container_width=True)
my_grid.button("Example 4", use_container_width=True)
# Row 4 (uses the spec from row 1):
with my_grid.expander("Show Filters", expanded=True):
    st.slider("Filter by Age", 0, 100, 50)
    st.slider("Filter by Height", 0.0, 2.0, 1.0)
    st.slider("Filter by Weight", 0.0, 100.0, 50.0)
my_grid.dataframe(random_df, use_container_width=True)
