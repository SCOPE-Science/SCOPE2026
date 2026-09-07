#!/usr/bin/env python3
"""Pratt certificate generation + standalone verification for q ~ 1e12.
Cert format (JSON):
  {"q": int, "g": int, "factors": [{"prime": r, "exp": e, "cert": <cert for r>}], "q_minus_1": {...}}
Base case q==2: {"q":2,"g":1,"factors":[]}
Verifier checks: q>1, g^(q-1)=1 mod q, g^((q-1)/r)!=1 for each distinct r, product r^e == q-1, recursive certs valid.
Factoring via trial division with primes to 1_000_500 (sieve once).
"""
import json, sys, os, math, time

def sieve_primes(limit):
    bs = bytearray(b'\x01')*(limit+1)
    bs[0:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5)+1):
        if bs[i]:
            bs[i*i:limit+1:i] = b'\x00'*(((limit - i*i)//i)+1)
    return [i for i in range(2, limit+1) if bs[i]]

PRIMES = None

def factorize(n):
    """Return dict {prime: exp} for n>=1 using PRIMES trial division (complete for n<=1e12+)."""
    global PRIMES
    f = {}
    tmp = n
    for p in PRIMES:
        if p*p > tmp:
            break
        if tmp % p == 0:
            e = 0
            while tmp % p == 0:
                tmp //= p; e += 1
            f[p] = e
        if tmp == 1:
            break
    if tmp > 1:
        # tmp is prime (since trial covered to sqrt(original))
        f[tmp] = f.get(tmp, 0) + 1
    return f

_cert_cache = {2: {"q": 2, "g": 1, "factors": []}}

def pratt_cert(q):
    if q in _cert_cache:
        return _cert_cache[q]
    assert q > 2 and q % 2 == 1
    fac = factorize(q-1)
    distinct = sorted(fac.keys())
    # find primitive-root-like witness g
    g = None
    for cand in range(2, q):
        if pow(cand, q-1, q) != 1:
            continue  # q composite? should not happen for our primes
        ok = True
        for r in distinct:
            if pow(cand, (q-1)//r, q) == 1:
                ok = False; break
        if ok:
            g = cand; break
        if cand > 1000:
            # for large q this should have been found quickly; continue anyway
            pass
    if g is None:
        raise ValueError(f"no Pratt witness found for {q}")
    factors = []
    for r in distinct:
        factors.append({"prime": r, "exp": fac[r], "cert": pratt_cert(r)})
    cert = {"q": q, "g": g, "factors": factors}
    _cert_cache[q] = cert
    return cert

def verify_cert(cert, depth=0):
    q = cert["q"]
    if q == 2:
        return True
    g = cert["g"]
    factors = cert["factors"]
    # check product
    prod = 1
    for f in factors:
        prod *= f["prime"]**f["exp"]
    if prod != q-1:
        raise ValueError(f"q={q}: factor product {prod} != q-1={q-1}")
    if pow(g, q-1, q) != 1:
        raise ValueError(f"q={q}: g^(q-1)!=1")
    for f in factors:
        r = f["prime"]
        if pow(g, (q-1)//r, q) == 1:
            raise ValueError(f"q={q}: g^((q-1)/{r})==1, not primitive for factor {r}")
        verify_cert(f["cert"], depth+1)
    return True

def main():
    global PRIMES
    t0 = time.time()
    print("sieving base primes to 1000500...", flush=True)
    PRIMES = sieve_primes(1000500)
    print(f"  {len(PRIMES)} primes, time={time.time()-t0:.1f}s", flush=True)
    cin = sys.argv[1] if len(sys.argv) > 1 else "output/artifacts/census.json"
    cdir = sys.argv[2] if len(sys.argv) > 2 else "output/artifacts/certs"
    os.makedirs(cdir, exist_ok=True)
    with open(cin) as f:
        data = json.load(f)
    offs = [0,4,6,10,12,16]
    qs = []
    for p in data["list"]:
        for o in offs:
            qs.append(p+o)
    qs = sorted(set(qs))
    print(f"generating Pratt certs for {len(qs)} primes...", flush=True)
    t1 = time.time()
    for q in qs:
        c = pratt_cert(q)
        # verify immediately
        verify_cert(c)
        with open(os.path.join(cdir, f"{q}.json"), "w") as f:
            json.dump(c, f)
    dt = time.time()-t1
    print(f"done {len(qs)} certs in {dt:.1f}s", flush=True)
    # write summary
    summ = {"n_certs": len(qs), "qs": qs, "elapsed_s": dt,
            "total_s": time.time()-t0, "n_base_primes": len(PRIMES)}
    with open(os.path.join(cdir, "_summary.json"), "w") as f:
        json.dump(summ, f, indent=1)
    print(f"summary written; total {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
