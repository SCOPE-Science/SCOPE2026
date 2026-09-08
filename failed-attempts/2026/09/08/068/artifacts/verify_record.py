"""Fast exact verifier for the length-6 y-AP Mordell record (stdlib only).

Checks, by exact integer arithmetic:
  R1  k = 197225 is nonzero and sixth-power-free (trial-division factorisation).
  R2  The six points lie on E_k: y^2 = x^3 + k (exact integers).
  R3  The six y-values are distinct and form an AP with d = 294 != 0.
  R4  Good reduction + point counts #E(F_13) = 19, #E(F_19) = 27 (brute force).
  R5  Reductions Abar,Bbar of A=(70,735), B=(-14,441) occupy 9 distinct
      cosets of 3*E(F_19)  =>  |im(E(Q) -> E(F_19)/3E(F_19))| >= 9.
      Since E(Q)_tors is trivial (Mazur + R4 at p=13, see DRAFT.md),
      rank(Q) <= 1 would give |image| <= 3 -- contradiction. Hence rank >= 2.

Run:  python3 verify_record.py   (seconds)
"""
import math

K = 197225
PTS = [(70, 735), (70, -735), (-14, 441), (-14, -441), (-56, 147), (-56, -147)]
A = (70, 735)
B = (-14, 441)

def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def eadd(P, Q, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P == Q:
        if y1 % p == 0:
            return None
        lam = (3 * x1 * x1 * pow(2 * y1, p - 2, p)) % p
    else:
        dx = (x2 - x1) % p
        if dx == 0:
            return None
        lam = ((y2 - y1) * pow(dx, p - 2, p)) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def eneg(P, p):
    return None if P is None else (P[0], (-P[1]) % p)

def emul(n, P, p):
    R = None
    Q = P
    while n:
        if n & 1:
            R = eadd(R, Q, p)
        Q = eadd(Q, Q, p)
        n >>= 1
    return R

def count_pts(k, p):
    kk = k % p
    n = 1  # point at infinity
    for x in range(p):
        r = (x * x * x + kk) % p
        for y in range(p):
            if (y * y) % p == r:
                n += 1
    return n

def main():
    # R1
    assert K != 0
    f = factorint(K)
    assert all(e < 6 for e in f.values()), f
    print("R1 sixth-power-free: k =", K, "factors =", f)
    # R2
    for (x, y) in PTS:
        assert y * y == x * x * x + K, (x, y)
    print("R2 on-curve: all six points satisfy y^2 = x^3 +", K)
    # R3
    ys = sorted(y for _, y in PTS)
    assert len(set(ys)) == 6
    ds = [ys[i + 1] - ys[i] for i in range(5)]
    assert all(d == 294 for d in ds), ds
    print("R3 y-AP: ys =", ys, "d = 294")
    # R4
    assert K % 13 != 0 and K % 19 != 0  # good reduction (13,19 not dividing disc)
    n13 = count_pts(K, 13)
    n19 = count_pts(K, 19)
    assert n13 == 19, n13
    assert n19 == 27, n19
    print("R4 counts: #E(F_13) =", n13, " #E(F_19) =", n19)
    # R5
    p = 19
    G = [None] + [(x, y) for x in range(p) for y in range(p)
                  if (y * y - (x ** 3 + K)) % p == 0]
    assert len(G) == 27
    G3 = set(emul(3, Q, p) for Q in G)
    Abar = (A[0] % p, A[1] % p)
    Bbar = (B[0] % p, B[1] % p)
    assert (Abar[1] ** 2 - (Abar[0] ** 3 + K)) % p == 0
    assert (Bbar[1] ** 2 - (Bbar[0] ** 3 + K)) % p == 0

    def coset_key(Q):
        best = None
        for H in G3:
            Qm = eadd(Q, eneg(H, p), p)
            s = (0, -1, -1) if Qm is None else (1, Qm[0], Qm[1])
            if best is None or s < best:
                best = s
        return best

    keys = set()
    for i in range(3):
        for j in range(3):
            Q = eadd(emul(i, Abar, p), emul(j, Bbar, p), p)
            keys.add(coset_key(Q))
    assert len(keys) == 9, len(keys)
    print("R5 mod-19 3-quotient: 9 distinct cosets of 3E(F_19); |3E(F_19)| =", len(G3))
    print("VERIFY_OK record + rank>=2 inputs (torsion/rank deduction in DRAFT.md)")

if __name__ == "__main__":
    main()
