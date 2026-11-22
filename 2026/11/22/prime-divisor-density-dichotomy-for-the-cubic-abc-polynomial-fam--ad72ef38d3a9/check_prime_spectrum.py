#!/usr/bin/env python3
"""Independent finite checks for the ABC cubic prime-root spectrum.

No third-party modules are required. Finite checks supplement, not replace,
the discriminant and Chebotarev arguments.
"""
from math import isqrt


def discr(u):
    return u**4 + 2*u**3 - 5*u**2 - 6*u - 23


def eval_f(u, x):
    return x*(x-1)*(x-u)+1


def cubic_discr_formula(u):
    a=-(u+1); b=u; c=1
    return a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c


def prime_list(n):
    ans=[]
    for k in range(2,n+1):
        if all(k%p for p in ans if p*p<=k):
            ans.append(k)
    return ans


def mull(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return c


def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]


def rem_mod_m(p):
    p=list(p)
    while len(p)>3:
        c=p[-1]; n=len(p)-1
        # z^3 = -z^2 + 2z + 1
        p[n-3]+=c; p[n-2]+=2*c; p[n-1]-=c
        p.pop()
    return tuple(p+[0]*(3-len(p)))


def f_in_m(u,t):
    one=(1,0,0); z=rem_mod_m(t)
    zm1=add(z,[-1]); zmu=add(z,[-u])
    return rem_mod_m(add(mull(mull(z,zm1),zmu),[1]))

# Closed cubic discriminant agrees with coefficient formula.
for u in range(-1000,1001):
    assert discr(u)==cubic_discr_formula(u)
    assert (discr(u)>=0 and isqrt(max(0,discr(u)))**2 == discr(u)) == (u in (-4,3))

# Direct identification of both special fields with the cubic cyclotomic field.
assert f_in_m(3, [1,-1]) == (0,0,0)
assert f_in_m(-4, [-4,1,2]) == (0,0,0)

ps=prime_list(347)
count=0
for u in range(-30,31):
    for p in ps:
        if discr(u)%p==0: continue
        roots=[x for x in range(p) if eval_f(u,x)%p==0]
        assert len(roots) in (0,1,3)
        if u in (-4,3):
            assert len(roots)==(3 if p%7 in (1,6) else 0)
        # Hensel: each root has exactly one lift to p^2 and p^3.
        for a in roots:
            lift=a
            for power in (p,p*p):
                choices=[lift+j*power for j in range(p) if eval_f(u,lift+j*power)%(power*p)==0]
                assert len(choices)==1
                lift=choices[0]
        count+=1
print('PASS: 2001 integer discriminants; two exceptional-field identities; '
      f'{count} prime-root spectra and unique lifts through p^3.')
