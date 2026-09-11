"""Hereditary branch-parity refinement probe.

Canonical fix: call beta EVEN iff #{xi<beta: osc(xi,beta) even} >= #{odd}
(analogue of 'club/stationary many even levels'), ODD otherwise.
A0 = union of branches f_beta|xi over even beta (hereditary by construction).
A1 = union over odd beta. Tests: both tall/nontrivial? widths per level?
levelwise fit? disjointness of branch sets?
"""
import sys


def build(N, mode):
    C = {}
    for a in range(N):
        if a == 0:
            C[a] = []
        elif a % 2 == 1:
            C[a] = [a - 1]
        else:
            if mode == 'sparse':
                C[a] = sorted(set(list(range(0, a, 2)) + [a - 1]))
            elif mode == 'mod3':
                C[a] = sorted(set(list(range(0, a, 3)) + [a - 1]))
            elif mode == 'ladder':
                C[a] = [0, a - 1] if a > 1 else [a - 1]

    def rho2(a, b):
        if a >= b:
            return 0
        cur = b
        steps = 0
        while cur != a:
            if cur <= a:
                break
            cand = [x for x in C[cur] if x >= a]
            nxt = min(cand) if cand else a
            if nxt >= cur:
                steps += 1
                break
            cur = nxt
            steps += 1
            if steps > 500:
                break
        return steps

    def osc(a, b):
        n = 0
        prev = None
        for xi in range(a):
            s = 1 if rho2(xi, a) <= rho2(xi, b) else -1
            if prev is not None and s != prev:
                n += 1
            prev = s
        return n

    return rho2, osc


def analyze(N, mode):
    rho2, osc = build(N, mode)
    branch = {}
    for beta in range(N):
        branch[beta] = tuple(rho2(a, beta) for a in range(beta + 1))
    parity = {}
    for beta in range(N):
        ev = sum(1 for xi in range(beta) if osc(xi, beta) % 2 == 0)
        od = beta - ev
        parity[beta] = ('even' if ev >= od else 'odd', ev, od)
    evens = [b for b in range(N) if parity[b][0] == 'even']
    odds = [b for b in range(N) if parity[b][0] == 'odd']
    A0 = set()
    for b in evens:
        for xi in range(b + 1):
            A0.add((xi, branch[b][:xi]))
    A1 = set()
    for b in odds:
        for xi in range(b + 1):
            A1.add((xi, branch[b][:xi]))

    def levsizes(S):
        d = {}
        for (xi, t) in S:
            d[xi] = d.get(xi, 0) + 1
        return dict(sorted(d.items()))

    def height(S):
        return max((xi for (xi, t) in S), default=-1)

    l0, l1 = levsizes(A0), levsizes(A1)
    fit10 = all(l1.get(l, 0) <= l0.get(l, 0) for l in l1)
    fit01 = all(l0.get(l, 0) <= l1.get(l, 0) for l in l0)
    return {
        'mode': mode, 'N': N,
        'n_even_beta': len(evens), 'n_odd_beta': len(odds),
        'A0': len(A0), 'A1': len(A1),
        'height0': height(A0), 'height1': height(A1),
        'lev0': l0, 'lev1': l1,
        'c1_fits_c0': fit10, 'c0_fits_c1': fit01,
        'parity': {b: parity[b] for b in range(N)},
    }


def main():
    for mode in ['sparse', 'mod3', 'ladder']:
        r = analyze(14, mode)
        print('mode=%s N=%d even_beta=%d odd_beta=%d |A0|=%d(h=%d) |A1|=%d(h=%d) '
              'fit10=%s fit01=%s' % (
                  r['mode'], r['N'], r['n_even_beta'], r['n_odd_beta'],
                  r['A0'], r['height0'], r['A1'], r['height1'],
                  r['c1_fits_c0'], r['c0_fits_c1']))
        print('   lev0=' + str(r['lev0']))
        print('   lev1=' + str(r['lev1']))
        print('   parity=' + str(r['parity']))


if __name__ == '__main__':
    sys.exit(main())
