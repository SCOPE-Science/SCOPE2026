"""HOMFLY-PT via terminating Conway skein tree on PD (descending-diagram induction).

Measure: (n_crossings, n_bad) lexicographic. Bad crossing = over-strand
traversed before under-strand along component traversal from basepoints.
- Flip a bad crossing: same n_crossings, n_bad drops by exactly 1
  (flip changes only over/under roles, not connectivity/traversal).
- Smooth any crossing (oriented smoothing): n_crossings drops by 1.
All-good (descending) diagram = unlink -> delta^{k-1}. Terminates.
Skein: v^{-1}P+ - vP- = zP0; P+ = v^2 P- + vz P0; P- = v^{-2}P+ - v^{-1}z P0.
"""
from fractions import Fraction

def padd(A, B, s=1):
    C = dict(A)
    for k, c in B.items():
        C[k] = C.get(k, 0) + s * c
        if C[k] == 0:
            del C[k]
    return C

def pmul(A, B):
    C = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            k = (a1 + a2, b1 + b2)
            C[k] = C.get(k, 0) + c1 * c2
    return {k: v for k, v in C.items() if v != 0}

def pscale(A, pv, pz, c=1):
    return {(k[0] + pv, k[1] + pz): v * c for k, v in A.items() if v * c != 0}

ONE = {(0, 0): Fraction(1)}
DELTA = padd({(-1, -1): Fraction(1)}, {(1, -1): Fraction(-1)})

def braid_closure_pd(word, n):
    cur = [f't{j}' for j in range(n)]
    crossings = []
    nc = [0]
    def new():
        nc[0] += 1
        return f'e{nc[0]}'
    for e in word:
        i = abs(e) - 1
        a_in = cur[i]; b_in = cur[i + 1]
        a_out = new(); b_out = new()
        if e > 0:
            crossings.append((b_in, a_out, a_in, b_out, 1))
        else:
            crossings.append((a_in, b_out, b_in, a_out, -1))
        cur[i], cur[i + 1] = a_out, b_out
    loose = tuple((cur[j], f't{j}') for j in range(n))
    return tuple(crossings), tuple(loose)

def traverse(cross, loose):
    """Return (order dict edge->first-visit index, n_components). Walk components."""
    nxt = {}
    for (iu, ou, io, oo, s) in cross:
        nxt[iu] = ou
        nxt[io] = oo
    for (b, t) in loose:
        nxt[b] = t
    order = {}
    idx = 0
    comps = 0
    seen = set()
    starts = list(nxt.keys())
    for st in starts:
        if st in seen:
            continue
        comps += 1
        x = st
        while x not in seen:
            seen.add(x)
            order[x] = idx
            idx += 1
            x = nxt[x]
    return order, comps

def homfly_braid(word, n):
    cross0, loose0 = braid_closure_pd(word, n)
    memo = {}
    def ev(cross, loose):
        key = (tuple(sorted(cross)), tuple(sorted(loose)))
        if key in memo:
            return memo[key]
        order, comps = traverse(cross, loose)
        # find bad crossings: over-in traversed before under-in
        bad = [X for X in cross if order[X[2]] < order[X[0]]]
        if not bad:
            res = dict(ONE)
            for _ in range(comps - 1):
                res = pmul(res, DELTA)
            memo[key] = res
            return res
        X = bad[0]
        (iu, ou, io, oo, s) = X
        rest = tuple(Y for Y in cross if Y != X)
        flipped = (io, oo, iu, ou, -s)
        sm = tuple(sorted(loose + ((iu, oo), (io, ou))))
        if s > 0:
            # current is L+: P+ = v^2 P- + vz P0
            t_flip = ev(tuple(sorted((flipped,) + tuple(rest))), loose)
            t_sm = ev(tuple(sorted(rest)), sm)
            res = padd(pscale(t_flip, 2, 0), pscale(t_sm, 1, 1))
        else:
            t_flip = ev(tuple(sorted((flipped,) + tuple(rest))), loose)
            t_sm = ev(tuple(sorted(rest)), sm)
            res = padd(pscale(t_flip, -2, 0), pscale(t_sm, -1, 1, -1))
        memo[key] = res
        return res
    return ev(tuple(sorted(cross0)), tuple(sorted(loose0)))

def fmt(P):
    return ' + '.join(f'{c}v^{a}z^{b}' for (a, b), c in sorted(P.items()))

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    print('unknot []:', fmt(homfly_braid([], 1)))
    print('2-unlink []2:', fmt(homfly_braid([], 2)))
    print('kink+ [1]:', fmt(homfly_braid([1], 2)))
    print('kink- [-1]:', fmt(homfly_braid([-1], 2)))
    print('hopf [1,1]:', fmt(homfly_braid([1, 1], 2)))
    print('trefoil [1,1,1]:', fmt(homfly_braid([1, 1, 1], 2)))
    print('fig8 [1,-2,1,-2]:', fmt(homfly_braid([1, -2, 1, -2], 3)))
