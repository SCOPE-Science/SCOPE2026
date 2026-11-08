#!/usr/bin/env python3
"""Finite consistency checks for an exact positivity frontier of a rational arrival process.

This is a diagnostic, not a substitute for the all-orders proof.
Standard-library only. Run: python3 verify.py
"""
import cmath
import math
import random

rng = random.Random(260328047)
count = 0


def check(condition, info=''):
    global count
    if not condition:
        raise AssertionError(info or 'finite check failed')
    count += 1


def approx(a, b, tol=5e-9):
    return abs(a-b) <= tol * max(1., abs(a), abs(b))


def matmul(a, b):
    return [[sum(a[i][p]*b[p][j] for p in range(3)) for j in range(3)] for i in range(3)]


def density_direct(phi, eps, times):
    z = math.cos(phi); s = math.sin(phi)
    g1 = [[1.,0.,0.],[2-z+s,z,-s],[2-z-s,s,z]]
    prod = [[float(i==j) for j in range(3)] for i in range(3)]
    for t in times:
        ex = [math.exp(-t),math.exp(-2*t),math.exp(-2*t)]
        prod = matmul(prod,[[ex[i]*g1[i][j] for j in range(3)] for i in range(3)])
    return sum(((1-eps) if i==0 else (eps if i==1 else 0))*sum(prod[i]) for i in range(3))


def w_interior(phi, j):
    return (2*math.cos((j-1)*phi)-math.cos(j*phi)
          -2*math.sin((j-1)*phi)+math.sin(j*phi))


def w_terminal(phi, k):
    return 2*(math.cos((k-1)*phi)-math.sin((k-1)*phi))


def density_formula(phi, eps, times):
    T=0.
    S=0.
    k=len(times)
    for j,t in enumerate(times,1):
        T += t
        S += math.exp(-T)*(w_interior(phi,j) if j<k else w_terminal(phi,j))
    return math.exp(-T)*(1-eps+eps*S), S


def threshold(phi):
    cot = 1/math.tan(phi/2)
    return 2/(cot-1 + math.sqrt(2*(9+cot*cot)))


phis = [math.pi/math.sqrt(2), math.pi/math.e, math.pi/math.sqrt(3),0.39,1.4,2.7]
for phi in phis:
    z=cmath.exp(1j*phi)
    A=(1+1j)*(1+1/(1-z))
    B=(1+1j)/(1-z)
    alpha=A.real-abs(A)
    beta=A.real-abs(B)
    cot=1/math.tan(phi/2)
    check(approx(alpha,(3-cot)/2-math.sqrt((9+cot*cot)/2)), 'closed alpha')
    check(approx(threshold(phi), 1/(1-alpha)), 'threshold')
    check(beta>alpha and alpha<0, 'strict terminal bound')
    check(0<threshold(phi)<1, 'parameter range')
    M=math.sqrt(2)*(2+1/math.sin(phi/2))
    check(threshold(phi)>1/(1+M), 'improves prior range')
    for k in range(1,19):
        W=0.
        for j in range(1,k):
            W+=w_interior(phi,j)
            Wi=(A*(1-z**j)).real
            check(approx(W,Wi), 'interior partial sum')
            check(Wi>=alpha-1e-9, 'interior geometric bound')
        W+=w_terminal(phi,k)
        Wt=A.real-(B*z**k).real
        check(approx(W,Wt), 'terminal partial sum')
        check(Wt>=beta-1e-9, 'terminal geometric bound')
        for _ in range(90):
            ts=[rng.random()*2 for _ in range(k)]
            eps=rng.random()*threshold(phi)
            direct=density_direct(phi,eps,ts)
            formula,S=density_formula(phi,eps,ts)
            check(approx(direct,formula), 'matrix vs formula')
            check(S>alpha-1e-10, 'strict normalized correction')
            check(formula>0, 'positivity below boundary')
            ac=[math.exp(-sum(ts[:j])) for j in range(1,k+1)]
            ws=[w_interior(phi,j) if j<k else w_terminal(phi,j) for j in range(1,k+1)]
            Ws=[sum(ws[:j]) for j in range(1,k+1)]
            Abel=sum(Ws[j-1]*(ac[j-1]-ac[j]) for j in range(1,k))+Ws[-1]*ac[-1]
            check(approx(Abel,S), 'Abel identity')
            # Critical endpoint: all finite waits strictly positive.
            endpoint,_=density_formula(phi,threshold(phi),ts)
            check(endpoint>0, 'critical endpoint')
    # Construct a genuinely negative finite-time density above the exact threshold.
    eps=threshold(phi)+(1-threshold(phi))*0.06
    target=1-1/eps
    found=False
    for j in range(1,22000):
        if (A*(1-z**j)).real < target-1e-7:
            k=j+1
            times=[0.]*j+[18.]
            val,S=density_formula(phi,eps,times)
            check(val<0, 'necessity witness')
            found=True
            break
    check(found, 'irrational orbit witness within search horizon')

print('PASS', count, 'finite diagnostic assertions')
print('Boundary values:')
for phi in phis:
    M=math.sqrt(2)*(2+1/math.sin(phi/2))
    print(' phi=%.12g exact=%.12g prior_sufficient=%.12g' % (phi,threshold(phi),1/(1+M)))
