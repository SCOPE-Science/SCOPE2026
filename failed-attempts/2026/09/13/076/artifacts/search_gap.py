#!/usr/bin/env python3
"""Search for two-valued restricted-assignment config-LP gap counterexample > 8/5.
Pure Python: hand-rolled two-phase simplex + exhaustive OPT (DFS branch&bound).
"""
import itertools, random, sys, json, math, time

def simplex_max(c, A, b, itlim=500000):
    """max c^Tx s.t. Ax<=b, x>=0. Tableau with objective row 0:
    row0: z + sum T0[j] x_j = T0[N]; entering col has T0[j]<0."""
    m = len(A); n = len(c)
    N = n + 2 * m
    T = [[0.0] * (N + 1) for _ in range(m + 1)]
    basis = [0] * (m + 1)  # basis[i] for rows 1..m
    artcols = set()
    for i in range(1, m + 1):
        bi = float(b[i - 1]); sgn = 1.0 if bi >= 0 else -1.0
        Ai = A[i - 1]
        for j in range(n):
            T[i][j] = sgn * float(Ai[j])
        T[i][n + (i - 1)] = sgn
        if sgn < 0:
            T[i][n + m + (i - 1)] = 1.0
            basis[i] = n + m + (i - 1)
            artcols.add(n + m + (i - 1))
        else:
            basis[i] = n + (i - 1)
        T[i][N] = abs(bi)

    def run(phase):
        it = 0
        while True:
            e = -1; best = 0.0
            for j in range(N):
                if T[0][j] < best - 1e-9:
                    best = T[0][j]; e = j
            if e < 0:
                return True
            l = -1; brat = None
            for i in range(1, m + 1):
                if T[i][e] > 1e-9:
                    r = T[i][N] / T[i][e]
                    if brat is None or r < brat - 1e-12 or \
                       (abs(r - brat) <= 1e-12 and basis[i] < basis[l]):
                        brat = r; l = i
            if l < 0:
                return False
            piv = T[l][e]
            Tl = T[l]
            for j in range(N + 1):
                Tl[j] /= piv
            for i in range(m + 1):
                if i != l and abs(T[i][e]) > 1e-14:
                    f = T[i][e]; Ti = T[i]
                    for j in range(N + 1):
                        Ti[j] -= f * Tl[j]
            basis[l] = e
            it += 1
            if it > itlim:
                raise RuntimeError("simplex iter limit phase %s" % phase)

    # Phase 1: maximize -sum(artificials); row0: z + sum a = 0, eliminate basic arts
    for a_ in artcols:
        T[0][a_] = 1.0
    for i in range(1, m + 1):
        if basis[i] in artcols:
            f = 1.0; Ti = T[i]
            for j in range(N + 1):
                T[0][j] -= f * Ti[j]
    run(1)
    if T[0][N] < -1e-7:
        return {'status': 'infeasible', 'value': None, 'x': None}
    # Phase 2: row0: z - c^Tx = 0, eliminate basic x cols
    for j in range(N + 1):
        T[0][j] = 0.0
    for j in range(n):
        T[0][j] = -float(c[j])
    for i in range(1, m + 1):
        bb = basis[i]
        if bb < n and abs(T[0][bb]) > 1e-14:
            f = T[0][bb]; Ti = T[i]
            for j in range(N + 1):
                T[0][j] -= f * Ti[j]
    feas = run(2)
    if not feas:
        return {'status': 'unbounded', 'value': None, 'x': None}
    x = [0.0] * n
    for i in range(1, m + 1):
        if basis[i] < n:
            x[basis[i]] = max(0.0, T[i][N])
    return {'status': 'optimal', 'value': T[0][N], 'x': x}

def selftest_simplex():
    r = simplex_max([1, 1], [[1, 2], [4, 2]], [4, 12])
    assert r['status'] == 'optimal' and abs(r['value'] - 10.0/3) < 1e-6, r
    r = simplex_max([1], [[1], [-1]], [1, -2])
    assert r['status'] == 'infeasible', r
    r = simplex_max([1], [[-1]], [0])
    assert r['status'] == 'unbounded', r
    r = simplex_max([1, 2], [[1, 1], [-1, -1]], [1, -1])
    assert r['status'] == 'optimal' and abs(r['value'] - 2) < 1e-6, r
    r = simplex_max([3, 2], [[1, 1], [2, 1], [1, 0]], [4, 5, 2])
    assert r['status'] == 'optimal' and abs(r['value'] - 9) < 1e-6, r
    print("simplex self-tests passed", flush=True)

def all_configs(elig_sizes, cap=1.0):
    jobs = [j for j, _ in elig_sizes]
    sz = dict(elig_sizes)
    out = []
    for r in range(len(jobs) + 1):
        for combo in itertools.combinations(jobs, r):
            if sum(sz[j] for j in combo) <= cap + 1e-9:
                out.append(frozenset(combo))
    return out

