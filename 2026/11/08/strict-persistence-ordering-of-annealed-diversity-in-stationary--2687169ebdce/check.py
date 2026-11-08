"""Independent finite-state checks of stationary refresh stick-breaking diversity identities.

Run: python check.py
Uses the standard library only; finite checks do not establish the theorem.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import log, isclose


def inverse(a):
    n = len(a)
    b = [[Q(x) for x in a[i]] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        t = next((i for i in range(k, n) if b[i][k]), None)
        assert t is not None
        b[k], b[t] = b[t], b[k]
        z = b[k][k]
        b[k] = [x / z for x in b[k]]
        for i in range(n):
            if i != k:
                z = b[i][k]
                b[i] = [b[i][j] - z * b[k][j] for j in range(2*n)]
    return [r[n:] for r in b]


def product_ratio(v, p, rho, q):
    a = [(1-x)**q for x in v]
    num = sum((p[i] * v[i]**q / (1-rho*a[i]) for i in range(len(v))), Q(0))
    den = sum((p[i] * (1-a[i]) / (1-rho*a[i]) for i in range(len(v))), Q(0))
    return num/den


def stationary_linear_system(v, p, rho, q):
    k = len(v)
    # Condition on state i and one future update. This solves a complete
    # finite-state rational linear system, separately from product_ratio.
    T = [[rho * int(i == j)+(1-rho)*p[j] for j in range(k)] for i in range(k)]
    mat = [[int(i == j) - (1-v[i])**q*T[i][j] for j in range(k)] for i in range(k)]
    inv = inverse(mat)
    f = [v[i]**q for i in range(k)]
    g = [sum((inv[i][j]*f[j] for j in range(k)), Q(0)) for i in range(k)]
    return sum((p[i]*g[i] for i in range(k)), Q(0))


def entropy_ratio(v, p, rho):
    def h(x):
        y=float(x)
        return -y*log(y)-(1-y)*log(1-y)
    num=sum(float(p[i])*h(v[i])/(1-float(rho)*(1-float(v[i]))) for i in range(len(v)))
    den=sum(float(p[i])*float(v[i])/(1-float(rho)*(1-float(v[i]))) for i in range(len(v)))
    return num/den


def entropy_linear(v,p,rho):
    k=len(v)
    T=[[float(rho*int(i==j)+(1-rho)*p[j]) for j in range(k)] for i in range(k)]
    m=[[float(int(i==j))-(1-float(v[i]))*T[i][j] for j in range(k)] for i in range(k)]
    # Rational inversion, times transcendental local entropies.
    matQ=[[Q(int(i==j))-(1-v[i])*(rho*int(i==j)+(1-rho)*p[j]) for j in range(k)] for i in range(k)]
    inv=inverse(matQ)
    h=[-float(x)*log(float(x))-(1-float(x))*log(1-float(x)) for x in v]
    g=[sum(float(inv[i][j])*h[j] for j in range(k)) for i in range(k)]
    return sum(float(p[i])*g[i] for i in range(k))


def direct_fraction_prefix(v, p, rho, q, depth):
    """Enumerate complete state paths up to depth; also return residual bound."""
    total = Q(0)
    rem = Q(0)
    k = len(v)
    for path in product(range(k), repeat=depth):
        probability = p[path[0]]
        for t in range(1,depth):
            probability *= rho*int(path[t]==path[t-1])+(1-rho)*p[path[t]]
        residual=Q(1)
        partial=Q(0)
        for state in path:
            x=v[state]
            partial += (residual*x)**q
            residual *= 1-x
        total += probability*partial
        rem += probability*residual**q
    return total, rem


def float_direct_markov(v, p, rho, q):
    """Solve a fresh floating-point linear system for fractional powers."""
    n=len(v)
    A=[[float(int(i==j))-(1-float(v[i]))**q * (float(rho)*int(i==j)+(1-float(rho))*float(p[j]))
        for j in range(n)] for i in range(n)]
    f=[float(x)**q for x in v]
    for k in range(n):
        pivot=max(range(k,n),key=lambda j:abs(A[j][k]))
        A[k],A[pivot]=A[pivot],A[k]
        f[k],f[pivot]=f[pivot],f[k]
        z=A[k][k]
        A[k]=[x/z for x in A[k]]
        f[k]/=z
        for i in range(n):
            if i==k:continue
            z=A[i][k]
            A[i]=[A[i][j]-z*A[k][j] for j in range(n)]
            f[i]-=z*f[k]
    return sum(float(p[i])*f[i] for i in range(n))


def run():
    exact=0
    approx=0
    for k in (2,3,4):
        for inds in combinations(range(1,9), k):
            v=[Q(j,10) for j in inds]
            p=[Q(j,k*(k+1)//2) for j in range(1,k+1)]
            for q in (2,3,4):
                last=None
                for rho in (Q(0),Q(1,5),Q(1,2),Q(4,5),Q(1)):
                    a=product_ratio(v,p,rho,q)
                    b=stationary_linear_system(v,p,rho,q)
                    assert a==b,(v,p,rho,q,a,b)
                    if last is not None:
                        assert last>a,(v,p,rho,q,last,a)
                    last=a
                    exact+=2
            last=None
            for rho in (Q(0),Q(1,5),Q(1,2),Q(4,5),Q(1)):
                q=0.5
                numerator=sum(float(p[i])*float(v[i])**q/(1-float(rho)*(1-float(v[i]))**q) for i in range(k))
                denominator=sum(float(p[i])*(1-(1-float(v[i]))**q)/(1-float(rho)*(1-float(v[i]))**q) for i in range(k))
                a=numerator/denominator
                b=float_direct_markov(v,p,rho,q)
                assert isclose(a,b,rel_tol=2e-12,abs_tol=1e-12)
                if last is not None:
                    assert a>last+1e-13
                last=a
                approx+=2
            last=None
            for rho in (Q(0),Q(1,5),Q(1,2),Q(4,5),Q(1)):
                a=entropy_ratio(v,p,rho)
                b=entropy_linear(v,p,rho)
                assert isclose(a,b,rel_tol=2e-12,abs_tol=1e-12)
                if last is not None:
                    assert a>last+1e-13
                last=a
                approx+=2
    # Two-point exact certificate at the endpoints.
    assert product_ratio([Q(1,4),Q(3,4)],[Q(1,2)]*2,Q(0),2)==Q(5,11)
    assert product_ratio([Q(1,4),Q(3,4)],[Q(1,2)]*2,Q(1),2)==Q(13,35)
    exact+=2
    for rho in (Q(0),Q(1,2),Q(1)):
        lower, remainder=direct_fraction_prefix([Q(1,4),Q(3,4)],[Q(1,2)]*2,rho,2,8)
        target=product_ratio([Q(1,4),Q(3,4)],[Q(1,2)]*2,rho,2)
        assert lower <= target <= lower + remainder
        exact+=1
    print(f"PASS: {exact} exact rational and {approx} float-accuracy assertions; two-point endpoints 5/11 and 13/35")

if __name__=='__main__':
    run()
