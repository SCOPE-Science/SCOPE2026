"""Step B: fit crossing signs so bracket Jones matches KnotAtlas Jones.
State sum: <D> = sum_states A^(a-b) (-A^2-A^-2)^(circles-1), then V from writhe.
We don't know A- vs B-smoothing convention mapping; try both global choices and
all writhe-compatible sign patterns implicitly via oriented bracket:
For each sign vector s (2^10 = 1024 options), compute Jones and compare to target.
Bracket per state needs only circle counts (have) + A-exponents from mask vs s.
Cost: 1024 signs x 1024 states x circle lookup = 1M ops per knot. Fine.
Jones polynomials compared as dicts exponent->coeff with q variable.
KnotAtlas Jones strings parsed manually below.
"""
import json, itertools
from collections import Counter

def parse_pd(s):
    out = []
    for t in s.split():
        body = t[1:]
        nums = body.split(',') if ',' in body else list(body)
        out.append(tuple(int(x) for x in nums))
    return out

def circles_all(pd):
    n = len(pd)
    res = {}
    for mask in range(1 << n):
        parent = {}
        labels = set()
        for (a, b, c, d) in pd:
            labels.update([a, b, c, d])
        for x in labels:
            parent[x] = x
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for k, (a, b, c, d) in enumerate(pd):
            m = (mask >> k) & 1
            ra, rb, rc, rd = find(a), find(b), find(c), find(d)
            if m == 0:
                # union a-b, c-d
                for x, y in ((ra, rb), (rc, rd)):
                    rx, ry = find(x), find(y)
                    if rx != ry:
                        parent[rx] = ry
            else:
                for x, y in ((ra, rd), (rb, rc)):
                    rx, ry = find(x), find(y)
                    if rx != ry:
                        parent[rx] = ry
        res[mask] = len(set(find(x) for x in labels))
    return res

# target Jones as dicts (exponent -> coeff), variable q
TARGETS = {
 '10_124': {10: -1, 6: 1, 4: 1},
 '10_125': {4: -1, 3: 1, 2: -1, 1: 2, 0: -1, -1: 2, -2: -1, -3: 1, -4: -1},
 '10_126': {0: -1, -1: 2, -2: -2, -3: 4, -4: -3, -5: 3, -6: -2, -7: 1, -8: -1},
 '10_127': {-2: 2, -3: -2, -4: 4, -5: -5, -6: 5, -7: -5, -8: 3, -9: -2, -10: 1},
 '10_128': {10: -1, 9: 1, 8: -2, 7: 2, 6: -1, 5: 2, 4: -1, 3: 1},
 '10_129': {3: -1, 2: 2, 1: -3, 0: 5, -1: -4, -2: 4, -3: -3, -4: 2, -5: -1},
 '10_130': {1: -1, 0: 2, -1: -2, -2: 3, -3: -2, -4: 3, -5: -2, -6: 1, -7: -1},
 '10_131': {-1: 2, -2: -3, -3: 5, -4: -5, -5: 5, -6: -5, -7: 3, -8: -2, -9: 1},
}

def bracket_jones(pd, circ, signs, flip):
    """signs: tuple of +1/-1 per crossing. flip: if True swap 0/1 smoothing roles.
    Returns Jones dict q-exp -> coeff (x4 exponents)."""
    n = len(pd)
    w = sum(signs)
    # bracket: sum over states; state bit m_k: use exponent contribution depending on
    # crossing sign and smoothing type. Standard: for + crossing, 0-smoothing = A-type.
    # With flip option for convention uncertainty.
    from collections import defaultdict
    br = defaultdict(int)  # A-exponent -> coeff, where loop value d=(-A^2-A^-2)
    for mask in range(1 << n):
        c = circ[mask]
        e = 0
        for k in range(n):
            m = (mask >> k) & 1
            if flip:
                m = 1 - m
            # A-smoothing contributes +1, B contributes -1; for negative crossing swap
            if signs[k] == 1:
                e += 1 if m == 0 else -1
            else:
                e += -1 if m == 0 else 1
        # multiply by d^(c-1): expand (-A^2 - A^-2)^(c-1)
        # represent polynomial in A as dict
        poly = {0: 1}
        for _ in range(c - 1):
            np = defaultdict(int)
            for ex, cf in poly.items():
                np[ex + 2] -= cf
                np[ex - 2] -= cf
            poly = np
        for ex, cf in poly.items():
            br[e + ex] += cf
    # normalize: V = (-A^3)^(-w) <D> with q = A^-4.
    # (-A^3)^(-w) = (-1)^(-w) A^(-3w) = (-1)^w A^{-3w}.
    br2 = defaultdict(int)
    for ex, cf in br.items():
        br2[ex - 3 * w] += cf * (1 if w % 2 == 0 else -1)
    # convert A-exp E -> q-exp -E/4; require E divisible by 4
    J = defaultdict(int)
    for ex, cf in br2.items():
        if ex % 4 != 0:
            return None
        J[-ex // 4] += cf
    return dict(J)

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    import sys
    only = sys.argv[1:] or list(TARGETS)
    for k in only:
        pd = parse_pd(d[k]['pd'])
        circ = circles_all(pd)
        tgt = TARGETS[k]
        hits = []
        for sm in range(1 << 10):
            signs = tuple(1 if (sm >> i) & 1 else -1 for i in range(10))
            for flip in (False, True):
                J = bracket_jones(pd, circ, signs, flip)
                if J == tgt:
                    hits.append((sm, sum(signs), flip))
        print(k, 'nhits=', len(hits), hits[:6])
