# CRUD Papelería / Biblioteca con Python y XML

Sistema CRUD ligero desarrollado en Python que utiliza un archivo XML como base de datos. No requiere MySQL ni servidor, toda la información se guarda, lee, actualiza y elimina directamente desde un archivo `datos.xml`.

Ideal para prácticas de manejo de archivos, estructura de datos y la librería `xml.etree.ElementTree`.

## 📖 Descripción

El programa simula la gestión de una papelería, biblioteca o tienda pequeña. En lugar de conectarse a una base de datos, crea y manipula un archivo XML con estructura jerárquica.

Cada producto / libro / artículo es un nodo `<producto>` dentro del archivo, con atributos como id, nombre, precio y stock.

## ✨ Funcionalidades CRUD con XML

**[C] Create - Crear:**
- Agregar nuevo elemento al archivo XML
- Genera ID automático
- Guarda cambios en `datos.xml`

**[R] Read - Leer:**
- Listar todos los registros del XML
- Buscar por ID o por nombre
- Mostrar en tabla bonita en consola

**[U] Update - Actualizar:**
- Modificar nombre, precio, stock o categoría por ID
- Reescribe el nodo en el XML

**[D] Delete - Eliminar:**
- Eliminar un nodo completo del XML por ID

**Extras:**
- Crear el archivo XML automáticamente si no existe
- Validación para no duplicar IDs
- Exportar XML a formato legible (indentado)

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.8+
- **Librería Principal:** `xml.etree.ElementTree` (nativa de Python)
- **Librerías de apoyo:** `os`, `tabulate` (opcional para tablas)

No necesitas instalar nada extra. ElementTree ya viene con Python.

## 📋 Instalación

```bash
git clone https://github.com/tu-usuario/crud-xml-python.git
cd crud-xml-python

# Opcional: instalar tabulate para ver tablas bonitas
pip install tabulate
