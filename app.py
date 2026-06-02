import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Clase 1 - Programacion", layout="wide")

# Menú lateral de navegación
st.sidebar.title("Navegacion")
seccion = st.sidebar.radio("Ir a:", [
    "1. Presentacion", 
    "2. El Equipo", 
    "3. Repaso: Pensamiento Logico",
    "4. Repaso: Codigo en Python", 
    "5. La Revelacion"
])

# --- SECCION 1: PRESENTACION ---
if seccion == "1. Presentacion":
    st.title("Hola Mundo")
    st.subheader("Bienvenidos a Programacion")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Quien soy
        * **Santiago Bayaslian**
        * Estudiante de Ciencia de Datos e Inteligencia Artificial.
        * Fundador de **Saian**, una agencia de software donde desarrollamos soluciones reales para empresas.
        * Apasionado por la resolucion logica de problemas y el entrenamiento de la disciplina.
        """)
    with col2:
        st.info("Mi objetivo en esta materia: Que pasen de ser simples consumidores de tecnologia a ser creadores de sus propias herramientas.")

# --- SECCION 2: USTEDES ---
elif seccion == "2. El Equipo":
    st.title("Conociendo al equipo")
    st.write("Vamos a inicializar nuestra base de datos en vivo.")
    
    with st.form("form_intereses"):
        juego_favorito = st.text_input("Que aplicacion o videojuego utilizan con mayor frecuencia?")
        tema_dificil = st.text_input("Cual fue el concepto mas complejo que vieron hasta el momento?")
        submit = st.form_submit_button("Registrar Datos")
        
        if submit:
            st.success(f"Registro exitoso. La aplicacion mas utilizada reportada es: {juego_favorito}.")

# --- SECCION 3: REPASO - PENSAMIENTO LOGICO ---
elif seccion == "3. Repaso: Pensamiento Logico":
    st.title("Repaso: La base de todo programa")
    st.write("Antes de escribir codigo, aprendieron a estructurar el pensamiento. La maquina solo hace lo que le ordenamos mediante instrucciones precisas.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Algoritmos sin computadora")
        st.markdown("""
        Recordemos la actividad de dibujar a ciegas:
        * Tuvieron que escribir secuencias de instrucciones en texto para que otro compañero dibuje figuras geometricas.
        * Comprendieron que si la instruccion no es exacta, el resultado falla. Asi funciona exactamente una computadora.
        """)
        
    with col2:
        st.subheader("Diagramas de Flujo")
        st.markdown("""
        Aprendieron a mapear procesos paso a paso:
        * **Inicio / Fin:** El ovalo que delimita el programa.
        * **Entrada / Salida:** El paralelogramo para leer o mostrar datos.
        * **Proceso:** El rectangulo para las acciones.
        * **Decision:** El rombo para evaluar condiciones (Si/No).
        """)

# --- SECCION 4: REPASO - CODIGO EN PYTHON ---
elif seccion == "4. Repaso: Codigo en Python":
    st.title("Repaso: De Scratch a Python")
    st.write("Dieron el salto mas importante: pasar de los bloques visuales a escribir instrucciones con texto en Google Colab.")
    
    tab1, tab2, tab3 = st.tabs(["Variables e Interaccion", "Condicionales (if)", "Bucles (for)"])
    
    with tab1:
        st.subheader("Guardar y mostrar informacion")
        st.code("""
        # Creamos una variable guardando lo que el usuario escribe
        nombre = input("Como te llamas? ")
        
        # Mostramos el resultado en pantalla
        print("Hola", nombre)
        """, language="python")
        
    with tab2:
        st.subheader("Toma de decisiones")
        st.code("""
        puntos = 15
        
        # Evaluamos una condicion logica
        if puntos > 10:
            print("Ganaste")
        else:
            print("Sigue intentando")
        """, language="python")

    with tab3:
        st.subheader("Repeticion de tareas")
        st.code("""
        # Repetimos una accion una cantidad especifica de veces
        for i in range(5):
            print("Hola")
        """, language="python")

# --- SECCION 5: LA REVELACION ---
elif seccion == "5. La Revelacion":
    st.title("Arquitectura del software")
    st.subheader("En que plataforma creen que esta construida esta presentacion?")
    
    mostrar_secreto = st.button("Ejecutar diagnostico")
    
    if mostrar_secreto:
        st.error("ESTO NO ES UN ARCHIVO DE POWERPOINT.")
        st.success("Estan navegando en una aplicacion web interactiva escrita 100% en Python usando el framework Streamlit.")
        st.markdown("### El objetivo final del curso es que ustedes construyan sus propios dashboards interactivos conectando la logica de programacion con el analisis de datos reales.")
