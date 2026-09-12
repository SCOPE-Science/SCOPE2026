"""Recovery test C: can unbounded-holes Toeplitz reach n log n?
Hole count h_k at scale 2^k with h_k/2^k -> 0 (regularity proxy).
Configs: h_k = k, k^2, 2^{k/2}. Generic fillings. Window M=60000, p(n) to n=3000.
Verdict criterion: p(n)/(n log2 n) bounded away from 0 across decade n=300..3000
would keep complexity route alive; collapse toward 0 => linear regime persists.
"""
import math, random

def build(M, K, hole_fn, seed):
    rng = random.Random(seed)
    x = [None] * (M + 1)
    for k in range(1, K + 1):
        p = 2 ** k
        h = min(hole_fn(k), p - 1)
        holes = set(rng.sample(range(p), h))
        for c in range(p):
            if c in holes:
                continue
            b = rng.randrange(2)
            step = p
            start = c if c < M + 1 else None
            for i in range(c, M + 1, p):
                if x[i] is None:
                    x[i] = b
    for i in range(M + 1):
        if x[i] is None:
            x[i] = 0
    return x

def pcount(w, ns):
    # rolling-hash factor counting for speed
    out = {}
    for n in ns:
        seen = set()
        for i in range(len(w) - n + 1):
            seen.add(tuple(w[i:i + n]))
        out[n] = len(seen)
    return out

M = 60000
NS = [100, 300, 1000, 3000]
configs = {
    'holes=k': (lambda k: k, 7),
    'holes=k^2': (lambda k: k * k, 8),
    'holes=2^{k/2}': (lambda k: int(2 ** (k / 2)), 9),
}
for name, (hf, K) in configs.items():
    w = build(M, K, hf, seed=12345)
    pc = pcount(w, NS)
    dens = sum(1 for v in w if v == 0) / len(w)
    print(f'--- {name} K={K}:')
    for n in NS:
        c = pc[n]
        print(f'    p({n})={c} c/(n log2 n)={c / (n * math.log2(n)):.4f} c/n={c / n:.4f}')
