#!/usr/bin/env python3
"""Independent section-level smoothness census and point counts.
Uses lexicographic elimination on every form (no orbit reduction), and
alternative polynomial models for the extension fields.
Requires Python 3 and sympy.
"""
import itertools
import sympy as sp

mons=list(itertools.product(range(5),range(4)))
P=[(1,0),(0,1),(1,1)]
rows=[]
for (X,Y) in itertools.product(P,P):
    row=0
    for k,(i,j) in enumerate(mons):
        row|=((X[0]**(4-i)*X[1]**i*Y[0]**(3-j)*Y[1]**j)&1)<<k
    rows.append(row)

# Produce the kernel by brute force in 20 binary coefficients rather than RREF.
forms=[f for f in range(1<<20) if all((f&r).bit_count()%2==0 for r in rows)]
assert len(forms)==2048
x,y=sp.symbols('x y')

def smooth(f):
    for u,v in itertools.product((0,1),repeat=2):
        poly=sum(x**(4-i if u else i)*y**(3-j if v else j)
                 for k,(i,j) in enumerate(mons) if (f>>k)&1)
        F=sp.Poly(poly,x,y,modulus=2)
        G=sp.groebner([F,F.diff(x),F.diff(y)],y,x,order='lex',modulus=2)
        if len(G.polys)!=1 or not G.polys[0].is_one:return False
    return True

POLY={1:3,2:7,3:13,4:25,5:41,6:73}
def mul(a,b,n):
    z=0
    for i in range(n):
        if (b>>i)&1:z^=a<<i
    while z.bit_length()>n:z^=POLY[n]<<(z.bit_length()-n-1)
    return z

def powgf(a,k,n):
    z=1
    for _ in range(k):z=mul(z,a,n)
    return z

def points(f,n):
    q=1<<n
    R=[(1,z) for z in range(q)]+[(0,1)]
    terms=[(i,j) for k,(i,j) in enumerate(mons) if (f>>k)&1]
    def is_point(X,Y):
        s=0
        for i,j in terms:
            a=mul(powgf(X[0],4-i,n),powgf(X[1],i,n),n)
            b=mul(powgf(Y[0],3-j,n),powgf(Y[1],j,n),n)
            s^=mul(a,b,n)
        return s==0
    return sum(is_point(X,Y) for X in R for Y in R)

if __name__=='__main__':
    S=[f for f in forms[1:] if smooth(f)]
    assert len(S)==66
    rep=[396246,399606,404886,420790]
    assert all(f in S for f in rep)
    exact={396246:[9,9,9,9,69,51],399606:[9,9,9,21,39,39],
           404886:[9,9,12,17,24,78],420790:[9,11,9,23,9,53]}
    for f in rep:
        ns=[points(f,n) for n in range(1,7)]
        assert ns==exact[f]
        print('REP',f,'N1..N6',ns)
    print('BIDEGREE43_INDEPENDENT_PASS 2048 66 4')
