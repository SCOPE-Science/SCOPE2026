"""Multi-hole 2-adic Toeplitz: complexity, complement-symmetry, regularity proxy."""
from collections import defaultdict

def build_multi(M, rounds, sym=True, asym_shift=1):
    # words indexed 0..M as finite windows of two-sided sequences.
    # Start x = [None]*(M+1); periodic skeletons with growing periods.
    x = [None] * (M + 1)
    holes_trace = []
    for k in range(1, rounds + 1):
        p = 2 ** k
        # fill: position i (mod p) with residue r_k: if currently None, assign bit
        # symmetric: bit alternates with k; asymmetric: bit = k mod 2 xor (k>=asym_shift)
        r = (7 * k + 3) % p  # deterministic residue choice
        if sym:
            b = k % 2
        else:
            b = (k % 2) ^ (1 if k >= asym_shift else 0)
        nfill = 0
        for i in range(M + 1):
            if i % p == r and x[i] is None:
                x[i] = b
                nfill += 1
        holes = sum(1 for v in x if v is None)
        holes_trace.append(holes / (M + 1))
    # branches to non-integer 2-adics: fill remaining Nones with tail bits
    tailbit = 0
    for i in range(M + 1):
        if x[i] is None:
            x[i] = tailbit
    return x, holes_trace

def factors(word, n):
    s = set()
    for i in range(len(word) - n + 1):
        s.add(tuple(word[i:i + n]))
    return s

def pcount(word, nmax, step=10):
    return {n: len(factors(word, n)) for n in range(1, nmax + 1, step)}

import math
M = 20000
for rounds in (8, 10, 12):
    for sym, tag in ((True, "SYM"), (False, "ASYM")):
        w, holes = build_multi(M, rounds, sym=sym)
        print(f"--- {tag} rounds={rounds} holedens={['%.3f' % h for h in holes]}")
        pc = pcount(w, 201, step=20)
        for n, c in pc.items():
            print(f"    p({n})={c}  ratio/nlog2n={c/(n*math.log2(n)):.3f}")
        # complement closure to length 12
        ok = True
        for n in range(1, 13):
            F = factors(w, n)
            for u in F:
                if tuple(1 - b for b in u) not in F:
                    ok = False
                    print(f"    NOT complement-closed at n={n}, e.g. {u}")
                    break
            if not ok:
                break
        if ok:
            print("    complement-closed to 12: True")
