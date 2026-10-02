"""Independent verifier for twin-interarrival census in [1030000000,1050000000].
Strategy (independent of census.py):
 - base primes by trial division (not mini-sieve);
 - odds-only segmented sieve with per-prime modular start;
 - twin extraction, gap log, maximal gap, first cousin;
 - deterministic Miller-Rabin (bases 2,7,61, valid <2^32) on the 6 witness primes;
 - cross-checks against twins.json/gaps.json/summary.json by hash + value.
Prints VERIFY_OK on success. Stdlib only.
"""
import json, hashlib, math, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # output/
LO, HI = 1030000000, 1050000000

def base_primes_trial(limit):
    ps = [2]
    for n in range(3, limit+1, 2):
        r = int(n**0.5)
        ok = True
        for p in ps:
            if p > r: break
            if n % p == 0: ok = False; break
        if ok: ps.append(n)
    return ps

def segmented_odds(lo, hi, base):
    # odds-only array: index i -> n = lo_odd + 2i
    lo_o = lo if lo % 2 == 1 else lo + 1
    n = ((hi - lo_o)//2)+1 if hi >= lo_o else 0
    a = bytearray(b'\x01')*n
    for p in base:
        if p == 2: continue
        if p*p > hi: break
        start = max(p*p, ((lo_o + p - 1)//p)*p)
        if start % 2 == 0 and p != 2:
            pass
        # ensure start odd multiple of p
        if start % 2 == 0:
            start += p  # p odd -> parity flips
        if start > hi: continue
        for m in range(start, hi+1, 2*p):
            a[(m-lo_o)//2] = 0
    # p*p may be even? p odd so p*p odd, fine
    primes = set()
    if lo <= 2 <= hi: primes.add(2)
    for i in range(n):
        if a[i]: primes.add(lo_o+2*i)
    return primes, a, lo_o

def mr_bases_2_7_61(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d, s = n-1, 0
    while d % 2 == 0: d//=2; s+=1
    for a in (2,7,61):
        if a % n == 0: continue
        x = pow(a, d, n)
        if x in (1, n-1): continue
        ok = False
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: ok=True; break
        if not ok: return False
    return True

def main():
    base = base_primes_trial(int(math.isqrt(HI))+1)
    primes, _, _ = segmented_odds(LO, HI, base)
    P = lambda n: n in primes
    twins = sorted(p for p in primes if p+2 <= HI and (p+2) in primes and p >= LO)
    # note: p odd always except 2; twins lower members
    C = len(twins)
    gaps = [twins[i+1]-twins[i] for i in range(C-1)]
    G = max(gaps)
    gi = gaps.index(G)
    p1, p2 = twins[gi], twins[gi+1]
    cousin = next(n for n in range(LO, HI-3) if n in primes and (n+4) in primes)
    print(f"C={C} G={G} idx={gi}")
    print(f"pair1=({p1},{p1+2}) pair2=({p2},{p2+2}) cousin=({cousin},{cousin+4})")
    # witness MR
    for w in (p1, p1+2, p2, p2+2, cousin, cousin+4):
        assert w < 2**32
        r = mr_bases_2_7_61(w)
        print(f"MR({w})={r}")
        assert r, w
    # maximality scan
    assert all(g <= G for g in gaps)
    assert sum(1 for g in gaps if g == G) >= 1
    # cousin minimality scan
    assert all(not (n in primes and (n+4) in primes) for n in range(LO, cousin))
    # cross-check committed files
    tj = json.load(open(os.path.join(OUT, "twins.json")))
    gj = json.load(open(os.path.join(OUT, "gaps.json")))
    sj = json.load(open(os.path.join(OUT, "summary.json")))
    assert tj == twins, "twins.json mismatch"
    assert gj == gaps, "gaps.json mismatch"
    assert sj["C"] == C and sj["G"] == G
    assert sj["pair1"] == [p1, p1+2] and sj["pair2"] == [p2, p2+2]
    assert sj["cousin"] == [cousin, cousin+4]
    for f in ("twins.json", "gaps.json"):
        h = hashlib.sha256(open(os.path.join(OUT, f), 'rb').read()).hexdigest()
        print(f"sha256({f})={h}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
