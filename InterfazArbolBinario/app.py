from flask import Flask, render_template
from controllers.tree_controller import tree_bp

# Configurar Flask para que use la carpeta 'views'
app = Flask(__name__, 
            template_folder='views', 
            static_folder='views/static')

# Registrar el controlador (API routes)
app.register_blueprint(tree_bp)

@app.route('/')
def index():
    """Ruta principal que renderiza la vista."""
    return render_template('index.html')

if __name__ == '__main__':
    # Modo debug para desarrollo
    app.run(debug=True, port=5000)
