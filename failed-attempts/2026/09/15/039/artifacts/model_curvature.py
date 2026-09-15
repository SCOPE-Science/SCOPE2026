"""Model-geometry half-PIC check (pure Python, no numpy).

Orthonormal frame e1..e4, orientation e1234. Curvature operator M on
basis [12,13,14,23,24,34] with M[a,b] = R_{ijkl}. Self-dual basis:
  eta1=(e12+e34)/s2, eta2=(e13-e24)/s2, eta3=(e14+e23)/s2
anti-self-dual:
  th1=(e12-e34)/s2, th2=(e13+e24)/s2, th3=(e14-e23)/s2
A[a][b] = Rm(eta_a,eta_b), C = Rm(th,th), B = Rm(eta,th).
For the product/diagonal models below all blocks are diagonal and
eigenvalues are read off directly.
"""
from fractions import Fraction as F

def block_diagonal_product(k12, k13, k14, k23, k24, k34):
    # M diagonal with these entries; cross terms assumed 0 (products).
    d = {'12': k12, '13': k13, '14': k14, '23': k23, '24': k24, '34': k34}
    A11 = (d['12'] + d['34']) / 2
    A22 = (d['13'] + d['24']) / 2
    A33 = (d['14'] + d['23']) / 2
    C11 = (d['12'] + d['34']) / 2
    C22 = (d['13'] + d['24']) / 2
    C33 = (d['14'] + d['23']) / 2
    B11 = (d['12'] - d['34']) / 2
    return sorted([A11, A22, A33]), sorted([C11, C22, C33]), B11

def two_sum(eigs):
    return eigs[0] + eigs[1]

def report(name, k):
    A, C, B11 = block_diagonal_product(*k)
    print(f"{name}: A={A} 2-sum={two_sum(A)} | C={C} 2-sum={two_sum(C)} | B11={B11}")

# Shrinker normalizations: Rc = (1/2) g on compact factors.
h = F(1, 2)   # S^2 factor K with Rc = K g = g/2
q = F(1, 4)   # S^3 factor K with Rc = 2K g = g/2
s4 = F(1, 6)  # S^4 K with Rc = 3K g = g/2
z = F(0, 1)
# (K12,K13,K14,K23,K24,K34); sphere factors span first indices.
report("S2xS2 (k=1/2,1/2)", (h, z, z, z, z, h))
report("S2xR2 (k=1/2)", (h, z, z, z, z, z))
report("S3xR  (K=1/4 on e123)", (q, q, z, q, z, z))
report("S4    (K=1/6)", (s4, s4, s4, s4, s4, s4))
