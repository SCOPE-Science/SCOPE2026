"""Finite sanity checks for the beta-prior finite-time mean theorem.
Only numerical tests; the general limit statements are proved in RESULT.md.
"""
import math


def sigmoid_minus(y):
    if y >= 0:
        e = math.exp(-y)
        return e/(1+e)
    e = math.exp(y)
    return 1/(1+e)


def sample_mean(a, b, r, n):
    y = a*n*r
    z = 0.
    for _ in range(n):
        x = sigmoid_minus(y)
        z += x
        y += a*(x-b)
    return z/n, b + (y-a*n*r)/(a*n)


def limit_mean(b,r):
    return max(0., min(1., b-r))


def rate(a,b,p,q,y):
    return a*p*(b-y) if y<=b else a*q*(y-b)


def log_slope_at(a,b,p,q,t):
    if t < -a*p:
        return -a*p*b
    if t > a*q:
        return t - a*q*(1-b)
    return b*t


def run():
    tests = 0
    for a,b in ((.2,.17),(2.7,.6),(4.,.31),(3.95,.83)):
        for n in (500,1500):
            for r in (-1.2,-.7,-.15,0.,.05,.2,.5,.9,1.4):
                x, telescoped=sample_mean(a,b,r,n)
                assert abs(x-telescoped) < 1e-12, (a,b,r,n)
                # Use a moderate finite-horizon tolerance for near-boundary transitions.
                assert abs(x-limit_mean(b,r)) < .022, (a,b,r,n,x,limit_mean(b,r))
                tests+=1
    for a,b,p,q in ((1.2,.37,2.,3.),(3.8,.81,.5,4.),(.25,.12,3.,.7)):
        for t in (-9.,-a*p-1e-5,-a*p,0.,a*q,a*q+1e-5,9.):
            claimed=log_slope_at(a,b,p,q,t)
            grid=max(t*y-rate(a,b,p,q,y) for y in (k/10000 for k in range(10001)))
            assert abs(claimed-grid)< 0.001,(a,b,p,q,t,claimed,grid)
            tests+=1
    print('PASS',tests,'finite numerical checks; no numerical inference used for infinite theorem')
if __name__=='__main__':
    run()
