"""Bounded numeric check for the Bolza quotient route (partial evidence only).

Chain: Aut(Bolza) order 48 -> quotient orbifold Q area = 4*pi/48 = pi/12.
Any Aut-invariant eigenfunction descends to Q. Yang-Yau gives
lambda1(Bolza) <= 8*pi*(2+1)/(4*pi) = 6.
Hyperbolic-disk Dirichlet lower bound via Euclidean comparison in the
Poincare model: lambda_hyp(D_rho) >= (j0/R_e)^2 / Cmax,
R_e = tanh(rho/2), Cmax = (2/(1-R_e^2))^2, j0 > 2.4.
Disk areas pi/12 (whole Q) and pi/24 (smaller nodal domain).
"""
import math

j0 = 2.4  # rigorous lower bound placeholder (true value 2.4048...)

def disk_lower_bound(A):
    # hyperbolic disk radius from area A = 2*pi*(cosh(rho)-1)
    cosh_rho = 1.0 + A / (2.0 * math.pi)
    rho = math.acosh(cosh_rho)
    Re = math.tanh(rho / 2.0)
    Cmax = (2.0 / (1.0 - Re ** 2)) ** 2
    return ((j0 / Re) ** 2) / Cmax, rho, Re, Cmax

for A, tag in [(math.pi / 12, "whole-Q area"), (math.pi / 24, "half-Q area")]:
    lb, rho, Re, Cmax = disk_lower_bound(A)
    print(f"{tag}: A={A:.6f} rho={rho:.6f} Re={Re:.6f} Cmax={Cmax:.6f} "
          f"disk-lambda-lower-bound={lb:.3f}")

print("Yang-Yau upper bound lambda1(Bolza) <= 6.0")
print("systole =", 2 * math.acosh(1 + math.sqrt(2)))
print("quotient area pi/12 =", math.pi / 12)
