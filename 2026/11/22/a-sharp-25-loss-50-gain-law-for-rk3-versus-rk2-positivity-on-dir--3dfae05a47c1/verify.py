"""Separate exact-matrix and boundary checks for RK2/RK3 Markov cycles.
Uses only Python's standard library. The theorem's all-rate proof is analytic.
"""
from fractions import Fraction as F
from random import Random
from math import isclose

def mul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]

def rk(Q,h,p):
    n=len(Q); T=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    P=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    from math import factorial
    for k in range(1,p+1):
        P=mul(P,Q)
        c=h**k / factorial(k)
        for i in range(n):
            for j in range(n):T[i][j]+=c*P[i][j]
    return T

def closed(r,h,p):
    n=len(r); O=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        a,b,c=(r[(i+j)%n] for j in range(3)); z=h*a
        O[i][i] = 1-z+z*z/2
        O[i][(i+1)%n] = h*a*(1-h*(a+b)/2)
        O[i][(i+2)%n] = h*h*a*b/2
        if p==3:
            O[i][i] -= z**3/6
            O[i][(i+1)%n]+=h**3*a*(a*a+a*b+b*b)/6
            O[i][(i+2)%n]-=h**3*a*b*(a+b+c)/6
            O[i][(i+3)%n]+=h**3*a*b*c/6
    return O

def exact_test():
    rng=Random(222707)
    checked=0; rowchecked=0
    for n in range(4,10):
      for k in range(32):
        rates=[F(rng.randint(1,11),rng.randint(1,5)) for _ in range(n)]
        Q=[[F(0) for j in range(n)] for i in range(n)]
        for i,a in enumerate(rates):
            Q[i][i]-=a;Q[i][(i+1)%n]+=a
        for h in [F(1,11),F(3,7),F(4,3)]:
          for p in (2,3):
            T=rk(Q,h,p);C=closed(rates,h,p)
            for i in range(n):
                assert sum(T[i],F(0))==1
                rowchecked+=1
                for j in range(n):
                    assert T[i][j]==C[i][j],(n,p,rates,h,i,j,T[i][j],C[i][j])
                    checked+=1
    print('PASS exact entry comparisons:',checked)
    print('PASS exact row sums:',rowchecked)

def root():
    lo,hi=F(3,2),F(2,1)
    def f(z): return 1-z+z*z/2-z**3/6
    assert f(lo)>0 and f(hi)<0
    for _ in range(90):
        m=(lo+hi)/2
        if f(m)>0:lo=m
        else:hi=m
    return float((lo+hi)/2)

def numerical_test(rho):
    rng=Random(514407)
    count=0
    for n in range(4,11):
      for k in range(80):
        r=[F(rng.randint(1,30),rng.randint(1,17)) for i in range(n)]
        M=max(r);A=max(r[i]+r[(i+1)%n] for i in range(n))
        T=max(r[i]+r[(i+1)%n]+r[(i+2)%n] for i in range(n))
        h2=2/float(A);h3=min(rho/float(M),3/float(T))
        R=h3/h2
        assert .75<R<1.5
        for p,hstar in [(2,h2),(3,h3)]:
          for h in [hstar*.9999,hstar*1.0001]:
            Q=[[0.0]*n for _ in range(n)]
            for i,a in enumerate(r):
                Q[i][i]=-float(a);Q[i][(i+1)%n]=float(a)
            P=[[float(i==j) for j in range(n)] for i in range(n)]
            S=[v[:] for v in P]
            from math import factorial
            for deg in range(1,p+1):
                P=[[sum(P[i][k]*Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(n):S[i][j]+=h**deg/factorial(deg)*P[i][j]
            mn=min(min(row) for row in S)
            if h<hstar: assert mn>=-1e-9,(n,r,p,hstar,mn)
            else: assert mn< -1e-11,(n,r,p,hstar,mn)
            count+=1
    print('PASS two-sided horizon checks:',count)

def extremizers(rho):
    def ratio(v):
        n=len(v);M=max(v)
        A=max(v[i]+v[(i+1)%n] for i in range(n))
        T=max(v[i]+v[(i+1)%n]+v[(i+2)%n] for i in range(n))
        return min(rho/M,3/T)/(2/A)
    for eps in [1e-2,1e-4,1e-6]:
        lower=ratio([1,eps,1,eps]);upper=ratio([1,1,eps,eps])
        assert 0.75<lower<0.76
        assert 1.49<upper<1.5
        assert isclose(lower,3*(1+eps)/(2*(2+eps)),abs_tol=1e-11)
        assert isclose(upper,3/(2+eps),abs_tol=1e-11)
    s=rho/(2-rho)
    for contrast in [1.1,2,3,4,5,10]:
        r=ratio([contrast,1,1,1,1])
        if 1<contrast<s:assert r>1
        else:assert r<1
    print('PASS sharpness families and one-defect crossing:',s)

if __name__=='__main__':
    exact_test()
    rho=root()
    print('PASS cubic root bracket:',rho)
    numerical_test(rho)
    extremizers(rho)
