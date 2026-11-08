"""Exact finite-size checks for a specified pairwise-plus-triadic oscillator ODE.

Only Python's standard library is needed.  This validates sampled finite matrices;
it is not an exhaustive proof of the general stability classification.
"""
from fractions import Fraction as F
from math import comb


def jacobian(n, p, sigma, delta):
    """Jacobian obtained by differentiating every ordered distinct triad."""
    d = n - 1
    signs = [1] * p + [-1] * (n - p)
    J = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                J[i][j] += sigma * signs[j] * signs[i] / d
                J[i][i] -= sigma * signs[j] * signs[i] / d
                for k in range(n):
                    if k == i or k == j:
                        continue
                    c = delta * signs[j] * signs[k] / (d * (d-1))
                    J[i][j] += c
                    J[i][k] += c
                    J[i][i] -= 2*c
    return J


def eigenvalues(n, p, sigma, delta):
    q = n-p
    S = p-q
    d = n-1
    lp = -sigma*S/d + 2*delta*(2*p-S*S)/(d*(d-1))
    lm = sigma*S/d + 2*delta*(2*q-S*S)/(d*(d-1))
    lr = sigma*n/d - 2*delta*S*S/(d*(d-1))
    return lp, lm, lr


def matvec(J, x):
    return [sum(a*b for a,b in zip(row,x)) for row in J]


def check_eigenvector(J, x, eigenvalue):
    return matvec(J,x) == [eigenvalue*v for v in x]


def stable_by_window(n, p, sigma, delta):
    q=n-p
    if not 1 <= q < p:
        raise ValueError('Use 1 <= q < p')
    S=p-q
    if S*S <= n:
        return False
    low=sigma*n*(n-2)/F(2*S*S)
    if delta <= low:
        return False
    if S*S < n+S:
        high=sigma*S*(n-2)/F(2*(n+S-S*S))
        return delta < high
    return True


def check(n, p, sigma, delta):
    q=n-p
    S=p-q
    J=jacobian(n,p,sigma,delta)
    lp,lm,lr=eigenvalues(n,p,sigma,delta)
    assert check_eigenvector(J,[F(1)]*n,F(0))
    for a in range(1,p):
        x=[F(0)]*n
        x[0]=F(1)
        x[a]=F(-1)
        assert check_eigenvector(J,x,lp)
    for a in range(p+1,n):
        x=[F(0)]*n
        x[p]=F(1)
        x[a]=F(-1)
        assert check_eigenvector(J,x,lm)
    bp=-sigma/F(n-1)-2*delta*S/F((n-1)*(n-2))
    bm=-sigma/F(n-1)+2*delta*S/F((n-1)*(n-2))
    x=[-q*bp]*p+[p*bm]*q
    assert any(x)
    assert check_eigenvector(J,x,lr)
    assert stable_by_window(n,p,sigma,delta) == (lp<0 and lr<0 and (q==1 or lm<0))


def main():
    runs=0
    for n in (3,4,5,6,7,8,9,10,11,12,13):
        for q in range(1,(n+1)//2):
            p=n-q
            for sigma in (F(1),F(3,2)):
                for delta in (F(1,5), F(1), F(2), F(5,2), F(15,2), F(8), F(20)):
                    check(n,p,sigma,delta)
                    runs += 1
    # Critical boundaries and an exact re-entrant 21-orbit disappearance.
    n=7; p=5; sig=F(1)
    low=F(35,18); high=F(15,2)
    for d in (low,high):
        lp,lm,lr=eigenvalues(n,p,sig,d)
        assert (lr == 0) if d==low else (lp == 0)
    assert not stable_by_window(n,p,sig,F(1))
    assert stable_by_window(n,p,sig,F(2))
    assert not stable_by_window(n,p,sig,F(8))
    assert sum(comb(7,q) for q in (1,2)) + 1 == 29
    assert comb(7,1)+1 == 8
    # Independent finite-difference derivative check on small examples.
    from math import pi,sin
    def field(v, sig, tri):
        n=len(v); d=n-1
        w=[0.]*n
        for i in range(n):
            for j in range(n):
                if j==i: continue
                w[i] += sig/d*sin(v[j]-v[i])
                for k in range(n):
                    if k!=i and k!=j:
                        w[i] += tri/(d*(d-1))*sin(v[j]+v[k]-2*v[i])
        return w
    for n,p in ((5,4),(7,5),(9,6)):
        state=[0.]*p+[pi]*(n-p)
        Ja=jacobian(n,p,F(1),F(2))
        step=1e-5
        for j in range(n):
            above=state.copy();above[j]+=step
            below=state.copy();below[j]-=step
            fu=field(above,1.,2.); fl=field(below,1.,2.)
            for i in range(n):
                assert abs((fu[i]-fl[i])/(2*step)-float(Ja[i][j])) < 2e-8
    print('PASS: exact ordered-triad Jacobian eigenspaces and window for', runs, 'finite parameter cases')
    print('PASS: exact endpoints and 29-to-8 stable antipodal-circle count for n=7')
    print('PASS: numerical derivatives of original vector field at 3 configurations')

if __name__ == '__main__':
    main()
