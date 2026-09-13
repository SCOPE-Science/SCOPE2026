import numpy as np

def Phi(u):
    u = np.asarray(u, float)
    out = np.zeros_like(u)
    nz = u != 0
    uu = u[nz]
    out[nz] = (uu**2/2)*(np.log(np.abs(uu))-1.5)
    return out

def build_Q(intervals, subdiv):
    J = []
    for (a, b) in intervals:
        h = (b-a)/subdiv
        for k in range(subdiv):
            J.append((a+k*h, a+(k+1)*h))
    m = len(J)
    Q = np.zeros((m, m))
    for i in range(m):
        a, b = J[i]
        hi = b-a
        for j in range(m):
            c, d = J[j]
            hj = d-c
            val = -Phi(b-d)+Phi(a-d)+Phi(b-c)-Phi(a-c)
            Q[i, j] = val/(hi*hj)
    return J, Q

def equil_weights(Q):
    m = Q.shape[0]
    ones = np.ones(m)
    v = np.linalg.solve(Q, ones)
    s = v.sum()
    w = v/s
    return w, 1/s

def cantor_intervals(n):
    ivs = [[0.0, 1.0]]
    for _ in range(n):
        n0 = []
        for (a, b) in ivs:
            L = (b-a)/3
            n0.append([a, a+L]); n0.append([b-L, b])
        ivs = n0
    return ivs

for n in [2, 3, 4]:
    ivs = cantor_intervals(n)
    print("n=", n, "num intervals", len(ivs), flush=True)
    for subdiv in [1, 2, 4, 8]:
        J, Q = build_Q(ivs, subdiv)
        w, en = equil_weights(Q)
        print(f" subdiv={subdiv} m={len(J)} energy={en:.8f} cap={np.exp(en):.8f} minw={w.min():.4e}", flush=True)
        masses = [0, 0, 0, 0]
        for k, (a, b) in enumerate(J):
            mid = (a+b)/2
            if mid < 1/9+1e-12: masses[0] += w[k]
            elif mid < 1/3+1e-12: masses[1] += w[k]
            elif mid < 7/9+1e-12: masses[2] += w[k]
            else: masses[3] += w[k]
        print("  masses", [round(x, 6) for x in masses], flush=True)
    print("", flush=True)
