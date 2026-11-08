"""Exact rational replay for complete-multipartite Crank-Nicolson positivity."""
import itertools
from fractions import Fraction as F
import sympy as S


def compositions(n):
    for mask in range(1, 1 << (n - 1)):
        ans=[]; k=1
        for j in range(n-1):
            if (mask>>j)&1:ans.append(k);k=1
            else:k+=1
        ans.append(k)
        yield tuple(ans)


def lap(parts):
    n=sum(parts);L=S.zeros(n);labels=sum(([i]*a for i,a in enumerate(parts)),[])
    for i in range(n):
        for j in range(i+1,n):
            if labels[i]!=labels[j]:L[i,i]+=1;L[j,j]+=1;L[i,j]=-1;L[j,i]=-1
    return L,labels


def threshold(n,a):
    A=(n-a)*(n-2)
    return S.Rational(a, A) + S.sqrt(a*a+4*A)/A # h, not s


def entry_formula(n,a,s):
    return S.Rational(1,n)+S.Rational(a-1,a)/(1+s*(n-a))+S.Rational(n-a,a*n)/(1+s*n)


def test():
    x,y,z,t=S.symbols('n a b s')
    def expr(a):return 1/x+(a-1)/a/(1+t*(x-a))+(x-a)/(a*x)/(1+t*x)
    assert S.simplify((expr(y)-expr(z))-t*(y-z)*(1+(x-1)*t)/((1+x*t)*(1+(x-y)*t)*(1+(x-z)*t)))==0
    assert S.simplify((2*expr(y)-1)*(1+x*t)*(1+(x-y)*t) - (1+y*t-(x-y)*(x-2)*t*t)) == 0
    cases=0; samples=0
    for n in range(3,9):
      for parts in compositions(n):
        L,labels=lap(parts);a=min(parts);h=threshold(n,a)
        for s in [S.Rational(1,5*n),S.Rational(1,n),S.Rational(2,n),S.Rational(1,2),S.Rational(2,1)]:
            R=(S.eye(n)+s*L).inv();C=2*R-S.eye(n)
            for i,ai in enumerate(labels):
                assert R[i,i]==entry_formula(n,parts[ai],s)
            assert all(C[i,j]>0 for i in range(n) for j in range(n) if i!=j)
            pred=(2*s<=h)
            assert (all(C[i,i]>=0 for i in range(n)))==pred
            assert min(C[i,i] for i in range(n))==2*entry_formula(n,a,s)-1
            samples+=1
        cases+=1
    print(f'PASS: {cases} complete multipartite ordered part profiles n=3..8; {samples} exact rational matrix checks; 2 symbolic identities')

if __name__=='__main__':test()
