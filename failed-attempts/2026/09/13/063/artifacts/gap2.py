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

def build(n):
    cells = cantor(n)
    N = len(cells)
    h = cells[0][1]-cells[0][0]
    Qavg = np.zeros((N, N))
    Qlow = np.zeros((N, N))
    for i, (a, b) in enumerate(cells):
        for j, (c, d) in enumerate(cells):
            Qavg[i, j] = Kavg(a, b, c, d)
            if i == j:
                Qlow[i, j] = math.log(4.0/h)
            else:
                mx = max(abs(b-c), abs(d-a))
                Qlow[i, j] = math.log(1.0/mx)
    o = np.zeros(N)
    for i, (a, b) in enumerate(cells):
        mid = (a+b)/2
        if mid < 1/9+1e-12 or mid > 8/9-1e-12:
            o[i] = 1.0
    return cells, Qavg, Qlow, o

def proj_psd_check(Q):
    N = Q.shape[0]
    # project onto {sum=0}: P = I - 11'/N
    P = np.eye(N) - np.ones((N, N))/N
    M = P @ Q @ P
    ev = np.linalg.eigvalsh(M)
    return ev  # one zero eigenvalue expected

def solve_eq(Q, o, t):
    N = Q.shape[0]
    M = np.zeros((N+2, N+2))
    M[:N, :N] = Q
    M[:N, N] = 1.0; M[:N, N+1] = o
    M[N, :N] = 1.0; M[N+1, :N] = o
    rhs = np.zeros(N+2); rhs[N] = 1.0; rhs[N+1] = t
    sol = np.linalg.solve(M, rhs)
    return sol[:N], sol[N], sol[N+1]

for n in [4, 5, 6]:
    cells, Qavg, Qlow, o = build(n)
    N = len(cells)
    ev_avg = proj_psd_check(Qavg)
    ev_low = proj_psd_check(Qlow)
    print(f"n={n} N={N} h={cells[0][1]-cells[0][0]:.6f}")
    print(f"  Qavg proj eig: min={ev_avg.min():.5f} 2nd={np.sort(ev_avg)[1]:.5f}")
    print(f"  Qlow proj eig: min={ev_low.min():.5f} 2nd={np.sort(ev_low)[1]:.5f}")
    print(f"  max|Qavg-Qlow| = {np.abs(Qavg-Qlow).max():.5f}")
    # free optima
    w_avg, _, _ = solve_eq(Qavg, o, 0.5)  # dummy; compute free separately
    ones = np.ones(N)
    v = np.linalg.solve(Qavg, ones); wf = v/v.sum(); Vf = 1/v.sum()
    print(f"  free Qavg: V={Vf:.7f} outer2a={o@wf:.5f} minw={wf.min():.2e}")
    for a0 in [0.25, 0.255]:
        t = 2*a0
        wc, lam, gam = solve_eq(Qlow, o, t)
        f = float(wc @ Qlow @ wc)
        print(f"   Qlow constr a0={a0}: f={f:.7f} excess_vs_Vf={f-Vf:.7f} minw={wc.min():.2e} lam={lam:.4f} gam={gam:.4f}")
