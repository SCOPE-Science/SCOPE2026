"""Exact arithmetic checks and finite-scale tests for least gaps of regular partitions."""
import math
from functools import lru_cache

@lru_cache(None)
def partitions(n, lower=1):
    if n == 0:
        return ((),)
    return tuple((k,) + rest for k in range(lower, n + 1)
                 for rest in partitions(n-k, k))

def pentagonal(N):
    p = [0] * (N + 1)
    p[0] = 1
    terms = []
    for k in range(1, int((2*N)**0.5) + 4):
        for v in (k*(3*k-1)//2, k*(3*k+1)//2):
            if v <= N:
                terms.append((v, (-1)**(k+1)))
    terms.sort()
    for n in range(1, N+1):
        p[n] = sum(sign*p[n-v] for v,sign in terms if v<=n)
    return p

def regular_counts(p, ell):
    N = len(p)-1
    terms = [(0,1)]
    for k in range(1, int((2*N/ell)**0.5)+5):
        for v in (ell*k*(3*k-1)//2, ell*k*(3*k+1)//2):
            if v<=N:
                terms.append((v,(-1)**k))
    return [sum(sign*p[n-v] for v,sign in terms if v<=n)
            for n in range(N+1)]

def A(ell,m):
    q=m//ell
    return m*(m+1)//2-ell*q*(q+1)//2

def local_model(ell,r,n,m):
    assert m>=1 and m%ell
    rho=(ell-1)/ell
    mu=math.pi**2*rho/6
    y=m/n**0.25
    t=n**(-0.25)
    gamma=r*rho*math.sqrt(mu)/2
    factor=math.exp(-gamma*y*y)
    leading=t*r*math.sqrt(mu)*y*factor
    correction=t*t*mu*r*r*(ell-2*(m%ell))/(2*ell)*y*y*factor
    return leading, leading+correction

def residue_model(ell,r,n,s):
    rho=(ell-1)/ell
    mu=math.pi**2*rho/6
    C=math.sqrt(math.pi)*mu**0.25*math.sqrt(r)/(2**1.5*ell**2*rho**1.5)
    return 1/(ell-1),1/(ell-1)+C*(ell-2*s)*n**(-0.25)

def exact_tests():
    pp=pentagonal(30)
    checks=0
    for ell in range(2,8):
        b=regular_counts(pp,ell)
        for n in range(23):
            ps=[part for part in partitions(n) if all(z%ell for z in part)]
            assert len(ps)==b[n]
            for r in (1,2,3):
                for m in range(min(n+4,12)):
                    direct=sum(all(part.count(a)>=r for a in range(1,m+1) if a%ell)
                               for part in ps)
                    h=r*A(ell,m)
                    shifted=b[n-h] if h<=n else 0
                    assert direct==shifted,(ell,r,n,m,direct,shifted)
                    checks+=1
                for m in range(1,min(14,n+5)):
                    if m%ell==0:
                        continue
                    direct=sum((next((a for a in range(1,n+ell+3)
                                      if a%ell and part.count(a)<r),None)==m)
                               for part in ps)
                    a1=r*A(ell,m-1)
                    a2=r*A(ell,m)
                    shifted=(b[n-a1] if a1<=n else 0)-(b[n-a2] if a2<=n else 0)
                    assert direct==shifted,(ell,r,n,m,direct,shifted)
                    checks+=1
    print('finite_exact_count_tests',checks)

def finite_asymptotic_tests():
    N=40000
    p=pentagonal(N)
    cases=[(3,1),(4,1),(5,2),(7,1)]
    tests=0
    for ell,r in cases:
        b=regular_counts(p,ell)
        probs=[]
        for s in range(1,ell):
            numer=0
            for m in range(s,N+1,ell):
                h0=r*A(ell,m-1)
                h1=r*A(ell,m)
                if h0>N:
                    break
                numer+=b[N-h0]-(b[N-h1] if h1<=N else 0)
            actual=numer/b[N]
            _,approx=residue_model(ell,r,N,s)
            assert abs(actual-approx)<0.004,(ell,r,s,actual,approx)
            probs.append(actual)
            tests+=1
            m=round(1.8*N**0.25/ell)*ell+s
            if r*A(ell,m)>=N: continue
            exact=(b[N-r*A(ell,m-1)]-b[N-r*A(ell,m)])/b[N]
            first,second=local_model(ell,r,N,m)
            assert abs(exact-second)<0.00011,(ell,r,m,exact,second)
            tests+=1
        assert abs(sum(probs)-1)<1e-14
        if ell>=3:
            assert all(probs[i]>probs[i+1] for i in range(len(probs)-1))
        print('ell',ell,'r',r,'n',N,'residue probabilities',
              ' '.join(f'{q:.8f}' for q in probs))
    print('finite_asymptotic_comparisons',tests)

if __name__=='__main__':
    exact_tests()
    finite_asymptotic_tests()
    print('VERIFY_OK')
