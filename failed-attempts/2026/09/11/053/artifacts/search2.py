"""Fast SA search for 9 RS[48,12]/F97 codewords with min top-2 agreement >= 32.
Moves: single-coeff delta updates (incremental eval) + interpolation jumps
(worst poly re-interpolated through 12 chosen list values). Stdlib only."""
import random, math, time, sys

Q = 97; N = 48; K = 12; T = 9; NEED = 32
EVAL = list(range(N))
# powers table: POW[x][j] = x^j
POW = [[1]*K for _ in range(N)]
for x in range(N):
    for j in range(1, K):
        POW[x][j] = (POW[x][j-1]*x) % Q

def eval_row(coeffs):
    return [sum(coeffs[j]*POW[x][j] for j in range(K)) % Q for x in EVAL]

def top2_stats(mat, distinct_penalty=True):
    """mat: T x N. returns (mincov, total, per_row_cov)."""
    rowcov = [0]*T
    for j in range(N):
        cnt = {}
        for i in range(T):
            v = mat[i][j]; cnt[v] = cnt.get(v, 0)+1
        s = sorted(cnt.items(), key=lambda kv: -kv[1])
        S = set([s[0][0]]) if len(s) == 1 else set([s[0][0], s[1][0]])
        for i in range(T):
            if mat[i][j] in S: rowcov[i] += 1
    return min(rowcov), sum(rowcov), rowcov

