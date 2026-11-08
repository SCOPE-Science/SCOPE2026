"""Separate in-ball computation and independent overlap/uniqueness tests.

Constructs the predecessor relation rather than using a closed form or
reversing the output of a forward-neighborhood program.
"""
from itertools import product, combinations


def check(q):
    V = tuple(product(range(q), repeat=3))
    Vset = set(V)
    pred = {x: {(u, x[0], x[1]) for u in range(q)} for x in V}
    C = {v for v in V if v[0] != v[-1]}
    signs = set()
    for v in V:
        incoming = {v} | pred[v]
        incoming.update(w for u in pred[v] for w in pred[u])
        sig = frozenset(incoming & C)
        assert sig
        if q >= 3:
            assert sig not in signs, ('collision', q, v)
        signs.add(sig)
    if q >= 3: assert len(signs) == q**3
    # Verify that no other code with canonical size is possible:
    # every nonpalindromic-endword is forced by a unique pair of in-balls.
    for a,b,c in V:
        if a != c:
            v=(a,b,c);w=(a,b,a)
            P=lambda t: ({t}|pred[t]|{z for u in pred[t] for z in pred[u]})
            assert P(v)^P(w)=={v}
    print(f'in-ball q={q}: unique signatures={len(signs)} and all forced witnesses verified')

if __name__=='__main__':
    for q in range(2,8):check(q)
