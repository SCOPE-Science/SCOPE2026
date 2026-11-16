#!/usr/bin/env python3
"""Independent finite tests of the positive triple Fourier-zero ray theorem.

Uses exact integer coefficients of the cyclotomic root to check the
triangle sine identity and Galois stabilizers. Its finite range is not
an infinite proof. Only the Python standard library is needed.
"""
import cmath
import math


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, math.isqrt(n) + 1))


def S(a, p):
    out = [0] * p
    out[a % p] += 1
    out[-a % p] -= 1
    return out


def cyclic_mul(a, b):
    p = len(a)
    c = [0] * p
    for j, aj in enumerate(a):
        if aj:
            for k, bk in enumerate(b):
                if bk:
                    c[(j+k) % p] += aj * bk
    return c


def sub(a,b):
    return [x-y for x,y in zip(a,b)]


def is_zero_cyclo(a):
    # A degree < p polynomial vanishes at primitive pth root iff
    # it is an integer multiple of 1+X+...+X^(p-1).
    return all(x == a[0] for x in a)


def test_prime(p):
    m=(p-1)//2
    reps=[]
    nchecks=0
    exact_fourier_checks=0
    for u in range(1,p):
        for v in range(u+1,p):
            if max(u,v-u,p-v)>m:
                continue
            reps.append((u,v))
            # Exact vanishing of S(v-u) - S(v)*zeta^u + S(u)*zeta^v.
            f=[0]*p
            for j,x in enumerate(S(v-u,p)):
                f[j]+=x
            for j,x in enumerate(S(v,p)):
                f[(j+u)%p]-=x
            for j,x in enumerate(S(u,p)):
                f[(j+v)%p]+=x
            assert is_zero_cyclo(f),(p,u,v,'identity')
            # Exhaust all p^2 Fourier pairs exactly for moderate primes.
            if p <= 19:
                zero_pairs=[]
                for U in range(p):
                    for V in range(p):
                        test=list(S(v-u,p))
                        for j,x in enumerate(S(v,p)):
                            test[(j+U)%p]-=x
                        for j,x in enumerate(S(u,p)):
                            test[(j+V)%p]+=x
                        if is_zero_cyclo(test):
                            zero_pairs.append((U,V))
                        exact_fourier_checks+=1
                assert sorted(zero_pairs)==sorted([(u,v),((-u)%p,(-v)%p)]),(p,u,v,zero_pairs)
            # Distinct Galois conjugates of the real projective ratio pair.
            denom=S(v-u,p)
            for s in range(2,p-1):
                b=sub(cyclic_mul(S(s*v,p),denom),
                      cyclic_mul(S(v,p),S(s*(v-u),p)))
                c=sub(cyclic_mul(S(s*u,p),denom),
                      cyclic_mul(S(u,p),S(s*(v-u),p)))
                assert not (is_zero_cyclo(b) and is_zero_cyclo(c)),(p,u,v,s)
                nchecks+=1
            A=math.sin(2*math.pi*(v-u)/p)
            B=-math.sin(2*math.pi*v/p)
            C=math.sin(2*math.pi*u/p)
            assert min(A,B,C)>1e-10,(p,u,v,A,B,C)
            z=cmath.exp(2j*math.pi/p)
            assert abs(A+B*z**u+C*z**v)<2e-11,(p,u,v)
            # Distinct phase assignments are the only possible conjugate zero pair.
            for U,V in ((u,v),(v,u)):
                x=(A,B,C) if U==u else (A,C,B)
                matches=[]
                for k in range(p):
                    w=cmath.exp(2j*math.pi*k/p)
                    if abs(x[0]+x[1]*w+x[2]*w**(V*pow(U,-1,p)%p))<2e-10:
                        matches.append(k)
                # The test here is a lightweight check on the subgroup line;
                # the proof treats all p^2 characters, not only this slice.
                assert len(matches)==2,(p,u,v,U,V,matches)
    assert len(reps)==(p*p-1)//8,(p,len(reps))
    return len(reps),nchecks,exact_fourier_checks


def main():
    total=0
    checks=0
    echecks=0
    for p in [n for n in range(5,54) if is_prime(n)]:
        rays,n,exact=test_prime(p)
        total+=rays
        checks+=n
        echecks+=exact
        print(f'p={p}: {rays} projective ray representatives; {n} exact Galois comparisons')
    print(f'PASS: {total} ray representatives, {checks} exact Galois nonstabilizer comparisons, {echecks} exact Fourier-pair tests, exact vanishing identities.')

if __name__=='__main__':
    main()
