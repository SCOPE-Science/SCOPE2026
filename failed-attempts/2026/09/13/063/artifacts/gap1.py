import numpy as np, math

def Fs(w):
    if w == 0: return 0.0
    return (w*w/2.0)*(math.log(abs(w))-1.5)

def Dlog(a, b, c, d):
    return Fs(b-c)-Fs(b-d)-Fs(a-c)+Fs(a-d)

def Kavg(a, b, c, d):
    return -Dlog(a, b, c, d)/((b-a)*(d-c))

def cantor(n):
    ivs = [[0.0, 1.0]]
    for _ in range(n):
        n0 = []
        for (a, b) in ivs:
            L = (b-a)/3
            n0.append([a, a+L]); n0.append([b-L, b])
        ivs = n0
    return ivs

def build_Qavg(cells):
    N = len(cells)
    Q = np.zeros((N, N))
    for i, (a, b) in enumerate(cells):
        for j, (c, d) in enumerate(cells):
            Q[i, j] = Kavg(a, b, c, d)
    return Q

def outer_mask(cells):
    m = np.zeros(len(cells))
    for i, (a, b) in enumerate(cells):
        mid = (a+b)/2
        if mid < 1/9+1e-12 or mid > 8/9-1e-12:
            m[i] = 1.0
    return m

def solve_free(Q):
    N = Q.shape[0]
    ones = np.ones(N)
    v = np.linalg.solve(Q, ones)
    s = v.sum()
    return v/s, 1/s

def solve_constrained(Q, o, t):
    # min w'Qw s.t. sum=1, o'w=t  (KKT, equality only)
    N = Q.shape[0]
    M = np.zeros((N+2, N+2))
    M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o
    M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    w = sol[:N]
    return w, float(w @ Q @ w)

for n in [5, 6, 7, 8]:
    cells = cantor(n)
    Q = build_Qavg(cells)
    w, V = solve_free(Q)
    o = outer_mask(cells)
    a_star = float(o @ w)/2
    print(f"n={n} N={len(cells)} V_up={V:.7f} a*={a_star:.6f} minw={w.min():.2e}", flush=True)
    if n == 8:
        for a0 in [0.245, 0.25, 0.255, 0.26, 0.27, 0.28, a_star]:
            wc, f = solve_constrained(Q, o, 2*a0)
            print(f"   a0={a0:.4f} f={f:.7f} excess={f-V:.7f} minw={wc.min():.2e}", flush=True)
