"""Exact finite graph certificate for two mod-three lag recurrence multipliers."""
from itertools import product

EXPECTED = {
6: {
 '000000': ('000000', '111111'),
 '000111': (),
 '001011': ('000111',),
 '001101': ('000111',),
 '010101': (),
 '111111': (),
},
7: {
 '0000000': ('0000000',),
 '0000111': ('0111111',),
 '0001011': ('0000111','0111111'),
 '0001101': ('0000111','0111111'),
 '0010011': ('0111111',),
 '0010101': (),
 '0111111': (),
}}

def canon(s):
    return min(s[i:] + s[:i] for i in range(len(s)))

def mask(seq):
    return ''.join('1' if v else '0' for v in seq)

def graph_from_binary(m):
    edges = {}
    for B in product((0,1), repeat=m):
        if sum(B) % 3: continue
        key=canon(mask(B))
        edges.setdefault(key,set())
        for first in range(3):
            Y=[first]
            for i in range(1,m):
                Y.append((Y[-1]+B[i])%3)
            if (Y[0]-Y[-1])%3 != B[0]:
                continue
            if sum(z!=0 for z in Y)%3==0:
                edges[key].add(canon(mask(Y)))
    return {key:tuple(sorted(val)) for key,val in sorted(edges.items())}

def graph_from_ternary(m):
    edges={}
    for B in product((0,1),repeat=m):
        if sum(B)%3==0:
            edges.setdefault(canon(mask(B)),set())
    for Y in product((0,1,2),repeat=m):
        D=tuple((Y[j]-Y[j-1])%3 for j in range(m))
        if any(z==2 for z in D):continue
        B=mask(D)
        V=mask(Y)
        if V.count('1')%3==0:
            edges[canon(B)].add(canon(V))
    return {key:tuple(sorted(val)) for key,val in sorted(edges.items())}

def no_nonzero_cycle(graph):
    remaining=set(graph)-{'0'*len(next(iter(graph)))}
    while remaining:
        leaves={v for v in remaining if not (set(graph[v])&remaining)}
        if not leaves:return False
        remaining-=leaves
    return True

def direct_fix_count(k,m):
    count=0
    for state in product((0,1,2),repeat=k):
        v=state
        for _ in range(m*k):
            v=v[1:]+((v[0]+(v[-1]!=0))%3,)
        count += (v==state)
    return count

def main():
    for m in (6,7):
        a=graph_from_binary(m)
        b=graph_from_ternary(m)
        assert a==b==EXPECTED[m],(m,a,b)
        assert no_nonzero_cycle(a)
        print('MASK_GRAPH_OK',m,'classes',len(a),'nonzero_cycles',0)
        for key, val in a.items():print(key,'->',','.join(val) if val else '(none)')
    states=0
    for k in range(2,10):
        for m in (6,7):
            assert direct_fix_count(k,m)==1,(k,m)
        states+=3**k
    assert direct_fix_count(2,8)==9
    assert direct_fix_count(2,2)==1  # only zero has period dividing four
    print('DIRECT_STATES_OK k=2..9 states_per_multiplier',states,'fixed_6k=fixed_7k=1')
    print('SHARP_ENDPOINT_OK k=2 fixed_8k=9')
    print('VERIFY_OK exact_integer=yes independent_binary_ternary_automata=yes finite_state_k=2..9')
if __name__=='__main__':main()
