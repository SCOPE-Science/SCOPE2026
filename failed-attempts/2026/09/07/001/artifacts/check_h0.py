"""Check H0 forcing claim: for H1=floor(H0)+1<pm, every interval (N,N+H1] in class a mod m
contains both a quadratic residue and a nonresidue. For H1>=pm the claim is trivial
(full period covers all of F_p). Run: python3 check_h0.py (needs numpy)."""
import math
import numpy as np
from verify_main import Bstar, E_val, primes_upto

def H0_val(p, m):
    return m * (2 * E_val(p, m) + 2) / (1 - 1 / p)

def main(pmax=5000, mmax=10):
    primes = [p for p in primes_upto(pmax) if p % 2 == 1]
    checked = 0; trivial = 0; fails = 0
    for p in primes:
        leg = np.zeros(p, dtype=np.int16)
        e = (p - 1) // 2
        for r in range(1, p):
            leg[r] = 1 if pow(r, e, p) == 1 else -1
        for m in range(1, mmax + 1):
            if math.gcd(m, p) != 1:
                continue
            H0 = H0_val(p, m)
            pm = p * m
            H1 = int(math.floor(H0)) + 1
            if H1 >= pm:
                trivial += 1
                continue
            chipm = np.tile(leg, m)
            ar = np.arange(pm)
            for a in range(1, m + 1):
                if math.gcd(a, m) != 1:
                    continue
                mask = (ar % m) == (a % m)
                is_res = (mask & (chipm == 1)).astype(np.int32)
                is_non = (mask & (chipm == -1)).astype(np.int32)
                is_res2 = np.concatenate([is_res, is_res])
                is_non2 = np.concatenate([is_non, is_non])
                cr = np.concatenate([[0], np.cumsum(is_res2)])
                cn = np.concatenate([[0], np.cumsum(is_non2)])
                idx = np.arange(pm)
                R = cr[idx + H1 + 1] - cr[idx + 1]
                Nn = cn[idx + H1 + 1] - cn[idx + 1]
                bad = int(np.sum((R == 0) | (Nn == 0)))
                checked += 1
                if bad:
                    fails += 1
                    print(f"H0-FAIL p={p} m={m} a={a} H0={H0:.1f} bad={bad}/{pm}")
    print(f"checked={checked} trivial={trivial} fails={fails}")

if __name__ == "__main__":
    main()
