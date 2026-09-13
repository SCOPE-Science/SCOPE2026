import numpy as np, math

P = 3**10
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

def cantor_int(n):
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def Kav_point_cell(xn, A2, B2):
    """(1/h2) int_{cell2} K(xn,y) dy with K=-log|x-y|/P-scale; xn int coord.
    Returns float (non-rigorous pilot)."""
    h = (B2-A2)/P
    F = lambda t: t*math.log(t)-t if t > 0 else 0.0
    if xn < A2:
        return -(F((B2-xn)/P)-F((A2-xn)/P))/h
    elif xn > B2:
        return -(F((xn-A2)/P)-F((xn-B2)/P))/h
    else:
        return (F((xn-A2)/P)+F((B2-xn)/P)+2*xn/P*0)/h * -1.0 + 0.0  # int = -(F(L1)+F(L2)); /h

n = 6
cells = cantor_int(n)
N = len(cells)
h = (cells[0][1]-cells[0][0])/P
def Qpair(A1, B1, A2, B2):
    F2 = lambda w: 0.0 if w == 0 else (w*w/2)*(math.log(abs(w))-1.5)
    a, b, c, d = A1/P, B1/P, A2/P, B2/P
    return -(F2(b-c)-F2(b-d)-F2(a-c)+F2(a-d))/(h*h)
Qm = np.array([[Qpair(A1, B1, A2, B2) for (A2, B2) in cells] for (A1, B1) in cells])
ones = np.ones(N)
v = np.linalg.solve(Qm, ones); m = v/v.sum(); Vf = 1/v.sum()
# symmetrize candidate
m = (m+m[::-1])/2; m = m/m.sum()
Ef = float(m@Qm@m)
print("Vf=", Vf, "Ef(sym)=", Ef)

# anchor via POINT-cell averages (exact, principal): U_k = sum_j m_j Kav(xk, cellj)
mids = [(A+B)//2 for (A, B) in cells]
Umid = np.array([sum(m[j]*Kav_point_cell(xn, A2, B2) for j, (A2, B2) in enumerate(cells)) for k, xn in enumerate(mids)])
print("Umid[:8] =", Umid[:8])
print("Umid[32:40] =", Umid[32:40])
print("mean Umid =", Umid.mean(), " m.Umid =", m@Umid)
# oscillation: sup over x in cell k of |U(x)-U(xk)|
def osc_k(k):
    A1, B1 = cells[k]; xk = mids[k]
    s = 0.0
    for j, (A2, B2) in enumerate(cells):
        if j == k:
            # self: sup_{x in cell} |S(x)-S(xk)|, S(x)=(1/h)int_cell K(x,y)dy
            # S(x) = -(F(x-A)+F(B-x))/h; max at endpoints? compute exactly by sampling endpoints+mid
            F = lambda t: t*math.log(t)-t if t > 0 else 0.0
            def S(x):
                return -(F((x-A2)/P)+F((B2-x)/P))/h
            cands = [S(A2), S(B2), S((A2+B2)//2)]
            s += m[j]*(max(cands)-min(cands))
        else:
            F = lambda t: t*math.log(t)-t if t > 0 else 0.0
            def T(x):
                if x < A2: return -(F((B2-x)/P)-F((A2-x)/P))/h
                else: return -(F((x-A2)/P)-F((x-B2)/P))/h
            cands = [T(A1), T(B1)]
            s += m[j]*(max(cands)-min(cands))
    return s
osc = np.array([osc_k(k) for k in range(N)])
print("osc[:8] =", osc[:8], "max=", osc.max())
# group cells by level-2 cylinder: outer = I00 u I11 ; inner = I01 u I10
def grp(k):
    A, B = cells[k]; mid = (A+B)/2
    if mid < P/9 or mid > 8*P/9: return 'out'
    return 'inm'
for g in ['out', 'inm']:
    idx = [k for k in range(N) if grp(k) == g]
    lo = min(Umid[k]-osc[k] for k in idx); hi = max(Umid[k]+osc[k] for k in idx)
    print(f"{g}: count={len(idx)} U in [{lo:.6f}, {hi:.6f}]")
    print("   anchors min/max:", min(Umid[k] for k in idx), max(Umid[k] for k in idx))
# scaling check: anchors should be ~ Vf + (per-cell deviation); anchors vary 0.3..1.5??
# That means candidate m is NOT near-constant potential -> because point-anchor != cell-average anchor.
# Cell-average anchor: A_k = sum_j m_j Qm[k,j] should be ~const=Vf. Verify:
A = Qm@m
print("cell-avg anchors: min/max/mean:", A.min(), A.max(), A.mean())
print("A[:8] =", A[:8])
