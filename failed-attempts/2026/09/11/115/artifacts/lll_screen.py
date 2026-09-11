"""Bounded recovery test: LLL / cluster-expansion / spectral feasibility screen.

Target: chi_mu(H4)=3 and chi_BM(H4)=3 for 4-regular acyclic Borel H4.
Question: does any off-the-shelf probabilistic bound give a measurable
3-coloring of a max-degree-4 graph? (Uniform random q-coloring, bad event
per edge = monochromatic, dependency degree d <= 2*(Delta-1) = 6.)

Run: python3 output/artifacts/lll_screen.py
"""
import math

Delta = 4
d = 2 * (Delta - 1)  # edge-adjacency dependency degree
print(f"Delta={Delta}, dependency degree d={d}")

print("\n-- symmetric LLL: need e*p*(d+1) <= 1 --")
for q in [3, 4, 5]:
    p = 1.0 / q
    val = math.e * p * (d + 1)
    print(f"q={q}: e*p*(d+1) = {val:.4f}  holds={val <= 1}")

print("\n-- cluster expansion (symmetric x): need max_x x*(1-x)^d >= p --")
xs = [i / 10000 for i in range(1, 10000)]
best_val, best_x = max((x * (1 - x) ** d, x) for x in xs)
print(f"max_x x(1-x)^d = {best_val:.5f} at x={best_x:.4f}; need >= p=1/3={1/3:.4f}")
print(f"gap factor p/max = {(1/3)/best_val:.2f}x short")
# analytic optimum x*=1/(d+1): value = (1/(d+1))*(d/(d+1))^d
xa = 1 / (d + 1)
va = xa * (1 - xa) ** d
print(f"analytic check: x*=1/(d+1)={xa:.4f} gives {va:.5f} (matches grid: {abs(va-best_val)<1e-4})")

print("\n-- Hoffman spectral screen on infinite 4-regular tree --")
lam_max = 4.0
lam_min = -2 * math.sqrt(3)
hoff = -lam_min / (lam_max - lam_min)
print(f"independence-ratio cap = {hoff:.4f}; need >= 1/3={1/3:.4f} for 3 classes")
print("-> no spectral obstruction to density-1/3 classes (necessary, not sufficient)")

print("\nCONCLUSION: symmetric LLL fails (6.34 > 1); cluster expansion fails by")
print("5.88x; spectral bound does not obstruct. No off-the-shelf probabilistic")
print("route yields a measurable 3-coloring beating the Brooks bound 4.")
print("RECOVERY_TEST_RESULT: NEGATIVE (blocked, logged with gap factors)")
