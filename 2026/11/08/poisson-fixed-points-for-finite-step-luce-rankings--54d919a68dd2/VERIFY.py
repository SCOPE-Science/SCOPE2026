#!/usr/bin/env python3
"""Exact finite-state tests for fixed points of piecewise-constant Luce permutations.
Run: python3 VERIFY.py
Uses only the Python standard library; no external data or credentials.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial, exp


def fall(n, r):
    result = 1
    for i in range(r):
        result *= max(n-i,0) if i < n else 0
    return result


def check(block_sizes, rates):
    n = sum(block_sizes)
    assert n <= 7 and len(block_sizes) == len(rates)
    labels = tuple(range(n))
    color = []
    for j, size in enumerate(block_sizes):
        color.extend([j] * size)
    color = tuple(color)
    weights = [Fraction(rates[color[i]]) for i in labels]
    joint = {}
    word_mass = {}
    total = Fraction(0)
    for order in permutations(labels):
        rest = sum(weights)
        prob = Fraction(1)
        for lab in order:
            prob *= weights[lab] / rest
            rest -= weights[lab]
        word = tuple(color[lab] for lab in order)
        fixed = tuple(sum(order[pos] == pos for pos in labels if color[pos] == j) for j in range(len(rates)))
        joint[(word, fixed)] = joint.get((word, fixed), Fraction(0)) + prob
        word_mass[word] = word_mass.get(word, Fraction(0)) + prob
        total += prob
    assert total == 1, (block_sizes, rates, total)
    checks = 1
    for word, mass in word_mass.items():
        H = tuple(sum(word[pos] == j for pos in labels if color[pos] == j) for j in range(len(rates)))
        for k in product(range(4), repeat=len(rates)):
            if sum(k) > 3:
                continue
            lhs = sum(p * prod(fall(f[j], k[j]) for j in range(len(rates)))
                      for (w, f), p in joint.items() if w == word)
            rhs = mass
            for j in range(len(rates)):
                rhs *= Fraction(fall(H[j], k[j]), fall(block_sizes[j], k[j])) if k[j] <= block_sizes[j] else 0
            assert lhs == rhs, (block_sizes, rates, word, k, lhs, rhs)
            checks += 1
    return checks, len(joint), len(word_mass)


def prod(xs):
    v = 1
    for x in xs:
        v *= x
    return v


def intensity(fracs, rates):
    assert abs(sum(fracs)-1)<1e-10
    def G(t):
        return sum(a * (1-exp(-w*t)) for a, w in zip(fracs, rates))
    s = 0.0
    tprev = 0.0
    lambdas = []
    for j in range(len(fracs)):
        s += fracs[j]
        if j == len(fracs)-1:
            lambdas.append(exp(-rates[j]*tprev))
        else:
            lo, hi = 0.0, 1.0
            while G(hi)<s:
                hi *= 2
            for _ in range(100):
                mid = (lo+hi)/2
                if G(mid)<s:
                    lo=mid
                else:
                    hi=mid
            t = (lo+hi)/2
            lambdas.append(exp(-rates[j]*tprev)-exp(-rates[j]*t))
            tprev=t
    return lambdas


def main():
    configs = [((2,2),(1,3)), ((3,2),(4,1)), ((2,1,2),(1,3,2)),
               ((2,2,2),(2,1,4)), ((2,2,3),(3,1,2)), ((3,4),(1,1))]
    nchecks=0
    for sizes, rates in configs:
        cnt, pairs, words = check(sizes,rates)
        nchecks += cnt
        print(f'exact split={sizes} rates={rates}: {cnt} factorial-moment comparisons; {words} words, {pairs} classes')
    for fracs,rates in [([.4,.6],[4,1]),([.5,.5],[1,4]),([.2,.3,.5],[2,1,5]),([.6,.4],[1,1])]:
        vals=intensity(fracs,rates)
        assert all(0<v<1 for v in vals)
        nchecks+=len(vals)
        print(f'large-n proportions={fracs}, rates={rates}, lambda_j={[round(v,9) for v in vals]}, total={sum(vals):.9f}')
    assert abs(sum(intensity([.6,.4],[1,1]))-1.0)<1e-12
    nchecks+=1
    print('PASS:', nchecks, 'exact factorial-moment and analytic-boundary checks')


if __name__ == '__main__':
    main()
