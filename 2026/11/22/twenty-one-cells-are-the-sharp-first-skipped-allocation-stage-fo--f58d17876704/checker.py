"""Exact, self-contained finite firebreak certificates. Python 3 standard library only."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json

def parts(n):
    return [t for t in combinations_with_replacement(range(1,n-1),3) if sum(t)==n]

def value(t,x):
    return sum(k*x**k for k in t)

def difference(a,b):
    d=max(max(a),max(b))
    c=[0]*(d+1)
    for k in a:c[k]+=k
    for k in b:c[k]-=k
    while c and c[-1]==0:c.pop()
    return c

def reduce_positive_domain(c):
    """Returns R with P(q)=q^m(1-q) R(q)."""
    m=next(i for i,v in enumerate(c) if v)
    p=c[m:]
    r=[]
    for a in p[:-1]:r.append(a+(r[-1] if r else 0))
    assert -r[-1]==p[-1]
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def bernstein(c,a,b):
    """Bernstein coefficients of polynomial sum_i c_i q^i on [a,b]."""
    d=len(c)-1
    # compute monomial coefficients after q=a+(b-a)t
    mono=[Q(0) for _ in range(d+1)]
    for i,co in enumerate(c):
        if not co:continue
        for j in range(i+1):
            mono[j]+=co*comb(i,j)*a**(i-j)*(b-a)**j
    return [sum((mono[i]*Q(comb(j,i),comb(d,i)) for i in range(j+1)),Q(0)) for j in range(d+1)]

def certify_positive(poly,a,b,level=0):
    # Positive Bernstein coefficients are an exact rational convex-hull certificate.
    coeff=bernstein(poly,a,b)
    if min(coeff)>0:return 1
    if level>=16:raise AssertionError(('insufficient exact Bernstein certificate',poly,a,b))
    m=(a+b)/2
    return certify_positive(poly,a,m,level+1)+certify_positive(poly,m,b,level+1)

def main():
    count=0
    witness=json.loads((Path(__file__).parent/'witnesses.json').read_text())
    countmax=0
    for n in range(3,21):
        pp=parts(n)
        assert set(map(int,witness[str(n)]))==set(range(1,n//3+1));count+=1
        for aa,ww in witness[str(n)].items():
            aa=int(aa)
            target=tuple(sorted((aa,aa,n-2*aa)))
            x=Q(ww)
            assert 0<x<1
            v=value(target,x)
            for other in pp:
                if other!=target:
                    assert v>value(other,x),('witness failed',n,target,x,other)
                    count+=1
            count+=1
    print('Canonical pre-cutoff witnesses',sum(len(v) for v in witness.values()),'all exact', 'comparisons',count)
    A=(5,5,11);B=(6,6,9);C=(7,7,7);q0=Q(759,1000)
    # For 0<q<=q0, A-B=q^5(q-1)S(q)>0 because S increasing, S(q0)<0.
    # For q0<=q<1, C-B=-3q^6(q-1)Q(q)>0 because Q increasing, Q(q0)>0.
    def S(q):return 11*q**5+11*q**4+2*q**3+2*q**2+2*q-10
    def T(q):return 3*q*q+3*q-4
    assert S(q0)<0 and T(q0)>0 and S(Q(0))<0 and T(Q(1))>0
    count+=4
    # Certified strictly greater than all other 35 profiles on each rational interval,
    # except for the opposite crossing winner A or C.
    ranges=[(A,C,Q(151,200),Q(3797,5000)),(C,A,Q(3797,5000),Q(153,200))]
    proofs=0
    for win,rival,l,r in ranges:
        for other in parts(21):
            if other in (win,rival):continue
            R=reduce_positive_domain(difference(win,other))
            proofs+=certify_positive(R,l,r)
            count+=1
    # F_A-F_C=q^5(q-1)(q+1)(11q^4+11q^2-10).
    # The last factor has one positive root in (0,1), whose exact expression is q*.
    from decimal import Decimal,getcontext
    getcontext().prec=60
    qstar=((Decimal(561).sqrt()-Decimal(11))/Decimal(22)).sqrt()
    assert Decimal(151)/Decimal(200)<qstar<Decimal(3797)/Decimal(5000)
    count+=1
    print('Global skipped allocation domination: exact polynomial sign inequalities verified')
    print('Local global optimality: 70 full-domain competitors, exact Bernstein certificates',proofs)
    print('Unique transition q* =',qstar)
    print('Total exact assertions/comparisons',count)
if __name__=='__main__':main()
