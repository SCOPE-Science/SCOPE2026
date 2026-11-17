"""Standalone reproducibility checks for finite-field monomial evolution algebras.

Runs exhaustive literal fixed-point enumeration in small binary extension fields,
then independently matches Euler products, logarithmic-derivative recurrences,
and predicted asymptotic constants. Python standard library only.
"""
from fractions import Fraction
from itertools import permutations, product
from math import gcd, factorial, exp, lgamma, log


def g(q, ell):
    return gcd(pow(2, ell, q - 1)-1, q-1) if q > 2 else 1


def period(q):
    m = q-1
    while m%2 == 0:
        m//=2
    if m==1:
        return 1
    h=1
    while pow(2,h,m)!=1:
        h+=1
    return h


def arith(q):
    h=period(q)
    aa={j:Fraction(g(q,j)-1,g(q,j)) for j in range(1,h+1)}
    bb={}
    for d in [d for d in range(1,h+1) if h%d==0]:
        bb[d]=aa[d]-sum((bb[e] for e in bb if d%e==0),Fraction())
    beta=sum(aa.values(),Fraction())/h
    # The leading singular constant at 1.
    const=exp(-sum(float(bb[d]/d)*log(d) for d in bb))
    admiss=[j for j in range(1,h+1) if aa[j]>0]
    support_gcd=0
    for j in admiss:
        support_gcd=gcd(support_gcd,j)
    return h,aa,bb,beta,const,support_gcd


def series_via_recurrence(q,N):
    h,aa,*_=arith(q)
    f=[Fraction(1)]
    for n in range(1,N+1):
        f.append(sum((aa[(j-1)%h+1]*f[n-j] for j in range(1,n+1)),Fraction())/n)
    return f


def series_via_finite_product(q,N):
    _,_,bb,*_=arith(q)
    ff=[Fraction(1)]+[Fraction()] * N
    for d,b in bb.items():
        alpha=b/d
        terms=[Fraction(1)]
        for k in range(1,N//d+1):
            terms.append(terms[-1]*(alpha+k-1)/k)
        hh=[Fraction()]*(N+1)
        for i,ci in enumerate(ff):
            if not ci: continue
            for k,t in enumerate(terms[:(N-i)//d+1]):
                hh[i+k*d]+=ci*t
        ff=hh
    return ff


def fmul(a,b,q,poly):
    result=0
    while b:
        if b&1: result^=a
        b>>=1
        a<<=1
        if a&q: a^=poly
    return result


def exhaustive(q,poly,n):
    # Literally solve each idempotence equation, rather than using cycle factors.
    total=0
    only_zero=0
    vv=list(product(range(q),repeat=n))
    square=[fmul(a,a,q,poly) for a in range(q)]
    for sigma in permutations(range(n)):
        for weights in product(range(1,q),repeat=n):
            total+=1
            solutions=0
            for v in vv:
                if all(fmul(weights[i],square[v[i]],q,poly)==v[sigma[i]] for i in range(n)):
                    solutions+=1
                    if solutions>1:
                        break
            if solutions==1:
                only_zero+=1
    want=series_via_recurrence(q,n)[n]
    assert Fraction(only_zero,total)==want,(q,n,total,only_zero,want)
    print('EXHAUSTIVE_OK',q,n,only_zero,total,str(want))


def asymptotic(q,N):
    h,aa,bb,beta,const,d=arith(q)
    if not d:return
    weights=[float(aa[(j-1)%h+1]) for j in range(1,N+1)]
    p=[1.0]
    for n in range(1,N+1):
        p.append(sum(weights[j-1]*p[n-j] for j in range(1,n+1))/n)
    n=N-(N%d)
    pred=d*const*exp(-lgamma(float(beta)))*n**(float(beta)-1)
    ratio=p[n]/pred
    # Secondary root-of-unity singularities give slow periodic corrections,
    # notably for q=64. This numerical test is illustrative, not a proof.
    assert abs(ratio-1)<0.18,(q,n,ratio)
    assert all(p[j]==0.0 for j in range(1,N+1) if j%d!=0)
    print('ASYMPTOTIC_OK',q,n,round(ratio,8),'beta',beta,'d',d)


def main():
    for q in [2,3,4,5,7,8,9,16,32,64,81,125]:
        h,aa,bb,beta,const,d=arith(q)
        f1=series_via_recurrence(q,28)
        f2=series_via_finite_product(q,28)
        assert f1==f2,(q,h)
        assert all(f1[n]==0 for n in range(1,29) if not d or n%d)
        print('SERIES_OK',q,'period',h,'beta',beta,'support',d)
    # q=64 has allowable lengths 2 and 3, so all n>=2 occur.
    assert all(series_via_recurrence(64,18)[n]>0 for n in range(2,19))
    for n in range(1,5):
        exhaustive(4,0b111,n)
    for n in range(1,4):
        exhaustive(8,0b1011,n)
    for n in range(1,3):
        exhaustive(16,0b10011,n)
    asymptotic(16,1200)
    asymptotic(64,1200)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
