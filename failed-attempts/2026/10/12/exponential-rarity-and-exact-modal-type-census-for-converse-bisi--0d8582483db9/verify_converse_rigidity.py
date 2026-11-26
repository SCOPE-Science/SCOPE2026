#!/usr/bin/env python3
"""Independent finite checks of a two-relation bisimulation-rigidity count."""
from itertools import product
from math import comb, factorial


def frame(q, h):
    paths = [()]
    for depth in range(h):
        paths += [p + (i,) for p in paths if len(p) == depth for i in range(q)]
    ids = {p: i for i, p in enumerate(paths)}
    children = [tuple(ids[p+(i,)] for i in range(q)) if len(p)<h else () for p in paths]
    parents = [() if not p else (ids[p[:-1]],) for p in paths]
    return paths, children, parents


def bisimulation_classes(colors, children, parents):
    """Compute greatest bisimulation of a finite two-modal graph by refinement."""
    distinct = {c: i for i,c in enumerate(sorted(set(colors)))}
    cls = tuple(distinct[c] for c in colors)
    while True:
        sig = [(colors[i], frozenset(cls[j] for j in children[i]),
                frozenset(cls[j] for j in parents[i])) for i in range(len(colors))]
        unique = {s: i for i,s in enumerate(dict.fromkeys(sig))}
        nxt = tuple(unique[s] for s in sig)
        if nxt == cls:
            return len(unique)
        cls = nxt


def sibling_forward_types(colors, children):
    types = [None] * len(colors)
    for i in reversed(range(len(colors))):
        types[i] = (colors[i], frozenset(types[j] for j in children[i]))
    return all(len({types[j] for j in children[i]}) == len(children[i])
               for i in range(len(colors)))


def exact(q,a,h):
    n=(q**(h+1)-1)//(q-1)
    r=a
    for _ in range(h):
        r = a*comb(r,q) if r>=q else 0
    return r*factorial(q)**((q**h-1)//(q-1)), n


def run():
    experiments = [(2,2,0),(2,2,1),(2,2,2),(2,2,3),
                   (2,3,2),(2,1,2),(3,3,1),(3,2,1),(3,4,1)]
    total = 0
    for q,a,h in experiments:
        paths, children, parents=frame(q,h)
        expected,n=exact(q,a,h)
        assert len(paths)==n
        good=0
        for colors in product(range(a),repeat=n):
            quotient=bisimulation_classes(colors, children, parents)
            sibling_condition=sibling_forward_types(colors, children)
            assert (quotient==n)==sibling_condition, (q,a,h,colors)
            good += quotient==n
        assert good==expected, (q,a,h,good,expected)
        total+=a**n
        print(f'CHECK q={q} a={a} h={h} tested={a**n} rigid={good}')
    print('VERIFY_OK',len(experiments),'parameter_cases',total,
          'exhaustive_colorings; independent greatest-bisimulation refinement')
if __name__=='__main__':run()
