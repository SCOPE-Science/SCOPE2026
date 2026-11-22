"""Independent finite checks for Farhi logarithmic limit law."""
from fractions import Fraction
from math import gcd, lcm, factorial, log, pi


def primes_up_to(k):
    ps=[]
    for n in range(2,k+1):
        if all(n%p for p in ps if p*p<=n):
            ps.append(n)
    return ps


def local_moments(k,p):
    e=0;q=1
    while q*p<=k:
        e+=1;q*=p
    L=k+1
    r={j:L%(p**j) for j in range(1,e+1)}
    m=sum((Fraction(L,p**j)-1 for j in range(1,e+1)),Fraction(0))
    v=sum((Fraction(r[j],p**j)*(1-Fraction(r[j],p**j)) for j in range(1,e+1)),Fraction(0))
    v+=2*sum((Fraction(r[i],p**j)*(1-Fraction(r[i],p**i)) for i in range(1,e+1) for j in range(i+1,e+1)),Fraction(0))
    return m,v,e


def valuation(n,p):
    z=0
    while n%p==0:
        n//=p;z+=1
    return z


def run():
    checks=0
    for k in range(2,11):
        P=1
        for v in range(1,k+1):P=lcm(P,v)
        for p in primes_up_to(k):
            m,v,e=local_moments(k,p)
            emax=p**e
            values=[]
            for n in range(1,emax+1):
                A=1;B=1
                for j in range(k+1):
                    A*=n+j;B=lcm(B,n+j)
                values.append(valuation(A//B,p))
            mu=Fraction(sum(values),emax)
            var=Fraction(sum(x*x for x in values),emax)-mu*mu
            assert (mu,var)==(m,v),(k,p,mu,var,m,v)
            checks+=1
        for n in range(1,P+1):
            A=1;B=1
            for j in range(k+1):A*=n+j;B=lcm(B,n+j)
            g=A//B
            assert factorial(k)%g==0,(k,n,g)
            for p in primes_up_to(k):
                assert valuation(g,p)==sum(sum(1 for i in range(k+1) if (n+i)%p**j==0)-1 for j in range(1,local_moments(k,p)[2]+1)),(k,p,n)
            checks+=1
    for k in (100,300,1000,3000,10000):
        mu=var=0.0
        for p in primes_up_to(k):
            m,v,e=local_moments(k,p)
            vfact=sum(k//p**j for j in range(1,e+1))
            mu+=(vfact-float(m))*log(p)
            var+=float(v)*log(p)**2
        assert mu>0 and var>0
        print(f'k={k} mean/k={mu/k:.6f}, variance/(k log k)={var/(k*log(k)):.6f}')
    print('finite exact checks passed:',checks)
    print('theoretical variance constant:',2-log(2*pi))
if __name__=='__main__':run()
