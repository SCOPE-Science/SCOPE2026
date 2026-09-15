"""Exact stationary analysis: densities, edge correlators, co-occupancies, BM-root comparison.
Appends: co-occ E[eta_p*eta_c] at levels 0->1 and 1->2, gap rho_i - J/q^i,
and checks internal consistency of the target's clauses."""
import numpy as np

def build(q, N, alpha, beta):
    S = (q**N - 1)//(q-1)
    lvl = np.zeros(S, dtype=int)
    start = [0]*N
    acc = 0
    for i in range(N):
        start[i] = acc; acc += q**i
    for s in range(S):
        for i in range(N):
            if s < start[i] + q**i:
                lvl[s] = i; break
    children = {}
    for s in range(S):
        i = int(lvl[s])
        if i < N-1:
            pos = s - start[i]
            c0 = start[i+1] + pos*q
            children[s] = [c0+k for k in range(q)]
    n = 2**S
    G = np.zeros((n, n))
    for st in range(n):
        occ = [(st >> s) & 1 for s in range(S)]
        if occ[0] == 0:
            G[st, st | 1] += alpha
        for s in range(S):
            if occ[s] == 0:
                continue
            i = int(lvl[s])
            if i == N-1:
                G[st, st ^ (1 << s)] += beta
            else:
                for c in children[s]:
                    if occ[c] == 0:
                        G[st, st ^ (1 << s) ^ (1 << c)] += 1.0/q
        G[st, st] = -G[st].sum()
    return G, lvl, S, start, children

def stat(G):
    n = G.shape[0]
    A = G.T.copy(); A[-1, :] = 1.0
    b = np.zeros(n); b[-1] = 1.0
    return np.linalg.solve(A, b)

def bm_root(alpha, q):
    lo, hi = 1e-14, min(alpha, q)*(1-1e-12)
    def f(J):
        r = 1 - J/alpha
        return J/r + (J/q)**q - 1
    for _ in range(300):
        m = (lo+hi)/2
        if f(m) > 0:
            hi = m
        else:
            lo = m
    J = (lo+hi)/2
    return J, 1-J/alpha

def analyze(q, N, alpha, beta):
    G, lvl, S, start, children = build(q, N, alpha, beta)
    pi = stat(G)
    n = len(pi)
    rho = np.zeros(N)
    for st in range(n):
        p = pi[st]
        for s in range(S):
            if (st >> s) & 1:
                rho[int(lvl[s])] += p
    rho = rho/np.array([q**i for i in range(N)])
    J = alpha*(1-rho[0])
    # edge correlators: pick first site of level i-1 and its first child
    out = {}
    for i in [1, 2]:
        if i > N-1:
            continue
        p = start[i-1]
        c = children[p][0]
        e_occ_occ = sum(pi[st] for st in range(n) if ((st >> p) & 1) and ((st >> c) & 1))
        e_p_notc = sum(pi[st] for st in range(n) if ((st >> p) & 1) and not ((st >> c) & 1))
        out[i] = (e_occ_occ, e_p_notc)
    Jbm, rbm = bm_root(alpha, q)
    print(f"q={q} N={N} a={alpha} b={beta}")
    print(f"  rho={np.round(rho,6).tolist()} J={J:.6f} Jbm={Jbm:.6f} rbm={rbm:.6f} simpleMF={alpha/(1+alpha):.6f}")
    for i in [1, 2]:
        if i in out:
            co, pnc = out[i]
            print(f"  edge L{i-1}->L{i}: E[occ,occ]={co:.6f} E[p,(1-c)]={pnc:.6f} "
                  f"J/q^{i-1}={J/q**(i-1):.6f} gap rho_{i-1}-J/q^{i-1}={rho[i-1]-J/q**(i-1):.6f}")
    # conservation check
    print(f"  conserv: beta*q^(N-1)*rho_L={beta*q**(N-1)*rho[-1]:.6f} (should equal J)")
    # internal-consistency check of target: BM root vs alpha/(1+alpha)
    r_simple = alpha/(1+alpha)
    Js = alpha*(1-r_simple)
    lhs = (1-Js/r_simple)**(1/q) if Js < r_simple else 0.0
    print(f"  target-consistency: r_simple={r_simple:.6f}, LHS(BM eq at r_simple)={lhs:.6f}, RHS={Js/q:.6f} -> {'CONSISTENT' if abs(lhs-Js/q)<1e-9 else 'CONTRADICTION'}")

analyze(2, 2, 0.5, 1.0)
analyze(2, 3, 0.5, 1.0)
analyze(2, 3, 1.0, 2.0)
analyze(2, 2, 1.0, 1.0)
