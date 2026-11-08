"""Finite verification for modal-root profiles in loopless directed graphs.

Run: python3 checker.py
Only the finite checks in this file are computational claims.
"""
from fractions import Fraction
from itertools import product


def statuses(out, root):
    n = len(out)
    children = out[root]
    serial = bool(children)
    symmetric = all(root in out[u] for u in children)
    transitive = all(out[u] <= children for u in children)
    euclidean = not bool(children)  # Loopless frames.
    # The McKinsey implication must hold for ALL valuations.
    mck = True
    for mask in range(1 << n):
        P = {v for v in range(n) if (mask >> v) & 1}
        premise = all(bool(out[u] & P) for u in children)
        conclusion = any(out[u] <= P for u in children)
        if premise and not conclusion:
            mck = False
            break
    return serial, symmetric, transitive, euclidean, mck


def profile(out, root):
    kids = out[root]
    if not kids:
        return 0
    d = [len(out[u]) for u in kids]
    if all(t == 0 for t in d):
        return 1
    if any(t <= 1 for t in d):
        return 2
    return 3


def profile_status(j):
    return [(False, True, True, True, False),
            (True, False, True, False, True),
            (True, False, False, False, True),
            (True, False, False, False, False)][j]


def closed_form(n):
    p = Fraction(1, 2)
    a0 = (1-p)**(n-1)
    a1 = (n-1)*p*(1-p)**(n-2)
    s = (1-p)**(n-1)
    t = (1-p*(1-a0))**(n-1)
    u = (1-p*(a0+a1))**(n-1)
    return [s, t-s, 1-t-u+s, u-s]


def enumerate_graphs(n):
    arcs = [(u,v) for u in range(n) for v in range(n) if u != v]
    cnt = [0]*4
    exceptional = 0
    for bits in range(1<<len(arcs)):
        out = [set() for _ in range(n)]
        for i, (u,v) in enumerate(arcs):
            if (bits>>i)&1:
                out[u].add(v)
        for root in range(n):
            j=profile(out,root)
            cnt[j]+=1
            st=statuses(out,root)
            if st != profile_status(j):
                exceptional+=1
    denom = n*(1<<len(arcs))
    return [Fraction(x,denom) for x in cnt], exceptional, denom

for n in (2,3,4):
    observed, exceptions, denom = enumerate_graphs(n)
    assert observed == closed_form(n), (n,observed,closed_form(n))
    print('n',n,'ideal profile probabilities',','.join(map(str,observed)),
          'actual exceptions',exceptions,'/',denom)

# Directly check the set-family characterization of the McKinsey axiom.
for n in (3,4):
    arcs = [(u,v) for u in range(n) for v in range(n) if u!=v]
    for bits in range(1<<len(arcs)):
        out=[set() for _ in range(n)]
        for i,(u,v) in enumerate(arcs):
            if (bits>>i)&1: out[u].add(v)
        for w in range(n):
            children=out[w]
            no_potential_counterexample = not children or any(len(out[u])<=1 for u in children)
            if not no_potential_counterexample:
                ground=set().union(*(out[u] for u in children))
                # The definition is: nonempty P meeting every successor set,
                # while containing none of them.
                has_two_coloring=False
                for pmask in range(1<<n):
                    P={v for v in range(n) if (pmask>>v)&1}
                    if all(bool(P&out[u]) and bool(out[u]-P) for u in children):
                        has_two_coloring=True
                        break
                expected=not has_two_coloring
            else:
                expected=bool(children)
            assert statuses(out,w)[4] == expected
print('ALL_MODAL_ROOT_CHECKS_OK')

# Nonasymptotic discrepancy estimate, with exact weighted enumeration.
n=4
p=Fraction(1,10)
arcs=[(u,v) for u in range(n) for v in range(n) if u!=v]
weighted_bad=Fraction(0)
for bits in range(1<<len(arcs)):
    out=[set() for _ in range(n)]
    for i,(u,v) in enumerate(arcs):
        if (bits>>i)&1:out[u].add(v)
    count_bad=sum(statuses(out,w)!=profile_status(profile(out,w)) for w in range(n))
    weighted_bad+=p**bits.bit_count()*(1-p)**(len(arcs)-bits.bit_count())*count_bad/n
bound=(n-1)*p*p+(n-1)*(n-2)*p**3+Fraction((n-1)*(n-2)**2,2)*p**4
assert weighted_bad <= bound
print('EXACT_EXCEPTION_PROBABILITY',weighted_bad,'PROVED_BOUND',bound)
