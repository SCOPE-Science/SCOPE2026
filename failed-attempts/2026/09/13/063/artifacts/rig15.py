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
# pointwise-minimum matrix M: off-diag log(1/maxdist), diag log(1/h)
M = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells):
    for j, (A2, B2) in enumerate(cells):
        if i == j: M[i, j] = math.log(1.0/h)
        else: M[i, j] = math.log(1.0/(max(abs(B1-A2), abs(B2-A1))/P))
Pp = np.eye(N) - np.ones((N, N))/N
evM = np.linalg.eigvalsh(Pp@M@Pp)
evQ = np.linalg.eigvalsh(Pp@Qm@Pp)
print("M proj eig min:", evM.min(), " 2nd:", np.sort(evM)[1])
print("Qm proj eig min:", evQ.min(), " 2nd:", np.sort(evQ)[1])
print("max|Qm-M|:", np.abs(Qm-M).max(), " mean:", np.abs(Qm-M).mean())
# V_up preview: free weights m via Qm, rigorous-upper-style energy with Khi~Qm+width(5e-7)
ones = np.ones(N)
v = np.linalg.solve(Qm, ones); m = v/v.sum(); m = (m+m[::-1])/2; m /= m.sum()
Vf = float(m@Qm@m)
print("Vf=", Vf, " + width margin 5e-7 -> V_up ~", Vf+5e-7)
# constrained min of p'Mp with outer<=0.5 (float preview, equality)
o = np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells])
def solve_eq(Q, o, t):
    N = Q.shape[0]
    MM = np.zeros((N+2, N+2)); MM[:N, :N] = Q
    MM[:N, N] = 1.0; MM[:N, N+1] = o; MM[N, :N] = 1.0; MM[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(MM, rhs)
    return sol[:N], sol[N], sol[N+1]
for a0 in [0.25, 0.255]:
    wc, lam, gam = solve_eq(M, o, 2*a0)
    f = float(wc@M@wc)
    print(f"M-model a0={a0}: f={f:.7f} exc_vs_Vf={f-Vf:.7f} gam={gam:.4f} minw={wc.min():.2e}")
