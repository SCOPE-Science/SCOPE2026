import numpy as np, math

def intlog(w):
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    wD = Decimal(str(w))
    e = int(math.floor(math.log2(w)))
    m = wD / (Decimal(2) ** e)
    z = (m-1)/(m+1)
    s = Decimal(0); t = z; k = 0
    while True:
        s += t/(2*k+1); k += 1; t = t*z*z
        if abs(float(t)) < 1e-55:
            tail = abs(float(t))/(1-float(z*z))/(2*k+1); break
    s = 2*s; tail2 = 2*tail
    v = s + e*Decimal(2).ln()
    return float(v)-tail2-1e-15, float(v)+tail2+1e-15

P = 3**8
def Gpos(wint):
    if wint == 0: return (0.0, 0.0)
    w = wint/P
    lo, hi = intlog(w)
    c = w*w
    m = 1e-13*(1+c)
    a, b = (c*lo-m, c*hi+m)
    c2, d2 = (c*(1-1e-15), c*(1+1e-15))
    return (a/2-3*d2/4-1e-14, b/2-3*c2/4+1e-14)

def Dlog_cell(A1, B1, A2, B2):
    Fbc = Gpos(abs(B1-A2)); Fbd = Gpos(abs(B1-B2)); Fac = Gpos(abs(A1-A2)); Fad = Gpos(abs(A1-B2))
    return (Fbc[0]-Fbd[1]-Fac[1]+Fad[0], Fbc[1]-Fbd[0]-Fac[0]+Fad[1])

def cantor_int(n):
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def outer_mask(cells):
    m = []
    for (A, B) in cells:
        mid = (A+B)/2
        m.append(1.0 if (mid < P/9+1e-9 or mid > 8*P/9-1e-9) else 0.0)
    return np.array(m)

def Kmin_off(A1, B1, A2, B2):
    mx = max(abs(B1-A2), abs(B2-A1))/P
    return math.log(1.0/mx) - 1e-12  # tiny downward margin (float log error << 1e-12)

n = 6
cells = cantor_int(n)
N = len(cells)
h_units = cells[0][1]-cells[0][0]
h = h_units/P
o = outer_mask(cells)
_, Dhi = Dlog_cell(0, h_units, 0, h_units)
Kself_up = -Dlog_cell(0, h_units, 0, h_units)[0]/(h*h)  # upper bound on Kavg self
Kself_lo = math.log(4.0/h)  # rigorous lower bound (proved in DRAFT)
print("Kself interval:", Kself_lo, Kself_up)

# Interval matrix Q with directed margins: off-diag Qlow=Kmin (minus margin),
# and Qup_gap = Kmin over min-dist? For circle-arc lemma we need, for each pair with
# both i,j in the SAME level-2 cylinder group G, a lower bound; for cross pairs upper.
# Simpler: certify lower bound f(w)-V_up >= gap via:
#   f(w) >= w'Qlow w + sum_i w_i^2 (Kself_lo - qlow_self_correction)...
# Actually Qlow has diag Kself_lo, off-diag Kmin. Then w'Qlow w <= f(w) entrywise. Good.
Qlow = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells):
    for j, (A2, B2) in enumerate(cells):
        if i == j: Qlow[i, j] = Kself_lo
        else: Qlow[i, j] = Kmin_off(A1, B1, A2, B2)

# V_up: rigorous upper bound on V via uniform-on-C8 competitor + exact-interval energy.
cells8 = cantor_int(8)
tot = len(cells8)*(cells8[0][1]-cells8[0][0])/P
E_lo, E_hi = 0.0, 0.0
for (A1, B1) in cells8:
    for (A2, B2) in cells8:
        lo, hi = Dlog_cell(A1, B1, A2, B2)
        E_lo += lo; E_hi += hi
E_lo /= tot*tot; E_hi /= tot*tot
V_up = -E_lo  # I = -E[log]/tot^2; E_lo<=E so -E_lo >= I... wait sign: I=E[-log]=-E[log]
print("uniform-C8 energy interval: [", -E_hi, ",", -E_lo, "]")
print("V_up =", V_up)

# Constrained minimizer of w'Qlow w over sum=1, o'w=t (equality), t=2*0.255 and 2*0.25
def solve_eq(Q, o, t):
    N = Q.shape[0]
    M = np.zeros((N+2, N+2)); M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o; M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    return sol[:N]
for a0 in [0.25, 0.255]:
    t = 2*a0
    wc = solve_eq(Qlow, o, t)
    f = float(wc @ Qlow @ wc)
    print(f"a0={a0}: f_lowmodel={f:.7f} excess vs V_up = {f-V_up:.7f} minw={wc.min():.2e}")
np.save("output/artifacts/Qlow_n6.npy", Qlow)
np.save("output/artifacts/cells_n6.npy", np.array(cells))
