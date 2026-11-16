"""Reproducibility checks for Ewens derangement assignment-score spectra.

Python 3 standard library only. Finite assertions support, but do not replace,
proofs for all dimensions and all positive activity parameters.
"""
from fractions import Fraction as F
from itertools import permutations
from math import isclose


def norm(n, t):
    z = [F(1), F(0)]
    for m in range(2, n + 1):
        z.append((m-1) * (z[-1] + t*z[-2]))
    return z


def cycles(perm):
    n = len(perm)
    marked = set()
    total = 0
    for i in range(n):
        if i not in marked:
            j = i
            while j not in marked:
                marked.add(j)
                j = perm[j]
            total += 1
    return total


def data(n,t):
    perms = []
    weights = []
    for p in permutations(range(n)):
        if all(p[i] != i for i in range(n)):
            perms.append(p)
            weights.append(t ** cycles(p))
    return perms, weights, sum(weights)


def main():
    checks = 0
    for n in range(4,9):
        for t in (F(1,2), F(2,3), F(1), F(2)):
            ps, ws, den = data(n,t)
            z=norm(n,t)
            assert den == z[n]; checks += 1
            def prob(edges):
                return sum(w for p,w in zip(ps,ws) if all(p[i]==j for i,j in edges))/den
            p = F(1,n-1)
            q2 = t*z[n-2]/z[n]
            qc = (z[n-2]+t*z[n-3])/z[n]
            qd = (z[n-2]+2*t*z[n-3]+t*t*z[n-4])/z[n]
            for obs, exp in [
                (prob([(0,1)]),p),
                (prob([(0,1),(1,0)]),q2),
                (prob([(0,1),(1,2)]),qc),
                (prob([(0,1),(2,3)]),qd),
            ]:
                assert obs == exp,(n,t,obs,exp)
                checks+=1
            lm = p+(2-t)*z[n-2]/z[n]+2*t*z[n-3]/z[n]
            lp = p+(t*z[n-2]+2*t*z[n-3]+2*t*t*z[n-4])/z[n]
            assert lp-lm == 2*((t-1)*z[n-2]+t*t*z[n-4])/z[n];checks+=1
            assert lm>0 and lp>0;checks+=1
            def covariance_score(A):
                vv=[]
                for perm in ps:
                    vv.append(sum(A[i][perm[i]] for i in range(n)))
                mean=sum(w*v for w,v in zip(ws,vv))/den
                return sum(w*(v-mean)**2 for w,v in zip(ws,vv))/den
            # A zero-margin skew 3-cycle circulation, supported on first three vertices.
            sk=[[F(0) for j in range(n)] for i in range(n)]
            for i,j in [(0,1),(1,2),(2,0)]:
                sk[i][j]=F(1);sk[j][i]=F(-1)
            assert covariance_score(sk)==lm*6;(n,t)
            checks+=1
            # A symmetric zero-margin 4-cycle: +/- on alternating undirected edges.
            sy=[[F(0) for j in range(n)] for i in range(n)]
            for i,j,s in [(0,1,1),(1,2,-1),(2,3,1),(3,0,-1)]:
                sy[i][j]=F(s);sy[j][i]=F(s)
            assert covariance_score(sy)==lp*8,(n,t)
            checks+=1
    # The isotropic roots: bisection using exact integer-polynomial recurrence.
    roots={4:.5,5:1.0,6:(105**.5-3)/8,7:(133**.5-1)/11}
    for n,expected in roots.items():
        def gap(t):
            z=norm(n,F(t))
            return (t-1)*z[n-2]+t*t*z[n-4]
        assert abs(float(gap(F(str(expected)))))<1e-9,(n,expected)
        checks+=1
    for n in (8,10,12,20,32,64,128):
        l=0.;u=1.
        for _ in range(65):
            m=(l+u)/2
            z=norm(n,F(str(m)))
            g=(m-1)*z[n-2]+m*m*z[n-4]
            if g>0: u=m
            else:l=m
        root=(l+u)/2
        assert 0<root<1
        if n>=64:
            assert abs((1-root)*n*n-1)<.12,(n,root,(1-root)*n*n)
        checks+=1
    print('PASS:',checks,'exact weighted-permutation, eigenvalue, root and asymptotic checks')

if __name__=='__main__': main()
