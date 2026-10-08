import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Colwagen BI Dashboard", page_icon="🚗", layout="wide")

st.title("🚗 Colwagen BI: Gestión del Conocimiento Técnico")
st.markdown("Este dashboard interactivo simula la **Capa 4 (Interfaz de Usuario)** de nuestra arquitectura. Visualiza las fallas atípicas y sugiere soluciones basadas en el conocimiento de técnicos maestros (Modelo SECI).")

# 1. Generación de Datos Simulados (ETL Simulado)
@st.cache_data
def generar_datos():
    np.random.seed(42)
    modelos = ['VW Jetta', 'VW Tiguan', 'Audi Q5', 'SEAT Leon', 'VW Amarok']
    fallas = ['Falla mecatrónica DSG', 'Ruido columna dirección', 'Testigo EPC', 'Desprogramación módulo confort', 'Fuga refrigerante']
    tecnicos = ['Junior', 'Maestro']
    
    # Crear 500 registros simulados
    df = pd.DataFrame({
        'ID_Orden': range(1001, 1501),
        'Modelo': np.random.choice(modelos, 500),
        'Falla_Atipica': np.random.choice(fallas, 500),
        'Nivel_Tecnico': np.random.choice(tecnicos, 500, p=[0.7, 0.3]),
        'Tiempo_Diagnostico_Min': np.random.randint(30, 120, 500)
    })
    
    # Simular que los técnicos Junior tardan más sin la herramienta de gestión de conocimiento
    df.loc[df['Nivel_Tecnico'] == 'Junior', 'Tiempo_Diagnostico_Min'] += np.random.randint(30, 90, size=(df['Nivel_Tecnico'] == 'Junior').sum())
    
    # Inventario asociado a la solución
    inventario_solucion = {
        'Falla mecatrónica DSG': 'Kit Mecatrónica (Ref: 0AM325025)',
        'Ruido columna dirección': 'Grasa especial y ajuste de torque',
        'Testigo EPC': 'Sensor de oxígeno (Ref: 06K906262)',
        'Desprogramación módulo confort': 'Actualización Software ODIS',
        'Fuga refrigerante': 'Bomba de agua (Ref: 06L121111H)'
    }
    df['Repuesto_Sugerido'] = df['Falla_Atipica'].map(inventario_solucion)
    return df

datos = generar_datos()

# 2. Panel Lateral (Filtros BI)
st.sidebar.header("Filtros de Búsqueda")
modelo_seleccionado = st.sidebar.selectbox("Seleccione Modelo de Vehículo:", ['Todos'] + list(datos['Modelo'].unique()))

if modelo_seleccionado != 'Todos':
    datos = datos[datos['Modelo'] == modelo_seleccionado]

# 3. Métricas Principales (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total de Casos Analizados", len(datos))
col2.metric("Tiempo Promedio Diagnóstico", f"{int(datos['Tiempo_Diagnostico_Min'].mean())} min")
col3.metric("Falla Más Frecuente", datos['Falla_Atipica'].mode()[0])

st.divider()

# 4. Gráficos de Business Intelligence
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Frecuencia de Fallas Atípicas")
    fig1 = px.bar(datos['Falla_Atipica'].value_counts().reset_index(), 
                  x='Falla_Atipica', y='count', 
                  labels={'Falla_Atipica': 'Tipo de Falla', 'count': 'Cantidad de Casos'},
                  color='count', color_continuous_scale='Blues')
    st.plotly_chart(fig1, use_container_width=True)

with col_graf2:
    st.subheader("Impacto del Conocimiento: Tiempo de Diagnóstico")
    st.markdown("*Muestra cómo los Técnicos Maestros resuelven más rápido gracias a la experiencia.*")
    fig2 = px.box(datos, x='Nivel_Tecnico', y='Tiempo_Diagnostico_Min', 
                  color='Nivel_Tecnico', 
                  labels={'Nivel_Tecnico': 'Nivel del Técnico', 'Tiempo_Diagnostico_Min': 'Minutos'})
    st.plotly_chart(fig2, use_container_width=True)

# 5. Repositorio de Lecciones Aprendidas (Gestión del Conocimiento)
st.subheader("📚 Motor de Recomendación y Lecciones Aprendidas")
st.markdown("Al ingresar un síntoma, el sistema extrae la solución histórica validada por técnicos maestros y cruza con el inventario.")
falla_busqueda = st.selectbox("Seleccione el síntoma detectado en el escáner:", datos['Falla_Atipica'].unique())

solucion = datos[datos['Falla_Atipica'] == falla_busqueda]['Repuesto_Sugerido'].iloc[0]
st.success(f"**Solución / Repuesto Sugerido:** {solucion}")
st.dataframe(datos[datos['Falla_Atipica'] == falla_busqueda].head(5))
