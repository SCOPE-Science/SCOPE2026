"""Exact arithmetic checks for the local-extrema covariance theorem.

Run with Python 3.10+ (standard library only): python verify.py

The full proof is analytic; finite enumeration is only an independent check.
"""
from fractions import Fraction as Q
from math import factorial, comb
from itertools import permutations


def edge_kernel(a, b):
    """Cov(I_u^min,I_v^max) for adjacent vertices of degrees a,b."""
    return Q(1, a*b) - Q(factorial(a-1)*factorial(b-1), factorial(a+b)) - Q(1, (a+1)*(b+1))


def two_step_kernel(a, b):
    """Sum of ordered min/max covariances for vertices at distance exactly two."""
    return -Q(2, a*b*(a+1)*(b+1)) + Q(2*factorial(a-1)*factorial(b-1), factorial(a+b+1))


def adjacency_path(n):
    return [set(([i-1] if i else [])+([i+1] if i+1<n else [])) for i in range(n)]


def adjacency_ary(m, h):
    a=[set()];level=[0]
    for depth in range(h):
        nxt=[]
        for u in level:
            for j in range(m):
                v=len(a);a.append({u});a[u].add(v);nxt.append(v)
        level=nxt
    return a


def local_cross_cov(adj):
    """All indicators depend only on closed neighborhoods: distance>2 independent."""
    n=len(adj);degree=[len(s) for s in adj]
    z=-sum((Q(1,(d+1)**2) for d in degree),Q())
    for u in range(n):
        for v in adj[u]:
            if u<v:z+=2*edge_kernel(degree[u],degree[v])
    for w in range(n):
        ns=sorted(adj[w]);
        for i,u in enumerate(ns):
            for v in ns[i+1:]:
                if v not in adj[u]:
                    # On a tree each distance-two pair has one common center.
                    z+=two_step_kernel(degree[u],degree[v])
    return z


def local_var_min(adj):
    n=len(adj);degree=[len(s) for s in adj]
    z=sum((Q(d,(d+1)**2) for d in degree),Q())
    for u in range(n):
        for v in adj[u]:
            if u<v:z-=Q(2,(degree[u]+1)*(degree[v]+1))
    for w in range(n):
        ns=sorted(adj[w]);
        for i,u in enumerate(ns):
            for v in ns[i+1:]:
                if v not in adj[u]:
                    a,b=degree[u],degree[v]
                    z+=Q(2,(a+1)*(b+1)*(a+b+1))
    return z


def brute_moments(adj):
    n=len(adj);samples=factorial(n);s=t=st=s2=0
    for order in permutations(range(n)):
        x=sum(all(order[v]<order[w] for w in adj[v]) for v in range(n))
        y=sum(all(order[v]>order[w] for w in adj[v]) for v in range(n))
        s+=x;t+=y;st+=x*y;s2+=x*x
    return (Q(st,samples)-Q(s*t,samples*samples),
            Q(s2,samples)-Q(s*s,samples*samples))


def constant_C(m):
    """Covariance per vertex limit for fixed arity m>=2."""
    assert m>=2
    d=m+1
    factorial_term=Q(factorial(m)**2,factorial(2*m+2))
    P=m**7+10*m**6+26*m**5+4*m**4-43*m**3-14*m*m-56*m-120
    return -Q(P,12*m*(m+1)**2*(m+2)**2*(m+3))-Q(3*m+5,m*(2*m+3))*factorial_term


def constant_V(m):
    """Variance per vertex limit for fixed arity m>=2."""
    assert m>=2
    P=2*m**5+19*m**4+42*m**3+7*m*m-10*m+36
    return Q(P,12*(m+2)**2*(m+3)*(2*m+3))


def remainder_R(m):
    """Exact covariance correction C(T_m,h)-|T_m,h|C_m for every h>=3."""
    c=Q(factorial(m)**2,factorial(2*m+2))
    P=m**6+11*m**5+37*m**4+41*m**3-2*m*m+32*m+120
    return -Q(P,12*m*(m+1)**2*(m+2)**2*(m+3))-Q(2*m**3+7*m*m+4*m-5,m*(2*m+3))*c


def h2_closed(m):
    """Exact finite-height-two covariance for m>=2."""
    c=Q(factorial(m)**2,factorial(2*m+2))
    P=m**7+8*m**6+13*m**5+2*m**4+16*m**3+8*m*m-96*m-48
    return -Q(P,12*(m+1)**2*(m+2)**2)-Q(7*m*m+21*m+12,2*m+3)*c


def check():
    assertions=0
    for n in range(4,35):
        a=adjacency_path(n)
        assert local_cross_cov(a)==Q(8*n-37,180);assertions+=1
        assert local_var_min(a)==Q(2*(n+1),45);assertions+=1
    assert local_cross_cov(adjacency_path(3))==-Q(1,9);assertions+=1
    for m in range(2,10):
        assert constant_C(m)<0 and constant_V(m)>0 and remainder_R(m)<0 and h2_closed(m)<0
        assertions+=4
        for h in (2,3):
            a=adjacency_ary(m,h)
            c=local_cross_cov(a)
            if h==2: assert c==h2_closed(m)
            else: assert c==len(a)*constant_C(m)+remainder_R(m)
            assertions+=1
    for m,h in [(2,4),(2,5),(2,6),(3,4),(4,4),(5,4)]:
        a=adjacency_ary(m,h)
        assert local_cross_cov(a)==len(a)*constant_C(m)+remainder_R(m)
        assertions+=1
    # Independently check the claimed linear variance coefficient: for h>=3
    # the exact intercept is unaffected by an extra complete generation.
    for m in range(2,6):
        a=adjacency_ary(m,3)
        b=adjacency_ary(m,4)
        diff_a=local_var_min(a)-len(a)*constant_V(m)
        diff_b=local_var_min(b)-len(b)*constant_V(m)
        assert diff_a==diff_b; assertions+=1
    for a in [adjacency_path(3),adjacency_path(4),adjacency_path(5),
              adjacency_path(6),adjacency_path(7),adjacency_ary(2,2),
              adjacency_ary(3,1),adjacency_ary(5,1)]:
        brute_c,brute_v=brute_moments(a)
        assert brute_c==local_cross_cov(a) and brute_v==local_var_min(a)
        assertions+=2
    assert constant_C(2)==-Q(323,5040); assertions+=1
    assert constant_V(2)==Q(187,1680); assertions+=1
    assert constant_C(2)/constant_V(2)==-Q(19,33);assertions+=1
    print(f"VERIFY_OK {assertions} exact identity and finite-enumeration checks")

if __name__=='__main__':check()
