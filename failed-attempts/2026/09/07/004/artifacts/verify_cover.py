"""Deterministic exact-integer covering verification for digit-restricted sumsets.
Usage: python3 verify_cover.py
Verifies: candidate sets, full-universe maxima, interval-gap impossibility certificates.
All arithmetic is exact integer modular arithmetic; no floats.
Runtime < 60s.
"""
import math, sys

def U_set(p, digits):
    digits = set(digits)
    return [x for x in range(p) if all(int(ch) in digits for ch in str(x))]

def sumset(A, p):
    return sorted(set((a + b) % p for a in A for b in A))

def check_cover(A, p, label):
    S = sumset(A, p)
    ok = (len(S) == p and S == list(range(p)))
    cov = [False]*p
    for s in S:
        cov[s] = True
    assert all(cov) == ok
    print(f"{label}: |A|={len(A)} |S|={len(S)}/{p} full={ok}")
    if not ok:
        missing = sorted(set(range(p)) - set(S))
        print(f"  missing({len(missing)}): {missing}")
    return ok, S

def interval_missing(p):
    """Residues impossible for ANY A subset of [0,44]U[100,144] via integer-interval argument.
    Integer sums lie in I1=[0,88], I2=[100,188], I3=[200,288]. Since r+2p>288, only r, r+p matter."""
    I1 = set(range(0, 89))
    I2 = set(range(100, 189))
    I3 = set(range(200, 289))
    missing = []
    for r in range(p):
        if r in I1 or r in I2:
            continue
        if (r + p) in I2 or (r + p) in I3:
            continue
        missing.append(r)
    return missing

if __name__ == "__main__":
    fail = 0
    # 1. Universe size assertion
    U = U_set(197, {0,1,2,3,4})
    assert len(U) == 50, f"|U|={len(U)} != 50"
    print("PASS universe |U(197,D4)|=50")
    # 2. Triangular bound
    assert 19*20//2 == 190 < 197 <= 20*21//2 == 210
    print("PASS triangular bound |A|>=20 for p=197")
    # 3. Interval-gap certificates (pure integer ranges, no enumeration of digits)
    expected = {
        191: [98,99,189,190],
        193: [96,97,98,99,189,190,191,192],
        197: [92,93,94,95,96,97,98,99,189,190,191,192,193,194,195,196],
    }
    for p, exp in expected.items():
        m = interval_missing(p)
        assert m == exp, f"p={p} {m} != {exp}"
        print(f"PASS interval impossibility p={p}: {len(m)} residues uncovered for ANY A (e.g. {m[:4]}...). Hence no basis.")
        # cross-check: these residues are indeed missing from full U+U
        U4 = U_set(p, {0,1,2,3,4})
        S = set((a+b) % p for a in U4 for b in U4)
        assert all(r not in S for r in m), f"interval missing residue covered?! p={p}"
    for p in [173,179,181]:
        m = interval_missing(p)
        assert m == [], f"p={p} unexpectedly has interval gap {m}"
        print(f"INFO p={p}: no pure-interval gap; impossibility (if any) needs digit-exact check below.")
    # 4. Full-universe exact checks: no D4/D3/D2 universe covers its Z_p
    for p in [173,179,181,191,193,197]:
        for D in [{0,1,2},{0,1,2,3},{0,1,2,3,4}]:
            U2 = U_set(p, D)
            S = set((a+b) % p for a in U2 for b in U2)
            assert len(S) < p, f"unexpected full cover p={p} D={sorted(D)}"
            print(f"PASS full-U exact check p={p} Dmax={max(D)}: |S(U)|={len(S)}<{p}, so no subset covers.")
    # 5. Counting certificate D2
    for p in [173,179,181,191,193,197]:
        U2 = U_set(p, {0,1,2})
        assert len(U2) == 18 and 18*19//2 == 171 < p
        print(f"PASS counting impossibility D2 p={p}: 18*19/2=171<{p}.")
    print("ALL VERIFICATION CHECKS PASSED")
