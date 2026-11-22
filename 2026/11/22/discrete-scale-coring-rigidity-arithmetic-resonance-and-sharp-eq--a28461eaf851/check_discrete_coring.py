#!/usr/bin/env python3
"""Numeric diagnostic for the discrete-scale coring rigidity theorem."""
import math
OMEGA = 2 * math.pi / math.log(2)
EPS = 0.001
M = math.hypot(2 - OMEGA*OMEGA, 3*OMEGA)
assert EPS * M < 2

def q(t):
    t = abs(float(t))
    return 1.0 if t == 0 else 1.0 - t*t*(1 + EPS*math.sin(OMEGA*math.log(t)))

def volume(scale,u,n=4000):
    assert n % 2 == 0 and 0<u<1 and scale>=1
    h=u/n
    v=lambda z: scale*scale*(q(z/scale)-q(u/scale))
    s=v(0)+v(u)+4*sum(v(k*h) for k in range(1,n,2))+2*sum(v(k*h) for k in range(2,n,2))
    return 2*math.pi*h*s/3

N=0; maxgap=0; maxdiff3=0
for i in range(1,51):
    u=i/51
    for s in (2.0,4.0):
        gap=abs(volume(s,u)-volume(1,u))
        maxgap=max(maxgap,gap)
        assert gap<1e-9,(u,s,gap)
        N+=1
    maxdiff3=max(maxdiff3,abs(volume(3,u)-volume(1,u)))
assert maxdiff3>1e-6,maxdiff3
for i in range(1,3001):
    t=i/3001
    sn=math.sin(OMEGA*math.log(t));cs=math.cos(OMEGA*math.log(t))
    qprime=-t*(2+EPS*(2*sn+OMEGA*cs))
    qsecond=-2-EPS*((2-OMEGA**2)*sn+3*OMEGA*cs)
    assert qprime<0 and qsecond<0 and 0<q(t)<1
for i in range(1,3001):
    t=i/3001
    for scale in (2.,4.):
        assert abs((q(t)-1)-scale*scale*(q(t/scale)-1))<5e-15
print('PASS: {} scaled-volume quadratures, {} strict concavity checks, {} dilation identities'.format(N,3000,6000))
print('Bound for q concavity: epsilon*M = {:.6g} < 2; maximum absolute 1/2/4 volume gap = {:.4g}'.format(EPS*M,maxgap))
print('Maximum 1-vs-3 volume mismatch on grid = {:.8g}'.format(maxdiff3))
