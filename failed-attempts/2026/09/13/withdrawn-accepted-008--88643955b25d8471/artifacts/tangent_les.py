"""Tangent LES dimension bookkeeping for W (naive) and W_res (via Springer)."""
# Dimensions: dim g=8, dim b=5, dim g/b=3, dim n=3, dim b*=5, r=2 (excess)
g, b, gmodb, n, r = 8, 5, 3, 3, 2

# Naive W = L0 x_X [N_der/G]: T = fib(T_L0 (+) T_L1 -> T_X)
# deg -1: g(+)g -> g surjective, ker = diag g
Hm1 = g  # 8
# deg 0: 0(+)g* -> g* iso
H0 = 0
# deg 1: 0(+)C^r -> 0
H1 = r  # 2
vd = -Hm1 + H0 - H1
print(f"W naive: H^-1={Hm1}, H^0={H0}, H^1={H1}, vd={vd}")
assert (Hm1, H0, H1, vd) == (8, 0, 2, -10)

# Resolved W_res = L0 x_X S at s=(eB,0):
# deg -1: g(+)b -> g surjective, ker dim = g+b-g
Rm1 = g + b - g  # 5 = b
# deg 0: 0(+)V -> g*, V=(g/b)(+)n dim 6, im = n dim 3
V = gmodb + n
assert V == 6
R0 = V - n  # ker dmu = g/b = 3
# deg 1: coker dmu = g*/n, dim 8-3
R1 = g - n  # 5 = b*
assert R1 == b
vdR = -Rm1 + R0 - R1
print(f"W_res: H^-1={Rm1}, H^0={R0}, H^1={R1}, vd={vdR}")
assert (Rm1, R0, R1, vdR) == (5, 3, 5, -7)
assert Rm1 == R1, "0-shifted symmetry requires H^-1 dual H^1"
# Relative tangent of S at s: H^-1=0, H^0 ext(g/b,g/b) dim 6, H^1=b* dim 5
# Cotangent L_S at s: [V* -> b*] dims (6,5). Ranks match.
print(f"S rel-tangent ranks (0,6,5) vs cotangent ranks (0,6,5): match = {V==6 and R1==b}")
print("OK: naive (8,0,2)/-10; resolved symmetric (5,3,5)/-7.")
