"""Independent verifier for lane-897 target falsification (stdlib only).

Checks:
  V1: G(n) by brute-force partition enumeration agrees with memoized DP to n<=13.
  V2: Product P(q)=(q^8;q^8)/((q^2;q^8)(q^3;q^8)(q^6;q^8)) series to N; [q^2]P=1 vs G(2)=0.
  V3: Claimed family g(11n+6)=0 mod 11 fails at first index: G(6)=1.
  V4: Full 11-residue first-nonzero-witness log for G to N (all residues obstructed).
Replay: python3 output/artifacts/verify_target.py  -> VERIFY_OK
"""
from functools import lru_cache
import sys

N = 200
sys.setrecursionlimit(100000)

# ---- G via memoized DP (first-part decomposition) ----
@lru_cache(maxsize=None)
def F(rem, prev):
    if rem == 0:
        return 1
    tot = 0
    up = rem if rem < prev - 1 else prev - 2
    pe = (prev % 2 == 0)
    for v in range(3, up + 1):
        if pe and (v % 2 == 0) and (prev - v < 4):
            continue
        tot += F(rem - v, v)
    return tot

def G_dp(N):
    G = [0] * (N + 1)
    G[0] = 1
    for n in range(1, N + 1):
        t = 0
        for v in range(3, n + 1):
            t += F(n - v, v)
        G[n] = t
    return G

# ---- G via brute-force enumeration (independent) ----
def all_partitions(n, maxv=None):
    if n == 0:
        yield []
        return
    if maxv is None:
        maxv = n
    for v in range(min(maxv, n), 0, -1):
        for tail in all_partitions(n - v, v):
            yield [v] + tail

def satisfies(p):
    if len(p) == 0:
        return True
    if p[-1] < 2:
        return False
    if 2 in p:
        return False
    for i in range(len(p) - 1):
        d = p[i] - p[i + 1]
        if d < 2:
            return False
        if p[i] % 2 == 0 and p[i + 1] % 2 == 0 and d < 4:
            return False
    return True

def G_brute(N):
    G = [0] * (N + 1)
    G[0] = 1
    for n in range(1, N + 1):
        c = 0
        for p in all_partitions(n):
            if satisfies(p):
                c += 1
        G[n] = c
    return G

# ---- Product series ----
def prod_series(N):
    s = [0] * (N + 1)
    s[0] = 1
    for r in [2, 3, 6]:
        m = r
        while m <= N:
            ns = [0] * (N + 1)
            for i in range(N + 1):
                if s[i]:
                    v = s[i]
                    j = 0
                    while i + j * m <= N:
                        ns[i + j * m] += v
                        j += 1
            s = ns
            m += 8
    num = [0] * (N + 1)
    num[0] = 1
    m = 8
    while m <= N:
        nn = [0] * (N + 1)
        for i in range(N + 1):
            nn[i] += num[i]
            if i + m <= N:
                nn[i + m] -= num[i]
        num = nn
        m += 8
    P = [0] * (N + 1)
    for i in range(N + 1):
        if num[i]:
            for j in range(N + 1 - i):
                if s[j]:
                    P[i + j] += num[i] * s[j]
    return P

def main():
    G = G_dp(N)
    Gb = G_brute(13)
    assert G[:14] == Gb[:14], (G[:14], Gb[:14])
    print("V1_OK brute==DP to 13:", G[:14])
    P = prod_series(N)
    # V2: headline product mismatch at n=2
    assert G[0] == 1 and P[0] == 1
    assert G[1] == 0 and G[2] == 0, G[:5]
    assert P[2] == 1, P[:8]
    assert G[2] != P[2]
    print("V2_OK product mismatch: G[2]=0 vs P[2]=1; G[:8]=%s P[:8]=%s" % (G[:8], P[:8]))
    # V3: claimed 11-family fails at first index
    assert G[6] == 1, G[:8]
    assert G[6] % 11 != 0
    print("V3_OK family fails at 11*0+6=6: G(6)=1 != 0 mod 11")
    # no monomial q^c prefactor can rescue: G0=P0=1 forces c=0, then n=2 refutes
    print("V3b_OK no q^c shift: const terms both 1 so c=0; n=2 mismatch stands")
    # V4: full residue log for G
    print("V4 residue log for G (first n in class with G(n)%%11 != 0):")
    for r in range(11):
        wit = None
        for n in range(N + 1):
            if n % 11 == r and G[n] % 11 != 0:
                wit = (n, G[n] % 11, G[n])
                break
        assert wit is not None, r
        print("  r=%d first_nonzero_n=%d val_mod11=%d val=%d" % ((r,) + wit))
    # divergence census
    nd = sum(1 for i in range(N + 1) if G[i] != P[i])
    print("divergence count G!=P over 0..%d: %d" % (N, nd))
    print("G[:40]=" + str(G[:40]))
    print("P[:40]=" + str(P[:40]))
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
