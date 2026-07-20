# =============================================================================
# PROYECTO 1 - APLICACIÓN EN STREAMLIT
# Especialización Python for Analytics | Módulo 1 - Python Fundamentals
# Autor: Otto Morales Gómez
# Año: 2026
# -----------------------------------------------------------------------------
# Esta aplicación integra los conceptos fundamentales del módulo:
# variables, estructuras de datos, control de flujo, funciones,
# programación funcional y programación orientada a objetos (POO).
#
# Para ejecutarla localmente:
#     streamlit run app.py
# =============================================================================

# --- Importación de librerías ---
# streamlit : framework para construir la interfaz web interactiva
# pandas    : manejo de tablas de datos (DataFrame)
# numpy     : manejo de arreglos numéricos (arrays)
import streamlit as st
import pandas as pd
import numpy as np

# --- Importación de las librerías externas del proyecto ---
# De la librería de funciones usamos calcular_wacc (área financiera).
# De la librería de clases usamos ProyectoInversion (VPN, ROI y Payback).
from libreria_funciones_proyecto1 import calcular_wacc
from libreria_clases_proyecto1 import ProyectoInversion

# =============================================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Proyecto 1 - Otto Morales",
    page_icon="🐍",
    layout="wide"
)

# =============================================================================
# INICIALIZACIÓN DEL ESTADO DE LA SESIÓN (st.session_state)
# -----------------------------------------------------------------------------
# Streamlit vuelve a ejecutar todo el script cada vez que el usuario
# interactúa con un widget. Para que los datos NO se pierdan entre
# interacciones, se guardan en st.session_state.
# =============================================================================

# Ejercicio 1: lista vacía donde se registran los movimientos del flujo de caja
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Ejercicio 2: arrays de NumPy (uno por cada campo del registro de productos)
if "arr_productos" not in st.session_state:
    st.session_state.arr_productos = np.array([], dtype=object)   # nombres
    st.session_state.arr_categorias = np.array([], dtype=object)  # categorías
    st.session_state.arr_precios = np.array([], dtype=float)      # precios
    st.session_state.arr_cantidades = np.array([], dtype=int)     # cantidades
    st.session_state.arr_totales = np.array([], dtype=float)      # totales

# Ejercicio 3: histórico de resultados de la función WACC
if "historico_wacc" not in st.session_state:
    st.session_state.historico_wacc = []

# Ejercicio 4: diccionario de proyectos de inversión para el CRUD
# La clave es el nombre del proyecto y el valor es un objeto ProyectoInversion
if "proyectos" not in st.session_state:
    st.session_state.proyectos = {}

# =============================================================================
# MENÚ LATERAL DE NAVEGACIÓN
# =============================================================================
st.sidebar.title("📌 Navegación")
seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)
st.sidebar.markdown("---")
st.sidebar.caption("Proyecto 1 · Otto Morales Gómez · 2026")


# =============================================================================
# SECCIÓN HOME
# =============================================================================
def mostrar_home():
    """Muestra la página de presentación del proyecto."""
    st.title("🐍 Proyecto 1 - Aplicación Interactiva en Streamlit")
    st.subheader("Especialización Python for Analytics")

    col_izq, col_der = st.columns([1, 2])

    with col_izq:
        # Logo de Python (imagen representativa del proyecto)
        st.image(
            "https://www.python.org/static/community_logos/python-logo-generic.svg",
            width=280
        )

    with col_der:
        st.markdown("""
        ### 👨‍💼 Información del estudiante

        | Campo | Detalle |
        |---|---|
        | **Nombre** | Otto Morales Gómez |
        | **Módulo** | Módulo 1 - Python Fundamentals |
        | **Curso** | Especialización Python for Analytics |
        | **Perfil** | Ingeniero y MBA |
        | **País** | Perú 🇵🇪 |
        | **Año** | 2026 |
        """)

    st.markdown("---")

    st.markdown("""
    ### 📋 Descripción del proyecto

    Esta aplicación integra los conceptos fundamentales aprendidos en el
    Módulo 1: **variables, estructuras de datos, control de flujo, funciones,
    programación funcional y programación orientada a objetos (POO)**,
    presentados en una interfaz interactiva desarrollada con Streamlit.

    ### 🧩 Secciones de la aplicación

    - **Ejercicio 1:** Flujo de caja con listas.
    - **Ejercicio 2:** Registro de productos con arrays de NumPy y DataFrame.
    - **Ejercicio 3:** Cálculo del WACC usando una función de librería externa.
    - **Ejercicio 4:** CRUD de proyectos de inversión usando una clase (POO).

    ### 🛠️ Tecnologías utilizadas

    - Python 3
    - Streamlit
    - Pandas
    - NumPy
    """)


