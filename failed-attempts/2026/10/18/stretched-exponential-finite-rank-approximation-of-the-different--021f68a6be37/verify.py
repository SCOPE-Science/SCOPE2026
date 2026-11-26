#!/usr/bin/env python3
"""Finite reproducibility checks for the differential-Hilbert quadrature theorem.
Uses only the Python standard library. These finite tests do not prove the infinite theorem.
"""
import math


def gauss_legendre(n, low, high):
    """Positive Gauss-Legendre nodes and weights on the specified interval."""
    assert n >= 1 and 0 <= low < high <= 1
    nodes = [0.0] * n
    weights = [0.0] * n
    for i in range((n + 1) // 2):
        z = math.cos(math.pi * (i + 0.75) / (n + 0.5))
        for _ in range(50):
            p0, p1 = 1.0, z
            if n == 1:
                pn, prev = z, 1.0
            else:
                for j in range(2, n + 1):
                    p0, p1 = p1, ((2*j - 1)*z*p1 - (j-1)*p0)/j
                pn, prev = p1, p0
            d = n * (z*pn - prev)/(z*z - 1)
            next_z = z - pn/d
            if abs(next_z - z) < 2e-15:
                z = next_z
                break
            z = next_z
        # recompute derivative at converged z
        p0, p1 = 1.0, z
        if n == 1:
            pn, prev = z, 1.0
        else:
            for j in range(2,n+1):
                p0,p1 = p1,((2*j-1)*z*p1-(j-1)*p0)/j
            pn,prev=p1,p0
        d=n*(z*pn-prev)/(z*z-1)
        w = 2 / ((1-z*z)*d*d)
        t1, t2 = (low+high)/2-(high-low)*z/2,(low+high)/2+(high-low)*z/2
        nodes[i], nodes[n-1-i] = t1, t2
        weights[i] = weights[n-1-i] = (high-low)*w/2
    return list(zip(nodes,weights))


def weights(gamma, n):
    a = [1.0]
    for j in range(n-1):
        a.append(a[-1]*(j+1)/(j+gamma+2))
    return a


def exact_matrix(alpha,beta,n):
    wa,wb = weights(alpha,n),weights(beta,n)
    return [[(r+1)/(r+k+1)*math.sqrt(wb[r]/wa[k]) for k in range(n)] for r in range(n)]


def approximate_matrix(alpha,beta,n,J,m):
    wa,wb = weights(alpha,n),weights(beta,n)
    a = [[0.0]*n for _ in range(n)]
    for j in range(J):
        low,high = 1.0-2.0**(-j),1.0-2.0**(-j-1)
        for t,w in gauss_legendre(m,low,high):
            base = [t**i for i in range(2*n-1)]
            for row in range(n):
                factor = w*(row+1)*math.sqrt(wb[row])
                for k in range(n):
                    a[row][k] += factor*base[row+k]/math.sqrt(wa[k])
    return a


def frobenius_diff(A,B):
    return math.sqrt(sum((x-y)**2 for ra,rb in zip(A,B) for x,y in zip(ra,rb)))


def check():
    assertions = 0
    for n in (1,2,3,4,8,12):
        for j in range(5):
            a,b = 1.0-2.0**(-j),1.0-2.0**(-j-1)
            nodes=gauss_legendre(n,a,b)
            assert len(nodes)==n
            assert all(a<x<b and w>0 for x,w in nodes)
            assert abs(sum(w for _,w in nodes)-(b-a))<1e-13
            assertions+=2
            for degree in range(2*n):
                # Work on [0,1] instead of differences of nearby powers.
                # Checking on dyadic I_j also tests affine transformations.
                got=sum(w*((x-a)/(b-a))**degree for x,w in nodes)
                expected=(b-a)/(degree+1)
                assert abs(got-expected)<4e-13, (n,j,degree,got,expected)
                assertions+=1
    for gamma in (-0.75,-0.5,1.6,1.75,2.0,2.7):
        w=weights(gamma,24)
        for i,v in enumerate(w):
            target=math.exp(math.lgamma(gamma+2)+math.lgamma(i+1)-math.lgamma(i+gamma+2))
            assert abs(v-target)/target<1e-12
            assertions+=1
    for alpha,beta in ((-0.75,1.6),(-0.5,1.75),(-0.5,2.0),(-0.25,2.7)):
        n=18
        exact=exact_matrix(alpha,beta,n)
        errors=[]
        for J,m in ((2,4),(4,8),(8,12),(14,18)):
            q=approximate_matrix(alpha,beta,n,J,m)
            err=frobenius_diff(exact,q)
            errors.append(err)
        assert all(x>y for x,y in zip(errors, errors[1:])),(alpha,beta,errors)
        assert errors[-1]<2e-3,(alpha,beta,errors)
        assertions+=2
        print(f'alpha={alpha:5.2f}, beta={beta:5.2f}, truncated Frobenius errors: '+', '.join(f'{x:.6g}' for x in errors))
    print(f'CHECKS_OK: {assertions} exact-node/weight, moment, coefficient and finite-matrix assertions')


if __name__ == '__main__':
    check()
