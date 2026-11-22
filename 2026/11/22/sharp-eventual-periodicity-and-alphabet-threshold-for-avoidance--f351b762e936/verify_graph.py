#!/usr/bin/env python3
"""Exact deterministic overlap-graph certificate and cycle/escape verification."""
from itertools import product


def good(t, orders):
    # Binary/ternary Parikh vectors computed by explicit symbol multiplicities.
    return all(any(t[i:i+r].count(c)!=t[i+r:i+2*r].count(c)
                   for c in set(t))
               for r in orders for i in range(len(t)-2*r+1))


def graph(alphabet, orders):
    width=2*max(orders)-1
    V=[''.join(p) for p in product(alphabet,repeat=width)
       if good(''.join(p),orders)]
    E={(v,v[1:]+c) for v in V for c in alphabet if good(v+c,orders)}
    return V,E

C=['00011','00111','01110','11100','11000','10001']
TAILS=[['00010','00100','01000'],['11101','11011','10111']]
V,E=graph('01',(2,3))
assert sorted(V)==sorted(C+sum(TAILS,[])),V
expected={(C[i],C[(i+1)%6]) for i in range(6)}
expected|={(t[i],t[i+1]) for t in TAILS for i in (0,1)}
assert E==expected, E^expected
# For lengths at least 5, allowed words correspond bijectively to walks.
v={s:1 for s in V}
assert sum(v.values())==12
values={5:12}
for n in range(6,101):
    v={t:sum(v[s] for s,u in E if u==t) for t in V}
    values[n]=sum(v.values())
assert (values[6],values[7])==(10,8)
assert all(values[n]==6 for n in range(8,101))

# Every returned path at vertex v can be concatenated in arbitrary order:
def return_paths(alphabet, orders, vertex, words):
    V,E=graph(alphabet,orders)
    assert vertex in V
    for word in words:
        st=vertex
        for c in word:
            t=st[1:]+c
            assert (st,t) in E,(st,t)
            st=t
        assert st==vertex

return_paths('012',(2,3),'00011',('100011','200011'))
return_paths('01',(2,),'000',('1000111000','1110001000'))
return_paths('01',(3,),'00011',('10000011','11100011'))
print('PASS: exact 12-state/10-edge binary graph, full walk count, three two-return certificates')
