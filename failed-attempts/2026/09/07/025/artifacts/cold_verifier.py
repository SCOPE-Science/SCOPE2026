#!/usr/bin/env python3
"""Cold independent verifier: reads output/artifacts/census_26_m6-9.csv
and rechecks every row from scratch with independently written code.
Also checks SHA hashes, counts, F-gaps, Wilf, and small-genus sanity totals.
Stdlib only."""
import csv, hashlib, sys
from fractions import Fraction

CSV = "output/artifacts/census_26_m6-9.csv"

def parse_intlist(s):
    return tuple(int(x) for x in s.split(";") if x != "")

def check_kunz(k, m):
    n = m-1
    assert len(k) == n and sum(k) == 26 and all(v >= 1 for v in k)
    for i in range(1, m):
        for j in range(1, m):
            s = i+j
            if s < m:
                assert k[i-1]+k[j-1] >= k[s-1], f"kunz fail {k} m={m} i={i} j={j}"
            elif s > m:
                assert k[i-1]+k[j-1]+1 >= k[s-m-1], f"kunz fail {k} m={m} i={i} j={j}"

def verify_row(m, k, w, F, c, e, n, Wfrac, gens):
    # recompute Apéry
    w2 = tuple([0]+[m*k[i]+(i+1) for i in range(m-1)])
    assert tuple(w) == w2, f"apery mismatch {k}"
    F2 = max(w2)-m
    assert F2 == F, f"F mismatch {k}: {F2} vs {F}"
    assert c == F+1
    # membership closure
    def member(x):
        return x >= w2[x % m] if x >= 0 else False
    # multiplicity check: 1..m-1 gaps, m in S
    for x in range(1, m):
        assert not member(x), f"multiplicity fail {k}: {x} in S"
    assert member(m)
    # genus via gap count up to F (all beyond F in S)
    gaps = [x for x in range(F+1) if not member(x)]
    assert len(gaps) == 26, f"genus fail {k}: {len(gaps)}"
    # conductor: F gap, F+1 in S, and all >=F+1 in S (check up to F+m+5)
    assert not member(F) and member(F+1)
    for x in range(F+1, F+m+10):
        assert member(x), f"conductor fail {k} at {x}"
    # embedding dimension via independent double loop (a<=b to differ from primary)
    cand = [m]+list(w2[1:])
    atoms = []
    for y in cand:
        dec = False
        a = 1
        while a <= y//2:
            b = y - a
            if member(a) and member(b):
                dec = True
                break
            a += 1
        if not dec:
            atoms.append(y)
    atoms.sort()
    assert atoms == sorted(gens), f"gens mismatch {k}: {atoms} vs {gens}"
    assert len(atoms) == e
    assert 2 <= e <= m
    # Wilf
    nn = c - 26
    assert nn == n
    assert Fraction(e*nn, c) == Wfrac
    assert Wfrac >= 1, f"Wilf violation {k}: {Wfrac}"
    return gaps

def main():
    rows = list(csv.DictReader(open(CSV)))
    print(f"rows={len(rows)}")
    assert len(rows) == 13139, f"total mismatch {len(rows)}"
    from collections import Counter
    per_m = Counter()
    fdist = {}
    minW = {}; minWk = {}; maxF = {}; maxFk = {}
    hashes = {}
    for r in rows:
        m = int(r["m"]); k = parse_intlist(r["kunz"]); w = parse_intlist(r["apery"])
        F = int(r["F"]); c = int(r["c"]); e = int(r["e"]); n = int(r["n"])
        num, den = r["W_frac"].split("/")
        Wfrac = Fraction(int(num), int(den))
        gens = parse_intlist(r["generators"])
        check_kunz(k, m)
        verify_row(m, k, w, F, c, e, n, Wfrac, gens)
        per_m[m] += 1
        fdist.setdefault(m, Counter())[F] += 1
        if m not in minW or Wfrac < minW[m]:
            minW[m] = Wfrac; minWk[m] = k
        if m not in maxF or F > maxF[m]:
            maxF[m] = F; maxFk[m] = k
    print(f"per-m={dict(per_m)}")
    assert dict(per_m) == {6:793, 7:1528, 8:4035, 9:6783}
    for m in [6,7,8,9]:
        d = dict(sorted(fdist[m].items()))
        print(f"m={m} Fdist={d} maxF={maxF[m]} minW={minW[m]} e.g. {minWk[m]}")
        # F mod m != 0 theorem check: no F divisible by m
        for F in d:
            assert F % m != 0, f"F={F} divisible by m={m} should be impossible"
        # completeness of range minus multiples
        lo, hi = min(d), max(d)
        missing = [F for F in range(lo, hi+1) if F not in d]
        print(f"  range=[{lo},{hi}] missing={missing}")
        # assert missing == exactly multiples of m in range
        expected_missing = [F for F in range(lo, hi+1) if F % m == 0]
        assert missing == expected_missing, f"gap pattern mismatch m={m}: {missing} vs {expected_missing}"
    # hash check vs summary
    import json
    summ = json.load(open("output/artifacts/summary.json"))
    for m in [6,7,8,9]:
        ks = sorted([parse_intlist(r["kunz"]) for r in rows if int(r["m"])==m])
        h = hashlib.sha256()
        for k in ks:
            h.update((",".join(map(str,k))+";").encode())
        assert h.hexdigest() == summ[str(m)]["sha"], f"hash mismatch m={m}"
        print(f"m={m} sha OK {h.hexdigest()[:16]}...")
    print("ALL COLD CHECKS PASSED")
    # small-genus sanity: recompute totals for g<=9 with same enumerator, compare to OEIS A007323
    # OEIS A007323: g=0..9: 1,1,2,4,7,12,23,39,67,118
    oeis = {0:1,1:1,2:2,3:4,4:7,5:12,6:23,7:39,8:67,9:118}
    def count_g(g):
        tot = 0
        for mm in range(2, g+2):  # m in 2..g+1 (m=1 only for g=0)
            if mm-1 > g: continue
            # compositions of g into mm-1 positive parts; for g small brute force
            def gen(n, parts):
                if parts == 1:
                    yield (n,)
                    return
                for f in range(1, n-parts+2):
                    for rest in gen(n-f, parts-1):
                        yield (f,)+rest
            for k in gen(g, mm-1):
                ok = True
                for i in range(1, mm):
                    for j in range(1, mm):
                        s=i+j
                        if s < mm:
                            if k[i-1]+k[j-1] < k[s-1]: ok=False; break
                        elif s > mm:
                            if k[i-1]+k[j-1]+1 < k[s-mm-1]: ok=False; break
                    if not ok: break
                if ok: tot += 1
        return tot
    for g in range(1, 10):
        t = count_g(g)
        status = "OK" if t == oeis[g] else "MISMATCH"
        print(f"g={g} computed_total={t} oeis={oeis[g]} {status}")
        assert t == oeis[g], f"sanity fail g={g}"
    print("SMALL-GENUS SANITY (OEIS A007323 g<=9) PASSED")

if __name__ == "__main__":
    main()
