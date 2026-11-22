#!/usr/bin/env python3
"""Exact arithmetic diagnostic for a finite-horizon scalar AR(1) SGD theorem."""
from fractions import Fraction as Q
from itertools import product

n_checks = 0

def ck(x):
    global n_checks
    assert x
    n_checks += 1

def solution(n, rho, t):
    s = n-(n-2)*rho
    k = t/(1+rho+t*s)
    b = [Q(1)] + [1-rho]*(n-2) + [Q(1)]
    w = [k*z for z in b]
    h = [w[j]/(1-sum(w[j+1:])) for j in range(n)]
    return w,h,k

def risk(n,rho,t,w):
    return t*(1-sum(w))**2 + sum(w[i]*w[j]*rho**abs(i-j)
          for i in range(n) for j in range(n))

for n in range(3,10):
    for rho in (Q(-9,10),Q(-3,4),Q(-1,2),Q(-1,10),Q(0),Q(1,10),Q(1,2),Q(3,4),Q(9,10)):
        for t in (Q(1,100),Q(1,10),Q(1,4),Q(1),Q(10)):
            w,h,k=solution(n,rho,t)
            s=n-(n-2)*rho
            ck(all(Q(0)<z<Q(1) for z in h))
            ck(all(z>0 for z in w) and sum(w)<1)
            ck([h[j]*__import__('functools').reduce(lambda a,b:a*(1-b),h[j+1:],Q(1))
                for j in range(n)]==w)
            ck(risk(n,rho,t,w)==t*(1+rho)/(1+rho+t*s))
            ck(all(sum(rho**abs(i-j)*w[j] for j in range(n))==t*(1-sum(w))
                for i in range(n)))
            ck(all(h[i]>h[i+1] for i in range(1,n-2)))
            ck((h[0]<h[1])==(t+rho*(1+rho)<0))
            ck((h[0]==h[1])==(t+rho*(1+rho)==0))
            ck((h[-1]>h[-2])==(rho*(1+rho)>t*(1-n*rho+(n-2)*rho*rho)))
            ck((h[-1]==h[-2])==(rho*(1+rho)==t*(1-n*rho+(n-2)*rho*rho)))
            ck(all(risk(n,rho,t,[w[i]+delta if i==j else w[i]
                        for i in range(n)])>risk(n,rho,t,w)
                   for j in range(n) for delta in (Q(1,1000),Q(-1,1000))))

w,h,k=solution(3,Q(-1,2),Q(1,10))
ck(h==[Q(1,6),Q(1,5),Q(2,17)] and risk(3,Q(-1,2),Q(1,10),w)==Q(1,17))
w,h,k=solution(3,Q(1,2),Q(1))
ck(h==[Q(2,5),Q(1,6),Q(1,4)] and risk(3,Q(1,2),Q(1),w)==Q(3,8))
# Equality in the start-boundary, plus independent-noise baseline.
w,h,k=solution(3,Q(-1,2),Q(1,4)); ck(h[0]==h[1])
w,h,k=solution(3,Q(0),Q(1)); ck(h==[Q(1,2),Q(1,3),Q(1,4)])
print('VERIFY_OK',n_checks)
