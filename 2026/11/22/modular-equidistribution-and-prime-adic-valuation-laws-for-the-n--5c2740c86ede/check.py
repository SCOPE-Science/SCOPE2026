"""Reproduce the modular orbit and direct-value checks for a ternary algebraic-integer sequence.
Run with Python 3, no dependencies.
"""
from collections import Counter, deque
from fractions import Fraction
from math import gcd


def step(state, r, m):
    a, b, parity = state
    if parity == 0:
        if r == 0: return (a, (2*a+b) % m, 0)
        if r == 1: return ((2*a+b) % m, (a+b) % m, 1)
        return ((a+b) % m, b, 0)
    if r == 0: return (a, (a+b) % m, 1)
    if r == 1: return ((a+b) % m, (a+2*b) % m, 0)
    return ((a+2*b) % m, b, 1)


def state_from_digits(n, m):
    state = (0, 1 % m, 0)
    digits = []
    while n:
        digits.append(n % 3)
        n //= 3
    for r in reversed(digits):
        state = step(state, r, m)
    return state


def expected_orbit(m):
    return {(a,b,e) for a in range(m) for b in range(m) for e in range(2)
            if gcd(gcd(a,b),m) == 1 and (m % 2 == 1 or (b % 2 if e == 0 else a % 2))}


def actual_orbit(m):
    init = (0,1%m,0)
    seen = {init}; todo=deque([init])
    while todo:
        s=todo.popleft()
        for r in range(3):
            t=step(s,r,m)
            if t not in seen:
                seen.add(t);todo.append(t)
    return seen


def expected_marginal(a,m):
    k=0; q=m
    while q%2==0:
        q//=2; k+=1
    two=Fraction(1) if k==0 else Fraction(3 if a%2 else 1, 2**(k+1))
    odd=Fraction(1,q)
    h=q; p=3
    while p*p<=h:
        if h%p==0:
            odd*=Fraction(p-1 if a%p==0 else p,p)/Fraction(p*p-1,p*p)
            while h%p==0: h//=p
        p+=2
    if h>1:
        odd*=Fraction(h-1 if a%h==0 else h,h)/Fraction(h*h-1,h*h)
    return two*odd


def direct_coefficients(N):
    # Independently construct a_n = u_n + v_n sqrt(2) in Z[sqrt(2)].
    u=[0]*N;v=[0]*N;u[1]=1
    for n in range((N-1)//3+1):
        if 3*n<N:
            u[3*n]=u[n]
            v[3*n]=v[n]
        if 3*n+1<N:
            u[3*n+1]=2*v[n]+u[n+1]
            v[3*n+1]=u[n]+v[n+1]
        if 3*n+2<N:
            u[3*n+2]=u[n]+2*v[n+1]
            v[3*n+2]=v[n]+u[n+1]
    return u,v


def run():
    for m in range(2,49):
        o=actual_orbit(m);wanted=expected_orbit(m)
        assert o==wanted, (m, len(o),len(wanted),o.symmetric_difference(wanted))
        counts=Counter(a for a,b,e in o)
        for a in range(m):
            assert Fraction(counts[a],len(o))==expected_marginal(a,m), (m,a)
    print('PASS: exact orbits and marginals for every modulus 2..48')
    N=3**9
    u,v=direct_coefficients(N+1)
    for n in range(N):
        assert (u[n]==0 if n%2==0 else v[n]==0)
        c=(v[n] if n%2==0 else u[n])
        assert c>=0
        for m in (2,3,4,5,6,8,9,10,12,16,25,32,49):
            assert (c%m, (v[n+1] if (n+1)%2==0 else u[n+1])%m, n%2)==state_from_digits(n,m),(n,m)
    print('PASS: independent direct algebraic-integer recurrence vs digit matrix for',N,'indices across 13 moduli')
    for L in range(10):
        count=sum(1 for n in range(3**L) if (v[n] if n%2==0 else u[n])%2==0)
        exact=(3**L+2+(-1)**L)//4
        assert count==exact,(L,count,exact)
    print('PASS: exact parity population for all ternary levels 0..9')

if __name__=='__main__':run()
