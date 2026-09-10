"""Verify same-sign (Laplace) CGO amplitude rows attain full rank 6 at LINEAR order (stdlib only).

zeta1 = tau e1 + iA, zeta2 = tau e1 + iB', A+B' = eta (transverse), |A|=|B'|=tau.
Transport: (e1+i m1).g1 = 0, (e1+i m2).g2 = 0 with m1=A/tau, m2=B'/tau.
Rows: 3 div-free + plane-wave + 8 amplitude rows; linear-only drops g1-g2 term.
Pass: full == 6 and linear == 6 for all eta/seeds.
"""
import math
import random


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


def build_same(eta, seed=0, tau=10.0, linear_only=False):
    n = math.sqrt(sum(v*v for v in eta))
    assert abs(eta[0]) < 1e-12 and n < 2 * tau
    R = math.sqrt(tau**2 - n**2 / 4)
    ex = [1, 0, 0]
    cr = [ex[(i+1)%3]*eta[(i+2)%3]-ex[(i+2)%3]*eta[(i+1)%3] for i in range(3)]
    nc = math.sqrt(sum(v*v for v in cr)); nn = [v/nc for v in cr]
    q = [R*v for v in nn]
    A = [eta[i]/2+q[i] for i in range(3)]; Bp = [eta[i]/2-q[i] for i in range(3)]
    z1 = [tau*ex[i]+1j*A[i] for i in range(3)]
    z2 = [tau*ex[i]+1j*Bp[i] for i in range(3)]
    assert abs(sum(v*v for v in z1)) < 1e-6 and abs(sum(v*v for v in z2)) < 1e-6

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

    m1 = [v/tau for v in A]; m2 = [v/tau for v in Bp]
    rnd = random.Random(seed)

    def rand_g(m):
        g = [0j]*3
        g[1] = rnd.uniform(-1, 1)+1j*rnd.uniform(-1, 1)
        g[2] = rnd.uniform(-1, 1)+1j*rnd.uniform(-1, 1)
        g[0] = (-1j*(m[1]*g[1]+m[2]*g[2]))/(1+1j*m[0])
        assert abs(g[0]+1j*sum(m[j]*g[j] for j in range(3))) < 1e-9
        return g

    Z = [0j]*3
    rows = [[eta[0],0,0,eta[1],eta[2],0],[0,eta[1],0,eta[0],0,eta[2]],
            [0,0,eta[2],0,eta[0],eta[1]], row(1.0, 1.0, Z, Z)]
    for _ in range(8):
        rows.append(row(1.0, 1.0, rand_g(m1), rand_g(m2)))
    return rows


if __name__ == "__main__":
    for eta in [[0, 3.0, 1.0], [0, 0, 2.0], [0, 1.0, 0.5], [0, 5.0, 0.0]]:
        for seed in [0, 1, 2]:
            rf = crank(build_same(eta, seed, linear_only=False))
            rl = crank(build_same(eta, seed, linear_only=True))
            assert rf == 6 and rl == 6, (eta, seed, rf, rl)
            print(f"eta={eta} seed={seed}: full={rf} linear={rl} OK")
    print("SAMESIGN-LINEAR-6_OK")
