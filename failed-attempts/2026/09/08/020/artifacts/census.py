"""Segmented-sieve census for H=(0,2,6,8,30,32,36,38,42) below 1e9."""
import numpy as np, json, time

H = [0, 2, 6, 8, 30, 32, 36, 38, 42]
X = 10**9
SEG = 5_000_000
DMAX = 42

def base_primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b'\x00' * (((limit - i*i)//i) + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]

def main():
    t0 = time.time()
    sq = int(X**0.5) + 1
    base = base_primes(sq)
    hits = []
    nseg = (X + SEG - 1)//SEG
    for s in range(nseg):
        low = s*SEG
        high = min(low + SEG, X)
        seg = high - low
        a = np.ones(seg, dtype=np.bool_)
        if low == 0:
            a[0] = False
            if seg > 1:
                a[1] = False
        for p in base:
            start = max(p*p, ((low + p - 1)//p)*p)
            if start < high:
                a[start-low::p] = False
        L = seg - DMAX
        if L > 0:
            m = a[0:L]
            for h in H[1:]:
                m = m & a[h:h+L]
            for i in np.flatnonzero(m):
                n = low + int(i)
                if n >= 2:
                    hits.append(n)
        if (s+1) % 20 == 0 or s+1 == nseg:
            print(f"seg {s+1}/{nseg} low={low} hits={hits} elapsed={time.time()-t0:.1f}s", flush=True)
    out = {"X": X, "SEG": SEG, "H": H, "sqrt_limit": sq,
           "n_base_primes": len(base), "hits": hits,
           "n_hits": len(hits), "elapsed_s": round(time.time()-t0, 2)}
    with open("output/artifacts/census.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
