"""Exact independent finite checks for joint ternary valuations of Catalan and central binomial numbers."""
from collections import Counter
from fractions import Fraction
from math import comb


def vfactorial(n):
    s=0
    while n:
        n//=3
        s+=n
    return s


def mul(p,q):
    r=Counter()
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            r[(a+c,b+d)]+=v*w
    return +r


def scale(p,c):
    return {k:v*c for k,v in p.items() if v*c}


def add(*polys):
    r=Counter()
    for p in polys:
        r.update(p)
    return +r

ZERO={}
ONE={(0,0):1}
D1={(0,0):2,(1,0):1,(1,1):2}
D2={(1,1):3,(1,0):2,(2,1):2}
D3={(2,1):3}
N1={(1,1):-2}
N2={(2,1):1,(1,1):1,(1,0):-1}
P=[ONE]
total_direct=0
for L in range(1,10):
    # Formula: P_L=D1*P_{L-1}-D2*P_{L-2}+D3*P_{L-3}+N_L.
    p=add(mul(D1,P[L-1]),scale(mul(D2,P[L-2]),-1) if L>=2 else ZERO,
          mul(D3,P[L-3]) if L>=3 else ZERO,
          N1 if L==1 else N2 if L==2 else ZERO)
    P.append(p)
    actual=Counter()
    for n in range(3**L):
        A=vfactorial(2*n)-2*vfactorial(n)
        B=A-vfactorial(n+1)+vfactorial(n)  # equals A-v_3(n+1)
        assert 0<=B<=A<=L
        actual[(A,B)]+=1
        total_direct+=1
    assert +actual==+Counter(p), (L,actual,p)
    assert sum(p.values())==3**L
    assert set(p)=={(a,b) for a in range(L+1) for b in range(a+1) if (a,b)!=(L,L)}
    assert [(p.get((L,b),0)) for b in range(L)]==[1]+[2**(b-1) for b in range(1,L)]
    q=Fraction(1,3**L)
    meanA=Fraction(L,2)-Fraction(1,4)+q/4
    meanB=Fraction(L,2)-Fraction(3,4)+3*q/4
    covariance=Fraction(L,2)-Fraction(17,16)+(Fraction(L,2)+Fraction(5,4))*q-3*q*q/16
    assert sum(Fraction(a*v,3**L) for (a,b),v in p.items())==meanA
    assert sum(Fraction(b*v,3**L) for (a,b),v in p.items())==meanB
    assert sum(Fraction(a*b*v,3**L) for (a,b),v in p.items())-meanA*meanB==covariance

# Separate integer binomial checks of Legendre identities for more than 500 indices.
for n in range(0,800):
    c=comb(2*n,n)
    k=c//(n+1)
    assert c%(n+1)==0
    a=b=0
    while c%3==0:
        c//=3; a+=1
    while k%3==0:
        k//=3; b+=1
    assert (a,b)==(vfactorial(2*n)-2*vfactorial(n),vfactorial(2*n)-vfactorial(n)-vfactorial(n+1))
print(f'VERIFY_OK levels=0..9, exact_index_pairs={total_direct}, binomial_cases=800, support_and_boundary=PASS, rational_moments=PASS')
