#!/usr/bin/env python3
"""Standalone exact verifier for a finite swap-channel theorem.

Run: python3 verify.py
Requires certificate.json beside this program; only Python standard library.
All fractional comparisons use fractions.Fraction, never floating point.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

EXPECTED_M = (2, 2, 3, 4, 6, 8, 12, 18, 25, 38)
EXPECTED_P = tuple(map(Fraction, ('2', '2', '3', '4', '6', '8', '61/5', '18', '126/5', '115/3')))
EXPECTED_OPT = (1, 2, 3, 3, 9, 24, 56, 24, 1260, 480)


def source_words(n, k):
    return tuple(''.join(b) for b in itertools.product('01', repeat=n)
                 if b.count('1') == k and all(not (b[i] == b[i+1] == '1') for i in range(n-1)))


def swap_ball(w):
    result = {w}  # at most one swap: the no-error output is essential
    for i in range(len(w)-1):
        if w[i] != w[i+1]:
            result.add(w[:i]+w[i+1]+w[i]+w[i+2:])
    return result  # outputs containing 11 ARE allowed


def get_graph(words, balls):
    return tuple(sum(1 << j for j in range(len(words))
                     if j != i and not balls[i].isdisjoint(balls[j]))
                 for i in range(len(words)))


def optimum_size_and_count(graph):
    n = len(graph)
    @lru_cache(maxsize=None)
    def solve(mask):
        if mask == 0:
            return (0, 1)
        v = mask & -mask
        i = v.bit_length() - 1
        without_size, without_count = solve(mask ^ v)
        with_size, with_count = solve(mask & ~(v | graph[i]))
        with_size += 1
        if with_size > without_size:
            return (with_size, with_count)
        if without_size > with_size:
            return (without_size, without_count)
        return (with_size, with_count + without_count)
    return solve((1 << n) - 1)


def optimum_masks(graph):
    @lru_cache(maxsize=None)
    def solve(mask):
        if mask == 0:
            return (0, (0,))
        bit = mask & -mask
        i = bit.bit_length() - 1
        skip_val, skip_masks = solve(mask ^ bit)
        take_val, take_masks = solve(mask & ~(bit | graph[i]))
        take_val += 1
        best = max(skip_val, take_val)
        masks = ((skip_masks if skip_val == best else ()) +
                 (tuple(m | bit for m in take_masks) if take_val == best else ()))
        return best, masks
    return solve((1 << len(graph)) - 1)


def check_certificate(part):
    n, k = part['n'], part['k']
    words = source_words(n, k)
    assert len(words) == part['source_count']
    balls = tuple(swap_ball(w) for w in words)
    outputs = set().union(*balls)
    graph = get_graph(words, balls)
    ans, count = optimum_size_and_count(graph)
    assert (ans, count) == (part['max_code'], part['optimal_codebooks']), (n, k, ans, count)
    code = part['integer_code']
    assert len(code) == ans and len(set(code)) == ans and set(code) <= set(words)
    assert all(swap_ball(a).isdisjoint(swap_ball(b))
               for i, a in enumerate(code) for b in code[i+1:]), (n,k,'code is not disjoint')

    p = {w: Fraction(x) for w, x in part['x'].items()}
    q = {v: Fraction(y) for v, y in part['y'].items()}
    assert p.keys() <= set(words) and q.keys() <= outputs
    assert all(value > 0 for value in p.values()) and all(value > 0 for value in q.values())
    assert all(sum((p.get(w, Fraction(0)) for w, b in zip(words, balls) if out in b), Fraction(0)) <= 1
               for out in outputs), (n,k,'primal infeasible')
    assert all(sum((q.get(out, Fraction(0)) for out in ball), Fraction(0)) >= 1
               for ball in balls), (n,k,'dual infeasible')
    primal_total = sum(p.values(), Fraction(0))
    dual_total = sum(q.values(), Fraction(0))
    assert primal_total == dual_total == Fraction(part['fractional_optimum']), (n,k,'duality')
    return ans, count, primal_total, graph, words


def reversal_fixed_optimal(graph, words):
    best, masks = optimum_masks(graph)
    reversals = tuple(words.index(w[::-1]) for w in words)
    fixed = sum(1 for mask in masks if mask == sum(1 << reversals[i]
                 for i in range(len(words)) if mask & (1 << i)))
    return len(masks), fixed


def main():
    cert = json.loads((Path(__file__).resolve().parent / 'certificate.json').read_text(encoding='utf-8'))
    got_parts = {(part['n'],part['k']): part for part in cert['parts']}
    assert len(got_parts) == len(cert['parts']) == 40
    total_m=[]; total_p=[]; total_count=[]
    for n in range(1,11):
        m=0; p=Fraction(0); count=1; fixed_count=1
        for k in range((n+1)//2+1):
            part=got_parts[(n,k)]
            a,b,fract,graph,words=check_certificate(part)
            m+=a;count*=b;p+=fract
            if n in (7,8):
                optimums, fixed = reversal_fixed_optimal(graph, words)
                assert optimums == b
                fixed_count *= fixed
        total_m.append(m); total_p.append(p); total_count.append(count)
        if n == 7:
            assert count==56 and fixed_count==4 and (count+fixed_count)//2==30
        if n == 8:
            assert count==24 and fixed_count==0 and count//2==12
    assert tuple(total_m)==EXPECTED_M, total_m
    assert tuple(total_p)==EXPECTED_P, total_p
    assert tuple(total_count)==EXPECTED_OPT, total_count
    print('VERIFY_OK')
    for n,(m,p,count) in enumerate(zip(total_m,total_p,total_count),1):
        print(n, m, p, count)
    print('REVERSAL_COUNTS n=7: 56 optimal, 4 fixed, 30 classes; n=8: 24 optimal, 0 fixed, 12 classes')


if __name__=='__main__':
    main()
