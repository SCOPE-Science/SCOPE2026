#!/usr/bin/env python3
"""Exact coefficient checks for two partition generating series (standard library)."""
from math import comb, gcd


def factors(n):
    result = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            result.append((p, a))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def divsum(nmax):
    s = [0]*(nmax+1)
    for d in range(1,nmax+1):
        for j in range(d,nmax+1,d):
            s[j] += d
    return s


def recurrence_series(t, cap):
    sig = divsum(cap)
    f, c = [1], [1]
    for n in range(1,cap+1):
        ff = -(t*t-1)*sum(sig[j]*f[n-j] for j in range(1,n+1))
        cc = sum((sig[j]-(t*t*sig[j//t] if j%t==0 else 0))*c[n-j] for j in range(1,n+1))
        assert ff%n==0 and cc%n==0
        f.append(ff//n)
        c.append(cc//n)
    return f,c


def multiply_one_factor(a, degree, exponent):
    cap=len(a)-1
    result=a[:]
    for k in range(1,min(exponent,cap//degree)+1):
        coef=(-1)**k*comb(exponent,k)
        lag=k*degree
        for n in range(lag,cap+1):
            result[n] += coef*a[n-lag]
    return result


def direct_series(t,cap):
    # Fully independent coefficient construction from finite Euler factors.
    f=[1]+[0]*cap
    b=[1]+[0]*cap
    partition=[1]+[0]*cap
    for d in range(1,cap+1):
        f=multiply_one_factor(f,d,t*t-1)
        if d%t==0:
            b=multiply_one_factor(b,d,t)
        for n in range(d,cap+1):
            partition[n]+=partition[n-d]
    c=[sum(b[j]*partition[n-j] for j in range(n+1)) for n in range(cap+1)]
    return f,c


def vp(n,p):
    if n==0: return 10**9
    k=0
    while n%p==0:
        n//=p
        k+=1
    return k


def run():
    cases=[2,3,4,5,6,7,8,9,10,12,15,16,18,20,24,25,27,30,32,36,49]
    checks=0
    for t in cases:
        ff=factors(t)
        cap = max(3*t, max(p**(2*a) for p,a in ff))
        cap=min(cap,160)
        f,c=recurrence_series(t,cap)
        fd,cd=direct_series(t,cap)
        assert f==fd and c==cd, ('engine mismatch',t)
        diff=[f[n]-c[n] for n in range(cap+1)]
        content=0
        for z in diff: content=gcd(content,abs(z))
        if len(ff)==1:
            p,a=ff[0]
            bound=p**(a+1)
            first=p**(a-1)
            assert content==bound, ('content',t,content,bound)
            assert all(vp(z,p)>=a+1 for z in diff)
            assert all(vp(diff[n],p)>=a+2 for n in range(first))
            assert diff[first] % (p**(a+2)) == (-bound) % (p**(a+2))
            assert vp(diff[first],p)==a+1
        else:
            assert content==1, ('content',t,content)
            for p,a in ff:
                if p**(2*a)<=cap:
                    n=p**(2*a)
                    m=t//p**a
                    assert all(diff[j]%p==0 for j in range(n))
                    assert diff[n]%p == (-m*m)%p
        checks+=len(diff)
    print(f'VERIFY_OK parameter_cases={len(cases)} coefficients_cross_checked={checks} exact_integer=yes')
    print('SAMPLE t=4 first_sharp_index=2 difference=88 modulus=8')
    print('SAMPLE t=6 mod2_first_index=4 mod3_first_index=9 content=1')

if __name__ == '__main__':
    run()
