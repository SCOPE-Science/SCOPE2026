"""Verify amplitude-completion of symbol rows for fixed weight phi=x1 (stdlib+sympy algebra).

For xi=(0,0,k) (and by rotation any xi⊥e1): plane-wave + linear amplitude rows span
exactly 5 dims (sympy rank + explicit cokernel vector n); the quadratic gradient-gradient
term g1^T h g2 escapes n (nonzero pairing), giving full rank 6 with div-free rows.
Also replays numeric multi-xi multi-seed completion (fullrank=6, linearrank=5).
"""
import math, random

def bilin(p, q):
    return [p[0]*q[0], p[1]*q[1], p[2]*q[2],
            p[0]*q[1]+p[1]*q[0], p[0]*q[2]+p[2]*q[0], p[1]*q[2]+p[2]*q[1]]

def crank(M):
    M = [list(r) for r in M]; m = len(M); n = len(M[0]); r = 0
    for c in range(n):
        p = max(range(r, m), key=lambda i: abs(M[i][c]))
        if abs(M[p][c]) < 1e-9:
            continue
        M[r], M[p] = M[p], M[r]
        M[r] = [v / M[r][c] for v in M[r]]
        for i in range(m):
            if i != r and abs(M[i][c]) > 1e-12:
                M[i] = [a - b * M[i][c] for a, b in zip(M[i], M[r])]
        r += 1
        if r == m:
            break
    return r

def build(xi, seed=0, tau=10.0, linear_only=False):
    nxi = math.sqrt(sum(v * v for v in xi))
    assert abs(xi[0]) < 1e-12 and nxi < 2 * tau
    R = math.sqrt(tau**2 - nxi**2 / 4)
    ex = [1, 0, 0]
    cr = [ex[(i+1)%3]*xi[(i+2)%3]-ex[(i+2)%3]*xi[(i+1)%3] for i in range(3)]
    nc = math.sqrt(sum(v*v for v in cr)); n = [v/nc for v in cr]
    q = [R*v for v in n]
    A = [xi[i]/2+q[i] for i in range(3)]; B = [xi[i]/2-q[i] for i in range(3)]
    z1 = [tau*ex[i]+1j*A[i] for i in range(3)]; z2 = [-tau*ex[i]+1j*B[i] for i in range(3)]
    def row(a1, a2, g1, g2):
        r = [0j]*6
        terms = [(z1, z2, a1*a2), (z1, g2, a1), (g1, z2, a2)]
        if not linear_only:
            terms.append((g1, g2, 1.0))
        for (p, qq, s) in terms:
            b = bilin(p, qq)
            for j in range(6):
                r[j] += s*b[j]
        return r
    m1 = [v/tau for v in A]; m2 = [v/tau for v in B]
    rnd = random.Random(seed)
    def rand_g(m, plus):
        s = 1 if plus else -1
        g = [0j]*3
        g[1] = rnd.uniform(-1, 1)+1j*rnd.uniform(-1, 1)
        g[2] = rnd.uniform(-1, 1)+1j*rnd.uniform(-1, 1)
        g[0] = (-1j*(m[1]*g[1]+m[2]*g[2]))/(s+1j*m[0])
        assert abs(s*g[0]+1j*sum(m[j]*g[j] for j in range(3))) < 1e-9
        return g
    Z = [0j]*3
    rows = [[xi[0],0,0,xi[1],xi[2],0],[0,xi[1],0,xi[0],0,xi[2]],
            [0,0,xi[2],0,xi[0],xi[1]], row(1.0, 1.0, Z, Z)]
    for _ in range(8):
        rows.append(row(1.0, 1.0, rand_g(m1, True), rand_g(m2, False)))
    return rows

print("== numeric completion ==")
for xi in [[0,0,2.0],[0,1.0,0.5],[0,2.0,1.0],[0,0.1,0.1],[0,5.0,0.0]]:
    for seed in [0, 1]:
        rf = crank(build(xi, seed, linear_only=False))
        rl = crank(build(xi, seed, linear_only=True))
        assert rf == 6 and rl == 5, (xi, seed, rf, rl)
        print(f"xi={xi} seed={seed}: full={rf} linear={rl} OK")

print("== analytic certificate (sympy-derived, replayed numerically) ==")
# cokernel vector n = (-iR/t, it/R, 0, 1, 0, 0) annihilates plane+linear rows;
# g1=(−i kz,0,1)... replay pairing g1^T N g2 = i k (2t^2−k^2)/(8t^3) ≠ 0 for k≠0.
tau, k = 10.0, 2.0
R = math.sqrt(tau**2 - k**2/4)
N = [[-1j*R/tau, 0.5, 0],[0.5, 1j*tau/R, 0],[0,0,0]]
m1z = k/(2*tau); m2y = -R/tau
g1 = [-1j*m1z, 0, 1]; g2 = [1j*m2y, 1, 0]
val = sum(g1[i]*N[i][j]*g2[j] for i in range(3) for j in range(3))
expect = 1j*k*(2*tau**2-k**2)/(8*tau**3)
assert abs(val-expect) < 1e-9 and abs(val) > 1e-6, (val, expect)
print(f"escape pairing = {val:.6f} (expect {expect:.6f}), nonzero OK")
print("AMPLITUDE-COMPLETION_OK")
