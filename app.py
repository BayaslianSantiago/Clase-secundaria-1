import streamlit as st
import pandas as pd
import sys
from io import StringIO
import contextlib

# Configuración de la página
st.set_page_config(page_title="Clase 1 - Programación", layout="wide", initial_sidebar_state="collapsed")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .stApp { background-color: #F4F6F9; }
    h1, h2, h3 { color: #007BC0 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background-color: #F39200; color: white; font-weight: bold; border-radius: 8px; border: none; padding: 10px 24px; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #D68000; color: white; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 4px 4px 0px 0px; padding-top: 10px; padding-bottom: 10px; }
    .stTabs [aria-selected="true"] { background-color: #e6f3fa; border-bottom: 3px solid #007BC0; }
    </style>
""", unsafe_allow_html=True)

# Manejo de estado
if 'slide_actual' not in st.session_state:
    st.session_state.slide_actual = 0

if 'datos_alumnos' not in st.session_state:
    st.session_state.datos_alumnos = []

diapositivas = [
    "1. Presentación",
    "2. El Equipo",
    "3. Repaso Lógico",
    "4. Repaso Python",
    "5. Código en Vivo",
    "6. La Revelación"
]

def cambiar_slide(direccion):
    if direccion == "siguiente" and st.session_state.slide_actual < len(diapositivas) - 1:
        st.session_state.slide_actual += 1
    elif direccion == "anterior" and st.session_state.slide_actual > 0:
        st.session_state.slide_actual -= 1

slide_activa = diapositivas[st.session_state.slide_actual]

# --- CONTENIDO DE LAS DIAPOSITIVAS ---

if slide_activa == "1. Presentación":
    st.title("¡Hola Mundo! 💻")
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Santiago Bayaslian
        * **Estudiante** avanzado en Ciencia de Datos e Inteligencia Artificial.
        * **Desarrollador de software de IA:** Trabajo construyendo soluciones y sistemas tecnológicos reales.
        * **Objetivo principal:** Transformarlos de simples consumidores de aplicaciones a creadores de su propia tecnología.
        """)
    with col2:
        st.info("La programación no es memorizar código, es aprender a pensar con lógica y resolver problemas de forma eficiente.")

elif slide_activa == "2. El Equipo":
    st.title("Inicializando la base de datos...")
    st.markdown("---")
    st.write("Vamos a guardar información en tiempo real en nuestro DataFrame.")
    
    col_form, col_tabla = st.columns([1, 1])
    
    with col_form:
        with st.form("form_intereses"):
            nombre_alumno = st.text_input("Nombre")
            juego_programa = st.text_input("¿Qué juego o programa te gusta usar?")
            interes = st.text_input("¿Tenés algún otro interés o hobby?")
            submit = st.form_submit_button("Registrar Dato")
            
            if submit:
                if nombre_alumno: # Se asegura de que al menos pongan el nombre
                    st.session_state.datos_alumnos.append({
                        "Nombre": nombre_alumno,
                        "Juego/Programa": juego_programa,
                        "Interés": interes
                    })
                    st.success(f"¡Dato de {nombre_alumno} registrado!")
                    st.balloons()
                else:
                    st.warning("Por favor, ingresá al menos el nombre.")
    
    with col_tabla:
        if st.session_state.datos_alumnos:
            df_alumnos = pd.DataFrame(st.session_state.datos_alumnos)
            st.dataframe(df_alumnos, use_container_width=True)
            
            csv = df_alumnos.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar Base de Datos (CSV)",
                data=csv,
                file_name='perfil_alumnos_1A.csv',
                mime='text/csv',
            )
        else:
            st.info("La base de datos está vacía. Ingresen datos para visualizar la tabla.")

elif slide_activa == "3. Repaso Lógico":
    st.title("Repaso: La base lógica")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Algoritmos Desconectados")
        st.markdown("""
        **La actividad de dibujar a ciegas:**
        * Escribieron instrucciones en texto para que un compañero dibujara figuras.
        * Comprendieron que la máquina necesita órdenes precisas. Si la instrucción no es exacta, el programa falla.
        """)
    with col2:
        st.subheader("Diagramas de Flujo")
        st.markdown("""
        **Mapeo de procesos:**
        * 🔵 **Óvalo:** Inicio / Fin del programa.
        * 🟦 **Rectángulo:** Proceso o acción.
        * 🔷 **Rombo:** Decisión lógica (Sí/No).
        * ▱ **Paralelogramo:** Entrada o Salida de datos.
        """)

elif slide_activa == "4. Repaso Python":
    st.title("El Salto: De Scratch a Python")
    st.markdown("---")
    st.write("Pasaron de unir bloques a escribir código real en Google Colab.")
    tab1, tab2, tab3 = st.tabs(["Variables y Entradas", "Condicionales (if)", "Bucles (for)"])
    with tab1:
        st.code("""
# Pedir un dato y guardarlo en memoria
nombre = input("¿Cómo te llamás? ")
# Mostrar el resultado
print("Hola", nombre)
        """, language="python")
    with tab2:
        st.code("""
# Toma de decisiones lógicas
puntos = 15
if puntos > 10:
    print("¡Ganaste la partida!")
else:
    print("Sigue intentando")
        """, language="python")
    with tab3:
        st.code("""
# Automatizar tareas repetitivas
for i in range(5):
    print("Esta instrucción se repite cinco veces")
        """, language="python")

elif slide_activa == "5. Código en Vivo":
    st.title("¡A programar!")
    st.markdown("---")
    st.write("Modifiquemos este código juntos y veamos qué pasa.")
    
    codigo_usuario = st.text_area("Consola de Python:", value='nombre = "1ro A"\nprint("¡Hola", nombre, "!")\n')
    
    if st.button("Ejecutar Código"):
        f = StringIO()
        with contextlib.redirect_stdout(f):
            try:
                exec(codigo_usuario)
                salida = f.getvalue()
                st.success("Resultado de la ejecución:")
                st.code(salida, language="text")
            except Exception as e:
                st.error(f"Error en el código: {e}")

elif slide_activa == "6. La Revelación":
    st.title("Arquitectura del Software")
    st.markdown("---")
    st.subheader("¿Con qué programa creen que estoy proyectando esto?")
    mostrar_secreto = st.button("Ejecutar diagnóstico del sistema")
    if mostrar_secreto:
        st.error("ESTO NO ES POWERPOINT.")
        st.success("Están interactuando con una aplicación web escrita 100% en Python usando la librería Streamlit.")
        st.markdown("### El objetivo del año es que construyan sistemas reales como este.")

# --- CONTROLES DE NAVEGACIÓN ---
st.markdown("---")
col_ant, col_espacio, col_sig = st.columns([1, 8, 1])
with col_ant:
    if st.session_state.slide_actual > 0:
        st.button("Anterior", on_click=cambiar_slide, args=("anterior",))
with col_sig:
    if st.session_state.slide_actual < len(diapositivas) - 1:
        st.button("Siguiente", on_click=cambiar_slide, args=("siguiente",))
    with col_form:
        with st.form("form_intereses"):
            juego_favorito = st.text_input("¿Qué aplicación o videojuego utilizan con mayor frecuencia?")
            tema_dificil = st.text_input("¿Cuál fue el concepto más complejo que aprendieron hasta hoy?")
            submit = st.form_submit_button("Registrar Dato")
            
            if submit:
                if juego_favorito or tema_dificil:
                    st.session_state.datos_alumnos.append({
                        "App/Videojuego": juego_favorito,
                        "Concepto Complejo": tema_dificil
                    })
                    st.success("¡Dato registrado!")
                    st.balloons()
    
    with col_tabla:
        if st.session_state.datos_alumnos:
            df_alumnos = pd.DataFrame(st.session_state.datos_alumnos)
            st.dataframe(df_alumnos, use_container_width=True)
            
            csv = df_alumnos.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar Base de Datos (CSV)",
                data=csv,
                file_name='perfil_alumnos.csv',
                mime='text/csv',
            )
        else:
            st.info("La base de datos está vacía. Ingresen datos para visualizar la tabla.")

