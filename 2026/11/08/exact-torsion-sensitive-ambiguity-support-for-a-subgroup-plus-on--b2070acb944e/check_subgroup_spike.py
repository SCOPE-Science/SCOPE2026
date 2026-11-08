"""Exact cyclotomic verification of subgroup-plus-impulse STFT support formulas.

Run with Python 3 and sympy. Every zero test is a polynomial congruence,
not floating-point thresholding. This finite test supplements a general proof.
"""
from itertools import product
from math import gcd, lcm
from sympy import Poly, ZZ, symbols, cyclotomic_poly

X = symbols('X')

def group_data(moduli):
    return list(product(*(range(m) for m in moduli)))

def add(u,v,moduli):
    return tuple((a+b)%m for a,b,m in zip(u,v,moduli))

def neg(u,moduli):
    return tuple(-a%m for a,m in zip(u,moduli))

def mul(n,u,moduli):
    return tuple(n*a%m for a,m in zip(u,moduli))

def ord_elem(u,moduli):
    return lcm(*(m//gcd(a,m) for a,m in zip(u,moduli)))

def quotient_order(y,H,moduli):
    for i in range(1,len(group_data(moduli))+1):
        if mul(i,y,moduli) in H:
            return i
    raise AssertionError

def phase_order(a,b):
    if b==0: return 2
    if a==0: return 1
    if abs(a)==abs(b): return 4
    return None

def predicted(moduli,H,y,a,b):
    G=group_data(moduli); n=len(G); h=len(H); q=n//h
    r=quotient_order(y,H,moduli)
    delta = (q//r if r%2==0 and a*a+b*b==h else 0)
    if r>2:
        return n+(h-1)*q+2*h*n-delta
    d=phase_order(a,b)
    coset={add(y,x,moduli) for x in H}
    lost=sum(n//ord_elem(x,moduli) for x in coset
             if d is not None and ord_elem(x,moduli)%d==0)
    return n+(h-1)*q+h*n-delta-lost

def exact_count(moduli,H,y,a,b):
    G=group_data(moduli); n=len(G); L=lcm(4,*moduli)
    phi=Poly(cyclotomic_poly(L,X),X,domain=ZZ)
    shift=L//4
    f={u: ((1,0) if u in H else ((a,b) if u==y else (0,0))) for u in G}
    ans=0
    for x in G:
        for k in G:
            coeffs={}
            for t in G:
                c=f[t]; d=f[add(t,neg(x,moduli),moduli)]
                real=c[0]*d[0]+c[1]*d[1]
                imag=c[1]*d[0]-c[0]*d[1]
                if not (real or imag): continue
                exponent=(-sum(ki*ti*(L//m) for ki,ti,m in zip(k,t,moduli)))%L
                coeffs[exponent]=coeffs.get(exponent,0)+real
                e=(exponent+shift)%L
                coeffs[e]=coeffs.get(e,0)+imag
            polynomial=Poly(sum(v*X**e for e,v in coeffs.items() if v),X,domain=ZZ)
            if not polynomial.rem(phi).is_zero:
                ans+=1
    return ans

cases=[
 ((4,),lambda u:u[0]%2==0,(1,)),
 ((6,),lambda u:u[0]%3==0,(1,)),
 ((6,),lambda u:u[0]%2==0,(1,)),
 ((8,),lambda u:u[0]%2==0,(1,)),
 ((12,),lambda u:u[0]%2==0,(1,)),
 ((2,2),lambda u:u[1]==0,(0,1)),
 ((2,4),lambda u:u[1]%2==0,(0,1)),
 ((3,3),lambda u:u[1]==0,(0,1)),
 ((4,3),lambda u:u[1]==0,(0,1)),
 ((4,2),lambda u:u[0]%2==0,(1,0)),
 ((2,2,2),lambda u:u[2]==0,(0,0,1)),
]
params=[(1,0),(0,1),(1,1),(1,-1),(2,0),(0,2),(2,1)]
if __name__=='__main__':
    assertions=0
    for mods,pred,y in cases:
        G=group_data(mods); H={u for u in G if pred(u)}
        assert len(H)>=2 and (0,)*len(mods) in H and y not in H
        for a,b in params:
            calc=exact_count(mods,H,y,a,b)
            expect=predicted(mods,H,y,a,b)
            assert calc==expect,(mods,H,y,a,b,calc,expect)
            assertions+=1
    # Direct exact algebraic check at the sharp binary equality case.
    from sympy import sqrt, I, simplify
    mods=(2,2); G=group_data(mods); H={(0,0),(1,0)}; y=(0,1)
    for z in (sqrt(2),I*sqrt(2)):
        val=0
        for x in G:
            for k in G:
                total=0
                for t in G:
                    u=add(t,neg(x,mods),mods)
                    ft=1 if t in H else z if t==y else 0
                    fu=1 if u in H else z if u==y else 0
                    total+=ft*fu.conjugate()*(-1)**sum(ki*ti for ki,ti in zip(k,t))
                val+=int(simplify(total)!=0)
        assert val==9
        assertions+=1
    # Exact primitive-eighth-root phase not representable by Gaussian integers.
    mods=(8,); G=group_data(mods); H={(0,),(2,),(4,),(6,)}; y=(1,)
    phi=Poly(cyclotomic_poly(16,X),X,domain=ZZ)
    nonzero=0
    for x in G:
        for k in G:
            poly=Poly(0,X,domain=ZZ)
            for t in G:
                u=add(t,neg(x,mods),mods)
                if (t not in H and t!=y) or (u not in H and u!=y): continue
                scale=4 if t==y and u==y else 2 if t==y or u==y else 1
                offset=3 if t==y and u!=y else -3 if u==y and t!=y else 0
                poly+=Poly(scale*X**((-2*k[0]*t[0]+offset)%16),X,domain=ZZ)
            nonzero+=int(not poly.rem(phi).is_zero)
    assert nonzero==41
    assertions+=1
    print('EXACT_CYCLOTOMIC_AMBIGUITY_CHECKS_PASS',assertions)
