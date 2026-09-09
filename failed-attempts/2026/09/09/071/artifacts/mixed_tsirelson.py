# TARGET work: exact finite-window mixed-Tsirelson norms via memoized recursion.
# X0 = T[(S_n, 2^{-n})]. Exact rationals. Exhaustive subset families at small N (rigorous
# upper bounds on the window), hand exhibits for lower bounds.
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
import json

def in_S(F, n):
    F = tuple(sorted(F))
    if len(F) == 0:
        return True
    if n == 0:
        return len(F) <= 1
    if n == 1:
        return len(F) <= F[0]
    m = len(F)
    def cnt(start, k_sofar, k_max):
        if k_sofar > k_max:
            return False
        if start == m:
            return True
        for end in range(start+1, m+1):
            if in_S(F[start:end], n-1):
                if cnt(end, k_sofar+1, k_max):
                    return True
        return False
    for end in range(1, m+1):
        if in_S(F[:end], n-1):
            if cnt(end, 1, F[0]):
                return True
    return False

def all_families(N, n):
    """All S_n-admissible successive families of nonempty subsets of {1..N} (as tuples of bitmasks)."""
    subs = []
    for r in range(1, N+1):
        for c in combinations(range(1, N+1), r):
            subs.append(c)
    fams = []
    def rec(after, cur, mins):
        if cur:
            fams.append(tuple(cur))
        for E in subs:
            if E[0] <= after:
                continue
            new_mins = tuple(sorted(mins + (E[0],)))
            if not in_S(new_mins, n):
                continue
            # encode E as bitmask
            mask = 0
            for i in E:
                mask |= 1 << (i-1)
            cur.append(mask)
            rec(E[-1], cur, new_mins)
            cur.pop()
    rec(0, [], ())
    return fams

class NormEngine:
    def __init__(self, N, levels):
        self.N = N
        self.levels = levels
        self.fams = {n: all_families(N, n) for n in range(1, levels+1)}
        self.masks_by_fam = self.fams  # already masks

    @lru_cache(maxsize=None)
    def norm(self, vec, depth):
        # vec: tuple of Fractions length N
        best = Fraction(0)
        for a in vec:
            aa = abs(a)
            if aa > best:
                best = aa
        if depth == 0:
            return best
        N = self.N
        for n in range(1, self.levels+1):
            th = Fraction(1, 2**n)
            for fam in self.fams[n]:
                s = Fraction(0)
                for mask in fam:
                    sub = tuple(vec[i] if (mask >> i) & 1 else Fraction(0) for i in range(N))
                    # skip zero pieces
                    if all(v == 0 for v in sub):
                        continue
                    s += self.norm(sub, depth-1)
                cand = th * s
                if cand > best:
                    best = cand
        return best

    def vec(self, d):
        # d: dict 1-based -> Fraction
        return tuple(Fraction(d.get(i+1, 0)) for i in range(self.N))

def main():
    out = {}
    out['S_checks'] = {
        '{3,4} in S1': in_S((3,4),1),
        '{1,2} in S1': in_S((1,2),1),
        '{1,2} in S2': in_S((1,2),2),
        '{2,3} in S2': in_S((2,3),2),
        '{5,6,7,8} in S1': in_S((5,6,7,8),1),
        '{5,6,7,8} in S3': in_S((5,6,7,8),3),
    }
    N = 6
    eng = NormEngine(N, 3)
    out['num_families'] = {str(n): len(eng.fams[n]) for n in eng.fams}
    # convergence check: depth 4 vs 5 on test vector
    t = eng.vec({3: Fraction(1,2), 4: Fraction(1,2), 5: Fraction(1,2), 6: Fraction(1,2)})
    out['converge'] = {'depth4': str(eng.norm(t,4)), 'depth5': str(eng.norm(t,5)),
                       'depth6': str(eng.norm(t,6))}
    D = 6
    # exact norms
    e3e4 = eng.vec({3:1, 4:1}); out['||e3+e4||'] = str(eng.norm(e3e4,D))
    e1e2 = eng.vec({1:1, 2:1}); out['||e1+e2||'] = str(eng.norm(e1e2,D))
    e5 = eng.vec({5:1}); out['||e5||'] = str(eng.norm(e5,D))
    avg2 = eng.vec({5:Fraction(1,2),6:Fraction(1,2)}); out['||(e5+e6)/2||'] = str(eng.norm(avg2,D))
    avg4 = eng.vec({3:Fraction(1,4),4:Fraction(1,4),5:Fraction(1,4),6:Fraction(1,4)})
    out['||(e3+..+e6)/4||'] = str(eng.norm(avg4,D))
    # truncated norm |.|_{>=2} (levels 2..3 only) on same vectors
    eng2 = NormEngine(N, 3)
    # emulate truncation by zeroing level-1 families
    eng2.fams = {1: [], 2: eng2.fams[2], 3: eng2.fams[3]}
    eng2.norm.cache_clear() if hasattr(eng2.norm,'cache_clear') else None
    out['|e3+e4|_tr'] = str(eng2.norm(e3e4,D))
    out['|(e5+e6)/2|_tr'] = str(eng2.norm(avg2,D))
    out['|(e3+..+e6)/4|_tr'] = str(eng2.norm(avg4,D))
    out['|e5|_tr'] = str(eng2.norm(e5,D))
    print(json.dumps(out, indent=1))
    with open('output/artifacts/norm_log.json','w') as f:
        json.dump(out, f, indent=1)

if __name__ == '__main__':
    main()
