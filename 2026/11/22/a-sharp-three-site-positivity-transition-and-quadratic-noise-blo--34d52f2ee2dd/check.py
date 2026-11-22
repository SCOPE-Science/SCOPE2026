"""Independent numerical consistency checks for symmetric three-site crowding.

Usage: python check.py
Requires only the Python standard library. Finite checks supplement the proof.
"""
import cmath
import math


def csc(x):
    return 1.0 / math.sin(x)


def weights(n, u):
    assert n >= 3 and n % 2 == 1 and 0 <= u < 1
    if u == 0:
        return [1 / n] * n
    t = math.pi / n
    f = lambda y: csc(t * y)
    s = f(u) - f(2 - u)
    w = [0.0] * n
    w[0] = w[2] = 1 / (math.sin(math.pi * u) * s)
    w[1] = (1 - 2 * f(1 - u) / s) / n
    for j in range(3, n):
        w[j] = (1 - (-1)**j * (f(j - 2 + u) - f(j - u)) / s) / n
    return w


def ratio(n, u):
    t = math.pi / n
    f = lambda y: csc(t * y)
    return 2*f(1-u) / (f(u)-f(2-u))


def threshold(n):
    lo, hi = 1e-8, 0.5
    assert ratio(n, lo) < 1 < ratio(n, hi)
    for _ in range(70):
        mid = (lo + hi) / 2
        if ratio(n, mid) > 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def nodes(n, u):
    h = 2 * math.pi / n
    return [u*h, h, (2-u)*h] + [j*h for j in range(3, n)]


def check():
    tests = 0
    for n in list(range(3, 42, 2)) + [51, 71, 101]:
        q = threshold(n)
        assert 0 < q < 0.5
        tests += 1
        for u in [0, 0.02, 0.11, q * 0.8, q, (q+0.5)/2, 0.5, 0.72, 0.9, 0.98]:
            w = weights(n, u)
            assert abs(sum(w)-1) < 1e-8, (n,u,sum(w))
            assert min(w[i] for i in range(n) if i!=1)>0, (n,u,w)
            if u < q-1e-9:
                assert w[1] > 0, (n,u,w[1])
            if u > q+1e-9:
                assert w[1] < 0, (n,u,w[1])
            predicted = 1+(2/n)*max(0,ratio(n,u)-1) if u!=0 else 1
            assert abs(sum(abs(x) for x in w)-predicted)<1e-8, (n,u)
            xs = nodes(n,u)
            for k in range(-(n//2),n//2+1):
                moment = sum(wj*cmath.exp(1j*k*x) for wj,x in zip(w,xs))
                assert abs(moment-(1 if k==0 else 0))<1e-8, (n,u,k,moment)
                tests += 1
            tests += 5
    assert abs(threshold(3)-.25)<1e-12
    tests += 1
    for n in [31,71,151,301,601,1201]:
        q=threshold(n)
        pred=1-1/math.sqrt(2)-math.pi**2/(24*math.sqrt(2)*n*n)
        assert abs(q-pred) < 4/n**4, (n,q,pred)
        tests+=1
    for n in [3,5,9,21,51]:
        t=math.pi/n
        exact=2*math.sin(t)**2/(n*t*t*math.cos(t))
        for eps in [.001,.0002]:
            observed=eps**2*sum(abs(w) for w in weights(n,1-eps))
            assert abs(observed-exact)/exact<.005, (n,eps,observed,exact)
            tests+=1
    print(f'PASS {tests} numerical assertions across odd Fourier grids, exactness, positivity, critical point and blowup')

if __name__ == '__main__':
    check()
