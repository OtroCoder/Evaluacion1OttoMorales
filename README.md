# Proyecto 1 – Aplicación Interactiva en Streamlit

**Especialización Python for Analytics · Módulo 1 – Python Fundamentals**

| | |
|---|---|
| **Autor** | Otto Morales Gómez |
| **Perfil** | Ingeniero y MBA |
| **País** | Perú |
| **Año** | 2026 |

## 📋 Descripción

Aplicación interactiva desarrollada en **Streamlit** que integra los conceptos fundamentales del Módulo 1: variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO).

## 🧩 Secciones de la aplicación

La navegación se realiza mediante un menú lateral (`st.sidebar.selectbox()`):

1. **Home** – Presentación del proyecto y datos del estudiante.
2. **Ejercicio 1 – Flujo de caja con listas.** Registro de ingresos y gastos en una lista, con totales, saldo final e indicador de flujo a favor o en contra.
3. **Ejercicio 2 – Registro con NumPy.** Formulario de productos almacenados en arrays de NumPy y mostrados como DataFrame actualizado.
4. **Ejercicio 3 – Función de librería externa.** Cálculo del **WACC** (costo promedio ponderado de capital) con la función `calcular_wacc()` de `libreria_funciones_proyecto1.py`, con histórico de resultados.
5. **Ejercicio 4 – Clase de librería externa con CRUD.** Gestión de proyectos de inversión (Crear, Leer, Actualizar, Eliminar) con la clase `ProyectoInversion` de `libreria_clases_proyecto1.py`, que calcula VPN, ROI y Payback.

## 📁 Estructura del repositorio

```
├── app.py                            # Aplicación principal de Streamlit
├── libreria_funciones_proyecto1.py   # Librería de funciones (provista en el curso)
├── libreria_clases_proyecto1.py      # Librería de clases (provista en el curso)
├── requirements.txt                  # Dependencias del proyecto
└── README.md                         # Este archivo
```

## ▶️ Ejecución local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la aplicación
streamlit run app.py
```

## 🛠️ Tecnologías

Python 3 · Streamlit · Pandas · NumPy

---

*Proyecto desarrollado como primer trabajo aplicado de la Especialización Python for Analytics — MSc. Carlos Carrillo Villavicencio.*
