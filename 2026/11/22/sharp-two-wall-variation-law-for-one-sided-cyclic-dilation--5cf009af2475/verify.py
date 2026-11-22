"""Exact finite checks for cyclic nearest-neighbour dilation in weighted variation.

Run: python3 verify.py
Only the stated finite checks are executed; the arbitrary-size theorem needs its proof.
"""
from fractions import Fraction as F
from itertools import product


def tv(z, weights):
    n = len(z)
    return sum(weights[i] * abs(z[(i + 1) % n] - z[i]) for i in range(n))


def dilation(z):
    n = len(z)
    return [max(z[i], z[(i + 1) % n]) for i in range(n)]


def arc(n, a, k):
    return [int(1 <= ((i - a) % n) <= k) for i in range(n)]


def modified_arc(n, a, k, u, v):
    z = arc(n, a, k)
    z[a] = u
    z[(a + k) % n] = 1 - v
    return z


def cut_formula(w):
    n = len(w)
    best = F(-1)
    attains = None
    for a in range(n):
        for k in range(1, n):
            b = (a + k) % n
            for u, v in product((0, 1), repeat=2):
                z = modified_arc(n, a, k, u, v)
                ratio = tv(z, w) / (w[a] + w[b])
                if ratio > best:
                    best, attains = ratio, (a, k, u, v)
    return best, attains


def compact_formula(w):
    n = len(w)
    terms = [F(1)]
    for k in range(n):
        den = w[(k-1)%n] + w[k]
        terms.extend(((w[(k-2)%n] + w[(k-1)%n]) / den,
                      (w[(k-2)%n] + w[k]) / den))
    for a in range(n):
        for k in range(2, n-1):
            b = (a + k) % n
            terms.append((max(w[(a-1)%n], w[a]) +
                          max(w[(b-1)%n], w[b])) / (w[a]+w[b]))
    return max(terms)


def chamber_max(w):
    # Independent enumeration of all realizable strict edge-sign chambers,
    # and all binary input perturbations. No cut formula is used here.
    n = len(w)
    best = F(0)
    for sigma in product((0, 1), repeat=n):
        if min(sigma) == max(sigma):
            continue  # impossible sign pattern of differences around a cycle
        selector = [(i + sigma[i]) % n for i in range(n)]
        for bits in range(1, 2**n - 1):
            z = [(bits >> i) & 1 for i in range(n)]
            projected = [z[selector[i]] for i in range(n)]
            best = max(best, tv(projected, w) / tv(z, w))
    return best


def realize_boundary_choices(n, a, k, u, v):
    # Strictly realize prescribed local choices at both domain walls.
    b = (a + k) % n
    sigma = [None] * n
    sigma[a], sigma[b] = u, v
    undecided = [i for i in range(n) if sigma[i] is None]
    if u == v:
        sigma[undecided[0]] = 1-u
    for i in undecided:
        if sigma[i] is None:
            sigma[i] = 0
    assert 0 < sum(sigma) < n
    positive = sum(sigma)
    negative = n - positive
    increments = [negative if bit else -positive for bit in sigma]
    assert sum(increments) == 0
    x = [0]
    for i in range(n-1):
        x.append(x[-1]+increments[i])
    assert all((x[(i+1)%n]-x[i]>0) == bool(sigma[i]) for i in range(n))
    z = arc(n, a, k)
    source = [4*t for t in x]
    changed = [source[i]+z[i] for i in range(n)]
    diff = [dilation(changed)[i]-dilation(source)[i] for i in range(n)]
    assert diff == modified_arc(n, a, k, u, v), (n,a,k,u,v,diff)
    return source, changed


def run():
    examined = 0
    witnessed = 0
    for n in range(3, 9):
        for seed in range(6):
            w = [F(((i*i + 7*seed + 5*i*seed + 11) % 17)+1) for i in range(n)]
            theory, params = cut_formula(w)
            assert theory == compact_formula(w)
            assert theory == chamber_max(w), (n, seed, w)
            for a in range(n):
                for k in range(1, n):
                    for u,v in product((0, 1), repeat=2):
                        src,dst=realize_boundary_choices(n,a,k,u,v)
                        assert tv([dilation(dst)[i]-dilation(src)[i] for i in range(n)],w) == tv(modified_arc(n,a,k,u,v),w)
                        witnessed += 1
            a,k,u,v=params
            src,dst=realize_boundary_choices(n,a,k,u,v)
            gain=tv([dilation(dst)[i]-dilation(src)[i] for i in range(n)],w)/tv([dst[i]-src[i] for i in range(n)],w)
            assert gain == theory
            examined += 1
    print('EXACT_CHAMBER_CUT_AND_COMPACT_FORMULAS_PASS', examined)
    print('EXACT_STRICT_TWO_INPUT_WITNESSES_PASS', witnessed)
    for n in range(3, 16):
        assert cut_formula([F(1)]*n)[0] == 1
    for n in (4,6,8,10,12):
        for a,b in ((1,2),(1,7),(3,4),(7,1)):
            weights=[F(a if i%2==0 else b) for i in range(n)]
            assert cut_formula(weights)[0] == max(F(a,b),F(b,a))
    print('UNIFORM_CONTRACTION_AND_ALTERNATING_SHARPNESS_PASS')
    weights=[F(1),F(2),F(1),F(2)]
    exact,params=cut_formula(weights)
    assert exact == 2
    singleton=max(max((weights[(k-2)%4]+weights[(k-1)%4])/(weights[(k-1)%4]+weights[k]),
                      (weights[(k-2)%4]+weights[k])/(weights[(k-1)%4]+weights[k])) for k in range(4))
    assert singleton == F(4,3) and exact > singleton
    assert 2 <= params[1] <= 2
    print('FOUR_CYCLE_TWO_WALL_VERSUS_SINGLETON_GAP_PASS',exact,singleton)
    print('ALL_CYCLIC_DILATION_VARIATION_CHECKS_PASS')

if __name__ == '__main__':
    run()
