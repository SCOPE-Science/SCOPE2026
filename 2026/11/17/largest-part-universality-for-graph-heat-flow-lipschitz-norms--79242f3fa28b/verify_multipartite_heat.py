"""Exact rational checks for heat flow on finite complete multipartite graphs.

No third-party dependencies. Run: python verify_multipartite_heat.py
"""
from fractions import Fraction as Q
from itertools import product


def graph(parts):
    group = tuple(i for i,m in enumerate(parts) for _ in range(m))
    n = len(group)
    edges = [(i,j) for i in range(n) for j in range(i+1,n) if group[i] != group[j]]
    return group, edges


def kernel(parts, q):
    group, _ = graph(parts)
    n = len(group)
    return [[Q(1,n)+q**n*(Q(int(group[u]==group[w]),parts[group[u]])-Q(1,n))
             +q**(n-parts[group[u]])*(Q(int(u==w))-Q(int(group[u]==group[w]),parts[group[u]]))
             for w in range(n)] for u in range(n)]


def metric_dual_extremes(parts):
    group, edges = graph(parts)
    n = len(group)
    # The fixed-basepoint Lipschitz polytope is integral by total
    # unimodularity of the incidence matrix; graph diameter <= 2.
    out=[]
    for tail in product(range(-2,3),repeat=n-1):
        f=(0,)+tail
        if all(abs(f[i]-f[j])<=1 for i,j in edges):
            out.append(f)
    return out


def target(parts, q):
    n=sum(parts)
    m=max(parts)
    return q**n * (1+2*Q(m-1,m)*(q**(-m)-1))


def check(parts, qs):
    group, edges = graph(parts)
    n=len(group)
    potentials=metric_dual_extremes(parts)
    assert potentials
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for a,b in edges:
        L[a][a]+=1; L[b][b]+=1
        L[a][b]-=1; L[b][a]-=1
    checked=0
    for q in qs:
        P=kernel(parts,q)
        assert all(sum(row)==1 for row in P)
        assert all(P[i][j]==P[j][i] and P[i][j]>=0 for i in range(n) for j in range(n))
        # The claimed heat kernel obeys its exact semigroup law.
        R=kernel(parts,q*q)
        assert all(sum(P[i][k]*P[k][j] for k in range(n))==R[i][j] for i in range(n) for j in range(n))
        best=Q(0)
        for a,b in edges:
            mu=[P[a][j]-P[b][j] for j in range(n)]
            value=max(sum(mu[j]*f[j] for j in range(n)) for f in potentials)
            size=max(parts[group[a]],parts[group[b]])
            expected=q**n*(1+2*Q(size-1,size)*(q**(-size)-1))
            assert value==expected,(parts,q,a,b,value,expected)
            best=max(best,value)
            checked+=1
        assert best==target(parts,q),(parts,q,best,target(parts,q))
    return checked,len(potentials)


if __name__=='__main__':
    families=[(1,1),(1,1,1),(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),
              (3,2,1),(3,3),(4,2,1),(2,2,2),(5,2),(3,1,1),(2,1,1,1)]
    cases=0; vertices=0
    for p in families:
        ne,np=check(p,[Q(1),Q(1,2),Q(2,3),Q(4,5)])
        cases+=ne; vertices+=np
    print('EXACT_EXHAUSTIVE_EDGE_DUAL_OPTIMIZATIONS_PASSED',cases)
    print('TOTAL_FEASIBLE_INTEGER_LIPSCHITZ_POTENTIALS',vertices)
    print('EXACT_HEAT_SEMIGROUP_IDENTITIES_PASSED',len(families)*4)
    print('ALL_MULTIPARTITE_HEAT_NORM_CHECKS_PASSED')
