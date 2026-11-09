"""Exact reproducibility tests for finite-memory threshold-graph motif fluctuations.

Only Python's standard library is required. Finite tests check algebraic identities
and stationary-process coefficients; they are not proofs of limit theorems.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

count = 0

def check(condition, label):
    global count
    count += 1
    if not condition:
        raise AssertionError(label)

def sequence_counts(bits):
    n = len(bits)
    edges = sum((j-1)*bits[j-1] for j in range(1,n+1))
    triangles = sum((j-1)*bits[j-1]*bits[k-1]
                    for j in range(1,n+1) for k in range(j+1,n+1))
    direct_edges = sum(bits[j] for i in range(n) for j in range(i+1,n))
    direct_triangles = sum(bits[j]*bits[k] for i in range(n)
                           for j in range(i+1,n) for k in range(j+1,n))
    return edges, triangles, direct_edges, direct_triangles

def polya_prefix_probability(bits, rho, delta):
    ones = 0
    prob = F(1)
    for t, bit in enumerate(bits):
        p = (rho+delta*ones)/(1+delta*t)
        prob *= p if bit else (1-p)
        ones += bit
    return prob

def transition(state,rho,delta):
    return (rho+delta*sum(state))/(1+len(state)*delta)

# All possible creation strings, with exact edge and triangle enumerations.
rho = F(2,5)
for n in range(1,11):
    for bits in product((0,1),repeat=n):
        e,t,ed,td=sequence_counts(bits)
        check(e==ed, ('edges', n,bits))
        check(t==td, ('triangles',n,bits))
        ys=[F(bit)-rho for bit in bits]
        s=[F(0)]
        for y in ys: s.append(s[-1]+y)
        # Avoid binary floating-point in the exact linearization.
        linear=sum((F(j-1)*(n-j)+F((j-1)*(j-2),2))*ys[j-1] for j in range(1,n+1))
        rr=sum(F(j-1)*ys[j-1]*ys[k-1] for j in range(1,n+1) for k in range(j+1,n+1))
        check(F(t)==rho*rho*comb(n,3)+rho*linear+rr,('expand',n,bits))
        if n>=2:
            a=sum(F(j-1)*ys[j-1] for j in range(1,n))
            rhs=s[n]*a-F(1,2)*((n-2)*s[n-1]**2-sum(s[j]**2 for j in range(1,n-1))+
                                     sum(F(j-1)*ys[j-1]**2 for j in range(1,n)))
            check(rr==rhs,('quadratic remainder',n,bits))

# Verify the exact stationary M-word law, and innovation-variance formula.
for M in range(1,6):
  for rho in (F(1,3),F(2,5)):
   for delta in (F(1,2),F(2)):
    states=list(product((0,1),repeat=M))
    pi={s:polya_prefix_probability(s,rho,delta) for s in states}
    check(sum(pi.values())==1,('normalization',M,rho,delta))
    for state in states:
      incoming=F(0)
      for leading in (0,1):
        old=(leading,)+state[:-1]
        p=transition(old,rho,delta)
        incoming+=pi[old]*(p if state[-1] else (1-p))
      check(incoming==pi[state],('stationary',M,state,rho,delta))
    for i in range(M):
      mean=sum(pi[s]*s[i] for s in states)
      check(mean==rho,('mean',M,i,rho,delta))
      for j in range(i+1,M):
        cov=sum(pi[s]*(s[i]-rho)*(s[j]-rho) for s in states)
        check(cov==rho*(1-rho)*delta/(1+delta),('within-block covariance',M,i,j,rho,delta))
    alpha=delta/(1+M*delta)
    q=sum(pi[s]*transition(s,rho,delta)*(1-transition(s,rho,delta)) for s in states)
    D=1+2*M*delta+F(M*(M-1))*delta*delta/(1+delta)
    check((1+M*delta)**2*q==rho*(1-rho)*D,('innovation',M,rho,delta))

# Independently verify the variance-covariance integrals as exact rationals.
edge=4*F(1,3)
cross=12*(F(1,3)-F(1,8))
triangle=36*(F(1,3)-F(1,4)+F(1,20))
residual=triangle-4*cross+4*edge
check(edge==F(4,3),'edge Gaussian coefficient')
check(cross==F(5,2),'cross Gaussian coefficient')
check(triangle==F(24,5),'triangle Gaussian coefficient')
check(residual==F(2,15),'excess Gaussian coefficient')
check(edge*triangle-cross*cross==F(3,20),'positive definite covariance')
print('PASS',count,'exact assertions; final excess coefficient =',residual)