def gauss_solve(A, b, q=97):
    n = len(A); M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        piv = None
        for r in range(c, n):
            if M[r][c] % q != 0: piv = r; break
        if piv is None: return None
        M[c], M[piv] = M[piv], M[c]
        inv = pow(M[c][c], -1, q)
        M[c] = [(v*inv) % q for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [(M[r][k]-f*M[c][k]) % q for k in range(n+1)]
    return [M[i][n] % q for i in range(n)]

def interp_jump(mat, coeffs, i, rng):
    """Re-interpolate poly i through 12 coords' list-preferred values."""
    # current top-2 lists
    cols = []
    for j in range(N):
        cnt = {}
        for a in range(T):
            v = mat[a][j]; cnt[v] = cnt.get(v, 0)+1
        s = sorted(cnt.items(), key=lambda kv: -kv[1])
        top = [s[0][0]] if len(s) == 1 else [s[0][0], s[1][0]]
        cols.append(top)
    # pick 12 coords: bias to ones where poly i uncovered
    uncovered = [j for j in range(N) if mat[i][j] not in cols[j]]
    cover = [j for j in range(N) if mat[i][j] in cols[j]]
    rng.shuffle(uncovered); rng.shuffle(cover)
    # take mostly uncovered (up to 12), fill with covered; values: preferred list val
    # for uncovered pick the top-1 value; for covered keep own value
    pick = uncovered[:10] + cover[:max(0, 12-len(uncovered[:10]))]
    if len(pick) < 12:
        rest = [j for j in range(N) if j not in pick]; rng.shuffle(rest)
        pick += rest[:12-len(pick)]
    xs = pick[:12]
    ys = []
    for j in xs:
        if mat[i][j] in cols[j]: ys.append(mat[i][j])
        else: ys.append(cols[j][0])
    A = [[POW[x][j] for j in range(K)] for x in xs]
    sol = gauss_solve(A, ys)
    return sol

def anneal(seed, iters, jump_frac=0.25, init=None, log=False):
    rng = random.Random(seed)
    if init is None:
        seen=set(); coeffs=[]
        while len(coeffs)<T:
            c=tuple(rng.randrange(Q) for _ in range(K))
            if c not in seen: seen.add(c); coeffs.append(list(c))
    else:
        coeffs = [r[:] for r in init]
    mat = [eval_row(c) for c in coeffs]
    m, t, rc = top2_stats(mat)
    best = (m, t); bestc = [r[:] for r in coeffs]
    cur = (m, t)
    for it in range(iters):
        Temp = max(0.3, 3.0*(1.0 - it/iters))
        if rng.random() < jump_frac:
            i = min(range(T), key=lambda a: rc[a])
            if rng.random() < 0.3: i = rng.randrange(T)
            sol = interp_jump(mat, coeffs, i, rng)
            if sol is None: continue
            old = coeffs[i][:]; oldrow = mat[i][:]
            newrow = eval_row(sol)
            if any(newrow==mat[a] for a in range(T) if a!=i):
                continue
            coeffs[i] = sol; mat[i] = newrow
            m2, t2, rc2 = top2_stats(mat)
            if (m2, t2) >= cur or rng.random() < math.exp(((m2-cur[0])*8 + (t2-cur[1])*0.05)/Temp):
                cur = (m2, t2); rc = rc2
                if (m2, t2) > best: best = (m2, t2); bestc = [r[:] for r in coeffs]
            else:
                coeffs[i] = old; mat[i] = oldrow
        else:
            i = rng.randrange(T); k = rng.randrange(K)
            delta = rng.choice([1, Q-1, 2, Q-2, 5, Q-5, 13, Q-13])
            old = coeffs[i][k]
            coeffs[i][k] = (old+delta) % Q
            # incremental row update
            mat[i] = [(mat[i][x]+delta*POW[x][k]) % Q for x in EVAL]
            # reject duplicate codewords (list-recovery needs distinct codewords)
            if any(mat[i]==mat[a] for a in range(T) if a!=i):
                coeffs[i][k] = old
                mat[i] = [(mat[i][x]-delta*POW[x][k]) % Q for x in EVAL]
                continue
            m2, t2, rc2 = top2_stats(mat)
            if (m2, t2) >= cur or rng.random() < math.exp(((m2-cur[0])*8 + (t2-cur[1])*0.05)/Temp):
                cur = (m2, t2); rc = rc2
                if (m2, t2) > best: best = (m2, t2); bestc = [r[:] for r in coeffs]
            else:
                coeffs[i][k] = old
                mat[i] = [(mat[i][x]-delta*POW[x][k]) % Q for x in EVAL]
        if best[0] >= NEED:
            break
    return best, bestc

def shared_h_seed(rng, nz=11):
    pts = rng.sample(range(N), nz)
    h = [1]
    for p in pts:
        nh = [0]*(len(h)+1)
        for i, c in enumerate(h):
            nh[i] = (nh[i]-p*c) % Q; nh[i+1] = (nh[i+1]+c) % Q
        h = nh
    while len(h) < K: h.append(0)
    h = h[:K]
    g0 = [rng.randrange(Q) for _ in range(K)]
    avals = rng.sample(range(1,Q), T)
    out = []
    for a in avals:
        out.append([(g0[i]+a*h[i]) % Q for i in range(K)])
    return out

def const_seed(rng):
    out = [[0]*K, [1]+[0]*(K-1)]
    # two constants 0 and 1
    h = None
    pts = rng.sample(range(N), 11)
    h = [1]
    for p in pts:
        nh = [0]*(len(h)+1)
        for i, c in enumerate(h):
            nh[i] = (nh[i]-p*c) % Q; nh[i+1] = (nh[i+1]+c) % Q
        h = nh
    while len(h) < K: h.append(0)
    h = h[:K]
    shifts = rng.sample(range(Q), T-2)
    for d in shifts:
        # g = h + d (as polys: h[0]+d)
        g = h[:]; g[0] = (g[0]+d) % Q
        out.append(g)
    return out

if __name__ == "__main__":
    t0 = time.time()
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 600.0
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
    seed0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nrun = 0
    global_best = (0, 0); gb_seed = None; gb_coeffs = None
    s = seed0
    while time.time()-t0 < budget:
        rng = random.Random(s)
        kind = s % 3
        init = None
        if kind == 1: init = shared_h_seed(rng)
        elif kind == 2: init = const_seed(rng)
        b, c = anneal(s, iters, init=init)
        nrun += 1
        if b > global_best:
            global_best = b; gb_seed = s; gb_coeffs = c
            print(f"[{time.time()-t0:.0f}s] run {nrun} seed {s}: NEW BEST min={b[0]} total={b[1]}", flush=True)
        if global_best[0] >= NEED:
            print("COUNTEREXAMPLE FOUND", flush=True)
            import json
            json.dump({"coeffs": gb_coeffs}, open("output/artifacts/counterexample.json", "w"))
            break
        s += 1
    print(f"done: {nrun} runs, best min={global_best[0]} total={global_best[1]} seed={gb_seed}", flush=True)
