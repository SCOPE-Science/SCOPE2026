#!/usr/bin/env python3
"""Direct perfect-matching enumeration to verify a finite Fourier covariance theorem.

Run: python check_prism.py
Requires Python 3 standard library only. Exhaustive for the reported finite sizes;
not an infinite-dimensional proof.
"""
import cmath
import math


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def luc(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def enumerate_matchings(n):
    # Array layout: top cyclic edges, bottom cyclic edges, vertical rungs.
    edges = ([(i, (i+1)%n) for i in range(n)]
        + [(n+i, n+(i+1)%n) for i in range(n)]
        + [(i,n+i) for i in range(n)])
    full = (1<<(2*n))-1
    def fill(occupied, chosen):
        if occupied == full:
            yield chosen
            return
        v = next(i for i in range(2*n) if not (occupied>>i)&1)
        for j,(a,b) in enumerate(edges):
            if v not in (a,b):
                continue
            w = b if a == v else a
            if (occupied>>w)&1:
                continue
            yield from fill(occupied|(1<<v)|(1<<w), chosen+(j,))
    yield from fill(0, ())


def predicted(n):
    f, l = fib(n), luc(n)
    extra = 2 if n%2==0 else 0
    z = l+extra
    if n%2:
        s0 = f/(5*l)-n/(5*l*l)
    else:
        s0 = (f+n/2)/(5*z)
    spec=[6*s0]
    for k in range(1,n):
        c = math.cos(2*math.pi*k/n)
        spec.append(f*(4+2*c)/(z*(3+2*c)))
    if n%2==0:
        spec.append(n/z)
    return spec, z


def test_one(n):
    matches=list(enumerate_matchings(n))
    spec,z=predicted(n)
    assert len(matches)==z, (n,len(matches),z)
    ss=[]; dd=[]
    for match in matches:
        bits=set(match)
        ss.append([(int(i in bits)+int(n+i in bits))/2 for i in range(n)])
        dd.append([(int(i in bits)-int(n+i in bits))/2 for i in range(n)])
    z=len(matches)
    maxerr=0.0
    for k in range(n):
        w=[cmath.exp(-2j*math.pi*k*i/n) for i in range(n)]
        sums=[sum(x[i]*w[i] for i in range(n)) for x in ss]
        av=sum(sums)/z
        var=sum(abs(y)**2 for y in sums)/z-abs(av)**2
        scov=var/n
        # The edge-vector squared norm of the spatial sector is
        # (2+|1+exp(i theta)|^2) times the S-coordinate variance.
        c=math.cos(2*math.pi*k/n)
        got=(4+2*c)*scov
        maxerr=max(maxerr,abs(got-spec[k]))
        assert abs(got-spec[k])<1e-9,(n,k,got,spec[k])
        dvals=[sum(x[i]*w[i] for i in range(n)) for x in dd]
        md=sum(dvals)/z
        dvar=(sum(abs(y)**2 for y in dvals)/z-abs(md)**2)/n
        wanted=(n/(2*z) if (n%2==0 and k==n//2) else 0)
        assert abs(dvar-wanted)<1e-9,(n,k,dvar,wanted)
    if n%2==0:
        assert abs(max(spec)/min(spec)-2*fib(n)/n)<1e-9
    else:
        c=math.cos(math.pi/n)
        ratio=((4-2*c)/(3-2*c))*5/6 * (fib(n)*luc(n))/(fib(n)*luc(n)-n)
        assert abs(max(spec)/min(spec)-ratio)<1e-9
    return z,maxerr


def test_fibonacci_identity():
    for n in range(3,70):
        b=[]
        for d in range(n):
            left=1 if d==0 else fib(d-1)
            b.append(left*fib(n-d-1))
        for d in range(n):
            lhs=3*b[d]+b[(d-1)%n]+b[(d+1)%n]
            rhs=luc(n-2)+(fib(n) if d==0 else 0)
            assert lhs==rhs,(n,d,lhs,rhs)


def main():
    test_fibonacci_identity()
    print('Exact integer Fibonacci cyclic identity: PASS (n=3..69)')
    for n in range(3,17):
        z,error=test_one(n)
        print(f'n={n:2d} matchings={z:5d} max absolute Fourier error={error:.2e}')
    print('Direct finite-matchings Fourier checks: PASS (n=3..16)')
    print('Limitations: finite verification is not a proof of the all-n theorem.')

if __name__=='__main__':
    main()
