import numpy as np, math, time

P = 3**10
def cantor_int(n):
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def Qpair(A1, B1, A2, B2, h):
    F2 = lambda w: 0.0 if w == 0 else (w*w/2)*(math.log(abs(w))-1.5)
    a, b, c, d = A1/P, B1/P, A2/P, B2/P
    return -(F2(b-c)-F2(b-d)-F2(a-c)+F2(a-d))/(h*h)

def solve_eq(Q, o, t):
    N = Q.shape[0]
    M = np.zeros((N+2, N+2)); M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o; M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    return sol[:N]

t0 = time.time()
n = 8
cells = cantor_int(n); N = len(cells); h = (cells[0][1]-cells[0][0])/P
o = np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells])
Qm = np.array([[Qpair(A1, B1, A2, B2, h) for (A2, B2) in cells] for (A1, B1) in cells])
M = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells):
    for j, (A2, B2) in enumerate(cells):
        if i == j: M[i, j] = math.log(1.0/h)
        else: M[i, j] = math.log(1.0/(max(abs(B1-A2), abs(B2-A1))/P))
ones = np.ones(N)
v = np.linalg.solve(Qm, ones); Vf = 1/v.sum()
wcQ = solve_eq(Qm, o, 0.5); fQ = float(wcQ@Qm@wcQ)
wcM = solve_eq(M, o, 0.5); fM = float(wcM@M@wcM)
print(f"n=8: Vf={Vf:.7f} fQ(0.5)={fQ:.7f} gap={fQ-Vf:.7f} | fM(0.5)={fM:.7f} minorant_loss={fQ-fM:.7f} (elapsed {time.time()-t0:.0f}s)", flush=True)

# Valid V_up via self-similar (Cantor) measure sigma supported on C: I(sigma) = 2 log 3 - E log(2+Z).
# E log(2+Z) by tree recursion to depth 22 (exact distribution of Z=B-A via pair recursion).
from collections import defaultdict
dist = {(0, 0): 1.0}  # (A_int, B_int) in units of 3^-d at current depth, weight
# A,B built digit by digit in {0,2}; Z enforcing... simpler: distribution of D_k = digits difference
# Z = sum_{k>=1} (b_k - a_k) 3^-k, each in {-2,0,2}/3^k with P(0)=1/2, P(+-2)=1/4.
from math import fsum
K = 22
# distribution of S = sum_{k=1..K} d_k 3^{K-k} (integer, units 3^-K), d_k in {-2,0,2}
d = {0: 1.0}
for k in range(1, K+1):
    nd = defaultdict(float)
    for s, p in d.items():
        nd[3*s] += p*0.5; nd[3*s+2] += p*0.25; nd[3*s-2] += p*0.25
    d = nd
scale = 3**K
E = 0.0
for s, p in d.items():
    z = s/scale
    E += p*math.log(2+z)
# tail: |Z - Z_K| <= 3^-K; |d/dz log(2+z)| <= 1 (z>=-1) so error <= 3^-K
print(f"E log(2+Z) ~= {E:.8f} +- {3**-K:.2e}")
Isig = 2*math.log(3) - E
print(f"I(sigma) ~= {Isig:.7f} (VALID V_up: sigma supported on C) vs fQ(0.5)={fQ:.7f} vs fM(0.5)={fM:.7f}")
