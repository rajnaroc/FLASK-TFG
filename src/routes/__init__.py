# importaciones routes 
from routes.auth import auth_bp
from routes.perfil import perfil_bp
from routes.eventos import eventos_bp
from routes.contacto import contacto_bp
from routes.general import general_bp

def register_blue(app):
    # blueprints de todas las funciones
    # Register, Iniciar sesion y cerrar sesion
    app.register_blueprint(auth_bp)
    # Perfil,Editar perfil, borrar Perfil
    app.register_blueprint(perfil_bp)
    # Crear eventos,Enseñar eventos,Editar eventos y eliminarlos
    app.register_blueprint(eventos_bp)
    # Contacto
    app.register_blueprint(contacto_bp)
    # Inicio,Política de Privacidad,Aviso Legal,Terminos y Condiciones
    app.register_blueprint(general_bp)