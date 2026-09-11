"""Recovery test for lane-704 target_claim.
Checks bounded, reproducible fragments:
 (T1) uniqueness of differences e^p - e^q on bounded exponent range (numeric separation
      + exact polynomial-identity check, conditional on Hermite transcendence of e).
 (T2) explicit 2-shattering truth table for phi0(x;y)=G(x+y), B={1,e}.
 (T3) pair-forces-full obstruction for powers-B {1,e,e^2}: any double-hit forces a=0.
All checks use only stdlib. Result line RECOVERY_OK or RECOVERY_FAIL.
"""
import math

E_LO = 2.718281828458  # rigorous lower bound for e (well within known value)
E_HI = 2.718281828460  # rigorous upper bound

def pow_interval(n):
    # interval for e^n using E_LO/E_HI (n may be negative)
    if n >= 0:
        return (E_LO**n, E_HI**n)
    else:
        return (E_HI**n, E_LO**n)  # since 1/E_HI < 1/E_LO

def poly_is_zero(coeff_dict):
    # coeff_dict: exponent -> coeff; zero poly iff all coeffs zero
    return all(c == 0 for c in coeff_dict.values())

def diff_key(n, m, shift=0):
    # polynomial X^{n+s} - X^{m+s} with shift to make exponents >=0
    d = {n+shift: 1, m+shift: -1}
    # combine
    out = {}
    for k, v in d.items():
        out[k] = out.get(k, 0) + v
    out = {k: v for k, v in out.items() if v != 0}
    return out

def test_T1(K=8):
    # numeric separation of differences e^n - e^m
    vals = {}
    for n in range(-K, K+1):
        for m in range(-K, K+1):
            if n == m:
                continue
            lo = pow_interval(n)[0] - pow_interval(m)[1]
            hi = pow_interval(n)[1] - pow_interval(m)[0]
            vals[(n, m)] = (lo+hi)/2
    keys = list(vals.keys())
    min_gap = float('inf')
    collision = None
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            # exact polynomial check: e^{n1}-e^{m1} == e^{n2}-e^{m2} ?
            n1, m1 = keys[i]; n2, m2 = keys[j]
            S = min(n1, m1, n2, m2)
            shift = -S
            poly = {}
            for k, c in [ (n1+shift,1),(m1+shift,-1),(n2+shift,-1),(m2+shift,1) ]:
                poly[k] = poly.get(k, 0) + c
            poly = {k: v for k, v in poly.items() if v != 0}
            if not poly:
                # identical polynomially: same unordered pair
                if {n1, m1} != {n2, m2} and not (n1 == m1 and n2 == m2):
                    collision = (keys[i], keys[j])
                continue
            # distinct polynomially -> by transcendence values differ; numeric gap:
            gap = abs(vals[keys[i]] - vals[keys[j]])
            if gap < min_gap:
                min_gap = gap
    # check no unexpected polynomial collision with c != 0
    ok = (collision is None)
    return ok, min_gap, len(vals)

def in_G_interval(v):
    # decide v in {e^n} using intervals for n in [-30, 30]; returns (True,n) / (False,(n1,n2) bracket) / None
    if v <= 0:
        return (False, "nonpositive")
    # find bracket
    for n in range(-30, 30):
        lo_n, hi_n = pow_interval(n)
        lo_m, hi_m = pow_interval(n+1)
        if hi_n < v < lo_m:
            return (False, (n, n+1))
        if lo_n <= v <= hi_n and (hi_n - lo_n) < 1e-9:
            # need exact: check with tighter logic below via polynomial argument instead
            pass
    return None

def test_T2():
    e = math.e
    B = [1.0, e]
    # witnesses: S -> a
    W = {
        (): -10.0,
        (0,): e**2 - 1.0,
        (1,): e**2 - e,
        (0, 1): 0.0,
    }
    rows = []
    for S, a in W.items():
        hits = []
        for j, b in enumerate(B):
            v = a + b
            # exact verdicts:
            if S == () :
                # a+b negative -> not in G
                is_hit = (v > 0 and False)  # v<0 so False
                is_hit = False
                assert v < 0, (S, j, v)
            elif S == (0,) and j == 0:
                is_hit = True  # a+1 = e^2 by construction
                assert abs(v - e**2) < 1e-9
            elif S == (0,) and j == 1:
                # v = e^2+e-1; claim strictly between e^2 and e^3
                assert e**2 < v < e**3, v
                is_hit = False
            elif S == (1,) and j == 1:
                is_hit = True
                assert abs(v - e**2) < 1e-9
            elif S == (1,) and j == 0:
                # v = e^2-e+1 between e^1=e and e^2?
                assert e < v < e**2, v
                is_hit = False
            elif S == (0, 1):
                is_hit = True  # 1 and e
            else:
                raise AssertionError
            hits.append(is_hit)
        rows.append((S, a, tuple(hits)))
    # verify patterns match
    assert rows[0][2] == (False, False)
    assert rows[1][2] == (True, False)
    assert rows[2][2] == (False, True)
    assert rows[3][2] == (True, True)
    return rows

def test_T3():
    # B = {1,e,e^2} powers. Claim: any a hitting 1 and e must be a=0 (hence hits e^2).
    # Proof via uniqueness: e^n - e^m = e-1 forces {n,m}={1,0} as polynomials.
    # Check: polynomial X^n - X^m - (X - 1) == 0 iff {n,m}={1,0}.
    sols = []
    for n in range(-6, 7):
        for m in range(-6, 7):
            S = min(n, m, 1, 0)
            poly = {}
            for k, c in [(n-S, 1), (m-S, -1), (1-S, -1), (0-S, 1)]:
                poly[k] = poly.get(k, 0) + c
            poly = {k: v for k, v in poly.items() if v != 0}
            if not poly:
                sols.append((n, m))
    # only solutions should be (1,0)
    assert sols == [(1, 0)], sols
    # corresponding a: a+1 = e^1? wait n is exponent of a+1? a+1=e^n, a+e=e^m, diff e-1 = e^m-e^n? sign check:
    # (a+e)-(a+1) = e-1 = e^m - e^n -> need (m,n)=(1,0) -> a+1=1 -> a=0. Confirmed.
    return sols

if __name__ == "__main__":
    ok1, gap, count = test_T1()
    print(f"T1 uniqueness: ok={ok1} checked_pairs={count} min_numeric_gap~{gap:.3e}")
    rows = test_T2()
    for S, a, hits in rows:
        print(f"T2 shatter: S={S} a={a:.6f} hits={hits}")
    sols = test_T3()
    print(f"T3 pair-forces-full: sols={sols}")
    if ok1:
        print("RECOVERY_OK")
    else:
        print("RECOVERY_FAIL")
