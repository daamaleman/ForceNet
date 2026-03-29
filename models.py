import math
from dataclasses import dataclass
from typing import List

@dataclass
class Vector2D:
    """Vector 2D reutilizable (modularidad)."""
    x: float
    y: float

    def magnitude(self) -> float:
        """Magnitud del vector (utilizado para |F|)."""
        return math.sqrt(self.x ** 2 + self.y ** 2)


class PointCharge:
    """Clase que representa una carga puntual (OOP)."""
    def __init__(self, q: float, x: float, y: float):
        self.q = q
        self.position = Vector2D(x, y)


class ForceCalculator:
    """Calculadora de fuerza neta (OOP + encapsulación)."""
    K = 8.99e9  # Constante de Coulomb (Nm²/C²)

    def __init__(self, target: PointCharge, other_charges: List[PointCharge]):
        self.target = target
        self.other_charges = other_charges

    def calculate_net_force(self) -> Vector2D:
        """Calcula la fuerza neta sobre la carga objetivo usando la ley de Coulomb en 2D."""
        net_fx = 0.0
        net_fy = 0.0

        for charge in self.other_charges:
            dx = self.target.position.x - charge.position.x
            dy = self.target.position.y - charge.position.y
            r_squared = dx * dx + dy * dy

            if r_squared < 1e-10:
                raise ValueError("Una carga puntual coincide con la posición de la carga objetivo. La fuerza sería infinita.")

            # Fórmula vectorial: F = k * q1 * q2 * (r1 - r2) / |r1 - r2|^3
            r_cubed = r_squared ** 1.5
            factor = self.K * self.target.q * charge.q / r_cubed

            net_fx += factor * dx
            net_fy += factor * dy

        return Vector2D(net_fx, net_fy)