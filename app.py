"""Aplicación web de ForceNet.

Este módulo define:
- La ruta principal que renderiza la interfaz.
- El endpoint REST que recibe cargas puntuales y devuelve la fuerza neta.

La lógica física no vive aquí: se delega al dominio en models.py.
"""

from flask import Flask, render_template, request, jsonify
from models import PointCharge, ForceCalculator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'electroforce-secret-key'  # Para futuras expansiones


@app.route('/')
def index():
    """Renderiza la página principal de ForceNet."""
    return render_template('index.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
        """Calcula la fuerza neta sobre la carga objetivo.

        Entrada JSON esperada:
        {
            "target": {"q": float, "x": float, "y": float},
            "charges": [{"q": float, "x": float, "y": float}, ...]
        }

        Respuesta JSON:
        - success=true con fx, fy y magnitude cuando todo es válido.
        - success=false con error cuando la entrada es inválida.
        """
    try:
        data = request.get_json()
        if not data or 'target' not in data or 'charges' not in data:
            return jsonify({'success': False, 'error': 'Datos incompletos'}), 400

        target_data = data['target']
        charges_data = data['charges']

        # Convierte el payload en objetos de dominio tipados.
        target = PointCharge(
            q=float(target_data['q']),
            x=float(target_data['x']),
            y=float(target_data['y'])
        )

        other_charges = [
            PointCharge(q=float(ch['q']), x=float(ch['x']), y=float(ch['y']))
            for ch in charges_data
        ]

        calculator = ForceCalculator(target, other_charges)
        net_force_vector = calculator.calculate_net_force()

        return jsonify({
            'success': True,
            'fx': round(net_force_vector.x, 6),
            'fy': round(net_force_vector.y, 6),
            'magnitude': round(net_force_vector.magnitude(), 6)
        })

    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': 'Error interno del servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)