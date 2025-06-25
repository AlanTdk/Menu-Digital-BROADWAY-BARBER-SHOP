from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal que renderizará el menú
@app.route('/')
def menu():
    """
    Renderiza la página principal del menú digital.
    """
    # === VERIFICA QUE ESTOS NOMBRES COINCIDAN CON TUS ARCHIVOS ===
    # Deben ser todos en minúsculas: .jpg
    servicios = [
        {
            "nombre": "Corte de Caballero",
            "precio": 250,
            "imagen": "images/cortecaballero.jpg",
            "descripcion": "Estilo y precisión para el hombre moderno."
        },
        {
            "nombre": "Corte de Niño",
            "precio": 200,
            "imagen": "images/corteniño.jpg",
            "descripcion": "Cortes frescos y divertidos para los más pequeños."
        },
        {
            "nombre": "Perfilado de Barba",
            "precio": 150,
            "imagen": "images/cortebarba.jpg", # Asegúrate de tener una imagen con este nombre
            "descripcion": "Define tu estilo con un arreglo de barba profesional."
        }
    ]

    promociones = [
        {
            "nombre": "Paquete Premium",
            "precio": 300,
            "imagen": "images/promocion300.jpg",
            "descripcion": "Incluye corte de cabello, exfoliante facial y mascarilla negra."
        }
    ]
    
    barberia_info = {
        "direccion": "13A Poniente Norte entre 1A Norte y Av. Central, #192-D Plaza La Trece, Planta Alta, Tuxtla Gutiérrez, Chiapas.",
        "map_url": "https://maps.app.goo.gl/jjXfaSV8STJVtNzP6",
        "instagram_url": "https://www.instagram.com/broadwaybarbershop1/"
    }

    return render_template('index.html', servicios=servicios, promociones=promociones, info=barberia_info)

# Permite ejecutar la aplicación directamente
if __name__ == '__main__':
    app.run(debug=True)
