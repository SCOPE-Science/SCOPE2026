"""Gillespie simulation of outward ASEP on rooted q-ary tree (q=2).
Estimates stationary J and per-level densities for larger N.
"""
import numpy as np, time, sys

def simulate(q, N, alpha, beta, T_burn, T_run, seed):
    rng = np.random.default_rng(seed)
    S = (q**N - 1)//(q-1)
    # level of each site; children
    lvl = np.zeros(S, dtype=int)
    start = [0]*N
    acc = 0
    for i in range(N):
        start[i] = acc; acc += q**i
    for s in range(S):
        # find level via start
        for i in range(N):
            if s < start[i] + q**i:
                lvl[s] = i; break
    children = {}
    for s in range(S):
        i = lvl[s]
        if i < N-1:
            pos = s - start[i]
            c0 = start[i+1] + pos*q
            children[s] = [c0+k for k in range(q)]
    occ = np.zeros(S, dtype=bool)
    occ_bulk_list = []  # not needed; compute rates directly
    t = 0.0
    # burn-in
    def step():
        nonlocal t
        # rates
        r_entry = alpha if not occ[0] else 0.0
        bulk = np.where(occ & (lvl < N-1))[0]
        leaves = np.where(occ & (lvl == N-1))[0]
        R = r_entry + len(bulk) + beta*len(leaves)
        dt = rng.exponential(1.0/R)
        t += dt
        u = rng.random()*R
        if u < r_entry:
            occ[0] = True
            return ('entry',)
        u -= r_entry
        if u < len(bulk):
            s = bulk[int(u)]
            ch = children[s][rng.integers(q)]
            if not occ[ch]:
                occ[s] = False; occ[ch] = True
            return ()
        else:
            k = int((u - len(bulk))/beta)
            s = leaves[k]
            occ[s] = False
            return ()
    while t < T_burn:
        step()
    # measurement
    integ = np.zeros(N)
    entries = 0
    t0 = t
    while t < T_burn + T_run:
        # rates
        r_entry = alpha if not occ[0] else 0.0
        bulk = np.where(occ & (lvl < N-1))[0]
        leaves = np.where(occ & (lvl == N-1))[0]
        R = r_entry + len(bulk) + beta*len(leaves)
        dt = rng.exponential(1.0/R)
        # accumulate
        for i in range(N):
            integ[i] += occ[start[i]:start[i]+q**i].sum()*dt
        t += dt
        u = rng.random()*R
        if u < r_entry:
            occ[0] = True; entries += 1
        else:
            u -= r_entry
            if u < len(bulk):
                s = bulk[int(u)]
                ch = children[s][rng.integers(q)]
                if not occ[ch]:
                    occ[s] = False; occ[ch] = True
            else:
                k = int((u - len(bulk))/beta)
                occ[leaves[k]] = False
    T = t - t0
    rho = integ/T/np.array([q**i for i in range(N)])
    J = entries/T
    return J, rho

if __name__ == '__main__':
    q = 2
    alpha, beta = float(sys.argv[1]), float(sys.argv[2])
    Ns = [int(x) for x in sys.argv[3].split(',')]
    for N in Ns:
        J, rho = simulate(q, N, alpha, beta, T_burn=2000, T_run=20000, seed=12345+N)
        print(f"N={N} a={alpha} b={beta} J={J:.5f} rho0={rho[0]:.5f} rho1={rho[1]:.5f} "
              + (f"rho2={rho[2]:.5f} " if N>3 else "") + (f"rhoL={rho[-1]:.6f} qL*rhoL={q**(N-1)*rho[-1]:.4f}" if True else ""), flush=True)
