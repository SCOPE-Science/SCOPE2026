#!/usr/bin/env python3
"""Exact finite checks for the dyadic Kepler set of Fibonacci quotients."""
from collections import Counter


def v2(x):
    assert x != 0
    x = abs(x)
    return (x & -x).bit_length() - 1


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def main():
    total=0
    # Fibonacci and Lucas valuations, and the signed Cassini difference.
    F=[0,1]
    for _ in range(1,2000):
        F.append(F[-1]+F[-2])
    for n in range(1,901):
        expected=0 if n%3 else (1 if n%6 else v2(n)+2)
        assert v2(F[n])==expected
        total+=1
        if n%6==0:
            L=F[n-1]+F[n+1]
            assert L%4==2 and F[2*n]==F[n]*L
            total+=2
    for n in range(1,70):
        for m in range(n+1,85):
            assert F[n+1]*F[m]-F[m+1]*F[n]==(-1)**n*F[m-n]
            total+=1
    # Check every modular class and fiber in one full period.
    for k in range(3,13):
        mod=1<<k
        z=3*(1<<(k-2))
        period=2*z
        F=[0,1]
        for _ in range(period):
            F.append((F[-1]+F[-2])%mod)
        q=[];s=[]
        for n in range(1,period+1):
            if n%3:
                assert F[n]&1
                q.append((F[n+1]*pow(F[n],-1,mod))%mod)
            else:
                assert F[n+1]&1
                s.append((F[n]*pow(F[n+1],-1,mod))%mod)
        cq,cs=Counter(q),Counter(s)
        Aq={a for a in range(mod) if a%8 in (0,1,2,7)}
        As={a for a in range(mod) if a%8 in (0,6)}
        assert set(cq)==Aq and set(cs)==As
        assert len(q)==1<<k and len(s)==1<<(k-1)
        assert len(cq)==1<<(k-1) and len(cs)==1<<(k-2)
        assert set(cq.values())=={2} and set(cs.values())=={2}
        total+=len(q)+len(s)+5
        # exact collision iff indices equivalent modulo z, for both types
        for n in range(1,period+1):
            r=(F[n+1]*pow(F[n],-1,mod))%mod if n%3 else (F[n]*pow(F[n+1],-1,mod))%mod
            m=n+z
            if m<=period:
                t=(F[m+1]*pow(F[m],-1,mod))%mod if m%3 else (F[m]*pow(F[m+1],-1,mod))%mod
                assert r==t
                total+=1
    print(f"CHECK_OK {total} exact assertions")


if __name__=='__main__':
    main()
