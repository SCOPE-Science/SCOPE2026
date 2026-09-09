# t1_levels.py — level-attribution + (M,eps)-average distortion probes for X0 (TARGET only).
from fractions import Fraction
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

def level_terms(vec, N, fams, norm, depth, upto=3):
    """Best exhibited term per level (lower-bound certificate) + argmax."""
    terms = {}
    for n in range(1, upto+1):
        th = Fraction(1, 2**n)
        best = Fraction(0); barg = None
        for fam in fams[n]:
            s = Fraction(0)
            for (l, r) in fam:
                sub = tuple(vec[i] if l <= i+1 <= r else Fraction(0) for i in range(N))
                if all(v == 0 for v in sub):
                    continue
                s += norm(sub, depth-1)
            cand = th * s
            if cand > best:
                best = cand; barg = fam
        terms[n] = (best, barg)
    return terms

def main():
    out = {}
    N = 7
    fams, norm = make_engine(N, 3)
    out['counts_N7'] = {str(n): len(fams[n]) for n in fams}
    D = 6
    cands = {
        'flat4_e4-e7': {4: Fraction(1,4), 5: Fraction(1,4), 6: Fraction(1,4), 7: Fraction(1,4)},
        'flat3_e5-e7': {5: Fraction(1,3), 6: Fraction(1,3), 7: Fraction(1,3)},
        'pair_e6e7': {6: 1, 7: 1},
        'single_e7': {7: 1},
    }
    for name, d in cands.items():
        v = V(N, d)
        nrm = norm(v, D)
        terms = level_terms(v, N, fams, norm, D)
        out[name] = {
            'norm': str(nrm),
            'per_level_best': {str(n): str(terms[n][0]) for n in terms},
            'argmax_level': max(terms, key=lambda n: terms[n][0]),
            'attaining_fam': str(terms[max(terms, key=lambda n: terms[n][0])][1]),
        }
    print(json.dumps(out, indent=1))
    with open('output/artifacts/level_log.json', 'w') as f:
        json.dump(out, f, indent=1)

if __name__ == '__main__':
    main()
