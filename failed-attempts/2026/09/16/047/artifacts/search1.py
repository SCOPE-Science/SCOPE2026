import itertools

def dbottleneck(D):
    r = len(D)
    vals = sorted({v for row in D for v in row})
    def has_perf(th):
        adj = [[j for j in range(r) if D[i][j] <= th] for i in range(r)]
        mt = [-1]*r
        def dfs(u, seen):
            for v in adj[u]:
                if seen[v]:
                    continue
                seen[v] = True
                if mt[v] == -1 or dfs(mt[v], seen):
                    mt[v] = u
                    return True
            return False
        m = 0
        for u in range(r):
            if dfs(u, [False]*r):
                m += 1
            else:
                break
        return m == r
    for v in vals:
        if has_perf(v):
            return v
    return vals[-1]

def supports(A, C, delta=1):
    r = len(A)
    n = len(A[0])
    SF = [[True]*r for _ in range(r)]
    SG = [[True]*r for _ in range(r)]
    for i, a in enumerate(A):
        for j, c in enumerate(C):
            s = [c[k]-a[k] for k in range(n)]
            SF[i][j] = all(x <= delta + 1e-9 for x in s)
            SG[j][i] = all(x >= -delta - 1e-9 for x in s)
    return SF, SG

def dmat(A, C, Csize=100):
    r = len(A)
    n = len(A[0])
    D = [[0]*r for _ in range(r)]
    for i, a in enumerate(A):
        for j, c in enumerate(C):
            D[i][j] = min(Csize/2, max(abs(c[k]-a[k]) for k in range(n)))
    return D

def matmul(X, Y):
    n = len(X); m = len(Y[0]); k = len(Y)
    return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]

def mattrans(X):
    return [list(r) for r in zip(*X)]

def frob(X):
    return sum(v*v for row in X for v in row) ** 0.5

def matsub(X, Y):
    return [[X[i][j]-Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def eye(r):
    return [[1.0 if i == j else 0.0 for j in range(r)] for i in range(r)]

def try_interleave(SF, SG, restarts=60, it=120, seed=0):
    import random
    r = len(SF)
    I = eye(r)
    best = (1e18, None, None)
    rnd = random.Random(seed)
    for _ in range(restarts):
        f = [[rnd.gauss(0, 1) if SF[i][j] else 0.0 for j in range(r)] for i in range(r)]
        g = [[rnd.gauss(0, 1) if SG[j][i] else 0.0 for i in range(r)] for j in range(r)]
        lr = 0.05
        for t in range(it):
            R1 = matsub(matmul(f, g), I)
            R2 = matsub(matmul(g, f), I)
            gT = mattrans(g); fT = mattrans(f)
            gf = matmul(R1, gT)
            tmp = matmul(gT, R2)
            gf = [[gf[i][j]+tmp[i][j] for j in range(r)] for i in range(r)]
            gg = matmul(fT, R1)
            tmp2 = matmul(R2, fT)
            gg = [[gg[i][j]+tmp2[i][j] for j in range(r)] for i in range(r)]
            for i in range(r):
                for j in range(r):
                    if SF[i][j]:
                        f[i][j] -= lr*gf[i][j]
                    if SG[j][i]:
                        g[j][i] -= lr*gg[j][i]
            lr *= 0.999
        res = frob(matsub(matmul(f, g), I)) + frob(matsub(matmul(g, f), I))
        if res < best[0]:
            best = (res, [row[:] for row in f], [row[:] for row in g])
        if best[0] < 1e-6:
            break
    return best

if __name__ == "__main__":
    import random
    Csize = 100; delta = 1; n = 3; r = 3
    rnd = random.Random(0)
    hits = 0
    for trial in range(300):
        A = [[float(rnd.randint(0, 4)) for _ in range(n)] for _ in range(r)]
        C = [[float(rnd.randint(0, 4)) for _ in range(n)] for _ in range(r)]
        D = dmat(A, C)
        db = dbottleneck(D)
        if db >= 4:
            SF, SG = supports(A, C)
            res, f, g = try_interleave(SF, SG, restarts=25, it=60, seed=trial)
            print("trial %d db=%s res=%.3f" % (trial, db, res))
            print("  A=%s C=%s" % (A, C))
            print("  SF=%s SG=%s" % (SF, SG))
            hits += 1
            if hits >= 15:
                break
    print("done hits=%d" % hits)
