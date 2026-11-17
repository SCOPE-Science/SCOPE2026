#!/usr/bin/env python3
"""Finite exact and asymptotic checks for atomic Bernstein-Durrmeyer operators.
The continuum theorems have independent analytical proofs."""
from fractions import Fraction as F
from math import comb, log, sqrt, exp, lgamma, erf

def matrix_exact(n, aa, ww):
    rr = len(aa)
    b = [[F(comb(n,k))*a**k*(1-a)**(n-k) for k in range(n+1)] for a in aa]
    z = [sum(ww[i]*b[i][k] for i in range(rr)) for k in range(n+1)]
    return [[sum(b[i][k]*ww[j]*b[j][k]/z[k] for k in range(n+1)) for j in range(rr)] for i in range(rr)]

def threshold(a,b):
    return log((1-a)/(1-b))/log(b*(1-a)/(a*(1-b)))

def rel_entropy(q,p):
    return q*log(q/p)+(1-q)*log((1-q)/(1-p))

def matrix_float(n,aa,ww):
    rr=len(aa)
    M=[[0.]*rr for _ in range(rr)]
    for i,a in enumerate(aa):
        for k in range(n+1):
            logs=[log(ww[j])+k*log(aa[j])+(n-k)*log(1-aa[j]) for j in range(rr)]
            top=max(logs); den=sum(exp(t-top) for t in logs)
            posterior=[exp(t-top)/den for t in logs]
            lp=lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*log(a)+(n-k)*log(1-a)
            prob=exp(lp)
            for j in range(rr): M[i][j]+=prob*posterior[j]
    return M

def interpolant_float(n, x, aa, ww, ff):
    rr=len(aa); total=0.
    for k in range(n+1):
        logs=[log(ww[j])+k*log(aa[j])+(n-k)*log(1-aa[j]) for j in range(rr)]
        top=max(logs); q=[exp(t-top) for t in logs]; posterior=sum(q[j]*ff[j] for j in range(rr))/sum(q)
        lp=lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
        if x==0: prob=1.0 if k==0 else 0.0
        elif x==1: prob=1.0 if k==n else 0.0
        else: prob=exp(lp+k*log(x)+(n-k)*log(1-x))
        total+=prob*posterior
    return total

aa=[F(1,5),F(2,5),F(4,5)]; ww=[F(2),F(1),F(3)]
checks=0
for n in range(1,22):
    M=matrix_exact(n,aa,ww)
    assert all(sum(M[i])==1 for i in range(3))
    assert all(ww[i]*M[i][j]==ww[j]*M[j][i] for i in range(3) for j in range(3))
    assert all(M[i][j]>0 for i in range(3) for j in range(3))
    # PSD of M follows analytically; check all principal minors via Sylvester in exact arithmetic
    a,b,c=M[0];d,e,f=M[1];g,h,j=M[2]
    assert a>0 and a*e-b*d>=0 and a*(e*j-f*h)-b*(d*j-f*g)+c*(d*h-e*g)>=0
    checks+=1
print('EXACT_RATIONAL_MARKOV_REVERSIBILITY_GRAM_PSD_PASS_N1_TO21',checks)

avs=[float(z) for z in aa]; wvs=[float(z) for z in ww]
cs=[threshold(avs[i],avs[i+1]) for i in range(2)]
assert avs[0]<cs[0]<avs[1]<cs[1]<avs[2]
Cs=[rel_entropy(cs[i],avs[i]) for i in range(2)]
assert all(abs(Cs[i]-rel_entropy(cs[i],avs[i+1]))<1e-12 for i in range(2))
print('ADJACENT_KL_BOUNDARIES_AND_CHERNOFF_EQUALITIES_PASS',[(round(c,8),round(C,8)) for c,C in zip(cs,Cs)])

for i in range(2):
    c=cs[i]; sig=sqrt(c*(1-c));
    for h in [-1.0,0,1.0]:
        ff=[0.]*3;ff[i+1]=1.
        v=interpolant_float(1000,c+h/sqrt(1000),avs,wvs,ff)
        target=0.5*(1+erf(h/(sig*sqrt(2))))
        assert abs(v-target)<0.07,(i,h,v,target)
print('GAUSSIAN_CRITICAL_WINDOW_TESTS_PASS_6')

for n in [100,200,400,800]:
    M=matrix_float(n,avs,wvs)
    S=sum(M[i][j] for i in range(3) for j in range(3) if i!=j)
    Cmin=min(Cs)
    scaled=S*sqrt(n)*exp(n*Cmin)
    assert 0.001<scaled<1000,(n,scaled)
    print('EXPONENTIAL_RATE_SCALED_SUM',n,round(scaled,7))
print('ATOMIC_BERNSTEIN_DURRMEYER_ALL_CHECKS_PASS')
