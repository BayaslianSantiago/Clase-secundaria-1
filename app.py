import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Clase 1 - Programación", layout="wide", initial_sidebar_state="collapsed")

# Estilos CSS personalizados (Identidad visual del colegio Innova)
st.markdown("""
    <style>
    /* Fondo general más limpio */
    .stApp {
        background-color: #F4F6F9;
    }
    /* Color azul principal para títulos */
    h1, h2, h3 {
        color: #007BC0 !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Color naranja para los botones */
    .stButton>button {
        background-color: #F39200;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #D68000;
        color: white;
    }
    /* Cajas de información con bordes y sombras sutiles */
    .css-1r6slb0, .css-12oz5g7 {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #90C226; /* Detalle verde institucional */
    }
    /* Estilizar las pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e6f3fa;
        border-bottom: 3px solid #007BC0;
    }
    </style>
""", unsafe_allow_html=True)

# Manejo de estado para la navegación tipo diapositivas
if 'slide_actual' not in st.session_state:
    st.session_state.slide_actual = 0

diapositivas = [
    "1. Presentación",
    "2. El Equipo",
    "3. Repaso Lógico",
    "4. Repaso Python",
    "5. La Revelación"
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
        * **Fundador de Saian**: Agencia de software donde desarrollamos soluciones y sistemas reales para empresas.
        * **Objetivo principal:** Transformarlos de simples consumidores de aplicaciones a creadores de su propia tecnología.
        """)
    with col2:
        st.info("La programación no es memorizar código, es aprender a pensar con lógica y resolver problemas de forma eficiente.")

elif slide_activa == "2. El Equipo":
    st.title("Inicializando la base de datos...")
    st.markdown("---")
    
    st.write("Vamos a guardar información en tiempo real.")
    
    with st.form("form_intereses"):
        juego_favorito = st.text_input("¿Qué aplicación o videojuego utilizan con mayor frecuencia en el aula?")
        tema_dificil = st.text_input("¿Cuál fue el concepto más complejo que aprendieron hasta hoy?")
        submit = st.form_submit_button("Registrar Datos en el Servidor")
        
        if submit:
            st.success(f"¡Registro exitoso! La aplicación más utilizada es: **{juego_favorito}**.")

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

elif slide_activa == "5. La Revelación":
    st.title("Arquitectura del Software")
    st.markdown("---")
    
    st.subheader("¿Con qué programa creen que estoy proyectando esto?")
    
    mostrar_secreto = st.button("Ejecutar diagnóstico del sistema")
    
    if mostrar_secreto:
        st.error("ESTO NO ES POWERPOINT.")
        st.success("Están interactuando con una aplicación web escrita 100% en Python usando la librería Streamlit.")
        st.markdown("### El objetivo del año es que construyan sistemas reales como este.")

# --- CONTROLES DE NAVEGACIÓN (Botones Inferiores) ---
st.markdown("---")
col_ant, col_espacio, col_sig = st.columns([1, 8, 1])

with col_ant:
    if st.session_state.slide_actual > 0:
        st.button("Anterior", on_click=cambiar_slide, args=("anterior",))

with col_sig:
    if st.session_state.slide_actual < len(diapositivas) - 1:
        st.button("Siguiente", on_click=cambiar_slide, args=("siguiente",))
