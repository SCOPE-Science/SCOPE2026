#!/usr/bin/env python3
"""Finite diagnostics for pinned damped-rotation three-event information design.
This script is not a proof of continuous optimality or literature priority.
"""
import math

CHECKS = 0

def check(v, context):
    global CHECKS
    CHECKS += 1
    if not v:
        raise AssertionError(context)

def data(eta, phi, x):
    q = math.exp(-2.0*eta*phi)
    return math.exp(-2.0*eta*x)*(math.sin(x)**2 + q*math.sin(phi-x)**2)

def derivative_core(eta, phi, x):
    q = math.exp(-2.0*eta*phi)
    return (math.sin(2*x)-2*eta*math.sin(x)**2
            -q*(math.sin(2*(phi-x))+2*eta*math.sin(phi-x)**2))

def bisection(eta, phi, left, right):
    fl=derivative_core(eta,phi,left)
    fr=derivative_core(eta,phi,right)
    assert fl*fr<0
    for _ in range(75):
        mid=(left+right)/2
        fm=derivative_core(eta,phi,mid)
        if fm*fl>0:
            left=mid;fl=fm
        else:
            right=mid
    return (left+right)/2

def candidates(eta, phi):
    stop = min(phi,math.pi)
    nodes=[stop*k/500 for k in range(501)]
    roots=[]
    for a,b in zip(nodes,nodes[1:]):
        if derivative_core(eta,phi,a)*derivative_core(eta,phi,b)<0:
            roots.append(bisection(eta,phi,a,b))
    return roots

for eta in (0.015,0.07,0.25,0.8,1.0,2.5,12.0):
    critical=math.atan(1/eta)
    for ratio in (0.12,0.5,0.97,1.0,1.03,1.2,1.8,2.1,3,7,15,38):
        phi=ratio*critical
        grid=[data(eta,phi,phi*j/4000) for j in range(4001)]
        endpoints=data(eta,phi,0)
        check(abs(data(eta,phi,phi)-endpoints)<=2e-13,'endpoint equality')
        roots=candidates(eta,phi)
        vals=[(data(eta,phi,r),r) for r in roots]+[(endpoints,0.0),(data(eta,phi,phi),phi)]
        maximum,max_loc=max(vals)
        check(maximum>=max(grid)-1e-11*(1+maximum),'root/global maximum discrepancy')
        if ratio<=1.0:
            check(abs(maximum-endpoints)<1e-10*(1+endpoints),'short horizon optimum')
        else:
            check(0<max_loc<min(math.pi,phi),'long horizon optimizer is interior first period')
            check(maximum>endpoints,'long horizon strict gain')
            check(sum(1 for value,r in vals if r not in (0,phi) and abs(value-maximum)<1e-13*(1+maximum))==1,
                  'unique stationary optimum')

for eta in (0.1,0.5,2.0):
    x0=math.atan(1/eta)
    for phi in (5.0,6.0,7.0,9.0,11.0,14.0):
        roots=candidates(eta,phi)
        best=max(roots,key=lambda z:data(eta,phi,z))
        q=math.exp(-2*eta*phi)
        r=phi-x0
        predicted=x0-0.5*q*(math.sin(2*r)+2*eta*math.sin(r)**2)
        check(abs(best-predicted)<25*(1+eta**4)*q**2+1e-12,'first-order oscillatory approach')

print('PINNED_ROTATION_FRAME_DIAGNOSTIC_OK',CHECKS)
