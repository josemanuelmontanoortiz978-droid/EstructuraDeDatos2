"""
main.py - Punto de entrada principal para ejecutar la aplicacion.
Ejecutar con: python main.py
"""
import socket
from app import app


def get_local_ip():
    """Obtiene la direccion IP local de la maquina."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "No disponible"


if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 50)
    print("  Visualizador de Arbol AVL")
    print(f"  Local:   http://127.0.0.1:5000")
    print(f"  Red:     http://{local_ip}:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
