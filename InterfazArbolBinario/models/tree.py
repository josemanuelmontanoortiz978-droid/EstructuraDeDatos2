"""
Modulo que contiene la logica del Arbol AVL (Adelson-Velsky y Landis).
Incluye la definicion del Nodo y la clase AVLTree que implementa
insercion, eliminacion y balanceo automatico.
"""

class Node:
    """Clase que representa un nodo en el Arbol AVL."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def to_dict(self):
        """Convierte el nodo y sus hijos a un diccionario para serializacion."""
        return {
            "key": self.key,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "height": self.height
        }


class AVLTree:
    """Clase que representa el Arbol AVL."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserta una nueva clave en el arbol AVL."""
        self.root = self._insert_node(self.root, key)

    def _insert_node(self, node, key):
        # 1. Insercion normal de BST
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert_node(node.left, key)
        elif key > node.key:
            node.right = self._insert_node(node.right, key)
        else:
            return node  # No se permiten claves duplicadas

        # 2. Actualizar la altura del nodo ancestro
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # 3. Obtener el factor de balance
        balance = self._get_balance(node)

        # 4. Balancear el arbol si es necesario
        # Caso Izquierda Izquierda
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # Caso Derecha Derecha
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # Caso Izquierda Derecha
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Caso Derecha Izquierda
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        """Elimina una clave del arbol AVL."""
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, root, key):
        # 1. Eliminacion normal de BST
        if not root:
            return root

        if key < root.key:
            root.left = self._delete_node(root.left, key)
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_node(root.right, temp.key)

        if root is None:
            return root

        # 2. Actualizar la altura del nodo actual
        root.height = 1 + max(self._get_height(root.left),
                              self._get_height(root.right))

        # 3. Obtener el factor de balance
        balance = self._get_balance(root)

        # 4. Balancear el arbol
        # Caso Izquierda Izquierda
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)

        # Caso Izquierda Derecha
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Caso Derecha Derecha
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)

        # Caso Derecha Izquierda
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def clear(self):
        """Limpia el arbol."""
        self.root = None

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self._get_min_value_node(root.left)

    def to_dict(self):
        """Convierte el arbol a un diccionario."""
        if self.root:
            return self.root.to_dict()
        return None
