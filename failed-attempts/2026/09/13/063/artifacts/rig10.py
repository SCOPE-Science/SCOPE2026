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

n = 8
cells = cantor_int(n); N = len(cells); h = (cells[0][1]-cells[0][0])/P
Qm = np.array([[Qpair(A1, B1, A2, B2, h) for (A2, B2) in cells] for (A1, B1) in cells])
ones = np.ones(N)
o = np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells])
def solve_eq(Q, o, t):
    N = Q.shape[0]
    M = np.zeros((N+2, N+2)); M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o; M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    return sol[:N], sol[N], sol[N+1]
wc, lam, gam = solve_eq(Qm, o, 0.5)
f = float(wc@Qm@wc)
print("f(a0=0.25)=", f, "minw=", wc.min())
# symmetrize wc
wc = (wc+wc[::-1])/2; wc /= wc.sum()
print("after sym: f=", float(wc@Qm@wc), "outer=", o@wc)
np.save("output/artifacts/wc_n8_a025.npy", wc)
np.save("output/artifacts/cells_n8.npy", np.array(cells))
# grouping diagnostics: mass per level-2 cylinder and per level-8 cell stats
masses = [0, 0, 0, 0]
for k, (A, B) in enumerate(cells):
    mid = (A+B)/2
    if mid < P/9: masses[0] += wc[k]
    elif mid < P/3: masses[1] += wc[k]
    elif mid < 2*P/3+1: masses[2] += wc[k]
    else: masses[3] += wc[k]
print("level-2 masses:", masses)
