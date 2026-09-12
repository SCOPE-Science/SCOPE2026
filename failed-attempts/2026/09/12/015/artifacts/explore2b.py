"""Recovery test A: multi-hole 2-adic Toeplitz with growing holes/scale.
Hole count per 2^k block grows (k holes) so hole density k/2^k -> 0 (regularity
proxy => unique ergodicity plausible) while hoping for superlinear complexity.
SYM fills bits complement-symmetrically around block centers; ASYM generically.
Measures: complexity p(n), complement-closure (proxy for involution on Y side)."""
import math

def build(M, K, sym):
    x = [None] * (M + 1)
    for k in range(1, K + 1):
        p = 2 ** k
        # hole residues: k evenly spaced residues stay holes; fill the rest
        holes = {(j * p) // (k + 1) % p for j in range(k)}
        # fill bit for class c at stage k:
        for c in range(p):
            if c in holes:
                continue
            b = ((c * 7 + k * 13) % 5 == 0)
            if sym:
                # symmetric fill: bit depends on min(c, p-1-c) orbit -> palindrome block
                b = ((min(c, p - 1 - c) * 7 + k * 13) % 5 == 0)
            for i in range(M + 1):
                if i % p == c and x[i] is None:
                    x[i] = 1 if b else 0
    for i in range(M + 1):
        if x[i] is None:
            x[i] = 0
    return x

def factors(w, n):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

M = 12000
for K in (7, 9):
    for sym, tag in ((True, 'SYM'), (False, 'ASYM')):
        w = build(M, K, sym=sym)
        print(f'--- {tag} K={K}')
        for n in (10, 20, 40, 80, 160, 320):
            c = len(factors(w, n))
            print(f'    p({n})={c} c/(n log2 n)={c / (n * math.log2(n)):.3f} c/n={c / n:.3f}')
        for n in range(1, 13):
            F = factors(w, n)
            bad = [u for u in F if tuple(1 - b for b in u) not in F]
            if bad:
                print(f'    complement-closure fails at n={n} (e.g. {bad[0]}); n<{n} ok')
                break
        else:
            print('    complement-closed to 12: True')
