import streamlit as st
import pandas as pd
import sys
from io import StringIO
import contextlib

# Configuracion de la pagina
st.set_page_config(page_title="Clase 1 - Programacion", layout="wide", initial_sidebar_state="collapsed")

# Estilos CSS personalizados (Modo Oscuro para Proyector)
st.markdown("""
    <style>
    /* Fondo oscuro de alto contraste */
    .stApp { background-color: #121212; color: #FFFFFF; }
    
    /* Textos generales en blanco/gris claro */
    p, li, span, label, div { color: #E0E0E0; }
    
    /* Titulos en azul brillante (celeste) para resaltar en oscuro */
    h1, h2, h3 { color: #4DA8DA !important; font-family: 'Segoe UI', Tahoma, sans-serif; }
    
    /* Botones naranjas Innova */
    .stButton>button { background-color: #F39200; color: white !important; font-weight: bold; border-radius: 8px; border: none; padding: 10px 24px; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #D68000; color: white !important; border: 1px solid #FFF; }
    
    /* Pestañas */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #E0E0E0; height: 50px; background-color: transparent; border-radius: 4px 4px 0px 0px; padding-top: 10px; padding-bottom: 10px; }
    .stTabs [aria-selected="true"] { background-color: #1E1E1E; border-bottom: 3px solid #4DA8DA; color: #FFFFFF !important; font-weight: bold;}
    
    /* Inputs y consolas */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #2D2D2D !important; color: white !important; border: 1px solid #4DA8DA; }
    
    /* Cajas de alerta (info, success, error) */
    div[data-testid="stAlert"] { background-color: #1E1E1E !important; border: 1px solid #333 !important; }
    div[data-testid="stAlert"] * { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# Manejo de estado
if 'slide_actual' not in st.session_state:
    st.session_state.slide_actual = 0

if 'datos_alumnos' not in st.session_state:
    st.session_state.datos_alumnos = []

diapositivas = [
    "1. Presentacion",
    "2. El Equipo",
    "3. Repaso Logico",
    "4. Repaso Python",
    "5. Codigo en Vivo",
    "6. La Revelacion"
]

def cambiar_slide(direccion):
    if direccion == "siguiente" and st.session_state.slide_actual < len(diapositivas) - 1:
        st.session_state.slide_actual += 1
    elif direccion == "anterior" and st.session_state.slide_actual > 0:
        st.session_state.slide_actual -= 1

slide_activa = diapositivas[st.session_state.slide_actual]

# --- CONTENIDO DE LAS DIAPOSITIVAS ---

if slide_activa == "1. Presentacion":
    st.title("¡Hola Mundo!")
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Santiago Bayaslian
        * **Estudiante** avanzado en Ciencia de Datos e Inteligencia Artificial.
        * **Desarrollador de software de IA:** Trabajo construyendo soluciones y sistemas tecnologicos reales.
        * **Objetivo principal:** Transformarlos de simples consumidores de aplicaciones a creadores de su propia tecnologia.
        """)
    with col2:
        st.info("La programacion no es memorizar codigo, es aprender a pensar con logica y resolver problemas de forma eficiente.")

elif slide_activa == "2. El Equipo":
    st.title("Inicializando la base de datos...")
    st.markdown("---")
    st.write("Vamos a guardar informacion en tiempo real en nuestro DataFrame.")
    
    col_form, col_tabla = st.columns([1, 1])
    
    with col_form:
        with st.form("form_intereses"):
            nombre_alumno = st.text_input("Nombre")
            juego_programa = st.text_input("¿Que juego o programa te gusta usar?")
            interes = st.text_input("¿Tenes algun otro interes o hobby?")
            submit = st.form_submit_button("Registrar Dato")
            
            if submit:
                if nombre_alumno:
                    st.session_state.datos_alumnos.append({
                        "Nombre": nombre_alumno,
                        "Juego/Programa": juego_programa,
                        "Interes": interes
                    })
                    st.success(f"¡Dato de {nombre_alumno} registrado!")
                    st.balloons()
                else:
                    st.warning("Por favor, ingresa al menos el nombre.")
    
    with col_tabla:
        if st.session_state.datos_alumnos:
            df_alumnos = pd.DataFrame(st.session_state.datos_alumnos)
            st.dataframe(df_alumnos, use_container_width=True)
            
            csv = df_alumnos.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Descargar Base de Datos (CSV)",
                data=csv,
                file_name='perfil_alumnos_1A.csv',
                mime='text/csv',
            )
        else:
            st.info("La base de datos esta vacia. Ingresen datos para visualizar la tabla.")

