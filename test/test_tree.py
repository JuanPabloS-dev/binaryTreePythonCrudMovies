import pytest


# =========================
# INSERTAR
# =========================

def test_insertar_raiz(arbol, pelicula_ejemplo):
    arbol.insertar(pelicula_ejemplo)

    assert arbol.root is not None
    assert arbol.root.value["name"] == "Forrest Gump"
    assert arbol.size == 1


def test_insertar_varios(arbol):
    from src.node import Node

    arbol.insertar(Node({"name": "M"}))
    arbol.insertar(Node({"name": "A"}))
    arbol.insertar(Node({"name": "Z"}))

    assert arbol.root.value["name"] == "M"
    assert arbol.root.left.value["name"] == "A"
    assert arbol.root.right.value["name"] == "Z"
    assert arbol.size == 3


# =========================
# BUSCAR
# =========================

def test_buscar_existente(arbol_poblado):
    nodo = arbol_poblado.buscar("M")

    assert nodo is not None
    assert nodo.value["name"] == "M"


def test_buscar_inexistente(arbol_poblado):
    nodo = arbol_poblado.buscar("X")

    assert nodo is None


def test_buscar_arbol_vacio(arbol):
    nodo = arbol.buscar("X")
    assert nodo is None


# =========================
# RECORRIDOS
# =========================

def test_recorrido_in_order(arbol_poblado):
    nombres = [n.value["name"] for n in arbol_poblado.recorrer("in")]
    assert nombres == ["A", "B", "M", "Y", "Z"]


def test_recorrido_pre_order(arbol_poblado):
    nombres = [n.value["name"] for n in arbol_poblado.recorrer("pre")]
    assert nombres[0] == "M"


def test_recorrido_post_order(arbol_poblado):
    nombres = [n.value["name"] for n in arbol_poblado.recorrer("post")]
    assert "M" in nombres


# =========================
# ELIMINAR
# =========================

def test_eliminar_hoja(arbol_poblado):
    exito = arbol_poblado.eliminar("B")

    assert exito is True
    assert arbol_poblado.buscar("B") is None
    assert arbol_poblado.size == 4


def test_eliminar_inexistente(arbol_poblado):
    exito = arbol_poblado.eliminar("X")

    assert exito is False
    assert arbol_poblado.size == 5


def test_eliminar_raiz(arbol_poblado):
    arbol_poblado.eliminar("M")

    assert arbol_poblado.buscar("M") is None
    assert arbol_poblado.size == 4
