#!/usr/bin/env python3
"""Direct finite-ring enumeration of prescribed Heisenberg commutator fibers."""
from collections import Counter
from itertools import product


def equal_characteristic(q, d):
    # The square-zero extension F_q[e_1,...,e_d]/(e_i e_j : all i,j).
    # The test implementation uses prime fields q=2,3,5.
    elements = list(product(range(q), repeat=d+1))
    index = {x:i for i,x in enumerate(elements)}
    def add(x,y):
        return tuple((u+v)%q for u,v in zip(x,y))
    def neg(x):
        return tuple((-u)%q for u in x)
    def mul(x,y):
        return (x[0]*y[0]%q,) + tuple((x[0]*y[i]+x[i]*y[0])%q for i in range(1,d+1))
    return f'F_{q}+square-zero ideal dimension {d}',q,d,elements,index,add,neg,mul


def mixed_characteristic():
    # Z/4[e]/(2e,e^2), maximal ideal (2,e) of F_2-dimension 2.
    elements = [(a,b) for a in range(4) for b in range(2)]
    index = {x:i for i,x in enumerate(elements)}
    def add(x,y):
        return ((x[0]+y[0])%4, (x[1]+y[1])%2)
    def neg(x):
        return ((-x[0])%4, (-x[1])%2)
    def mul(x,y):
        return ((x[0]*y[0])%4, ((x[0]%2)*y[1]+x[1]*(y[0]%2))%2)
    return 'Z/4[e]/(2e,e^2)',2,2,elements,index,add,neg,mul


def predicted(q,d,h,z_is_zero,z_in_radical):
    t=q**(d+1)
    v=q**d
    A=t**(4*h-1)
    B=t**(2*h-1)*v**(2*h)
    C=t**(2*h-1)*(v//q)**(2*h)
    if z_is_zero:
        return A+(q-1)*B+(t-q)*C
    if z_in_radical:
        return A+(q-1)*B-q*C
    return A-B


def run_one(case):
    name,q,d,R,index,add,neg,mul=case
    t=len(R)
    zero=index[tuple(0 for _ in R[0])]
    addition=[[index[add(x,y)] for y in R] for x in R]
    negatives=[index[neg(x)] for x in R]
    multiplication=[[index[mul(x,y)] for y in R] for x in R]
    out=[0]*t
    for a in range(t):
        for b in range(t):
            for c in range(t):
                bc=negatives[multiplication[b][c]]
                for dd in range(t):
                    z=addition[multiplication[a][dd]][bc]
                    out[z]+=1
    assert sum(out)==t**4
    for z,item in enumerate(R):
        radical = (item[0]%q == 0)
        assert out[z] == predicted(q,d,1,z==zero,radical),(name,z,out[z],predicted(q,d,1,z==zero,radical))
    print(f'PASS: {name}, |R|={t}, h=1, exhaustive {t**4} horizontal quadruples, {t} targets')
    rank_one=out[:]
    for h in (2,3):
        out2=[0]*t
        # Convolution builds rank h from the independently enumerated rank-one map.
        for i in range(t):
            for j in range(t):
                out2[addition[i][j]]+=out[i]*rank_one[j]
        out=out2
        assert sum(out)==t**(4*h)
        for z,item in enumerate(R):
            radical=(item[0]%q == 0)
            assert out[z]==predicted(q,d,h,z==zero,radical),(name,h,z,out[z],predicted(q,d,h,z==zero,radical))
        print(f'PASS: {name}, h={h}, exact convolution from independent enumeration, {t} targets')


if __name__=='__main__':
    for case in [equal_characteristic(2,1), equal_characteristic(2,2),
                 equal_characteristic(2,3), equal_characteristic(3,1),
                 equal_characteristic(3,2), equal_characteristic(5,1),
                 mixed_characteristic()]:
        run_one(case)
    # Structural comparator: the principal ring Z/8 has four output levels, unlike
    # the nonprincipal ring of the same order with a two-dimensional square-zero radical.
    z8=Counter((a*d-b*c)%8 for a,b,c,d in product(range(8),repeat=4))
    assert z8[0]==736 and sorted(z8.values())==[384,384,384,384,576,576,672,736]
    print('PASS: principal Z/8 comparison: zero-det 736 and four fiber sizes')
    print('PASS: all exhaustive tests and convolution comparisons')
