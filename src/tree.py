from src.node import Node

import json
import os
from typing import Optional, Generator
class Tree:
    def __init__(self, root:Optional[Node]=None) -> None:
        self.root = root
        self.size = 0
        
    def insertar(self,nodo:Node) -> None:
        if(not self.root):
            self.root = nodo
            self.size += 1
        else: self.insertar_recursivo(nodo,self.root)
        
    def insertar_recursivo(self,nodo:Node,actual:Node):
        if(nodo.value["name"] < actual.value["name"]):
            if(actual.left == None):
                actual.left = nodo
                self.size += 1
            else:
                self.insertar_recursivo(nodo,actual.left)
        elif(nodo.value["name"] > actual.value["name"]):
            if(actual.right == None):
                actual.right = nodo
                self.size += 1
            else:
                self.insertar_recursivo(nodo,actual.right)
        else: return
        
    def buscar(self, sku:str) -> Optional[Node]:
        if (self.root):
            if(sku == self.root.value["name"]):
                return self.root
            else: return self._buscar_recursivo(sku,self.root)
        else: return None
    def _buscar_recursivo(self,sku:str, actual:Node):
        if(actual):
            if(sku<actual.value["name"]):
                return self._buscar_recursivo(sku,actual.left)
            elif(sku>actual.value["name"]):
                return self._buscar_recursivo(sku,actual.right)
            else: return actual
        else: return None
    
    def recorrer(self,tipo:str):
        match (tipo):
            case ("in"):
                return self._in_order(self.root)
            case ("pre"):
                return self._pre_order(self.root)
            case ("post"):
                return self._post_order(self.root)
            case (_):
                return None      
    def _in_order(self,actual:Node) -> Generator[Node,None,None]:
        if (actual):
            yield from self._in_order(actual.left)
            yield actual
            yield from self._in_order(actual.right)
            
    def _pre_order(self,actual:Node) -> Generator[Node,None,None]:
        if (actual):
            yield actual
            yield from self._pre_order(actual.left)
            yield from self._pre_order(actual.right)
            
    def _post_order(self,actual:Node) -> Generator[Node,None,None]:
        if (actual):
            yield from self._post_order(actual.left)
            yield from self._post_order(actual.right)
            yield actual
            
            
    def guardar_json(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(base_dir,"..","data","movies.json")
        contenido = [p.value for p in self.recorrer("pre")]
        with open(ruta,"w",encoding="utf-8") as f:
            json.dump(contenido,f,indent=4,ensure_ascii=False)
    
    def importar_json(self,archivo):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(base_dir,"..",archivo)
        with open(ruta,"r",encoding="utf-8") as f:
           datos = json.load(f)
        return datos
    
    def eliminar(self, valor) -> bool:
        self.root,eliminado = self._eliminar_recursivo(self.root,valor)
        if(eliminado):
            self.size -= 1
            return eliminado
        return eliminado

    
    def _eliminar_recursivo(self,actual:Node, valor:str):
        if(not actual): return actual, False
        if(valor<actual.value["name"]):
            actual.left,eliminado = self._eliminar_recursivo(actual.left,valor)
        elif(valor>actual.value["name"]):
            actual.right,eliminado = self._eliminar_recursivo(actual.right,valor)
        else:
            if not actual.right:
                return actual.left, True
            if not actual.left:
                return actual.right, True

            sucesor = self._buscar_minimo(actual.right)
            actual.value = sucesor.value
            actual.right,_ = self._eliminar_recursivo(actual.right,sucesor.value["name"])
            return actual,True
        return actual,eliminado
    
    def _buscar_minimo(self,actual:Node)->Node:
        resultado = actual
        while resultado.left:
            resultado = resultado.left 
        return resultado