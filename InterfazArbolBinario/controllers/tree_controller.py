"""
Controlador para el Arbol AVL.
Maneja las rutas de la API para interactuar con el modelo del arbol.
"""
from flask import Blueprint, jsonify, request
from models.tree import AVLTree

# Se crea un Blueprint para agrupar las rutas del arbol
tree_bp = Blueprint('tree_bp', __name__)

# Instancia global del arbol en memoria (para propositos de demostracion)
avl_tree = AVLTree()

@tree_bp.route('/api/tree', methods=['GET'])
def get_tree():
    """Devuelve la representacion actual del arbol en formato JSON."""
    return jsonify({"tree": avl_tree.to_dict()}), 200

@tree_bp.route('/api/tree/insert', methods=['POST'])
def insert_node():
    """Inserta un nodo en el arbol."""
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({"error": "Valor no proporcionado"}), 400
    
    try:
        value = int(data['value'])
        avl_tree.insert(value)
        return jsonify({
            "message": f"Nodo {value} insertado correctamente",
            "tree": avl_tree.to_dict()
        }), 200
    except ValueError:
        return jsonify({"error": "El valor debe ser un entero"}), 400

@tree_bp.route('/api/tree/delete', methods=['POST'])
def delete_node():
    """Elimina un nodo del arbol."""
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({"error": "Valor no proporcionado"}), 400
    
    try:
        value = int(data['value'])
        avl_tree.delete(value)
        return jsonify({
            "message": f"Nodo {value} eliminado (si existia)",
            "tree": avl_tree.to_dict()
        }), 200
    except ValueError:
        return jsonify({"error": "El valor debe ser un entero"}), 400

@tree_bp.route('/api/tree/clear', methods=['POST'])
def clear_tree():
    """Limpia todo el arbol."""
    avl_tree.clear()
    return jsonify({
        "message": "Arbol vaciado correctamente",
        "tree": None
    }), 200
