#!/usr/bin/env python3
"""Exact classification of smooth (4,3) filling curves on P1 x P1 over F2.
Requires Python 3 and sympy. All tests are exhaustive or symbolic.

Coefficient bit 4*i+j represents X0^(4-i) X1^i Y0^(3-j) Y1^j.
The two factors have ordered rulings; transformations are GL2(F2)^2.
"""
import itertools
import collections
import math
from sympy import Poly, groebner, symbols

D, E = 4, 3
MONS = list(itertools.product(range(5), range(4)))
P1 = [(1,0), (0,1), (1,1)]
x,y=symbols('x y')

def kernel_rref(rows, n):
    a=list(rows); r=0; piv=[]
    for c in range(n):
        k=next((i for i in range(r,len(a)) if (a[i]>>c)&1),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        for i in range(len(a)):
            if i!=r and (a[i]>>c)&1: a[i]^=a[r]
        piv.append(c);r+=1
        if r==len(a):break
    free=[i for i in range(n) if i not in piv]
    basis=[]
    for c in free:
        z=1<<c
        for j,pc in enumerate(piv):
            if (a[j]>>c)&1: z|=1<<pc
        basis.append(z)
    return basis,piv

def filling_space():
    rows=[]
    for X,Y in itertools.product(P1,repeat=2):
        rows.append(sum(1<<k for k,(i,j) in enumerate(MONS)
              if (X[0]**(4-i)*X[1]**i*Y[0]**(3-j)*Y[1]**j)%2))
    b,p=kernel_rref(rows,20)
    F=[0]
    for v in b: F += [z^v for z in F]
    assert len(p)==9 and len(b)==11 and len(F)==2048
    assert all(all((row & f).bit_count()%2==0 for row in rows) for f in F)
    return F

def gl2():
    return [g for g in itertools.product((0,1),repeat=4)
            if (g[0]*g[3]+g[1]*g[2])%2]

def mult(p,q):
    o={}
    for i in p:
        for j in q: o[i+j]=o.get(i+j,0)^1
    return {e:1 for e,c in o.items() if c}

def linear_power(a,b,k):
    p={0:1}
    for _ in range(k):p=mult(p,{i:1 for i,z in enumerate((a,b)) if z})
    return p

def action(g,h):
    X=[mult(linear_power(g[0],g[1],4-i),linear_power(g[2],g[3],i)) for i in range(5)]
    Y=[mult(linear_power(h[0],h[1],3-j),linear_power(h[2],h[3],j)) for j in range(4)]
    return [sum(1<<(4*u+v) for u in X[i] for v in Y[j]) for i,j in MONS]

def substitute(f,columns):
    out=0
    while f:
        b=f&-f; f-=b
        out^=columns[b.bit_length()-1]
    return out

def smooth(f,order='grevlex'):
    for a,b in itertools.product((0,1),repeat=2):
        expr=sum(x**(i if a==0 else 4-i)*y**(j if b==0 else 3-j)
                 for k,(i,j) in enumerate(MONS) if (f>>k)&1)
        p=Poly(expr,x,y,modulus=2)
        G=groebner([p,p.diff(x),p.diff(y)],x,y,order=order,modulus=2)
        if len(G.polys)!=1 or not G.polys[0].is_one:
            return False
    return True

IRR={1:3,2:7,3:11,4:19,5:37,6:67}
def mul(a,b,n):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&(1<<n):a^=IRR[n]
    return z

def counts(f,n):
    q=1<<n
    P=[(1,i) for i in range(q)]+[(0,1)]
    def powers(t):
        a,b=t
        aa=[1];bb=[1]
        for _ in range(4):
            aa.append(mul(aa[-1],a,n));bb.append(mul(bb[-1],b,n))
        return aa,bb
    X=[];Y=[]
    for t in P:
        aa,bb=powers(t)
        X.append([mul(aa[4-i],bb[i],n) for i in range(5)])
        Y.append([mul(aa[3-j],bb[j],n) for j in range(4)])
    terms=[(i,j) for k,(i,j) in enumerate(MONS) if (f>>k)&1]
    return sum(not (lambda a,b: __import__('functools').reduce(
            int.__xor__,(mul(a[i],b[j],n) for i,j in terms),0))(A,B)
            for A in X for B in Y)

def weil_poly(N):
    g=6;q=2;c=[1]
    for n in range(1,g+1):
        s=sum((N[i-1]-1-q**i)*c[n-i] for i in range(1,n+1))
        assert s%n==0
        c.append(s//n)
    c.extend(q**(g-i)*c[i] for i in range(g-1,-1,-1))
    return c

def mat_mult(g,h):
    a,b,c,d=g; A,B,C,D=h
    return ((a*A+b*C)&1,(a*B+b*D)&1,(c*A+d*C)&1,(c*B+d*D)&1)

def order(g):
    p=(1,0,0,1)
    for n in range(1,7):
        p=mat_mult(p,g)
        if p==(1,0,0,1):return n
    raise AssertionError('no order')

EXPECTED={
    396246: (6, {1:1,2:1,3:2,6:2}, [9,9,9,9,69,51], [1,6,20,48,90,144,211,288,360,384,320,192,64]),
    399606: (18,{1:1,2:1},[9,9,9,21,39,39],[1,6,20,48,93,156,233,312,372,384,320,192,64]),
    404886: (36,{1:1},[9,9,12,17,24,78],[1,6,20,49,98,167,250,334,392,392,320,192,64]),
    420790: (6,{1:1,2:3,3:2},[9,11,9,23,9,53],[1,6,21,54,114,204,313,408,456,432,336,192,64])
}

def main():
    forms=filling_space();G=gl2();maps=[action(a,b) for a in G for b in G]
    assert len(G)==6 and len(maps)==36
    for f in forms:
        for M in maps:
            assert substitute(f,M) in forms
    seen=set();orbit_sizes=collections.Counter();smooth_reps={}
    for f in sorted(forms[1:]):
        if f in seen:continue
        O={substitute(f,M) for M in maps}
        assert f==min(O) and not(O&seen)
        seen.update(O); orbit_sizes[len(O)]+=1
        if smooth(f):
            stab=[(g,h) for g in G for h in G if substitute(f,action(g,h))==f]
            oh=dict(collections.Counter(math.lcm(order(g),order(h)) for g,h in stab))
            ns=[counts(f,n) for n in range(1,7)]
            pol=weil_poly(ns)
            smooth_reps[f]=(len(O),oh,ns,pol)
            print('CLASS',f,'size',len(O),'stabilizer_orders',oh,'points',ns,'weil',pol)
    assert len(seen)==2047
    assert sum(v for k,v in orbit_sizes.items())==99
    assert smooth_reps==EXPECTED,(smooth_reps,EXPECTED)
    assert sum(z[0] for z in smooth_reps.values())==66
    # The explicit Homma--Kim (4,3) example belongs to the second class.
    hk=429846
    assert min(substitute(hk,M) for M in maps)==399606
    assert len({tuple(z[3]) for z in smooth_reps.values()})==4
    print('BIDEGREE43_FILLING_PASS 2048 99 66 4')

if __name__=='__main__':main()
