import numpy as np, math

P = 3**10  # finer integer lattice; level n<=10 cells exact
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

def Kavg_lo(A1, B1, A2, B2):
    h = (B1-A1)/P
    lo, hi = Dlog_cell(A1, B1, A2, B2)
    return -hi/(h*h)

def Kavg_hi(A1, B1, A2, B2):
    h = (B1-A1)/P
    lo, hi = Dlog_cell(A1, B1, A2, B2)
    return -lo/(h*h)

# Level-6 cells, then MIDPOINT masses from mirror-symmetric Qmid solve;
# anchor potential at midpoint m_k of each cell: U_k = sum_j m_j K(x_k, y_j avg over cell j)
# K(x_k, cell j) for k!=j: interval via intlog on [mindist,maxdist] (log concave -> trap bounds).
# For k==j: self potential at midpoint: (1/h) int_{cell} -log|x-y| dy = -h_mid... closed form.
def Kpoint_cell_lo_hi(xn, A2, B2):
    # xn int coord of point; returns enclosure of (1/h) int_{cell2} K(xn,y) dy
    h = (B2-A2)/P
    if xn < A2 or xn > B2:
        d1 = abs(xn-A2)/P; d2 = abs(xn-B2)/P
        lo1, hi1 = intlog(d1); lo2, hi2 = intlog(d2)
        # H(d) = d log d - d; integral of -log over [d1..d2]-ish orientation
        # int_{A2}^{B2} -log|xn-y| dy = H(|xn-A2|)-H(|xn-B2|) with sign: F(d)=d log d - d
        F = lambda d, l: d*l-d
        # lower: use lo where coefficient positive... d>0: F increasing iff log d > 0
        # do brute 4-corner enclosure
        vals_lo = [F(d1, lo1)-F(d2, hi2), F(d1, hi1)-F(d2, lo2), F(d1, lo1)-F(d2, lo2), F(d1, hi1)-F(d2, hi2)]
        # actually for xn outside, all terms same orientation; widen by float margin
        return (min(vals_lo)-1e-12, max(vals_lo)+1e-12)
    else:
        # split at xn
        L1 = abs(xn-A2)/P; L2 = abs(B2-xn)/P
        tot_lo, tot_hi = 0.0, 0.0
        for L in [L1, L2]:
            if L == 0: continue
            lo, hi = intlog(L)
            tot_lo += L*lo-L; tot_hi += L*hi-L
        m = 1e-12*(1+tot_hi)
        return (-(tot_hi)-m, -(tot_lo)+m)  # still integral, divide below

n = 6
cells = cantor_int(n)
N = len(cells)
h = (cells[0][1]-cells[0][0])/P
# midpoint Q model (float ok for CANDIDATE masses; certification via interval lower bounds)
Qm = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells):
    for j, (A2, B2) in enumerate(cells):
        a, b, c, d = A1/P, B1/P, A2/P, B2/P
        Qm[i, j] = -((lambda a=a,b=b,c=c,d=d: (lambda F: F(b-c)-F(b-d)-F(a-c)+F(a-d))(lambda w: 0.0 if w==0 else (w*w/2)*(math.log(abs(w))-1.5)))())/(h*h)
ones = np.ones(N)
v = np.linalg.solve(Qm, ones); m = v/v.sum(); Vf = 1/v.sum()
print("candidate energy:", Vf)
# symmetry check
print("max |m_i - m_{N-1-i}| =", np.abs(m-m[::-1]).max())
# anchor potentials at midpoints, interval certified
mids = [(A+B)//2 for (A, B) in cells]
Ulo = np.zeros(N); Uhi = np.zeros(N)
for k, xn in enumerate(mids):
    slo, shi = 0.0, 0.0
    for j, (A2, B2) in enumerate(cells):
        lo, hi = Kpoint_cell_lo_hi(xn, A2, B2)
        slo += m[j]*lo/h; shi += m[j]*hi/h
    Ulo[k], Uhi[k] = slo, shi
print("anchor U intervals (first 8):")
for k in range(8):
    print(f"  k={k}: [{Ulo[k]:.6f}, {Uhi[k]:.6f}] width={Uhi[k]-Ulo[k]:.2e}")
print("max width:", (Uhi-Ulo).max())
# oscillation of U^m over each cell: for x in cell k, |U(x)-U(xk)| <= sum_j m_j osc_{kj}
# osc for j!=k: log(maxdist/mindist); j==k (self): sup over x in cell of |selfpot(x)-selfpot(mid)|
# selfpot(x) = (1/h) int_cell -log|x-y| dy; max at endpoints? compute: range <= h*(1+|log|)... bound:
# selfpot(x)-selfpot(mid): both in [h*(log(1/h)+1)-ish]. Use explicit: selfpot(x) <= selfpot-mid + h.
osc_self = h  # placeholder to be proved: actually prove osc_self <= h*|log|? refine below
# compute offdiag osc exactly
def osc_off(A1, B1, A2, B2):
    mx = max(abs(B1-A2), abs(B2-A1))/P
    mn = min(abs(B1-A2), abs(B2-A1), abs(A1-A2), abs(B1-B2))/P
    return math.log(mx/mn)
osc = np.zeros(N)
for k, (A1, B1) in enumerate(cells):
    s = 0.0
    for j, (A2, B2) in enumerate(cells):
        if j == k: s += m[j]*osc_self
        else: s += m[j]*osc_off(A1, B1, A2, B2)
    osc[k] = s
print("osc bounds (first 8):", osc[:8])
print("max osc:", osc.max())
# With U(x) in [Ulo[k]-osc[k], Uhi[k]+osc[k]] on cell k, and anchor values ~?
# mu-outer vs inner: which cells are outer (within level-2 extreme)?
outer = np.array([1.0 if ((A+B)/2 < P/9+1 or (A+B)/2 > 8*P/9-1) else 0.0 for (A, B) in cells])
print("outer count:", outer.sum())
# group bounds
for name, sel in [("outer", outer == 1), ("inner", outer == 0)]:
    lo = min(Ulo[k]-osc[k] for k in np.where(sel)[0])
    hi = max(Uhi[k]+osc[k] for k in np.where(sel)[0])
    print(f"{name}: U in [{lo:.6f}, {hi:.6f}]")
