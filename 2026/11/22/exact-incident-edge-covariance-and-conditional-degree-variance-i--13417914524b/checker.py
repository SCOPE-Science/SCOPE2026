"""Exact finite rank checks and geometry-conditioned degree variance for horizontal visibility graphs.
Requires Python standard library. Run: python checker.py
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
import random


def joint_formula(A,B,root,j,k):
    A,B=set(A),set(B)
    assert root not in A|B and j not in A and k not in B and j!=k and root not in {j,k}
    m,n,s=len(A),len(B),len(A&B)
    N=m+n-s
    if j in B and k in A: return Q(0)
    if j in B: return Q(2,(m+1)*(N+1)*(N+2))
    if k in A: return Q(2,(n+1)*(N+1)*(N+2))
    return Q(2,(N+2)*(N+3))*(Q(1,N+1)+Q(1,m+1)+Q(1,n+1))


def enumerate_exact(A,B,root,j,k):
    vs=sorted(set(A)|set(B)|{root,j,k})
    yes=0
    for order in permutations(vs):
        z={v:q for q,v in enumerate(order)}
        if all(z[x]<min(z[root],z[j]) for x in A) and all(z[x]<min(z[root],z[k]) for x in B): yes+=1
    return Q(yes,factorial(len(vs)))


def check_abstract():
    # all block sets on 7 vertices including all endpoint incidences, without simulating heights
    for n in range(3,8):
        root,j,k=0,1,2
        allA=[frozenset(q for q in range(1,n) if q!=j and (mask>>(q-1))&1) for mask in range(1<<(n-1))]
        allB=[frozenset(q for q in range(1,n) if q!=k and (mask>>(q-1))&1) for mask in range(1<<(n-1))]
        allA=list(set(allA));allB=list(set(allB))
        for A in allA:
            for B in allB:
                exact=enumerate_exact(A,B,root,j,k)
                expected=joint_formula(A,B,root,j,k)
                if exact!=expected:raise AssertionError((n,A,B,exact,expected))
        print('abstract n=',n,'pairs=',len(allA)*len(allB),'PASS')


def crossed(P,i,j):
    # Exact mathematical form of Voronoi interval constraints evaluated on given sites.
    # Strictly positive intersection with line segment (P[i],P[j]) is the obstacle criterion.
    x0,y0=P[i];dx=P[j][0]-x0;dy=P[j][1]-y0
    answer=set()
    for k,(kx,ky) in enumerate(P):
        if k in (i,j): continue
        low,high=0.0,1.0
        for l,(lx,ly) in enumerate(P):
            if l==k:continue
            # |P0+tD-Pk|^2 - |P0+tD-Pl|^2 <=0
            c=(x0-kx)**2+(y0-ky)**2-(x0-lx)**2-(y0-ly)**2
            slope=2*(dx*(lx-kx)+dy*(ly-ky))
            if abs(slope)<1e-12:
                if c>1e-10:high=-1
            elif slope>0:high=min(high,-c/slope)
            else:low=max(low,-c/slope)
            if high-low<1e-10: break
        if high-low>1e-9:answer.add(k)
    return answer


def check_geometric():
    random.seed(17232)
    for n in range(4,9):
        for q in range(16):
            P=[(random.random(),random.random()) for _ in range(n)]
            C={(i,j):crossed(P,i,j) for i in range(n) for j in range(n) if i!=j}
            for i in range(n):
                for j in range(n):
                    if j==i:continue
                    assert C[i,j]==C[j,i],('asymmetric cells!',n,q,i,j)
                for j in range(n):
                    if j==i:continue
                    for k in range(j+1,n):
                        if k==i:continue
                        assert joint_formula(C[i,j],C[i,k],i,j,k)==enumerate_exact(C[i,j],C[i,k],i,j,k)
        print('geometric n=',n,'random configurations=16 PASS')


def variance_formula(C,i,n):
    ps={j:Q(2,(len(C[i,j])+1)*(len(C[i,j])+2)) for j in range(n) if j!=i}
    mu=sum(ps.values(),Q(0))
    var=sum((p*(1-p) for p in ps.values()),Q(0))
    for j in ps:
        for k in ps:
            if k<=j:continue
            var+=2*(joint_formula(C[i,j],C[i,k],i,j,k)-ps[j]*ps[k])
    return mu,var


def check_variance():
    random.seed(28403)
    for n in range(3,8):
        for z in range(12):
            P=[(random.random(),random.random()) for _ in range(n)]
            C={(i,j):crossed(P,i,j) for i in range(n) for j in range(n) if i!=j}
            i=0
            vals=[]
            for perm in permutations(range(n)):
                order={t:v for t,v in enumerate(perm)}
                vals.append(sum(all(order[a]<min(order[i],order[j]) for a in C[i,j]) for j in range(n) if j!=i))
            em=Q(sum(vals),len(vals))
            ev=Q(sum(v*v for v in vals),len(vals))-em*em
            fm,fv=variance_formula(C,i,n)
            assert em==fm and ev==fv,(n,z,em,fm,ev,fv)
        print('variance n=',n,'random configurations=12 PASS')

def crossed_exact(P,i,j):
    """Exact-rational intersection of the segment with each Voronoi cell."""
    P=[(Q(x),Q(y)) for x,y in P]
    x0,y0=P[i]; dx=P[j][0]-x0; dy=P[j][1]-y0
    blockers=set()
    for k,(kx,ky) in enumerate(P):
        if k in (i,j):continue
        low,high=Q(0),Q(1)
        for l,(lx,ly) in enumerate(P):
            if l==k:continue
            c=(x0-kx)**2+(y0-ky)**2-(x0-lx)**2-(y0-ly)**2
            slope=2*(dx*(lx-kx)+dy*(ly-ky))
            if slope==0:
                if c>0:high=Q(-1)
            elif slope>0:
                high=min(high,-c/slope)
            else:
                low=max(low,-c/slope)
        if low<high:blockers.add(k)
    return blockers


def check_witnesses():
    # The specified four-site coordinate sets are exact integers; no floating-point geometry.
    witnesses=[
      ([(-7,-9),(-8,4),(7,-4),(-4,-1)],{3},{3},Q(5,36)),
      ([(-8,-4),(2,1),(0,9),(0,-5)],{3},{1},Q(-1,36)),
    ]
    for P,A,B,cov in witnesses:
        assert crossed_exact(P,0,1)==A and crossed_exact(P,0,2)==B
        # Four points are in general position: no three collinear, no four cocircular.
        from itertools import combinations
        for (x1,y1),(x2,y2),(x3,y3) in combinations(P,3):
            assert (x2-x1)*(y3-y1)!=(x3-x1)*(y2-y1)
        # Determinant of lifted [x,y,x*x+y*y,1] matrix.
        from itertools import permutations as perms
        M=[[x,y,x*x+y*y,1] for x,y in P]
        det=0
        for perm in perms(range(4)):
            inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
            v=1
            for i,j in enumerate(perm):v*=M[i][j]
            det+=(-1)**inv*v
        assert det!=0
        p=lambda C:Q(2,(len(C)+1)*(len(C)+2))
        assert joint_formula(A,B,0,1,2)-p(A)*p(B)==cov
    print('two integer-site opposite covariance signs with exact geometry PASS')

if __name__=='__main__':
    check_abstract()
    check_geometric()
    check_variance()
    check_witnesses()
    print('All exact finite-rank and Voronoi geometry checks passed.')
