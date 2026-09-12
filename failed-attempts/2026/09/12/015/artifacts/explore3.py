"""Recovery test B (obstacle T1): Toeplitz-defect of complement-symmetric
constant-length S-adic fixed points. tau(1) = overline{tau(0)} has no
coincidences; quantify the density of 'holes' (positions never forced by any
finite skeleton) at scales 2^k for the Thue-Morse-like symmetric morphism
0 -> 01, 1 -> 10. If hole density stays bounded away from 0, the symmetric
morphism route cannot be Toeplitz (Toeplitz needs arbitrarily fine full periods).
Proxy: fraction of length-L window offsets NOT covered by any 2^k-periodic
skeleton consistent with the fixed point word."""
from collections import Counter

def tm(n):
    return bin(n).count('1') % 2

L = 4096
w = [tm(i) for i in range(L)]
print('word built (Thue-Morse prefix)')
for k in range(1, 9):
    p = 2 ** k
    # a residue class c mod p is 'forced at scale p' if all occurrences agree
    forced = 0
    for c in range(p):
        vals = {w[i] for i in range(c, L, p)}
        if len(vals) == 1:
            forced += 1
    print(f'  scale 2^{k}={p}: forced classes {forced}/{p} density {forced / p:.4f} '
          f'hole density {1 - forced / p:.4f}')
