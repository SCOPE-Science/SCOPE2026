#!/usr/bin/env python3
"""Exact direct test of square-zero pairwise-commuting sl_2 truncated-series tuples.
Only uses elementary integer arithmetic and finite enumeration. No outside packages.
"""
from itertools import product

def expected(q,m,r):
    b=(q+1)*(q**r-1)
    return q**(3*r*(m//2)) + b*sum(q**(3*r*j+(m-2*j-1)*(r+1)) for j in range((m-1)//2+1))

def mul(x,y,q,m):
    out=[0]*m
    for i in range(m):
        for j in range(m-i):out[i+j]=(out[i+j]+x[i]*y[j])%q
    return tuple(out)

def iszero(x):return not any(x)

def enumerate_tuples(q,m,r):
    S=[tuple(z) for z in product(range(q),repeat=m)]
    triples=list(product(S, repeat=3))
    squares=[]
    for a,b,c in triples:
        if iszero(tuple((x+y)%q for x,y in zip(mul(a,a,q,m),mul(b,c,q,m)))):
            squares.append((a,b,c))
    # [X,Y] in trace-zero variables has coordinates b*c'-c*b', 2(a*b'-a'*b), etc; odd q:
    def commute(x,y):
        a,b,c=x;d,e,f=y
        be=mul(b,f,q,m); cf=mul(c,e,q,m)
        ae=mul(a,e,q,m); db=mul(d,b,q,m)
        cd=mul(c,d,q,m); fa=mul(f,a,q,m)
        return all((u-v)%q==0 for u,v in zip(be,cf)) and all((u-v)%q==0 for u,v in zip(ae,db)) and all((u-v)%q==0 for u,v in zip(cd,fa))
    n=0
    neighbors=[]
    for i,x in enumerate(squares):
        neighbors.append([j for j,y in enumerate(squares) if commute(x,y)])
    if r==2:n=sum(map(len,neighbors))
    if r==3:
        sets=[set(x) for x in neighbors]
        n=sum(len([k for k in neighbors[j] if k in sets[i]]) for i in range(len(squares)) for j in neighbors[i])
    return n,len(squares)

def main():
    cases=[(3,1,2),(3,1,3),(5,1,2),(3,2,2),(3,2,3),(5,2,2),(3,3,2)]
    for q,m,r in cases:
        seen, square = enumerate_tuples(q,m,r)
        target=expected(q,m,r)
        print(f'q={q} m={m} r={r}: squarezero={square}, actual={seen}, predicted={target}, {"PASS" if seen==target else "FAIL"}',flush=True)
        assert seen==target
    print('ALL_SL2_ARC_TESTS_PASS')
if __name__=='__main__':main()
