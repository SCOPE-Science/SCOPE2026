"""Target-route §4: Dehn-twist homology search on closed S3.
Looks for words whose H1-action has a Perron root in (1, lambda_H),
the only window where a target witness (tau*, M*) could live.
Method: Humphries chain homology classes + LT Theorem 2.2 criteria.
Pure stdlib (no numpy/sympy) to avoid env issues.
"""
import itertools, math

# Basis order: a1,a2,a3,b1,b2,b3. J = [0 I; -I 0]; (x,y) = x^T J y.
# Twist matrix T_v = I - v (v^T J) acting on column vectors.
N = 6
def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(N)) for i in range(N)]

def ident():
    return [[1 if i == j else 0 for j in range(N)] for i in range(N)]

def twist_matrix(v):
    # w = v^T J  (row vector); T = I - v outer w
    # (Jx)_i = x_{i+3} for i<3, -x_{i-3} for i>=3.
    w = [0] * N
    for j in range(N):
        # w_j = sum_i v_i J_ij; J_ij nonzero: J[i][i+3]=1, J[i+3][i]=-1
        s = 0
        for i in range(3):
            if j == i + 3:
                s += v[i]
            if j == i:
                s -= v[i + 3]
        w[j] = s
    T = ident()
    for i in range(N):
        for j in range(N):
            T[i][j] -= v[i] * w[j]
    return T

# Humphries chain homology classes (signs fixed as derived in WORKLOG T4)
A1 = [1,0,0, 0,0,0]; B1 = [0,0,0, 1,0,0]
A2 = [0,1,0, 0,0,0]; B2 = [0,0,0, 0,1,0]
A3 = [0,0,1, 0,0,0]; B3 = [0,0,0, 0,0,1]
def vadd(u, v): return [a + b for a, b in zip(u, v)]
CHAIN = [A1, B1, vadd(A1,A2), B2, vadd(A2,A3), B3, A3]
NAMES = ["a1","b1","a1+a2","b2","a2+a3","b3","a3"]

def char_poly(M):
    # Faddeeva-LeVerrier, exact integers
    n = N
    I = ident()
    c = [1]  # c[0]=1; coeffs of x^n + c1 x^{n-1} + ... + cn
    B = [[0]*n for _ in range(n)]
    for k in range(1, n + 1):
        if k == 1:
            B = [row[:] for row in M]
        else:
            # B_new = M*(B_old + c_{k-1} I): shift FIRST, then multiply.
            S = [row[:] for row in B]
            for i in range(n):
                S[i][i] += c[k-1]
            B = mat_mul(M, S)
        ck = -sum(B[i][i] for i in range(n)) // k
        c.append(ck)
    return c  # length 7: x^6 + c1 x^5 + ... + c6

defeval = None
def poly_val(c, x):
    # c: [1, c1, ..., c6]; evaluate monic poly at float x
    r = 0.0
    for a in c:
        r = r * x + a
    return r

def perron_bisect(c):
    # largest real root > 1 if sign change on (1, R]; coarse scan then bisect
    f = lambda x: poly_val(c, x)
    R = 1.0
    # grow R until f(R) > 0 (leading coeff positive so eventually positive)
    while f(R) <= 0 and R < 1e6:
        R *= 2
    if f(R) <= 0:
        return None
    # scan for sign changes above 1 to find the LARGEST root: bisect from top
    lo, hi = 1.0, R
    # First check any root > 1 exists: f(1) < 0 suffices given f(R) > 0? Only if
    # no even number of crossings; we want largest root: standard bisect on
    # truncated interval after coarse scan for the topmost sign change.
    xs = [1.0 + i * 0.01 for i in range(int((R - 1.0) / 0.01) + 1)]
    top = None
    for i in range(len(xs) - 1, 0, -1):
        a, b = xs[i-1], xs[i]
        fa, fb = f(a), f(b)
        if fa == 0:
            top = (a, a)
            break
        if fa * fb < 0:
            top = (a, b)
            break
    if top is None:
        return None
    a, b = top
    if a == b:
        return a
    for _ in range(60):
        m = 0.5 * (a + b)
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)

def main():
    LAM_H = 1.40127  # upper edge of target window (certified bracket 1.40126-1.40127)
    Tw = [twist_matrix(v) for v in CHAIN]
    Twi = []  # inverses via transpose wrt J? T_v^{-1} = T_{-v} = I + v w
    for v in CHAIN:
        w = [0]*N
        for j in range(N):
            s = 0
            for i in range(3):
                if j == i+3: s += v[i]
                if j == i: s -= v[i+3]
            w[j] = s
        Ti = ident()
        for i in range(N):
            for j in range(N):
                Ti[i][j] += v[i]*w[j]
        Twi.append(Ti)
    gens = []
    for i, Tm in enumerate(Tw):
        gens.append((NAMES[i], Tm))
    for i, Tm in enumerate(Twi):
        gens.append((NAMES[i]+"^-1", Tm))
    print(f"generators: {len(gens)}; scanning words up to length 5 (14^5 = 537824 homological actions)")
    hits = []
    total = 0
    # iterative deepening BFS over matrix products
    cur = {"": ident()}
    seen_polys = {}
    for length in range(1, 6):
        nxt = {}
        for w, M in cur.items():
            for name, G in gens:
                w2 = (w + "*" + name) if w else name
                M2 = mat_mul(G, M)
                total += 1
                c = tuple(char_poly(M2))
                if c in seen_polys:
                    continue
                seen_polys[c] = w2
                r = perron_bisect(list(c))
                if r is not None and 1.0 < r < LAM_H - 1e-9:
                    hits.append((r, w2, c))
        cur = {}
        # keep only a sample to bound growth? No — dedupe by matrix? matrices
        # explode; dedupe by char poly is too coarse for extension. Instead cap:
        # retain all (length<=5 is only 537k products; each product 6x6 mult ~ cheap).
        # Rebuild cur as all words of this length is too many; do DFS below instead.
        break
    # Full DFS with dedupe by matrix entries (exact), capped
    best = []
    stack = [(ident(), "")]
    count = [0]
    while stack:
        M, w = stack.pop()
        L = 0 if not w else w.count("*") + 1
        if L >= 5:
            continue
        for name, G in gens:
            M2 = mat_mul(G, M)
            w2 = (w + "*" + name) if w else name
            count[0] += 1
            c = tuple(char_poly(M2))
            r = perron_bisect(list(c))
            if r is not None and 1.0 < r < LAM_H - 1e-9:
                key = (round(r, 6), c)
                best.append((r, w2, c))
            stack.append((M2, w2))
    print(f"products evaluated: {count[0]}")
    # dedupe hits by rounded root + poly
    uniq = {}
    for r, w, c in best:
        uniq.setdefault((round(r, 6), c), w)
    print(f"words with homological Perron root in (1, {LAM_H}): {len(uniq)} (unique root+poly classes)")
    for (rr, c), w in sorted(uniq.items())[:30]:
        print(f"  root~{rr} word={w} char={list(c)}")

if __name__ == "__main__":
    main()
