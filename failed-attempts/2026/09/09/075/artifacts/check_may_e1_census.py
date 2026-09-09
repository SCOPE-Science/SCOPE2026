"""Lane-480: May E1 census at stems 253/254, low Adams filtration (stdlib only).

May SS (p=2) E1 = F2[h_{i,j} : i>=1, j>=0], each generator with
  Adams filt s=1, internal t = 2^j*(2^i-1)+1, stem = t-s = 2^j*(2^i-1).
A May-E1 monomial of Adams length s and total stem N is a multiset of s
generators whose stems sum to N. We count such multisets by DP and extract
samples. Reading:
  - If May E1 at (stem N, filt s) is EMPTY, then Ext_A^{s,N+s} = 0 rigorously
    (SS converges from E1; empty E1 => zero abutment). That would EXCLUDE the
    corresponding d_r target (necessary-condition failure, cf. falsifiability).
  - If NONEMPTY, Ext may still vanish via May differentials; inconclusive alone.

Scope: N=253, s=7..11 (d5..d9 targets) and N=254, s=2 (source sanity: h7^2).

Run: python3 output/artifacts/check_may_e1_census.py -> MAY_E1_CENSUS_OK
"""
import sys
from functools import lru_cache

def generators(max_stem):
    gens = []
    i = 1
    while (2**i - 1) <= max_stem:
        j = 0
        while (2**j) * (2**i - 1) <= max_stem:
            gens.append((i, j, (2**j) * (2**i - 1)))
            j += 1
        i += 1
    gens.sort(key=lambda g: (g[2], g[0], g[1]))
    return gens

def count_monomials(gens, s, target):
    # DP over generator types (multisets): dp[k][u] using types processed so far
    stems = [g[2] for g in gens]
    n = len(gens)
    # dp[t][k][u]: use memo recursion idx,k,remaining
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(idx, k, rem):
        if k == 0:
            return 1 if rem == 0 else 0
        if idx == n or rem <= 0:
            return 0
        total = 0
        st = stems[idx]
        # prune: smallest achievable with k factors from idx.. is k*st (types sorted asc)
        c = 0
        while c <= k and c * st <= rem:
            total += f(idx + 1, k - c, rem - c * st)
            c += 1
        return total
    return f(0, s, target)

def sample_monomials(gens, s, target, limit=6):
    stems = [g[2] for g in gens]
    n = len(gens)
    out = []
    def rec(idx, k, rem, cur):
        if len(out) >= limit:
            return True
        if k == 0:
            if rem == 0:
                out.append(tuple(cur))
            return False
        if idx == n or rem <= 0:
            return False
        st = stems[idx]
        c = 0
        while c <= k and c * st <= rem:
            cur.extend([idx] * c)
            # quick prune: remaining k-c factors each >= stems[idx+1] if idx+1<n
            if idx + 1 < n:
                lo = (k - c) * stems[idx + 1]
            else:
                lo = 0 if k - c == 0 else 10**18
            if lo <= rem - c * st:
                if rec(idx + 1, k - c, rem - c * st, cur):
                    return True
            del cur[len(cur) - c:]
            c += 1
        return False
    rec(0, s, target, [])
    labels = []
    for m in out:
        labels.append("*".join(f"h_{gens[i][0]},{gens[i][1]}" for i in m))
    return labels

def main():
    gens = generators(254)
    print(f"May generator types with stem<=254: {len(gens)}")
    # source sanity
    c = count_monomials(gens, 2, 254)
    print(f"N=254 s=2: May-E1 monomials = {c} (expect >=1: h_8,0^2)")
    print("  samples:", sample_monomials(gens, 2, 254, 4))
    assert c >= 1
    for s in (7, 8, 9, 10, 11):
        c = count_monomials(gens, s, 253)
        r = s - 2
        tag = f"d_{r}" if r in (5, 6, 7, 8, 9) else "?"
        print(f"N=253 s={s} ({tag} target): May-E1 monomials = {c}")
        if c > 0:
            for lab in sample_monomials(gens, s, 253, 4):
                print(f"    e.g. {lab}")
        else:
            print("    EMPTY E1 => Ext=0 there (exclusion!)")
    print("MAY_E1_CENSUS_OK")

if __name__ == "__main__":
    sys.exit(main())
