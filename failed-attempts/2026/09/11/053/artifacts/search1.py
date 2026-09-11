"""Heuristic search for 9 RS[48,12]/F97 codewords + size-2 lists with agreement>=32.
Also checks interpolation count feasibility. Stdlib only."""
import random, math

Q = 97
N = 48
K = 12
EVAL = list(range(48))
RHO = 0.33
AGREE_NEED = 32  # (1-rho)n = 32.16 -> need >=32 (use 32; also test 33)
L_PLUS1 = 9

def eval_poly(coeffs, x):
    r = 0
    for c in reversed(coeffs):
        r = (r * x + c) % Q
    return r

def codeword(coeffs):
    return [eval_poly(coeffs, x) for x in EVAL]

def top2_coverage(cws):
    """cws: list of n lists length N. Returns (min_agree, total, cover_lists)."""
    t = len(cws)
    min_ag = N + 1
    total = 0
    ag = []
    for c in cws:
        ag.append([0]*1)
    # per coordinate
    per = []
    for j in range(N):
        from collections import Counter
        vals = [c[j] for c in cws]
        cnt = Counter(vals)
        top = cnt.most_common(2)
        S = set(v for v, _ in top)
        per.append(S)
    ags = []
    for c in cws:
        a = sum(1 for j in range(N) if c[j] in per[j])
        ags.append(a)
    return min(ags), sum(ags), ags, per

def score_of_coeffs(coefflist):
    cws = [codeword(c) for c in coefflist]
    m, t, ags, per = top2_coverage(cws)
    return m, t, ags

def random_coeffs():
    return [[random.randrange(Q) for _ in range(K)] for _ in range(L_PLUS1)]

def shared_zero_family(nshare=11):
    """9 polys sharing nshare zeros: f = g0 + a*h, h vanishes at 0..nshare-1."""
    pts = list(range(nshare))
    # h(x) = prod (x-p)
    h = [1]
    for p in pts:
        nh = [0]*(len(h)+1)
        for i, c in enumerate(h):
            nh[i] = (nh[i] - p*c) % Q
            nh[i+1] = (nh[i+1] + c) % Q
        h = nh
    # h degree nshare <=11 ok
    g0 = [random.randrange(Q) for _ in range(K)]
    avals = random.sample(range(Q), L_PLUS1)
    out = []
    for a in avals:
        f = g0[:]
        for i, c in enumerate(h):
            if i < K:
                f[i] = (f[i] + a*c) % Q
        out.append(f)
    return out

def anneal(seed=0, iters=4000, init=None):
    random.seed(seed)
    cur = init if init is not None else random_coeffs()
    cm, ct, _ = score_of_coeffs(cur)
    best = (cm, ct, [r[:] for r in cur])
    curbest = (cm, ct)
    for it in range(iters):
        # mutate: pick random poly, random coeff, random step
        nxt = [r[:] for r in cur]
        p = random.randrange(L_PLUS1)
        k = random.randrange(K)
        step = random.choice([1, -1, 2, -2, 5, -5, 13, -13, random.randrange(Q)])
        nxt[p][k] = (nxt[p][k] + step) % Q
        # occasionally swap whole poly
        if random.random() < 0.05:
            nxt[p] = [random.randrange(Q) for _ in range(K)]
        m, t, _ = score_of_coeffs(nxt)
        if (m, t) >= curbest or random.random() < 0.03:
            cur = nxt
            curbest = (m, t)
            if (m, t) > (best[0], best[1]):
                best = (m, t, [r[:] for r in cur])
    return best

if __name__ == "__main__":
    print("Johnson recovery benchmark:", 1 - math.sqrt(2*0.25))
    print("need agree >=", AGREE_NEED)
    # baseline random
    for s in range(3):
        random.seed(s)
        m, t, ags = score_of_coeffs(random_coeffs())
        print(f"random init {s}: min={m} total={t} ags={ags}")
    # shared-zero family baseline
    for s in range(3):
        random.seed(100+s)
        m, t, ags = score_of_coeffs(shared_zero_family())
        print(f"sharedzero init {s}: min={m} total={t} ags={ags}")
    # anneal runs
    for s in range(6):
        random.seed(1000+s)
        init = shared_zero_family() if s % 2 == 0 else random_coeffs()
        m, t, cf = anneal(seed=2000+s, iters=2500, init=init)
        print(f"anneal {s}: min={m} total={t} (need min>=32 total>=288)", flush=True)