elif slide_activa == "3. Repaso Lógico":
    st.title("Repaso: La base lógica")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Algoritmos Desconectados")
        st.markdown("""
        **La actividad de dibujar a ciegas:**
        * Escribieron instrucciones en texto para que un compañero dibujara figuras.
        * Comprendieron que la máquina necesita órdenes precisas. Si la instrucción no es exacta, el programa falla.
        """)
    with col2:
        st.subheader("Diagramas de Flujo")
        st.markdown("""
        **Mapeo de procesos:**
        * 🔵 **Óvalo:** Inicio / Fin del programa.
        * 🟦 **Rectángulo:** Proceso o acción.
        * 🔷 **Rombo:** Decisión lógica (Sí/No).
        * ▱ **Paralelogramo:** Entrada o Salida de datos.
        """)

elif slide_activa == "4. Repaso Python":
    st.title("El Salto: De Scratch a Python")
    st.markdown("---")
    st.write("Pasaron de unir bloques a escribir código real en Google Colab.")
    tab1, tab2, tab3 = st.tabs(["Variables y Entradas", "Condicionales (if)", "Bucles (for)"])
    with tab1:
        st.code("""
# Pedir un dato y guardarlo en memoria
nombre = input("¿Cómo te llamás? ")
# Mostrar el resultado
print("Hola", nombre)
        """, language="python")
    with tab2:
        st.code("""
# Toma de decisiones lógicas
puntos = 15
if puntos > 10:
    print("¡Ganaste la partida!")
else:
    print("Sigue intentando")
        """, language="python")
    with tab3:
        st.code("""
# Automatizar tareas repetitivas
for i in range(5):
    print("Esta instrucción se repite cinco veces")
        """, language="python")