elif slide_activa == "3. Repaso Logico":
    st.title("Repaso: La base logica")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Algoritmos Desconectados")
        st.markdown("""
        **La actividad de dibujar a ciegas:**
        * Escribieron instrucciones en texto para que un compañero dibujara figuras.
        * Comprendieron que la maquina necesita ordenes precisas. Si la instruccion no es exacta, el programa falla.
        """)
    with col2:
        st.subheader("Diagramas de Flujo")
        st.markdown("""
        **Mapeo de procesos:**
        * **Ovalo:** Inicio / Fin del programa.
        * **Rectangulo:** Proceso o accion.
        * **Rombo:** Decision logica (Si/No).
        * **Paralelogramo:** Entrada o Salida de datos.
        """)

elif slide_activa == "4. Repaso Python":
    st.title("El Salto: De Scratch a Python")
    st.markdown("---")
    st.write("Pasaron de unir bloques a escribir codigo real en Google Colab.")
    
    tab1, tab2, tab3 = st.tabs(["Variables y Entradas", "Condicionales (if)", "Bucles (for)"])
    
    with tab1:
        st.code("# Pedir un dato y guardarlo en memoria\nnombre = input('¿Como te llamas? ')\n\n# Mostrar el resultado\nprint('Hola', nombre)", language="python")
        
    with tab2:
        st.code("# Toma de decisiones logicas\npuntos = 15\n\nif puntos > 10:\n    print('¡Ganaste la partida!')\nelse:\n    print('Sigue intentando')", language="python")
        
    with tab3:
        st.code("# Automatizar tareas repetitivas\nfor i in range(5):\n    print('Esta instruccion se repite cinco veces')", language="python")

elif slide_activa == "5. Codigo en Vivo":
    st.title("¡A programar!")
    st.markdown("---")
    st.write("Modifiquemos este codigo juntos y veamos que pasa.")
    
    codigo_usuario = st.text_area("Consola de Python:", value='nombre = "1ro A"\nprint("¡Hola", nombre, "!")')
    
    if st.button("Ejecutar Codigo"):
        f = StringIO()
        with contextlib.redirect_stdout(f):
            try:
                exec(codigo_usuario)
                salida = f.getvalue()
                st.success("Resultado de la ejecucion:")
                st.code(salida, language="text")
            except Exception as e:
                st.error(f"Error en el codigo: {e}")

elif slide_activa == "6. La Revelacion":
    st.title("Arquitectura del Software")
    st.markdown("---")
    st.subheader("¿Con que programa creen que estoy proyectando esto?")
    
    mostrar_secreto = st.button("Ejecutar diagnostico del sistema")
    
    if mostrar_secreto:
        st.error("ESTO NO ES POWERPOINT.")
        st.success("Estan interactuando con una aplicacion web escrita 100% en Python usando la libreria Streamlit.")
        st.markdown("### El objetivo del año es que construyan sistemas reales como este.")

# --- CONTROLES DE NAVEGACION ---
st.markdown("---")
col_ant, col_espacio, col_sig = st.columns([1, 8, 1])

with col_ant:
    if st.session_state.slide_actual > 0:
        st.button("Anterior", on_click=cambiar_slide, args=("anterior",))

with col_sig:
    if st.session_state.slide_actual < len(diapositivas) - 1:
        st.button("Siguiente", on_click=cambiar_slide, args=("siguiente",))
