#!/usr/bin/env python3
"""Finite diagnostics for Sturmian-indexed gap shift entropy phases.

No finite test is used in place of the infinite symbolic/renewal proof.
Uses only Python standard library.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
from math import floor


def golden_alpha():
    return (Decimal(5).sqrt() - 1) / 2


def digit(alpha, j, theta=Decimal(0)):
    a = theta + Decimal(j) * alpha
    b = a + alpha
    return int(b // 1) - int(a // 1)


def root(alpha, cutoff=None, terms=550):
    seq = [digit(alpha, j) for j in range(terms)]
    def f(x):
        r = 1 / x
        power = r
        total = Decimal(0)
        for j, a in enumerate(seq):
            if cutoff is None:
                coeff = a
            elif j < cutoff:
                coeff = a
            else:
                coeff = 1
            if coeff:
                total += power
            power *= r
        if cutoff is not None:
            # Replace truncated tail with the exact geometric tail.
            total += power / (1-r)
        return total
    lo, hi = Decimal(1), Decimal(2)
    for _ in range(250):
        mid = (lo + hi) / 2
        if f(mid)>1:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def disc_sum(alpha, x, terms=500):
    r = 1/x
    s = Decimal(0)
    power=r
    for j in range(terms):
        if digit(alpha,j):
            s += Decimal(j+1)*power
        power *= r
    return s


def discounted(alpha, theta, r, terms=500):
    p = Decimal(1)
    out = Decimal(0)
    for j in range(terms):
        out += digit(alpha,j,theta)*p
        p *= r
    return out


def direct_allowed(word, alpha):
    positions = [i for i,c in enumerate(word) if c=='1']
    for a,b in zip(positions, positions[1:]):
        if not digit(alpha,b-a-1):
            return False
    return True


def cover_allowed(word, alpha, N):
    positions = [i for i,c in enumerate(word) if c=='1']
    for a,b in zip(positions, positions[1:]):
        d=b-a-1
        if d < N and not digit(alpha,d):
            return False
    return True


def main():
    with localcontext() as ctx:
        ctx.prec=90
        alpha=golden_alpha()
        x=root(alpha)
        T=disc_sum(alpha,x)
        r=1/x
        # Independent finite language check of the canonical cover cutoff.
        checked=0
        for N in range(1,10):
            for length in range(1,11):
                for k in range(2**length):
                    word=format(k,f'0{length}b')
                    # Independent local-window definition of the canonical cover:
                    # each visible window of length <= N+1 is a word of the base shift.
                    windows_valid = all(
                        direct_allowed(word[i:i+l], alpha)
                        for l in range(1, min(len(word), N+1)+1)
                        for i in range(len(word)-l+1)
                    )
                    assert cover_allowed(word,alpha,N)==windows_valid
                    checked+=1
        assert checked==18414, checked
        # Inclusion is strict precisely when next gap length is disallowed.
        for N in range(1,24):
            w='1'+'0'*N+'1'
            assert cover_allowed(w,alpha,N)
            assert cover_allowed(w,alpha,N+1)==bool(digit(alpha,N))
        # Every jump at -n alpha has the predicted geometric width.
        eps=Decimal('1e-25')
        max_jump_err=Decimal(0)
        for n in range(1,19):
            theta = -(Decimal(n)*alpha)
            theta -= theta.to_integral_value(rounding=ROUND_FLOOR)
            left=discounted(alpha,theta-eps,r)
            right=discounted(alpha,theta+eps,r)
            expected=(1-r)*r**(n-1)
            err=abs((right-left)-expected)
            max_jump_err=max(max_jump_err,err)
            assert err<Decimal('1e-18'), (n,err)
        # Total interval length and total removed gap length both equal 1.
        eps=Decimal('1e-25')
        span=discounted(alpha,1-eps,r)-discounted(alpha,eps,r)
        assert abs(span-1)<Decimal('1e-18')
        assert abs(sum(((1-r)*r**(n-1) for n in range(1,450)),Decimal(0))-1)<Decimal('1e-60')
        # Uniform root expansion along distinct Sturmian phases.
        errors=[]
        for N in (12,18,24,30,40,52,64,82):
            xn=root(alpha,cutoff=N)
            hn=xn.ln()
            h=x.ln()
            scaled=x**(N+1)*(hn-h)
            R=sum((Decimal(1-digit(alpha,N+j))*r**j for j in range(350)),Decimal(0))/T
            err=abs(scaled-R)
            errors.append((N,err))
            assert err < Decimal(4)*Decimal(N+1)*r**N
        print('PASS canonical cover membership',checked,'finite comparisons')
        print('PASS exact plateau witnesses',23)
        print('PASS jump-width comparisons',18,'max_error=',max_jump_err)
        print('PASS hull and jump-sum normalization; span=',span)
        print('PASS normalized finite-cover root comparisons',len(errors))
        print('alpha=',str(alpha)[:32])
        print('lambda=',str(x)[:35])
        print('T=',str(T)[:35])
        print('hull_length=',str(1/T)[:35])
        print('first_gap=',str((1-r)/T)[:35])
        print('error_samples=',[(n,str(e)[:14]) for n,e in errors])

if __name__=='__main__':
    main()
