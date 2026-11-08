#!/usr/bin/env python3
"""Exact six-frequency triangular L6 phase-alphabet certificate.

Standard-library only. Reconstructs the Fourier convolution polynomial before
using exact cyclotomic arithmetic to exhaust all normalized coefficient arrays.
"""
from collections import defaultdict
from itertools import product
from fractions import Fraction

SUPPORT = ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
VARS = ((0,0,0),)*3+((1,0,0),(0,1,0),(0,0,1))
PAIR_TERMS = (
 (78,(1,0,0)), (78,(0,0,1)), (144,(0,1,0)),
 (9,(1,0,-1)), (36,(1,-1,1)),
 (144,(1,-1,0)), (144,(0,-1,1)),
 (78,(1,-2,1)), (9,(1,-2,0)), (9,(0,-2,1)),
)
COS4 = {
 2: ((4,0),(-4,0)),
 3: ((4,0),(-2,0),(-2,0)),
 4: ((4,0),(0,0),(-4,0),(0,0)),
 5: ((4,0),(-1,1),(-1,-1),(-1,-1),(-1,1)),
 6: ((4,0),(2,0),(-2,0),(-4,0),(-2,0),(2,0)),
}
PHI = {2:(1,1), 3:(1,1,1), 4:(1,0,1),
       5:(1,1,1,1,1), 6:(1,-1,1)}
# q -> (4 times minimal moment as U+V sqrt(5), exact normalized minimizers)
EXPECTED = {
 2: ((2328,0), ((0,1,0),)),
 3: ((1824,0), ((1,2,1),(2,1,2))),
 4: ((2328,0), ((0,2,0),(2,1,2),(2,3,2))),
 5: ((2976,-408), ((1,3,2),(2,3,1),(2,4,2),
                    (3,1,3),(3,2,4),(4,2,3))),
 6: ((1824,0), ((2,4,2),(4,2,4))),
}

def add3(a,b): return tuple(x+y for x,y in zip(a,b))
def sub3(a,b): return tuple(x-y for x,y in zip(a,b))

def build_formal_moment():
    # P^3, organized by Fourier position and symbolic gauge monomial.
    d={(0,0):{(0,0,0):1}}
    for _ in range(3):
        out=defaultdict(lambda: defaultdict(int))
        for (a,b),poly in d.items():
            for (u,v),phase in zip(SUPPORT,VARS):
                for m,c in poly.items():
                    out[(a+u,b+v)][add3(m,phase)] += c
        d=out
    result=defaultdict(int)
    for poly in d.values():
        for m,a in poly.items():
            for n,b in poly.items():
                result[sub3(m,n)]+=a*b
    return {e:c for e,c in result.items() if c}


def predicted_formula():
    form=defaultdict(int)
    form[(0,0,0)]=996
    for w,exp in PAIR_TERMS:
        form[exp]+=w
        form[tuple(-k for k in exp)]+=w
    return dict(form)

def exact_4moment(q, exponent):
    a,b=3984,0
    for w,pow3 in PAIR_TERMS:
        r=sum(t*k for t,k in zip(pow3,exponent))%q
        c,d=COS4[q][r]
        a+=2*w*c
        b+=2*w*d
    return a,b

def sign(a,b):
    if a==0 and b==0:return 0
    if a>=0 and b>=0:return 1
    if a<=0 and b<=0:return -1
    # Otherwise integers have opposing signs; sqrt(5) is irrational.
    if a*a>5*b*b: return 1 if a>0 else -1
    return 1 if b>0 else -1

def red_poly(q,raw):
    p=PHI[q]; n=len(p)-1
    w=list(raw)+[0]*max(0,n-len(raw))
    for i in range(len(w)-1,n-1,-1):
        a=w[i]
        if a:
            for j in range(n): w[i-n+j]-=a*p[j]
    return tuple(w[:n])

def ringvec(q,r):
    return red_poly(q,[0]*(r%q)+[1])

def eval_form(q,exponents,form):
    dim=len(PHI[q])-1
    v=[0]*dim
    for monom,c in form.items():
        phase=sum(a*b for a,b in zip(monom,exponents))%q
        rr=ringvec(q,phase)
        for i in range(dim):v[i]+=c*rr[i]
    return tuple(v)

def expected_ring4(q,UV):
    u,v=UV
    dim=len(PHI[q])-1
    ones=(1,)+(0,)*(dim-1)
    if q!=5:
        assert v==0
        return tuple(u*t for t in ones)
    # sqrt(5) = 1 + 2(zeta + zeta^-1) in Z[zeta_5].
    sqrt5=tuple(ones[i]+2*(ringvec(q,1)[i]+ringvec(q,-1)[i]) for i in range(dim))
    return tuple(u*ones[i]+v*sqrt5[i] for i in range(dim))

def exact_rational_witness():
    # Unrestricted unit-circle coefficients, exact Gaussian-rational arithmetic.
    one=(Fraction(1),Fraction(0))
    u=(Fraction(-3,5),Fraction(4,5))
    v=(Fraction(-39,89),Fraction(-80,89))
    coeffs=(one,one,one,u,v,u)
    assert all(a*a+b*b==1 for a,b in coeffs)
    def cmul(s,t):
        a,b=s; c,d=t
        return a*c-b*d,a*d+b*c
    d={(0,0):one}
    for _ in range(3):
        out=defaultdict(lambda:(Fraction(0),Fraction(0)))
        for (a,b),val in d.items():
            for (u0,v0),co in zip(SUPPORT,coeffs):
                rr=cmul(val,co); x,y=out[(a+u0,b+v0)]
                out[(a+u0,b+v0)]=(x+rr[0],y+rr[1])
        d=out
    moment=sum((a*a+b*b for a,b in d.values()),Fraction(0))
    assert moment==Fraction(89848422,198025)
    assert moment<456

def main():
    formal=build_formal_moment()
    assert formal==predicted_formula(),(formal,predicted_formula())
    assert len(formal)==21
    total=0
    for q in range(2,7):
        best=None; minargs=[]; high=None
        for e in product(range(q),repeat=3):
            val=exact_4moment(q,e)
            # 4 * P^3 convolution squared, evaluated in a cyclotomic integer ring
            lhs=eval_form(q,e,formal)
            assert tuple(4*t for t in lhs)==expected_ring4(q,val), (q,e,lhs,val)
            if best is None or sign(val[0]-best[0],val[1]-best[1])<0:
                best=val; minargs=[e]
            elif val==best:
                minargs.append(e)
            if high is None or sign(val[0]-high[0],val[1]-high[1])>0:
                high=val
            total+=1
        assert (best,tuple(minargs))==EXPECTED[q],(q,best,minargs)
        assert high==(9816,0) # 4*2454, all-one coefficients
        print('q=%d minimum=(%d+%d sqrt(5))/4 normalized=%d full=%d'%
              (q,*best,len(minargs),q**3*len(minargs)))
    assert total==440
    exact_rational_witness()
    for q, (_,triples) in EXPECTED.items():
        fixed=sum(1 for a,b,c in triples if a==c)
        assert fixed == (2 if q==5 else len(triples))
    print('TRIANGULAR_SIXTH_EXACT_PASS configurations=%d formal_terms=%d'%
          (total,len(formal)))

if __name__=='__main__':main()
