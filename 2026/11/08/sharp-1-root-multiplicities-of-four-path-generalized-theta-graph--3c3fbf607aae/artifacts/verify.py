#!/usr/bin/env python3
"""Independent exact checks for four-path theta independence polynomials."""
from functools import lru_cache
from itertools import combinations_with_replacement
from math import isqrt

@lru_cache(None)
def path(n):
    if n in (-1, 0):
        return (1,)
    if n == 1:
        return (1, 1)
    a,b=path(n-1),path(n-2)
    return tuple((a[j] if j<len(a) else 0)+ (b[j-1] if 0<=j-1<len(b) else 0)
                 for j in range(max(len(a),len(b)+1)))

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def theta_formula(lengths):
    out=[0]
    for shift, factor in ((0,1),(1,2),(2,1)):
        part=[1]
        for l in lengths:
            part=multiply(part,path(l-1-shift))
        if len(out)<len(part)+shift:
            out.extend([0]*(len(part)+shift-len(out)))
        for j,v in enumerate(part):
            out[j+shift]+=factor*v
    while len(out)>1 and out[-1]==0:
        out.pop()
    return tuple(out)

def taylor_coefficient(poly, order):
    from math import comb
    return sum(coef*comb(j,order)*((-1)**(j-order))
               for j,coef in enumerate(poly) if j>=order)

def order_at_minus_one(poly):
    for j in range(len(poly)):
        if taylor_coefficient(poly,j): return j
    raise AssertionError('zero polynomial')

def predicted_order(lengths):
    groups={i:[] for i in range(3)}
    for l in lengths: groups[l%3].append(l)
    if min(map(len,groups.values()))==0:return 0
    if sorted(map(len,groups.values()))==[1,1,2] and len(groups[0])==2:
        (a,b)=groups[0]
        m,n=a//3,b//3
        p=(groups[1][0]-1)//3
        q=(groups[2][0]-2)//3
        if p==q+1:
            Q=q*q-(m+n)*q-(m+n+2*m*n+1)
            return 3 if Q==0 else 2
    return 1

def graph_edges(lengths):
    # Ends 0 and 1, internal vertices unique on each path.
    edges=[];next_id=2
    for ell in lengths:
        interior=list(range(next_id,next_id+ell-1))
        next_id+=ell-1
        chain=[0]+interior+[1]
        edges.extend(zip(chain,chain[1:]))
    return next_id,edges

def graph_polynomial(lengths):
    n,edges=graph_edges(lengths)
    nbr=[0]*n
    for u,v in edges:
        nbr[u]|=1<<v; nbr[v]|=1<<u
    @lru_cache(None)
    def recur(mask):
        if not mask: return (1,)
        bit=mask&-mask;v=bit.bit_length()-1
        no=recur(mask^bit); yes=recur(mask&~(bit|nbr[v]))
        return tuple((no[i] if i<len(no) else 0)+(yes[i-1] if 0<=i-1<len(yes) else 0)
                     for i in range(max(len(no),len(yes)+1)))
    return recur((1<<n)-1)

def verify():
    # Independent construction of the graph and deletion-contraction polynomial.
    instances=0
    for lengths in combinations_with_replacement(range(2,7),4):
        if sum(lengths)>20:continue
        actual=graph_polynomial(lengths)
        assert actual==theta_formula(lengths),(lengths,actual,theta_formula(lengths))
        instances+=1
    print('DIRECT_GRAPH_INDEPENDENT_SET_POLYNOMIAL_OK',instances)
    # Exhaustive parameter-residue classification on a large finite grid.
    instances=0
    for lengths in combinations_with_replacement(range(2,20),4):
        poly=theta_formula(lengths)
        got=order_at_minus_one(poly)
        expected=predicted_order(lengths)
        assert got==expected,(lengths,got,expected)
        instances+=1
    print('FOUR_PATH_ORDER_CLASSIFICATION_OK',instances)
    # Reproduce the symbolic coefficients of the exceptional configuration.
    for m in range(1,9):
      for n in range(m,9):
       for q in range(0,18):
        lengths=(3*m,3*n,3*q+4,3*q+2)
        poly=theta_formula(lengths)
        sign=(-1)**(m+n+(q+1)+q)
        assert taylor_coefficient(poly,0)==taylor_coefficient(poly,1)==0
        Q=q*q-(m+n)*q-(m+n+2*m*n+1)
        assert taylor_coefficient(poly,2)==sign*Q,(lengths,'quadratic')
        if Q==0:
            R=-2*(m*n+(m+n)*q+(m+n)+q+1)
            assert taylor_coefficient(poly,3)==sign*R,(lengths,'cubic')
            assert R<0
    print('EXCEPTIONAL_TAYLOR_COEFFICIENTS_OK')
    for t in range(1,15):
        lengths=(3*t,6*t+6,12*t+13,12*t+11)
        assert order_at_minus_one(theta_formula(lengths))==3
    assert order_at_minus_one(theta_formula((3,3,4,2)))==2
    assert order_at_minus_one(theta_formula((3,12,25,23)))==3
    print('INFINITE_FAMILY_FIRST_VALUES_OK t=1..14')
    # The first triple root among all length>=2 four-path thetas.
    # Any repeated-root parameterization has N=3(m+n+2q)+4 vertices.
    for m in range(1,20):
      for n in range(1,20):
       for q in range(20):
        if 3*(m+n+2*q)+4 < 61:
            assert q*q != (m+n)*q+m+n+2*m*n+1
    print('SHARP_61_VERTEX_TRIPLE_ROOT_BOUND_OK')
    print('VERIFY_OK')

if __name__=='__main__': verify()