def config_lp_feasible(cfgs_per_machine, njobs):
    """Decide config-LP feasibility at T=1 via max-slack LP.
    Vars x[i][C]>=0; s.t. sum_C x = 1 per machine i (2 ineq each);
    sum_{i,C ni j} x >= 1 per job j. Feasible iff max 0-s... use Phase-I style:
    add per-job slack? Simplest: maximize sum_j cov_j capped... Standard trick:
    maximize t s.t. cov_j >= t, dist_i == 1. We do LP: vars x + t; constraints
    dist<=1, dist>=1, cov - t >= 0, t free. Handle t free as t+ - t-.
    Return (feasible_bool, max_t)."""
    m = len(cfgs_per_machine)
    xs = []  # (i, C)
    for i, cl in enumerate(cfgs_per_machine):
        for C in cl:
            xs.append((i, C))
    nx = len(xs)
    # vars: x_0..x_{nx-1}, tp, tm. maximize tp - tm  <=> c
    n = nx + 2
    c = [0.0]*nx + [1.0, -1.0]
    A = []; b = []
    # dist_i <= 1
    for i in range(m):
        row = [0.0]*n
        for k,(ii,C) in enumerate(xs):
            if ii==i: row[k]=1.0
        A.append(row); b.append(1.0)
    # -dist_i <= -1
    for i in range(m):
        row=[0.0]*n
        for k,(ii,C) in enumerate(xs):
            if ii==i: row[k]=-1.0
        A.append(row); b.append(-1.0)
    # -(cov_j - tp + tm) <= 0  i.e. -cov + tp - tm <= 0 ; cov>=t needed only
    # relative to candidate; feasibility of t>=1 <=> max t >= 1.
    for j in range(njobs):
        row=[0.0]*n
        for k,(ii,C) in enumerate(xs):
            if j in C: row[k]=-1.0
        row[nx]=1.0; row[nx+1]=-1.0
        A.append(row); b.append(0.0)
    r = simplex_max(c, A, b)
    if r['status']!='optimal':
        return (False, None, None)
    t = r['x'][nx]-r['x'][nx+1]
    return (t>=1.0-1e-7, t, r['x'][:nx])

def min_makespan(p, elig, timeout_ok=True):
    """Exhaustive DFS branch & bound. p[i][j]=size or None. Returns OPT."""
    m=len(p); n=len(p[0])
    order=sorted(range(n), key=lambda j: (sum(1 for i in range(m) if p[i][j] is not None), -max([p[i][j] for i in range(m) if p[i][j] is not None] or [0])))
    best=[float('inf')]
    loads=[0.0]*m
    # order machines per job by size
    cand=[[i for i in range(m) if p[i][j] is not None] for j in range(n)]
    for j in range(n):
        cand[j].sort(key=lambda i: p[i][j])
    # lower bound: max current maxload, max remaining single min
    minneed=[min([p[i][j] for i in cand[j]]) if cand[j] else float('inf') for j in range(n)]
    def dfs(k, cur):
        if cur>=best[0]: return
        if k==n:
            best[0]=cur; return
        j=order[k]
        if not cand[j]: return
        # try machines sorted by resulting load
        opts=sorted(cand[j], key=lambda i: loads[i]+p[i][j])
        for i in opts:
            nl=loads[i]+p[i][j]
            if nl>=best[0]: continue
            loads[i]=nl
            dfs(k+1, max(cur,nl))
            loads[i]=nl-p[i][j]
            if best[0]<=max(cur,minneed[j]):
                pass
        # lb prune with remaining min needs on empty machines is weak; skip
    dfs(0,0.0)
    return best[0]

def check_instance(p, elig_sizes_per_machine, label=""):
    nj=len(p[0]); m=len(p)
    cfgs=[all_configs(es) for es in elig_sizes_per_machine]
    feas,t,_=config_lp_feasible(cfgs,nj)
    if not feas:
        return None
    opt=min_makespan(p,None)
    return (t,opt)

def rand_instance(m,n,alpha,beta,rng,dens=0.6):
    p=[[None]*n for _ in range(m)]
    for j in range(n):
        Ej=rng.sample(range(m),k=max(1,int(round(dens*m))))
        for i in Ej:
            p[i][j]=alpha if rng.random()<0.5 else beta
    return p

def main():
    selftest_simplex()
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
    ntrials=int(sys.argv[2]) if len(sys.argv)>2 else 2000
    rng=random.Random(seed)
    best={'gap':0,'info':None}
    checked=0; feasct=0
    t0=time.time()
    pairs=[(0.2,0.8),(0.3,0.7),(0.25,0.75),(0.4,0.9),(0.1,0.7),(0.5,1.0),(0.33,0.66),(0.2,0.6),(0.3,0.8),(0.45,0.8),(0.15,0.55),(0.35,0.7)]
    cfgsizes=[(3,5),(3,6),(4,6),(4,7),(4,8),(5,8),(2,4)]
    for t in range(ntrials):
        a,b=rng.choice(pairs)
        m,n=rng.choice(cfgsizes)
        dens=rng.choice([0.4,0.5,0.6,0.7])
        p=rand_instance(m,n,a,b,rng,dens)
        elig=[[ (j,p[i][j]) for j in range(n) if p[i][j] is not None] for i in range(m)]
        cfgs=[all_configs(es) for es in elig]
        feas,tv,_=config_lp_feasible(cfgs,n)
        checked+=1
        if not feas: continue
        feasct+=1
        opt=min_makespan(p,None)
        gap=opt  # T=1
        if gap>best['gap']+1e-9:
            best={'gap':gap,'info':(a,b,m,n,[sorted([i for i in range(m) if p[i][j] is not None]) for j in range(n)], [[p[i][j] for j in range(n)] for i in range(m)])}
            print(f"[{t}] NEW BEST gap={gap:.4f} sizes=({a},{b}) m={m} n={n} t={tv:.4f}",flush=True)
            if gap>1.6+1e-9:
                print("COUNTEREXAMPLE FOUND",flush=True)
                with open("output/artifacts/counterexample.json","w") as f:
                    json.dump(best,f,indent=1,default=str)
                return
    print(f"done checked={checked} feas={feasct} best_gap={best['gap']:.4f} time={time.time()-t0:.1f}s best={json.dumps(best['info'])[:800]}",flush=True)

if __name__=="__main__":
    main()
