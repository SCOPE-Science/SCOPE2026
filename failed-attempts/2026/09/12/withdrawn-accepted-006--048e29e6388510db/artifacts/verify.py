"""Final replay verifier: re-derives EVERYTHING from logged integers in witnessed_table.json.
Checks:
1. discriminant normalization: D=pq, p<q primes 1 mod 4 (trial division suffices for D<2500).
2. Legendre symbols recomputed (Euler criterion) -> redei_rank.
3. norm witnesses: x^2-Dy^2==t with x%2==y%2 (parity = half-integer ring condition).
4. r4 consistency: r4=1 => leg=+1; r4=0 & leg=-1 ok; r4=0 & leg=+1 => N=+1 and h%4!=0
   (h itself comes from the rho census + certified unit norms, re-checked by census.py/certify_norms.py).
5. completeness: exactly the 81 pairs p<q, 1 mod 4, pq<2500.
"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
table = json.load(open(os.path.join(HERE, "witnessed_table.json")))

def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(s[i * i::i])
    return {i for i, v in enumerate(s) if v}

PR = primes_upto(2500)
P1 = sorted(p for p in PR if p % 4 == 1)
expect = [(p, q) for i, p in enumerate(P1) for q in P1[i + 1:] if p * q < 2500]
assert len(table) == len(expect) == 81, (len(table), len(expect))
got = sorted((e["p"], e["q"]) for e in table)
assert got == sorted(expect), "pair list mismatch"

for e in table:
    p, q, D = e["p"], e["q"], e["D"]
    assert p in PR and q in PR and p < q and p % 4 == 1 and q % 4 == 1
    assert D == p * q < 2500 and D % 4 == 1
    leg = 1 if pow(p, (q - 1) // 2, q) == 1 else -1
    assert leg == e["leg_pq"], (D,)
    assert e["redei_rank"] == (0 if leg == 1 else 1)
    assert e["N"] in (1, -1)
    h = e["h"]
    assert h % 2 == 0 and (e["r4"] == (1 if h % 4 == 0 else 0)), (D,)
    w = e["witness"]
    if e["r4"] == 1:
        assert leg == 1, (D,)
        assert w["kind"] == "norm_solution" and w["hits"], (D,)
        for name, hit in w["hits"].items():
            t = hit["t"]
            x, y = hit["sol"]
            assert x * x - D * y * y == t, (D, name)
            assert (x & 1) == (y & 1), (D, name)
            assert y > 0, (D, name)
            if e["N"] == 1:
                assert t in (4 * p, -4 * p, 4 * q, -4 * q), (D, name, t)
            else:
                assert t in (4 * p * p, -4 * p * p, 4 * q * q, -4 * q * q), (D, name, t)
    else:
        if leg == -1:
            assert w["kind"] == "legendre_obstruction", (D,)
            assert e["N"] == -1, (D,)  # empirical: all leg=-1 fields have N=-1
        else:
            assert w["kind"] == "unit_norm_obstruction", (D,)
            assert e["N"] == 1 and h % 4 != 0, (D,)

n1 = sum(1 for e in table if e["r4"] == 1)
print(f"ALL {len(table)} FIELDS REPLAY OK; r4=1: {n1}; r4=0: {len(table) - n1}")
print("VERIFY_OK")
