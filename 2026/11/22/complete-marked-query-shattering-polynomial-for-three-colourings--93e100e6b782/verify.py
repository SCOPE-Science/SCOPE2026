#!/usr/bin/env python3
"""Independent finite check of three-colour query shattering on bistar trees.

Only Python standard library. Run: python3 verify.py
"""
from itertools import product
from math import comb

COLORS = range(3)


def poly_add(*items):
    n = max(map(len, items))
    return [sum(p[i] if i < len(p) else 0 for p in items) for i in range(n)]


def poly_mul(p,q):
    r = [0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            r[i+j] += x*y
    return r


def poly_scale(p,s):
    return [s*x for x in p]


def poly_shift(p,i):
    return [0]*i+p


def formula(a,b):
    X = lambda n:[comb(n,k) for k in range(n+1)]
    Y = lambda n:[comb(n,k)*2**k for k in range(n+1)]
    xa,xb,ya,yb=X(a),X(b),Y(a),Y(b)
    one=[1]
    La=poly_add(one,poly_scale(ya,3),poly_scale(xa,-3))
    Lb=poly_add(one,poly_scale(yb,3),poly_scale(xb,-3))
    Da=poly_add(ya,poly_scale(xa,-2),one)
    Db=poly_add(yb,poly_scale(xb,-2),one)
    F00=poly_add(poly_mul(La,Lb),poly_scale(poly_mul(Da,Db),-3))
    F10=poly_add(poly_scale(poly_mul(xa,poly_add(xb,yb,[-1])),6),poly_scale(xb,-9),[6])
    F01=poly_add(poly_scale(poly_mul(xb,poly_add(xa,ya,[-1])),6),poly_scale(xa,-9),[6])
    F11=poly_scale(poly_add(xa,xb,[-1]),6)
    z=poly_add(F00,poly_shift(poly_add(F10,F01),1),poly_shift(F11,2))
    while z and z[-1]==0:z.pop()
    return z


def colorings(a,b):
    # Vertex 0 = left hub, 1 = right hub, leaves 2..a+1 and a+2..a+b+1.
    for c0 in COLORS:
        for c1 in COLORS:
            if c0==c1:continue
            for left in product([i for i in COLORS if i!=c0],repeat=a):
                for right in product([i for i in COLORS if i!=c1],repeat=b):
                    yield (c0,c1)+left+right


def full_trace(a,b):
    cls=list(colorings(a,b));n=a+b+2
    yes={}
    full=(1<<len(cls))-1
    for v in range(n):
        for t in COLORS:
            yes[(v,t)]=sum(1<<j for j,cs in enumerate(cls) if cs[v]==t)
    hist=[0]*(n+1); tested=0; mismatches=0
    for choices in product(range(4),repeat=n):
        queries=[(v,ch-1) for v,ch in enumerate(choices) if ch>0]
        active=[full]
        for q in queries:
            s=yes[q]
            nxt=[]
            for cmask in active:
                neg=cmask & (full^s)
                pos=cmask & s
                if not neg or not pos:
                    nxt=[];break
                nxt.extend((neg,pos))
            active=nxt
            if not active:break
        passes=bool(active)
        if passes:hist[len(queries)]+=1
        # Separate three-colour centre feasibility, tested against raw full trace.
        U={t for v,t in queries if 2<=v<2+a}
        V={t for v,t in queries if 2+a<=v}
        p=next((t for v,t in queries if v==0),None)
        q=next((t for v,t in queries if v==1),None)
        center_pairs=[(x,y) for x in COLORS for y in COLORS if x!=y and x not in U and y not in V]
        bits={(int(x==p) if p is not None else 0,int(y==q) if q is not None else 0) for x,y in center_pairs}
        k=(int(p is not None)+int(q is not None))
        predicted=len(bits)==(1<<k)
        if predicted!=passes:
            mismatches+=1;raise AssertionError(('profile error',a,b,choices,predicted,passes))
        tested+=1
    want=formula(a,b)
    assert hist[:len(want)]==want,(a,b,hist,want)
    assert all(x==0 for x in hist[len(want):])
    top=6*(2**a+2**b+2+int(a==1)+int(b==1))
    assert want[a+b+1]==top,(a,b,want[-1],top)
    assert len(cls)==6*2**(a+b)
    return tested,hist,len(cls),mismatches


def main():
    cases=[(1,1),(1,2),(2,1),(1,3),(2,2),(1,4),(2,3),(3,2),(1,5),(2,4),(3,3)]
    num=0
    for a,b in cases:
        t,h,c,m=full_trace(a,b)
        num+=t
        print(f'PASS a={a} b={b} queries={t} colourings={c} polynomial={h[:a+b+2]}')
    print(f'PASS {len(cases)} trees, {num} complete query-support profiles; full traces, centre profile, all coefficients, and top coefficient agree.')
    for a in range(1,12):
        for b in range(1,12):
            p=formula(a,b)
            assert len(p)==a+b+2 and p[-1]==6*(2**a+2**b+2+(a==1)+(b==1))
            assert p[0]==1 and p[1]==3*(a+b+2)
            assert all(x>=0 for x in p)
    print('PASS additional 121 exact-integer polynomial/top-coefficient arithmetic checks (not an infinite proof).')

if __name__=='__main__':main()
