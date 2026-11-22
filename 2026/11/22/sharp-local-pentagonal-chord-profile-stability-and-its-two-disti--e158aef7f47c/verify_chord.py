#!/usr/bin/env python3
"""Independent finite-mode/trig and finite-difference checks of the analytic chord theorem.
Only Python's standard library; numerical tests do not replace the infinite proof."""
import math
import bisect

pi=math.pi
s0=math.sin(pi/5)
phi=(1+math.sqrt(5))/2

def bracket(k,n):
    a=2*pi*k/5
    return 2*(math.sin(a/2)*math.cos(n*a/2)-math.cos(a/2)*math.sin(n*a/2)/n)

k1={2:(phi-3)/2, 3:(2-4*phi)/3,4:-5*phi/4,5:-2.,6:-5*phi/6,7:(8-6*phi)/7}
k2={2:-(3*phi+1)/2,3:-(2*phi+4)/3,4:5/4,5:2*phi,6:5/6}
d1=(3*math.sqrt(5)-5)*s0/7
d2=5*s0/6
for k, table, nstar, delta in [(1,k1,7,d1),(2,k2,6,d2)]:
    for n,val in table.items():
        err=abs(bracket(k,n)/s0-val)
        assert err<2e-13,(k,n,err)
    assert abs(bracket(k,nstar))>0 and abs(abs(bracket(k,nstar))-delta)<1e-13
    assert all(abs(bracket(k,n))>delta+1e-6 for n in table if n!=nstar)
    u=math.cos(2*pi/5); v=math.sin(2*pi/5)
    if k==1:
        tail=2*(s0*u-math.cos(pi/5)/8)
    else:
        tail=2*u*(v-1/7)
    assert tail>delta+1e-6
    for n in range(max(table)+1,4001):
        assert abs(bracket(k,n))>=tail-1e-11
    print('linear',k,'sharp n=',nstar,'delta=',format(delta,'.15f'),'tail lower=',format(tail,'.15f'))

def numerical_chord(k,n,ampl,ns=8192):
    # Piecewise-linear interpolation of exact arclength primitive for a polar curve.
    step=2*pi/ns
    th=[j*step for j in range(ns+1)]
    radius=lambda x:1+ampl*math.cos(n*x)
    speed=lambda x:math.hypot(radius(x),-ampl*n*math.sin(n*x))
    w=[speed(t) for t in th]
    cum=[0.0]
    for j in range(ns):cum.append(cum[-1]+step*(w[j]+w[j+1])/2)
    P=cum[-1]
    chords=[]
    for j in range(ns):
        target=cum[j]+k*P/5
        if target>=P:target-=P
        idx=bisect.bisect_right(cum,target)-1
        idx=min(idx,ns-1)
        frac=(target-cum[idx])/(cum[idx+1]-cum[idx])
        theta2=step*(idx+frac)
        angle=th[j]
        x1,y1=radius(angle)*math.cos(angle),radius(angle)*math.sin(angle)
        x2,y2=radius(theta2)*math.cos(theta2),radius(theta2)*math.sin(theta2)
        chords.append(math.hypot(x2-x1,y2-y1))
    avg=sum(chords)/ns
    var=sum((x-avg)**2 for x in chords)/ns
    # rms(f)=abs(ampl)/sqrt(2)
    return math.sqrt(var)*math.sqrt(2)/abs(ampl)

for k,n,d in [(1,7,d1),(2,6,d2)]:
    measured=numerical_chord(k,n,2e-5)
    assert abs(measured-d)<4e-5,(k,n,measured,d)
    print('arclength endpoint finite difference',k,n,format(measured,'.12f'))
print('finite checks passed; universal theorem is analytic')
