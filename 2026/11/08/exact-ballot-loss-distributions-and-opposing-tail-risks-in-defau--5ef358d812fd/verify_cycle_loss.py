"""Exact small-instance checks for ballot loss in functional delegation graphs.

Run: python verify_cycle_loss.py
All arithmetic is rational; no external packages are required.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def mul(a, b):
    c = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def component_data(f):
    n = len(f)
    done = set()
    result = []
    for start in range(n):
        if start in done:
            continue
        seq, seen = [], {}
        v = start
        while v not in seen and v not in done:
            seen[v] = len(seq)
            seq.append(v)
            v = f[v]
        if v in seen:
            cycle = tuple(seq[seen[v]:])
            result.append(cycle)
        done.update(seq)
    # Every vertex reaches one of the cycles.
    cycles = {v: c for c in result for v in c}
    length = {}
    for v in range(n):
        path = []
        w = v
        while w not in cycles and w not in length:
            path.append(w)
            w = f[w]
        l = len(cycles[w]) if w in cycles else length[w]
        for u in reversed(path):
            l += 1
            length[u] = l
        if v in cycles:
            length[v] = len(cycles[v])
    return result, length


def theoretical_pmf(f, p):
    n = len(f)
    cycles, _ = component_data(f)
    cycverts = {v for c in cycles for v in c}
    kids = [[] for _ in f]
    for v, to in enumerate(f):
        if v not in cycverts:
            kids[to].append(v)

    def subtree(u):
        poly = [Fraction(1)]
        for v in kids[u]:
            poly = mul(poly, subtree(v))
        return add([1-p], [Fraction(0)] + [p * a for a in poly])

    out = [Fraction(1)]
    for cycle in cycles:
        c = len(cycle)
        conditional = [Fraction(1)]
        for v in cycle:
            for child in kids[v]:
                conditional = mul(conditional, subtree(child))
        conditional = [Fraction(0)] * c + conditional
        factor = add([1 - p ** c], [p ** c * a for a in conditional])
        out = mul(out, factor)
    out += [Fraction(0)] * (n + 1 - len(out))
    return out


def brute_pmf(f, p):
    n = len(f)
    ans = [Fraction(0)] * (n+1)
    for mask in range(1 << n):
        direct = {i for i in range(n) if mask & (1 << i)}
        lost = 0
        for v in range(n):
            seen = set()
            w = v
            while w not in direct and w not in seen:
                seen.add(w)
                w = f[w]
            if w not in direct:
                lost += 1
        ans[lost] += (1-p)**len(direct) * p**(n-len(direct))
    return ans


def test():
    num_graphs = 0
    pmf_checks = 0
    mean_checks = 0
    bound_equality_checks = 0
    for n in range(2, 7):
        options = [tuple(j for j in range(n) if j != i) for i in range(n)]
        for choices in product(*options):
            f = tuple(choices)
            cycles, depth_lengths = component_data(f)
            c_lengths = [len(c) for c in cycles]
            for p in (Fraction(2,5), Fraction(3,4)):
                E = sum((p**l for l in depth_lengths.values()), Fraction(0))
                low = n*p**n
                high = n*p*p if n%2==0 else (n-1)*p*p+p**3
                assert low <= E <= high, (f, p, E, low, high)
                if E == low:
                    assert len(cycles) == 1 and len(cycles[0]) == n
                if E == high:
                    assert all(c==2 for c in c_lengths)
                    assert len(cycles) == n//2
                    assert n%2==0 or sum(c_lengths)==n-1
                event_prob = 1
                for c in c_lengths:
                    event_prob *= 1 - p**c
                event_prob = 1-event_prob
                assert p**n <= event_prob <= 1-(1-p*p)**(n//2)
                mean_checks += 1
                bound_equality_checks += 4
            if n <= 5 or (n == 6 and num_graphs % 11 == 0):
                p = Fraction(2,5)
                exact = theoretical_pmf(f, p)
                brute = brute_pmf(f, p)
                assert exact == brute, (f, exact, brute)
                assert sum(exact) == 1
                assert sum(i*x for i,x in enumerate(exact)) == sum((p**l for l in depth_lengths.values()), Fraction(0))
                pmf_checks += 1
            num_graphs += 1
    p=Fraction(2,5)
    twos = (1,0,3,2,5,4)
    threes = (1,2,0,4,5,3)
    dist_a=theoretical_pmf(twos,p)
    dist_b=theoretical_pmf(threes,p)
    assert sum(dist_a[3:]) == 3*p**4 - 2*p**6
    assert sum(dist_b[3:]) == 2*p**3 - p**6
    assert sum(dist_b[3:]) > sum(dist_a[3:])
    assert sum(i*x for i,x in enumerate(dist_a)) > sum(i*x for i,x in enumerate(dist_b))
    print('PASS graph profiles:',num_graphs)
    print('PASS exact expectation and risk bounds:',mean_checks, 'parameter cases')
    print('PASS bound equality structure checks:',bound_equality_checks)
    print('PASS full-distribution brute comparisons:',pmf_checks)
    print('PASS six-voter tail-risk reversal: three 2-cycles versus two 3-cycles')
    print('E[L] for two-cycle graph:',sum(i*x for i,x in enumerate(dist_a)))
    print('E[L] for three-cycle graph:',sum(i*x for i,x in enumerate(dist_b)))
    print('P[L>=3] two-cycle graph:',sum(dist_a[3:]))
    print('P[L>=3] three-cycle graph:',sum(dist_b[3:]))

if __name__ == '__main__':
    test()
