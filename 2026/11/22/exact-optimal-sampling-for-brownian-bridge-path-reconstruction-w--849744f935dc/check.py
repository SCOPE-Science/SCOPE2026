"""Exact-rational finite checks for optimal Bernoulli-erasure Brownian bridge sampling.
The general proof is analytic and does not depend on finite tests.
Run: python3 check.py
"""
from fractions import Fraction as F
from itertools import combinations, product


def q_cost(t, p):
    n = len(t)
    q = 1-p
    ans = F(0)
    for mask in range(1 << n):
        indices = [i for i in range(n) if mask >> i & 1]
        xs = [F(0)] + [t[i] for i in indices] + [F(1)]
        gaps = [xs[i+1]-xs[i] for i in range(len(xs)-1)]
        ans += p**len(indices) * q**(n-len(indices)) * sum(g*g for g in gaps)
    return ans


def q_quadratic(t,p):
    n=len(t); q=1-p
    return (F(1) +2*p*sum(x*x for x in t)
       - 2*p*p*sum(q**(j-i-1)*t[i]*t[j] for i in range(n) for j in range(i+1,n))
       - 2*p*sum(q**(n-i-1)*t[i] for i in range(n)))


def grad_quadratic(t,p):
    n=len(t); q=1-p
    return [4*p*t[i]-2*p*p*sum(q**(abs(i-j)-1)*t[j] for j in range(n) if j!=i)
            -2*p*q**(n-i-1) for i in range(n)]


def optimum(n,p):
    den=2+(n-1)*p
    return [ (1+i*p)/den for i in range(n)]


def check():
    checks=0
    for n in range(1,8):
      for p in [F(1,9),F(1,4),F(1,2),F(3,4),F(1)]:
        t=optimum(n,p)
        assert F(0)<t[0] and t[-1]<F(1) and all(t[i]<t[i+1] for i in range(n-1))
        a=q_cost(t,p);b=q_quadratic(t,p)
        expected=(2-p)/(2+(n-1)*p)
        assert a==b==expected,(n,p,a,b,expected)
        assert all(x==0 for x in grad_quadratic(t,p))
        checks+=3
        # Exact rational, ordered perturbations; check independent formula and excess risk.
        if n<=5:
          for k in range(n):
            for sign in [-1,1]:
              u=t.copy(); u[k]+=F(sign,10**4)
              if F(0)<u[0] and u[-1]<F(1) and all(u[i]<u[i+1] for i in range(n-1)):
                assert q_cost(u,p)==q_quadratic(u,p)
                assert q_cost(u,p)>a
                checks+=2
    # Exact strict-convexity witness: all-surviving event has probability p**n>0.
    # Its sum-of-squared-gaps Hessian is positive definite (see RESULT.md).
    print(f'PASS: {checks} exact rational assertions; n=1..7; p=1/9,1/4,1/2,3/4,1.')

if __name__=='__main__':
    check()
