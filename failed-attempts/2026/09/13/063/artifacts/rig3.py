import numpy as np, math

P = 3**8
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

# overlap mass of each level-6 cell with outer cylinders O = [0,1/9]u[8/9,1]
cells6 = cantor_int(6)
h = (cells6[0][1]-cells6[0][0])/P
o = []
for (A, B) in cells6:
    a, b = A/P, B/P
    ov = max(0.0, min(b, 1/9)-max(a, 0.0)) + max(0.0, min(b, 1.0)-max(a, 8/9))
    o.append(ov/h)
print("distinct overlap fractions:", sorted(set([round(x, 6) for x in o])))
# Kavg matrix exactly (float) + Kavg interval bounds
N = len(cells6)
Klo = np.zeros((N, N)); Khi = np.zeros((N, N)); Kf = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells6):
    for j, (A2, B2) in enumerate(cells6):
        lo, hi = Dlog_cell(A1, B1, A2, B2)
        Klo[i, j] = -hi/(h*h); Khi[i, j] = -lo/(h*h)
        Kf[i, j] = (Klo[i, j]+Khi[i, j])/2
print("max interval width:", np.abs(Khi-Klo).max())
o = np.array(o)
def solve_eq(Q, o, t):
    N = Q.shape[0]
    M = np.zeros((N+2, N+2)); M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o; M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    return sol[:N], sol[N], sol[N+1]
# free optimum of midpoint model + outer mass
ones = np.ones(N)
v = np.linalg.solve(Kf, ones); wf = v/v.sum(); Vf = 1/v.sum()
print("Vf(mid)=", Vf, "outer=", o@wf)
for a0 in [0.25, 0.255, 0.26, 0.27]:
    t = 2*a0
    wc, lam, gam = solve_eq(Kf, o, t)
    f = float(wc@Kf@wc)
    # rigorous lower bound: f_true(wc) >= wc'Klo wc (entrywise) ; V_up=1.53755583
    flow = float(wc@Klo@wc)
    print(f"a0={a0}: fmid={f:.7f} flow={flow:.7f} exc_flow={flow-1.53755583:.7f} minw={wc.min():.2e} gam={gam:.4f}")
