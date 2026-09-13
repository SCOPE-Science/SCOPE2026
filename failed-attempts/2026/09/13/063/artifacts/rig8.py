import numpy as np, math

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

n = 6
cells = cantor_int(n); N = len(cells); h = (cells[0][1]-cells[0][0])/P
Qm = np.array([[Qpair(A1, B1, A2, B2, h) for (A2, B2) in cells] for (A1, B1) in cells])
ones = np.ones(N)
v = np.linalg.solve(Qm, ones); m = v/v.sum(); m = (m+m[::-1])/2; m /= m.sum()
Vf = 1/v.sum()
print("Vf=", Vf)

# normalized first-variation direction at m: d_k = m_k*((Qm m)_k - Ef); sum=0.
Ef = float(m@Qm@m)
r = Qm@m - Ef
d = m*r
print("max|r|=", np.abs(r).max(), "(expect ~1e-12)")
# Instead use EXACT parametric direction: transfer eps mass outer->inner uniformly over CANDIDATE m.
# d = u_in - u_out where u_out[k] = m_k/O for outer cells, u_in[k]=m_k/In for inner (O=In=1/2 mass).
O = sum(m[k] for k in range(N) if (cells[k][0]+cells[k][1])/2 < P/9 or (cells[k][0]+cells[k][1])/2 > 8*P/9)
In = 1-O
print("O=", O, "In=", In)
u = np.zeros(N)
for k in range(N):
    mid = (cells[k][0]+cells[k][1])/2
    u[k] = m[k]/In if (P/9 <= mid <= 8*P/9) else -m[k]/O
print("sum u =", u.sum())
# first-order energy change per unit eps: 2 r'u ; second order: u'Q u
g1 = 2*float(r@u)
g2 = float(u@Qm@u)
print("g1=", g1, "g2=", g2)
# constrained optimum shift: eps* = -g1/(2 g2); gap = g1^2/(4 g2)
print("eps*=", -g1/(2*g2), "gap=", g1**2/(4*g2))
# So the transfer direction barely helps (m already optimal). Need SECOND-ORDER/robust argument.
# Robust route: for ANY mu with outer mass 2a0, I(mu) >= m-anchored lower bound:
# I(mu) >= sum_k mu_k (Umid_k - osc_k) - tail, where mu_k = mu(cell k), tail = far-field C\C6 error.
# Then min over mu_k in outer/inner groups: I >= 2a0*minOut + (1-2a0)*minIn - tail.
# Compute:
mids = [(A+B)//2 for (A, B) in cells]
def Kav(xn, A2, B2):
    h = (B2-A2)/P
    F = lambda t: t*math.log(t)-t if t > 0 else 0.0
    if xn < A2: return -(F((B2-xn)/P)-F((A2-xn)/P))/h
    elif xn > B2: return -(F((xn-A2)/P)-F((xn-B2)/P))/h
    else: return -(F((xn-A2)/P)+F((B2-xn)/P))/h
Umid = np.array([sum(m[j]*Kav(xn, A2, B2) for j, (A2, B2) in enumerate(cells)) for xn in mids])
def osc_k(k):
    A1, B1 = cells[k]
    F = lambda t: t*math.log(t)-t if t > 0 else 0.0
    def T(x, A2, B2):
        if x < A2: return -(F((B2-x)/P)-F((A2-x)/P))/((B2-A2)/P)
        elif x > B2: return -(F((x-A2)/P)-F((x-B2)/P))/((B2-A2)/P)
        else: return -(F((x-A2)/P)+F((B2-x)/P))/((B2-A2)/P)
    s = 0.0
    for j, (A2, B2) in enumerate(cells):
        if j == k:
            cands = [T(A2, A2, B2), T(B2, A2, B2)]
            s += m[j]*(max(cands)-min(cands))
        else:
            cands = [T(A1, A2, B2), T(B1, A2, B2)]
            s += m[j]*(max(cands)-min(cands))
    return s
osc = np.array([osc_k(k) for k in range(N)])
L = Umid-osc
def grp(k):
    mid = (cells[k][0]+cells[k][1])/2
    return 'out' if (mid < P/9 or mid > 8*P/9) else 'inm'
minOut = min(L[k] for k in range(N) if grp(k) == 'out')
minIn = min(L[k] for k in range(N) if grp(k) == 'inm')
print("minOut=", minOut, "minIn=", minIn)
for a0 in [0.25, 0.255, 0.26, 0.27, 0.287]:
    print(f"  a0={a0}: lower={2*a0*minOut+(1-2*a0)*minIn:.7f}")
print("Vf=", Vf, "V_up~1.5376 (loose uniform competitor)")
