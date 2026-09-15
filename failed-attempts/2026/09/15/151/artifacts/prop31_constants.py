"""Illustrate degeneration of Prop 3.1 uniformity as I0 = 1+eta -> 1+.

From the proof: alpha < min{2*(I0-1), 1-delta2}; rho_u = 2^{-5*kappa};
need 8^m * rho_u^{2*alpha} <= (1/2) * rho_l^alpha, and C^kappa * eps^2 <= eps3^2,
plus m_{x,k} <= rho_l threshold. Hence kappa -> infinity and (eps, tau, r0) -> 0
as eta -> 0. Purely illustrative arithmetic of these constraints.
"""
import math

m = 3
delta2 = 0.1
C = 4.0  # illustrative geometric constant
eps3 = 0.01

print(f"{'eta':>8} {'alpha':>8} {'kappa_min':>10} {'rho_u':>12} {'eps_max':>12}")
for eta in [0.5, 0.25, 0.125, 1/3, 0.1, 0.05, 0.02, 0.01]:
    alpha = min(2*eta, 1-delta2) * 0.9  # strictly below the min
    # Need decay factor (s/t)^alpha <= 1/4 say, with s/t >= 2^{-5 kappa} worst
    # case available ratio per step; require kappa*alpha >= 2 (illustrative):
    kappa_min = math.ceil(2.0/alpha)
    rho_u = 2.0**(-5*kappa_min)
    # C^kappa eps^2 <= eps3^2  =>  eps <= eps3 * C^{-kappa/2}
    eps_max = eps3 * C**(-kappa_min/2.0)
    print(f"{eta:8.4f} {alpha:8.4f} {kappa_min:10d} {rho_u:12.2e} {eps_max:12.2e}")
print("\nConclusion: kappa_min ~ 2/alpha ~ 1/eta -> inf, eps_max and r0 -> 0 as eta->0.")
print("No positive uniform starting scale survives at eta = 0 (degree exactly 1).")