# =============================================================================
# EJERCICIO 1 - FLUJO DE CAJA CON LISTAS
# =============================================================================
def mostrar_ejercicio1():
    """Registra ingresos y gastos en una lista y calcula el saldo final."""
    st.title("💰 Ejercicio 1 - Flujo de caja con listas")

    st.markdown("""
    **Descripción:** este módulo registra movimientos financieros
    (ingresos y gastos) en una **lista**. Cada movimiento se guarda como un
    diccionario con su concepto, tipo y valor. Al final se calcula el total
    de ingresos, el total de gastos y el saldo, indicando si el flujo de
    caja está **a favor** o **en contra**.
    """)

    # --- Formulario de ingreso de datos ---
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto del movimiento", placeholder="Ej: Venta de servicios")
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor (S/.)", min_value=0.0, step=10.0, format="%.2f")

    # --- Botón para agregar el movimiento a la lista ---
    if st.button("➕ Agregar movimiento"):
        # Validación: el concepto no puede estar vacío y el valor debe ser mayor a cero
        if concepto.strip() == "":
            st.error("⚠️ Debes ingresar un concepto.")
        elif valor <= 0:
            st.error("⚠️ El valor debe ser mayor a cero.")
        else:
            # Se agrega el movimiento (un diccionario) a la lista en session_state
            st.session_state.movimientos.append({
                "Concepto": concepto.strip(),
                "Tipo": tipo,
                "Valor (S/.)": valor
            })
            st.success(f"✅ Movimiento '{concepto}' agregado correctamente.")

    st.markdown("---")

    # --- Resultados: solo se muestran si la lista tiene movimientos ---
    if len(st.session_state.movimientos) > 0:
        st.subheader("📄 Movimientos registrados")
        # La lista de diccionarios se convierte en DataFrame para mostrarla como tabla
        df_movimientos = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movimientos, width="stretch")

        # --- Cálculos con programación funcional (list comprehension + sum) ---
        total_ingresos = sum(
            m["Valor (S/.)"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso"
        )
        total_gastos = sum(
            m["Valor (S/.)"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto"
        )
        saldo = total_ingresos - total_gastos

        # --- Métricas en pantalla ---
        c1, c2, c3 = st.columns(3)
        c1.metric("Total ingresos", f"S/. {total_ingresos:,.2f}")
        c2.metric("Total gastos", f"S/. {total_gastos:,.2f}")
        c3.metric("Saldo final", f"S/. {saldo:,.2f}")

        # --- Control de flujo: el saldo define el mensaje final ---
        if saldo >= 0:
            st.success(f"✅ El flujo de caja está **A FAVOR** por S/. {saldo:,.2f}")
        else:
            st.error(f"❌ El flujo de caja está **EN CONTRA** por S/. {abs(saldo):,.2f}")

        # Botón opcional para reiniciar la lista de movimientos
        if st.button("🗑️ Limpiar movimientos"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("ℹ️ Aún no hay movimientos registrados. Agrega el primero arriba.")


# =============================================================================
# EJERCICIO 2 - REGISTRO CON NUMPY, ARRAYS Y DATAFRAME
# =============================================================================
def mostrar_ejercicio2():
    """Registra productos en arrays de NumPy y los muestra en un DataFrame."""
    st.title("📦 Ejercicio 2 - Registro de productos con NumPy")

    st.markdown("""
    **Descripción:** este formulario registra productos usando **arrays de
    NumPy** (un array por cada campo). Con cada registro, los arrays se
    actualizan con `np.append()` y luego se convierten en un **DataFrame**
    de Pandas que se muestra actualizado en pantalla.
    """)

    # --- Formulario de ingreso de datos ---
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre del producto", placeholder="Ej: Laptop")
        categoria = st.selectbox(
            "Categoría",
            ["Tecnología", "Alimentos", "Ropa", "Hogar", "Servicios", "Otros"]
        )
    with col2:
        precio = st.number_input("Precio unitario (S/.)", min_value=0.0, step=1.0, format="%.2f")
        cantidad = st.number_input("Cantidad", min_value=1, step=1)

    # El total se calcula automáticamente: precio × cantidad
    total = precio * cantidad
    st.markdown(f"**Total del registro:** S/. {total:,.2f}")

    # --- Botón para agregar el registro a los arrays ---
    if st.button("➕ Agregar registro"):
        if nombre.strip() == "":
            st.error("⚠️ Debes ingresar el nombre del producto.")
        elif precio <= 0:
            st.error("⚠️ El precio debe ser mayor a cero.")
        else:
            # np.append crea un nuevo array agregando el elemento al final
            st.session_state.arr_productos = np.append(st.session_state.arr_productos, nombre.strip())
            st.session_state.arr_categorias = np.append(st.session_state.arr_categorias, categoria)
            st.session_state.arr_precios = np.append(st.session_state.arr_precios, precio)
            st.session_state.arr_cantidades = np.append(st.session_state.arr_cantidades, cantidad)
            st.session_state.arr_totales = np.append(st.session_state.arr_totales, total)
            st.success(f"✅ Producto '{nombre}' registrado correctamente.")

    st.markdown("---")

    # --- Tabla actualizada: los arrays se convierten en DataFrame ---
    if st.session_state.arr_productos.size > 0:
        st.subheader("📄 Registros almacenados (arrays → DataFrame)")
        df_registros = pd.DataFrame({
            "Producto": st.session_state.arr_productos,
            "Categoría": st.session_state.arr_categorias,
            "Precio (S/.)": st.session_state.arr_precios,
            "Cantidad": st.session_state.arr_cantidades,
            "Total (S/.)": st.session_state.arr_totales
        })
        st.dataframe(df_registros, width="stretch")

        # Estadísticas rápidas aprovechando las operaciones vectorizadas de NumPy
        c1, c2, c3 = st.columns(3)
        c1.metric("Registros", int(st.session_state.arr_productos.size))
        c2.metric("Venta total", f"S/. {st.session_state.arr_totales.sum():,.2f}")
        c3.metric("Ticket promedio", f"S/. {st.session_state.arr_totales.mean():,.2f}")
    else:
        st.info("ℹ️ Aún no hay registros. Agrega el primer producto arriba.")


# =============================================================================
# EJERCICIO 3 - FUNCIÓN DE LIBRERÍA EXTERNA: CÁLCULO DEL WACC
# =============================================================================
def mostrar_ejercicio3():
    """Conecta la función calcular_wacc() de la librería externa con widgets."""
    st.title("📊 Ejercicio 3 - Cálculo del WACC (librería externa)")

    st.markdown("""
    **Descripción:** se utiliza la función `calcular_wacc()` del archivo
    `libreria_funciones_proyecto1.py`, seleccionada por su relación con el
    área financiera. El **WACC** (*Weighted Average Cost of Capital*) es el
    costo promedio ponderado de capital de una empresa: la tasa mínima de
    retorno que debe exigirse a un proyecto para crear valor.

    **Fórmula:**  `WACC = (D/V) × Kd × (1 - T) + (E/V) × Ke`

    donde **D** = deuda, **E** = patrimonio, **V** = D + E,
    **Kd** = costo de la deuda, **Ke** = costo del patrimonio y
    **T** = tasa de impuestos.
    """)

    # --- Selector de función (requisito de la interfaz) ---
    st.selectbox(
        "Función seleccionada de la librería:",
        ["calcular_wacc - Costo promedio ponderado de capital"]
    )

    # --- Widgets para ingresar los parámetros de la función ---
    col1, col2 = st.columns(2)
    with col1:
        deuda = st.number_input("Deuda total (S/.)", min_value=0.0, value=400000.0, step=10000.0)
        patrimonio = st.number_input("Patrimonio total (S/.)", min_value=0.0, value=600000.0, step=10000.0)
        impuesto_pct = st.number_input("Tasa de impuestos (%)", min_value=0.0, max_value=100.0, value=29.5)
    with col2:
        costo_deuda_pct = st.number_input("Costo de la deuda Kd (%)", min_value=0.0, max_value=100.0, value=8.0)
        costo_patrimonio_pct = st.number_input("Costo del patrimonio Ke (%)", min_value=0.0, max_value=100.0, value=15.0)

    # --- Botón para ejecutar la función ---
    if st.button("🧮 Calcular WACC"):
        # try/except captura las validaciones internas de la librería
        try:
            resultado = calcular_wacc(
                deuda=deuda,
                patrimonio=patrimonio,
                costo_deuda_pct=costo_deuda_pct,
                costo_patrimonio_pct=costo_patrimonio_pct,
                impuesto_pct=impuesto_pct
            )
            wacc = resultado["wacc_pct"]

            # --- Resultado en pantalla ---
            st.metric("WACC calculado", f"{wacc:.2f} %")
            st.success(
                f"✅ El costo promedio ponderado de capital es **{wacc:.2f}%**. "
                "Los proyectos de la empresa deberían rendir por encima de esta tasa."
            )

            # --- Se agrega el resultado al histórico ---
            st.session_state.historico_wacc.append({
                "Deuda (S/.)": deuda,
                "Patrimonio (S/.)": patrimonio,
                "Kd (%)": costo_deuda_pct,
                "Ke (%)": costo_patrimonio_pct,
                "Impuesto (%)": impuesto_pct,
                "WACC (%)": wacc
            })
        except ValueError as error:
            # Si la librería detecta un dato inválido, se muestra el mensaje
            st.error(f"⚠️ Error en los datos ingresados: {error}")

    st.markdown("---")

    # --- Tabla histórica de resultados ---
    if len(st.session_state.historico_wacc) > 0:
        st.subheader("📄 Histórico de cálculos")
        df_historico = pd.DataFrame(st.session_state.historico_wacc)
        st.dataframe(df_historico, width="stretch")
    else:
        st.info("ℹ️ Aún no hay cálculos en el histórico.")


# =============================================================================
# EJERCICIO 4 - CLASE DE LIBRERÍA EXTERNA CON CRUD: ProyectoInversion
# =============================================================================
def mostrar_ejercicio4():
    """CRUD de proyectos de inversión usando la clase ProyectoInversion."""
    st.title("🏗️ Ejercicio 4 - CRUD de proyectos de inversión (POO)")

    st.markdown("""
    **Descripción:** se utiliza la clase `ProyectoInversion` del archivo
    `libreria_clases_proyecto1.py`. Cada proyecto se crea como un **objeto**
    con nombre, inversión inicial, flujos anuales y tasa de descuento, y sus
    métodos calculan el **VPN**, el **ROI** y el **Payback**. Se implementan
    las cuatro operaciones **CRUD**: Crear, Leer, Actualizar y Eliminar.
    """)

    # Las 4 operaciones CRUD se organizan en pestañas
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["➕ Crear", "📖 Leer", "✏️ Actualizar", "🗑️ Eliminar"]
    )

    # -------------------------------------------------------------------------
    # CREAR: registra un nuevo objeto ProyectoInversion
    # -------------------------------------------------------------------------
    with tab_crear:
        st.subheader("Crear un nuevo proyecto")

        nombre_proy = st.text_input("Nombre del proyecto", placeholder="Ej: Planta de Arequipa")
        col1, col2 = st.columns(2)
        with col1:
            inversion = st.number_input("Inversión inicial (S/.)", min_value=0.0, value=100000.0, step=5000.0)
            tasa = st.number_input("Tasa de descuento (%)", min_value=0.0, max_value=100.0, value=12.0)
        with col2:
            anios = st.number_input("Número de años de flujos", min_value=1, max_value=10, value=3)

        # Se genera un number_input por cada año de flujo proyectado
        st.markdown("**Flujos de caja anuales proyectados (S/.):**")
        flujos = []
        columnas_flujos = st.columns(int(anios))
        for i, col in enumerate(columnas_flujos):
            with col:
                flujo = st.number_input(f"Año {i + 1}", min_value=0.0, value=40000.0,
                                        step=5000.0, key=f"flujo_{i}")
                flujos.append(flujo)

        if st.button("➕ Crear proyecto"):
            if nombre_proy.strip() == "":
                st.error("⚠️ Debes ingresar el nombre del proyecto.")
            elif nombre_proy.strip() in st.session_state.proyectos:
                st.error("⚠️ Ya existe un proyecto con ese nombre. Usa 'Actualizar' para modificarlo.")
            else:
                try:
                    # Se instancia el objeto y se guarda en el diccionario
                    proyecto = ProyectoInversion(
                        nombre_proyecto=nombre_proy.strip(),
                        inversion_inicial=inversion,
                        flujos=flujos,
                        tasa_descuento_pct=tasa
                    )
                    st.session_state.proyectos[nombre_proy.strip()] = proyecto
                    st.success(f"✅ Proyecto '{nombre_proy}' creado correctamente.")
                except ValueError as error:
                    st.error(f"⚠️ Error al crear el proyecto: {error}")

    # -------------------------------------------------------------------------
    # LEER: muestra todos los proyectos con sus indicadores calculados
    # -------------------------------------------------------------------------
    with tab_leer:
        st.subheader("Proyectos registrados")

        if len(st.session_state.proyectos) > 0:
            # El método resumen() de cada objeto devuelve un diccionario
            # con VPN, ROI, Payback y la decisión (Viable / No viable)
            resumenes = [p.resumen() for p in st.session_state.proyectos.values()]
            df_proyectos = pd.DataFrame(resumenes)
            df_proyectos.columns = ["Proyecto", "VPN (S/.)", "ROI (%)",
                                    "Payback (años)", "Decisión"]
            st.dataframe(df_proyectos, width="stretch")

            # Detalle individual del proyecto seleccionado
            seleccionado = st.selectbox("Ver detalle de:", list(st.session_state.proyectos.keys()))
            proyecto = st.session_state.proyectos[seleccionado]
            resumen = proyecto.resumen()

            c1, c2, c3 = st.columns(3)
            c1.metric("VPN", f"S/. {resumen['vpn']:,.2f}")
            c2.metric("ROI", f"{resumen['roi_pct']:.2f} %")
            c3.metric("Payback", f"{resumen['payback_anios']:.2f} años")

            if resumen["decision"] == "Viable":
                st.success(f"✅ El proyecto '{seleccionado}' es **VIABLE** (VPN positivo).")
            else:
                st.error(f"❌ El proyecto '{seleccionado}' **NO es viable** (VPN negativo).")
        else:
            st.info("ℹ️ No hay proyectos registrados. Crea uno en la pestaña 'Crear'.")

    # -------------------------------------------------------------------------
    # ACTUALIZAR: modifica los atributos de un proyecto existente
    # -------------------------------------------------------------------------
    with tab_actualizar:
        st.subheader("Actualizar un proyecto existente")

        if len(st.session_state.proyectos) > 0:
            nombre_actualizar = st.selectbox(
                "Proyecto a actualizar:",
                list(st.session_state.proyectos.keys()),
                key="sel_actualizar"
            )
            proyecto_actual = st.session_state.proyectos[nombre_actualizar]

            # Los campos se precargan con los valores actuales del objeto
            col1, col2 = st.columns(2)
            with col1:
                nueva_inversion = st.number_input(
                    "Nueva inversión inicial (S/.)",
                    min_value=0.0,
                    value=float(proyecto_actual.inversion_inicial),
                    step=5000.0,
                    key="upd_inversion"
                )
            with col2:
                nueva_tasa = st.number_input(
                    "Nueva tasa de descuento (%)",
                    min_value=0.0, max_value=100.0,
                    value=float(proyecto_actual.tasa_descuento_pct),
                    key="upd_tasa"
                )

            st.markdown("**Flujos de caja anuales (S/.):**")
            nuevos_flujos = []
            columnas_upd = st.columns(len(proyecto_actual.flujos))
            for i, col in enumerate(columnas_upd):
                with col:
                    flujo = st.number_input(
                        f"Año {i + 1}",
                        min_value=0.0,
                        value=float(proyecto_actual.flujos[i]),
                        step=5000.0,
                        key=f"upd_flujo_{i}"
                    )
                    nuevos_flujos.append(flujo)

            if st.button("✏️ Guardar cambios"):
                try:
                    # Se reemplaza el objeto por uno nuevo con los datos actualizados
                    st.session_state.proyectos[nombre_actualizar] = ProyectoInversion(
                        nombre_proyecto=nombre_actualizar,
                        inversion_inicial=nueva_inversion,
                        flujos=nuevos_flujos,
                        tasa_descuento_pct=nueva_tasa
                    )
                    st.success(f"✅ Proyecto '{nombre_actualizar}' actualizado correctamente.")
                except ValueError as error:
                    st.error(f"⚠️ Error al actualizar: {error}")
        else:
            st.info("ℹ️ No hay proyectos para actualizar.")

    # -------------------------------------------------------------------------
    # ELIMINAR: quita un proyecto del diccionario
    # -------------------------------------------------------------------------
    with tab_eliminar:
        st.subheader("Eliminar un proyecto")

        if len(st.session_state.proyectos) > 0:
            nombre_eliminar = st.selectbox(
                "Proyecto a eliminar:",
                list(st.session_state.proyectos.keys()),
                key="sel_eliminar"
            )
            if st.button("🗑️ Eliminar proyecto"):
                # del elimina la clave (y su objeto) del diccionario
                del st.session_state.proyectos[nombre_eliminar]
                st.success(f"✅ Proyecto '{nombre_eliminar}' eliminado.")
                st.rerun()
        else:
            st.info("ℹ️ No hay proyectos para eliminar.")


# =============================================================================
# ENRUTAMIENTO PRINCIPAL
# -----------------------------------------------------------------------------
# Según la opción elegida en el menú lateral, se llama a la función
# que dibuja la sección correspondiente.
# =============================================================================
if seccion == "Home":
    mostrar_home()
elif seccion == "Ejercicio 1":
    mostrar_ejercicio1()
elif seccion == "Ejercicio 2":
    mostrar_ejercicio2()
elif seccion == "Ejercicio 3":
    mostrar_ejercicio3()
elif seccion == "Ejercicio 4":
    mostrar_ejercicio4()
