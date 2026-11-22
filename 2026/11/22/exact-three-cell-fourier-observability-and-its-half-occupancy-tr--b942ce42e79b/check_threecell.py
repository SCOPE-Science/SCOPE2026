#!/usr/bin/env python3
"""Supplementary numerical spot checks of the analytic three-cell Fourier theorem.
The finite grids are diagnostic only; the proof in RESULT.md covers all measurable masks.
"""
import math
import cmath

PI=math.pi
L=2*PI/3
count=0

def check(assertion, message):
    global count
    assert assertion, message
    count+=1

def F(gamma):
    t=PI*min(gamma,1-gamma)/3
    return 2*math.sin(t)*(1+2*math.cos(PI/3+t))

def support_formula(gamma, phi):
    assert 0 < gamma <= 0.5 and 0 <= phi <= L/2
    length=L*gamma
    if phi<=length/2:
        return 2*math.sin(L+length/2)+2*(math.sin(length)-math.sin(L))*math.cos(phi)
    return 2*math.sin(length/2)*(1+2*math.cos((L+length)/2)*math.cos(phi-L/2))

def intervals(gamma,phi):
    """Maximizing cos(t-phi) sets in three fixed cells for gamma<=1/2."""
    length=L*gamma
    if phi<=length/2:
        c0=[(0,length)]
        c1=[(L,L+length/2+phi),(2*L-length/2+phi,2*L)]
    else:
        c0=[(phi-length/2,phi+length/2)]
        c1=[(L,L+length)]
    return [c0,c1,[(3*L-length,3*L)]]

def moment(blocks):
    z=0j
    for block in blocks:
        for lo,hi in block:
            z+=(cmath.exp(1j*hi)-cmath.exp(1j*lo))/1j
    return z

for g in (.01,.05,.17,.3,.49,.5):
    for i in range(81):
        ph=L*i/160
        blocks=intervals(g,ph)
        for j,cell in enumerate(blocks):
            check(abs(sum(b-a for a,b in cell)-L*g)<1e-12,'wrong measure')
            check(all(j*L-1e-12<=a<=b<=(j+1)*L+1e-12 for a,b in cell),'outside cell')
        z=moment(blocks)
        observed=(z*cmath.exp(-1j*ph)).real
        check(abs(observed-support_formula(g,ph))<2e-12,'incorrect phase support')
        check(observed<=F(g)+2e-12,'exceeds bound')
    check(abs(support_formula(g,L/2)-F(g))<2e-12,'incorrect max')

for g in (.001,.02,.1,.25,.49,.5,.51,.75,.9,.98,.999):
    c=F(g)/(2*PI)
    check(0<c<g,'frame bound not positive')
    check(abs(F(g)-F(1-g))<1e-12,'complement symmetry')
    if g<=0.5:
        blocks=intervals(g,L/2)
        z=moment(blocks)
    else:
        blocks=intervals(1-g,L/2)
        z=-moment(blocks)
    check(abs(abs(z)-F(g))<2e-12,'attaining moment incorrect')
    check(abs(abs(z)/(2*PI)-c)<2e-12,'normalization incorrect')
    check(abs((g+c)+(g-c)-2*g)<2e-12,'trace failed')
    check(g-c>0,'lower bound fails')

# Separate finite-grid rearrangement tests for the full phase support,
# not a certificate for infinitely many phases or measurable masks.
for g in (.1,.24,.46,.5):
    subdivisions=1600
    delta=L/subdivisions
    xs=[(j+0.5)*delta for j in range(3*subdivisions)]
    chosen=round(g*subdivisions)
    for i in range(21):
        phi=L*i/40
        discrete=0
        for k in range(3):
            cell=sorted((math.cos(xs[k*subdivisions+j]-phi) for j in range(subdivisions)),reverse=True)
            discrete+=sum(cell[:chosen])*delta
        target=support_formula(g,phi)
        check(abs(discrete-target)<.0013,'grid disagrees with exact rearrangement')

# The half-filling support is exactly flat in phase, a nontrivial test of the transition.
for i in range(101):
    check(abs(support_formula(.5,L*i/200)-1)<2e-12,'flat support at half filling fails')

print('PASS',count,'supplementary assertions')
