# 🌳 Árbol Binario de Búsqueda (BST) en Python

Este proyecto implementa un **Árbol Binario de Búsqueda (Binary Search Tree - BST)** en Python con soporte para:

- Inserción de nodos
- Búsqueda de elementos
- Eliminación de nodos (con manejo completo de los 3 casos)
- Importación de datos desde JSON
- Exportación del árbol a JSON

---

## 📌 ¿Qué hace este árbol?

El árbol organiza datos en una estructura jerárquica siguiendo la regla del BST:

- Todos los valores menores van al subárbol izquierdo.
- Todos los valores mayores van al subárbol derecho.

La comparación se realiza usando el campo:

value["name"]


Es decir, el árbol ordena los nodos según el campo `"name"` del diccionario almacenado en cada nodo.

---

## ⚙️ Funcionalidades Implementadas

### ✅ Insertar
Agrega un nuevo nodo respetando la propiedad del BST.

### 🔎 Buscar
Busca un nodo comparando el campo `"name"`.

### ❌ Eliminar
Elimina nodos manejando correctamente los tres casos clásicos:

1. Nodo sin hijos
2. Nodo con un hijo
3. Nodo con dos hijos (reemplazo por el sucesor in-order)

---

## 🧠 Cómo funciona la eliminación

Cuando se elimina un nodo:

- Si no tiene hijos → se elimina directamente.
- Si tiene un hijo → el hijo lo reemplaza.
- Si tiene dos hijos:
  - Se busca el nodo mínimo del subárbol derecho (sucesor).
  - Se copia su valor al nodo actual.
  - Se elimina el sucesor recursivamente.

La función recursiva siempre devuelve:

(nueva_raiz_del_subarbol, eliminado)


Esto permite reconstruir correctamente la estructura del árbol después de cada operación.

---

## 📂 Estructura de los Nodos

Cada nodo contiene un diccionario con la forma:

{
"name": "clave",
...
}


El campo `"name"` es la clave usada para ordenar el árbol.

---

## 📤 Exportación a JSON

El árbol puede convertirse en una estructura serializable y guardarse en un archivo `.json`.

- Se utiliza el módulo estándar `json` de Python.
- El árbol se recorre y se transforma en una estructura tipo diccionario/lista.
- Se guarda en un archivo para persistencia de datos.

---

## 📥 Importación desde JSON

El árbol puede reconstruirse a partir de un archivo `.json`.

- Se lee el archivo.
- Se insertan los elementos en el árbol respetando la propiedad del BST.
- Se restaura la estructura completa.

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Programación orientada a objetos
- Recursividad
- Módulo estándar `json`

---

## 🎯 Objetivo del Proyecto

Este proyecto fue desarrollado para practicar y comprender:

- Estructuras de datos
- Recursividad estructural
- Manejo de referencias en árboles
- Serialización y deserialización de datos

---

## 🚀 Posibles Mejoras Futuras

- Recorridos en orden, preorden y postorden
- Balanceo automático (AVL o Red-Black Tree)
- Visualización gráfica del árbol
- Manejo de claves duplicadas