elif slide_activa == "5. Código en Vivo":
    st.title("¡A programar!")
    st.markdown("---")
    st.write("Modifiquemos este código juntos y veamos qué pasa.")
    
    codigo_usuario = st.text_area("Consola de Python:", value='nombre = "1ro A"\nprint("¡Hola", nombre, "!")\n')
    
    if st.button("Ejecutar Código"):
        f = StringIO()
        with contextlib.redirect_stdout(f):
            try:
                # Ejecuta el código ingresado en el text_area
                exec(codigo_usuario)
                salida = f.getvalue()
                st.success("Resultado de la ejecución:")
                st.code(salida, language="text")
            except Exception as e:
                st.error(f"Error en el código: {e}")

elif slide_activa == "6. La Revelación":
    st.title("Arquitectura del Software")
    st.markdown("---")
    st.subheader("¿Con qué programa creen que estoy proyectando esto?")
    mostrar_secreto = st.button("Ejecutar diagnóstico del sistema")
    if mostrar_secreto:
        st.error("ESTO NO ES POWERPOINT.")
        st.success("Están interactuando con una aplicación web escrita 100% en Python usando la librería Streamlit.")
        st.markdown("### El objetivo del año es que construyan sistemas reales como este.")

# --- CONTROLES DE NAVEGACIÓN ---
st.markdown("---")
col_ant, col_espacio, col_sig = st.columns([1, 8, 1])
with col_ant:
    if st.session_state.slide_actual > 0:
        st.button("Anterior", on_click=cambiar_slide, args=("anterior",))
with col_sig:
    if st.session_state.slide_actual < len(diapositivas) - 1:
        st.button("Siguiente", on_click=cambiar_slide, args=("siguiente",))
        
