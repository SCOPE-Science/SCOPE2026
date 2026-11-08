"""Independent finite checks for clique-joined cycle greedy RSA.
Run: python verify.py (Python 3 standard library only).
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
from math import factorial, exp


def path_law(m):
    if m <= 0:
        return {0: Q(1)}
    out = defaultdict(Q)
    for j in range(m):
        l = path_law(j-1)
        r = path_law(m-j-2)
        for a, pa in l.items():
            for b, pb in r.items():
                out[1+a+b] += pa*pb/Q(m)
    return dict(out)


def join_cycle_law(n,k):
    p = Q(k,n+k)
    out=defaultdict(Q,{1:p})
    for x,v in path_law(n-3).items():
        out[x+1] += (1-p)*v
    return dict(out)


def independent_enum(n,k):
    N=n+k
    adjacency=[set() for _ in range(N)]
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n):
            adjacency[i].add(j);adjacency[j].add(i)
    for i in range(n,N):
        for j in range(N):
            if i!=j:
                adjacency[i].add(j);adjacency[j].add(i)
    counter=defaultdict(int)
    for perm in permutations(range(N)):
        accepted=set()
        for v in perm:
            if not (adjacency[v]&accepted):accepted.add(v)
        counter[len(accepted)]+=1
    return {j:Q(c,factorial(N)) for j,c in counter.items()}


def expcoef(a,n):
    return Q(a**n,factorial(n))


def series_moments(N):
    # From A(t)=(1-exp(-2t))/(2(1-t)^2)
    # B(t)=(3t-1-4t^2 exp(-2t)+(1+t)exp(-4t))/(4(1-t)^3).
    def c2(j):return j+1 if j>=0 else 0
    def c3(j):return Q((j+2)*(j+1),2) if j>=0 else 0
    mu=[];fm=[]
    for n in range(N+1):
        a=Q(0)
        for j in range(n+1):a += expcoef(-2,j)*c2(n-j)
        mu.append((Q(c2(n))-a)/2)
        b=3*c3(n-1)-c3(n)
        for j in range(n+1):
            b-=4*expcoef(-2,j)*c3(n-j-2)
            b+=expcoef(-4,j)*(c3(n-j)+c3(n-j-1))
        fm.append(b/4)
    return mu,fm


def main():
    tests=0
    import functools
    global path_law
    path_law=functools.lru_cache(None)(path_law)
    for n in range(4,8):
        for k in range(1,3):
            if n+k>8:continue
            a=join_cycle_law(n,k);b=independent_enum(n,k)
            assert a==b,(n,k,a,b)
            assert sum(a.values())==1
            tests+=2
    mu,fm=series_moments(15)
    for m in range(16):
        d=path_law(m)
        assert sum(d.values())==1
        assert sum(Q(j)*p for j,p in d.items())==mu[m],m
        assert sum(Q(j*(j-1))*p for j,p in d.items())==fm[m],m
        tests+=3
    rho=(1-exp(-2))/2;sigma2=exp(-4)
    for m in (40,80,140):
        # Exact path moment recurrence via series and asymptotics.
        M,Q2=series_moments(m)
        v=float(Q2[m]+M[m]-M[m]**2)
        assert abs(float(M[m])/m-rho)<1/m
        assert abs(v/m-sigma2)<0.08/m
        tests+=2
    print('VERIFY_OK',tests,'exact-moment-and-enumeration-assertions')

if __name__=='__main__':main()
