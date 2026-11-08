#!/usr/bin/env python3
"""Exact and numerical finite checks for the biased Hata-map occupation theorem.
Scientific checks only; not a substitute for its infinite-time argument.
Run: python verify.py (requires sympy)."""
from fractions import Fraction as F
import random
import math
import sympy as S

checks=0

def check(c, description):
    global checks
    assert c,description
    checks += 1

# Verify branch images by exact rational endpoints, including crossings.
for j in range(12):
    lo=F(1,2**(j+2)); hi=F(1,2**(j+1))
    check((lo/2,hi/2)==(F(1,2**(j+3)),F(1,2**(j+2))), 'left inward')
    if j:
        check((2*lo,2*hi)==(F(1,2**(j+1)),F(1,2**j)), 'left outward')
    else:
        check((2*lo,2*hi)==(F(1,2),F(1)), 'left cross')
    rlo=1-hi; rhi=1-lo
    check(((rlo+1)/2,(rhi+1)/2)==(1-F(1,2**(j+2)),1-F(1,2**(j+3))), 'right outward')
    if j:
        check((2*rlo-1,2*rhi-1)==(1-F(1,2**j),1-F(1,2**(j+1))), 'right inward')
    else:
        check((2*rlo-1,2*rhi-1)==(F(0),F(1,2)), 'right cross')

for p in [F(3,5),F(2,3),F(3,4),F(9,10)]:
    q=1-p; delta=p-q; r=q/p; theta=r/(2-r)
    check(theta==q/(3*p-1), 'return probability')
    check(theta/(1-theta)==(1-delta)/(4*delta), 'switch mean')
    check(F(2)/(delta*(1-theta))==(1+3*delta)/(2*delta**2), 'occupation mean')

# Algebraic pgf check at p=3/4, including exact probability coefficients.
z=S.symbols('z'); p=S.Rational(3,4); q=1-p
root=S.sqrt(1-4*p*q*z**2)
g=(1-root)/(2*q*z)
b=p*z/(1-q*z*g)
phi=b/(2-g)
theta=(q/p)/(2-q/p)
P=S.cancel((1-theta)*phi/(1-theta*phi))
ser=S.series(P,z,0,7).removeO().expand()
expected=[S.Rational(0),S.Rational(3,10),S.Rational(27,200),
          S.Rational(117,1000),S.Rational(6237,80000),
          S.Rational(27027,400000),S.Rational(796311,16000000)]
for n,c in enumerate(expected):
    check(S.simplify(ser.coeff(z,n)-c)==0,f'pgf coefficient n={n}')
check(S.simplify(P.subs(z,1)-1)==0,'pgf normalization')
check(S.simplify(S.diff(P,z).subs(z,1)-5)==0,'pgf mean p=3/4')

# Critical scaling: direct evaluation at small nonzero bias, not a limit proof.
for delta in [.04,.02,.01,.005]:
    pp=(1+delta)/2; qq=1-pp
    for s in [.3,1.,3.]:
        zz=math.exp(-s*delta**2)
        gg=(1-math.sqrt(1-4*pp*qq*zz**2))/(2*qq*zz)
        bb=pp*zz/(1-qq*zz*gg)
        phi=bb/(2-gg)
        th=qq/(3*pp-1)
        exact=(1-th)*phi/(1-th*phi)
        target=2/(1+math.sqrt(1+2*s))
        check(abs(exact-target)<.13,'finite-bias Laplace crossover approximation')

# Sample entire stochastic cell trajectories; no floating-point underflow.
def simulate(p,seed_count,seed):
    rng=random.Random(seed)
    ns=[]; occupations=[]
    for _ in range(seed_count):
        side=1  # 1 = disfavored right half, 0 = favored left half
        j=0
        # Uniform on (1/2,1) => P(J=j) = 2^(-j-1).
        while rng.random()<.5:j+=1
        N=0; S_count=0; left_before=False
        for steps in range(100000):
            if side == 1: S_count += 1
            choose0=rng.random()<p
            if side==1:
                if choose0:
                    if j==0:
                        side=0; left_before=True; j=0
                        while rng.random()<.5:j+=1
                    else:j-=1
                else:j+=1
            else:
                if choose0:j+=1
                elif j:
                    j-=1
                else:
                    side=1; N+=1; j=0
                    while rng.random()<.5:j+=1
            if side==0 and left_before and j>90:
                # Probability of returning to R from L_j <= (q/p)^(j+1).
                break
        else:raise AssertionError('simulation did not settle')
        ns.append(N); occupations.append(S_count)
    return ns,occupations
for p in [.6,.75]:
    ns,occ=simulate(p,4000,3117)
    d=2*p-1; th=(1-p)/(3*p-1)
    for k in range(4):
        est=sum(n==k for n in ns)/len(ns)
        check(abs(est-(1-th)*th**k)<.04, 'empirical switch histogram')
    check(abs(sum(occ)/len(occ)-(1+3*d)/(2*d*d))<.13*(1+3*d)/(2*d*d),'empirical occupation mean')

# Independent check on the *original real interval maps*, not just the cell chain.
for prob in [.6,.75]:
    rng=random.Random(104729)
    counts=[]; returns=[]
    for _ in range(1100):
        x=.5+.5*rng.random()
        occ=0; nr=0; exited=False
        for _ in range(850):
            was_right=(x>.5)
            if was_right:occ+=1
            if rng.random()<prob:
                x=(x/2 if x<.5 else 2*x-1)
            else:
                x=(2*x if x<.5 else (x+1)/2)
            is_right=(x>.5)
            if was_right and not is_right:exited=True
            if exited and not was_right and is_right:nr+=1
        counts.append(occ); returns.append(nr)
    d=2*prob-1; t=(1-d)/(1+3*d)
    check(abs(sum(counts)/len(counts)-(1+3*d)/(2*d*d))<.18*(1+3*d)/(2*d*d),
          'direct-map occupation mean')
    check(abs(sum(n==0 for n in returns)/len(returns)-(1-t))<.06,
          'direct-map first-exit no-return probability')

print(f'PASS: {checks} exact/symbolic/finite-sample checks')
