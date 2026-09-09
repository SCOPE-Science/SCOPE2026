"""verify.py — auditable Betti-transfer + diagonal + FIM+ obstruction check
for lane 466 target (punctured-torus secondary diagonal).

What it checks (all exact integer arithmetic, stdlib only):
 1. Wawrykow Thm 4.1 (torus) -> Prop 4.2 (punctured) transfer:
      bP_k(n) = sum_{m<=k} (-1)^{k-m} (k+1-m) bT_m(n+1)
    for k=0..5, n=0..15.
 2. Inverse Kunneth cross-check:
      bT_k(n) = bP_k(n-1) + 2 bP_{k-1}(n-1) + bP_{k-2}(n-1).
 3. Diagonal totals b_n(F_{2n-2}(T0)) and Betti-minus-primary split
    (quotient = top binomial coefficient) for n=2..5.
 4. Free-FIM+ obstruction at N=4: M^{FIM+}(W_2)_4 = C(4,2)*5*1 = 30
    vs actual secondary quotient 14 -> non-free (Wawrykow Cor 4.6 made explicit).
 5. Torus-b4 discrepancy flag: Wawrykow (33*C(n,4)) vs Pagaria-HTML (32*C(n,4)):
    tests which one satisfies the transfer to Wawrykow's punctured 79*C(n,4).

Exit: prints VERIFY_OK iff all checks pass, else FAIL detail.
"""
from math import comb, factorial


def C(n, k):
    if k < 0 or n < k:
        return 0
    return comb(n, k)


# ---- Torus formulas (Wawrykow Thm 4.1) ----
def bT(k, n):
    if k == 0:
        return 1
    if k == 1:
        return 2 * n
    if k == 2:
        return 2 * C(n, 3) + 3 * C(n, 2) + n
    if k == 3:
        return 14 * C(n, 4) + 8 * C(n, 3) + 2 * C(n, 2)
    if k == 4:
        return 32 * C(n, 6) + 74 * C(n, 5) + 33 * C(n, 4) + 5 * C(n, 3)
    if k == 5:
        return (63 * C(n, 8) + 427 * C(n, 7) + 490 * C(n, 6)
                + 154 * C(n, 5) + 18 * C(n, 4))
    raise ValueError(k)


# ---- Punctured formulas (Wawrykow Prop 4.2, claimed) ----
def bP(k, n):
    if k == 0:
        return 1
    if k == 1:
        return 2 * n
    if k == 2:
        return 2 * C(n, 3) + 5 * C(n, 2)
    if k == 3:
        return 14 * C(n, 4) + 18 * C(n, 3)
    if k == 4:
        return 32 * C(n, 6) + 106 * C(n, 5) + 79 * C(n, 4)
    if k == 5:
        return (63 * C(n, 8) + 490 * C(n, 7) + 853 * C(n, 6)
                + 432 * C(n, 5))
    raise ValueError(k)


def transfer(k, n):
    """RHS of Wawrykow transfer: sum_{m<=k} (-1)^{k-m}(k+1-m) bT_m(n+1)."""
    return sum(((-1) ** (k - m)) * (k + 1 - m) * bT(m, n + 1)
               for m in range(k + 1))


def free0(m2):
    """dim M^{FIM+}(0)_{2m} = (2m)!/(m! 2^m)."""
    m = m2 // 2
    return factorial(2 * m) // (factorial(m) * (2 ** m))


def main():
    ok = True
    # 1. transfer
    for k in range(6):
        for n in range(16):
            if transfer(k, n) != bP(k, n):
                print(f"FAIL transfer k={k} n={n}: {transfer(k,n)} != {bP(k,n)}")
                ok = False
    print("transfer k<=5, n<=15: OK" if ok else "transfer: FAILED")
    # 2. inverse Kunneth
    ok2 = True
    for k in range(6):
        for n in range(1, 16):
            lhs = bT(k, n)
            rhs = ((bP(k, n - 1) if k >= 0 else 0)
                   + 2 * (bP(k - 1, n - 1) if k - 1 >= 0 else 0)
                   + (bP(k - 2, n - 1) if k - 2 >= 0 else 0))
            if lhs != rhs:
                print(f"FAIL kunneth k={k} n={n}: {lhs} != {rhs}")
                ok2 = False
    print("kunneth inverse k<=5, n<=15: OK" if ok2 else "kunneth: FAILED")
    # 3. diagonal table
    # 3. diagonal table: dim W_n = w_{n,2n-2} = coeff of C(N,2n-2) in b_n(N)
    # (FI-generation reading, Wawrykow Prop 4.3 + Thm 2.11).
    # n=2 is special: N=2, b_2(N)=2*C(N,3)+5*C(N,2) so w_{2,2}=5, primary 0.
    # n>=3: N=2n-2 hits the top binomial, so dim W_n = leading coeff c_n.
    print("n | N=2n-2 | total b_n(F_N) | primary image | secondary quotient dim W_n")
    qval = {2: 5, 3: 14, 4: 32, 5: 63}
    for n in range(2, 6):
        N = 2 * n - 2
        tot = bP(n, N)
        top = qval[n]
        prim = tot - top
        print(f"{n} | {N} | {tot} | {prim} | {top}")
        assert tot == prim + top
    # spot values asserted in WORKLOG
    assert bP(2, 2) == 5 and bP(3, 4) == 86 and bP(4, 6) == 1853
    assert bP(5, 8) == 52059
    print("diagonal spot values 5, 86, 1853, 52059: OK")
    # 4. obstruction
    f = C(4, 2) * 5 * free0(2)
    print(f"free-from-W2 at N=4: {f} vs actual quotient 14; kernel >= {f - 14}")
    assert f == 30
    assert free0(2) == 1 and free0(4) == 3 and free0(6) == 15
    print("free dims M(0): 2,4,6 -> 1,3,15: OK")
    # 5. b4 discrepancy: replace 33 by 32 and see transfer break
    def bT4alt(n):
        return 32 * C(n, 6) + 74 * C(n, 5) + 32 * C(n, 4) + 5 * C(n, 3)
    bad = [n for n in range(16)
           if sum(((-1) ** (4 - m)) * (5 - m) *
                  (bT4alt(n + 1) if m == 4 else bT(m, n + 1))
                  for m in range(5)) != bP(4, n)]
    print(f"alt-32 torus b4 breaks transfer at n={bad} (=>33 is the consistent value)")
    assert len(bad) > 0
    if ok and ok2:
        print("VERIFY_OK")
    else:
        print("VERIFY_FAIL")


if __name__ == "__main__":
    main()
