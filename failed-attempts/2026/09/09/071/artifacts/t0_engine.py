# Fast interval-family implicit-norm engine for X0 = T[(S_n,2^{-n})]. Exact rationals.
# Reduction lemma (used): sup over arbitrary successive E_i equals sup over interval E_i,
# since ||E x|| <= ||hull(E) x|| by 1-unconditionality (coordinate projection contractive;
# hull adds only zero-coefficient coords of Ex? PROOF: Ex supported in E; hull(E)x = Ex +
# extra terms x_i e_i for i in hull\E -- NOT zero. So hull gives LARGER vector, norm larger
# by unconditionality applied to hull(E)x projected onto E: ||Ex|| = ||P_E hull(E)x|| <=
# ||hull(E)x||. Hence replacing E by hull can only increase term. sup over intervals >= sup
# over sets; reverse inclusion trivial. Equality holds.)
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
    def cnt(start, k, kmax):
        if k > kmax:
            return False
        if start == m:
            return True
        for end in range(start+1, m+1):
            if in_S(F[start:end], n-1):
                if cnt(end, k+1, kmax):
                    return True
        return False
    for end in range(1, m+1):
        if in_S(F[:end], n-1):
            if cnt(end, 1, F[0]):
                return True
    return False

def interval_families(N, n):
    """All S_n-admissible successive interval families on [1..N] as tuples of (l,r)."""
    ivs = [(l, r) for l in range(1, N+1) for r in range(l, N+1)]
    fams = []
    def rec(after, cur, mins):
        if cur:
            fams.append(tuple(cur))
        for (l, r) in ivs:
            if l <= after:
                continue
            nm = tuple(sorted(mins + (l,)))
            if not in_S(nm, n):
                continue
            cur.append((l, r))
            rec(r, cur, nm)
            cur.pop()
    rec(0, [], ())
    return fams

def make_engine(N, levels):
    fams = {n: interval_families(N, n) for n in range(1, levels+1)}
    @lru_cache(maxsize=None)
    def norm(vec, depth):
        best = Fraction(0)
        for a in vec:
            aa = abs(a)
            if aa > best:
                best = aa
        if depth == 0:
            return best
        for n in range(1, levels+1):
            th = Fraction(1, 2**n)
            for fam in fams[n]:
                s = Fraction(0)
                for (l, r) in fam:
                    sub = tuple(vec[i] if l <= i+1 <= r else Fraction(0) for i in range(N))
                    if all(v == 0 for v in sub):
                        continue
                    s += norm(sub, depth-1)
                cand = th * s
                if cand > best:
                    best = cand
        return best
    return fams, norm

def V(N, d):
    return tuple(Fraction(d.get(i+1, 0)) for i in range(N))

def main():
    out = {}
    out['Schreier'] = {
        '{1,2} in S1': in_S((1, 2), 1),
        '{1,2} in S2': in_S((1, 2), 2),
        '{1,2} in S3': in_S((1, 2), 3),
        '{3,4} in S1': in_S((3, 4), 1),
        '{2,3} in S1': in_S((2, 3), 1),
        '{1} in S1': in_S((1,), 1),
        'S1 subset S2 check {3,4} in S2': in_S((3, 4), 2),
    }
    N = 5
    fams, norm = make_engine(N, 3)
    out['num_interval_families_N5'] = {str(n): len(fams[n]) for n in fams}
    tests = {
        'e1+e2': {1: 1, 2: 1},
        'e3+e4': {3: 1, 4: 1},
        'e5': {5: 1},
        'e4+e5': {4: 1, 5: 1},
        'avg_e4e5': {4: Fraction(1, 2), 5: Fraction(1, 2)},
        'e3+e4+e5': {3: 1, 4: 1, 5: 1},
    }
    for name, d in tests.items():
        v = V(N, d)
        vals = [str(norm(v, k)) for k in range(0, 7)]
        out[name] = vals
    # shift identity + AO ratio (exact)
    out['shift_identity'] = all(
        Fraction(1, 2**(n+j)) / Fraction(1, 2**j) == Fraction(1, 2**n)
        for n in range(1, 8) for j in [1, 2, 3])
    out['AO_ratio_identically_1'] = all(
        (Fraction(1, 2**n) / Fraction(1, 2)**n) == 1 for n in range(1, 8))
    print(json.dumps(out, indent=1))
    with open('output/artifacts/norm_log.json', 'w') as f:
        json.dump(out, f, indent=1)

if __name__ == '__main__':
    main()
