"""Numerical cross-checks for a local polygon boundary chord law.

Requires only Python 3's standard library. Finite tests supplement, rather
than establish, the proof for arbitrary polygons.
"""
from __future__ import annotations
import bisect
import math
import random


def side_geometry(vertices):
    lengths=[]
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        lengths.append(math.dist(a,b))
    return lengths, sum(lengths)


def exterior_angles(vertices):
    out=[]
    n=len(vertices)
    for i in range(n):
        a,b,c=vertices[i-1],vertices[i],vertices[(i+1)%n]
        e1=(b[0]-a[0],b[1]-a[1])
        e2=(c[0]-b[0],c[1]-b[1])
        cross=e1[0]*e2[1]-e1[1]*e2[0]
        dot=e1[0]*e2[0]+e1[1]*e2[1]
        out.append(math.atan2(cross,dot))
    assert min(out)>0 and max(out)<math.pi
    assert abs(sum(out)-2*math.pi)<1e-9
    return out


def corner_coefficient(angles):
    return sum(d/math.sin(d)-1 for d in angles)


def local_probability(vertices,t):
    lengths,L=side_geometry(vertices)
    ds=exterior_angles(vertices)
    return 2*t/L+corner_coefficient(ds)*t*t/(L*L)


def sample_perimeter(vertices, lengths, cumul, total, rng):
    z=rng.random()*total
    i=bisect.bisect_left(cumul,z)
    prev=cumul[i-1] if i else 0.0
    frac=(z-prev)/lengths[i]
    a,b=vertices[i],vertices[(i+1)%len(vertices)]
    return a[0]+frac*(b[0]-a[0]),a[1]+frac*(b[1]-a[1])


def finite_threshold(vertices):
    lengths,_=side_geometry(vertices)
    ds=exterior_angles(vertices)
    n=len(vertices)
    cap=min(lengths)
    for i,d in enumerate(ds):
        cap=min(cap,lengths[i-1]*math.sin(d),lengths[i]*math.sin(d))
    return cap


def sample_check(vertices,rad,seed):
    lengths,L=side_geometry(vertices)
    cumul=[]
    s=0.0
    for a in lengths:
        s+=a;cumul.append(s)
    rng=random.Random(seed)
    hits=0
    trials=250000
    for _ in range(trials):
        p=sample_perimeter(vertices,lengths,cumul,L,rng)
        q=sample_perimeter(vertices,lengths,cumul,L,rng)
        if math.dist(p,q)<=rad:
            hits+=1
    observed=hits/trials
    expected=local_probability(vertices,rad)
    # Rigorous Hoeffding threshold: failure probability < 2 exp(-2 N *.007^2).
    assert abs(observed-expected)<.007,(observed,expected)
    return observed,expected


def cone_grid(theta,rad,n=2200):
    # Integrate the cross-edge indicator over a bounding square by midpoint rule.
    side=rad/math.sin(theta)
    step=side/n
    acc=0
    ct=math.cos(theta)
    for i in range(n):
        s=(i+.5)*step
        # For s fixed, count midpoint v meeting s*s+v*v-2*s*v*cos(theta)<=r*r.
        center=s*ct
        discr=rad*rad-s*s*math.sin(theta)**2
        if discr<0: continue
        d=math.sqrt(discr)
        lo=max(0,center-d)
        hi=min(side,center+d)
        if hi>lo: acc+=(hi-lo)*step
    return acc


def stability_check():
    rng=random.Random(103217)
    for n in (3,4,5,8,16,40):
        b=2*math.pi/n
        for _ in range(300):
            z=[rng.uniform(-.2,.2) for _ in range(n)]
            avg=sum(z)/n
            ds=[b+(v-avg)*min(b/4,.12) for v in z]
            if min(ds)<=0 or max(ds)>=math.pi:continue
            dev=sum((x-b)**2 for x in ds)
            excess=corner_coefficient(ds)-n*(b/math.sin(b)-1)
            assert excess+1e-11>=dev/6,(n,excess,dev)
    ratios=[]
    for n in (20,40,80,160,320):
        b=2*math.pi/n
        ep=1/(5*n)
        # Avoid subtractive cancellation by higher precision series for large n.
        h=lambda x:x/math.sin(x)
        ratio=(h(b+ep)+h(b-ep)-2*h(b))/(2*ep*ep)
        ratios.append(ratio)
    assert abs(ratios[-1]-1/6)<.002,ratios
    return ratios


def main():
    square=[(0.,0.),(1.,0.),(1.,1.),(0.,1.)]
    triangle=[(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)]
    uneven=[(0.,0.),(1.7,0.),(2.4,.8),(1.6,1.7),(.1,1.2)]
    print('corner cone integrations:')
    for theta in (.4, .9,math.pi/2,2.1):
        exact=rad=0.15
        exact=(math.pi-theta)*rad*rad/(2*math.sin(theta))
        numeric=cone_grid(theta,rad,n=1600)
        assert abs(numeric-exact)<.0002,(theta,exact,numeric)
        print(round(theta,3),round(numeric,7),round(exact,7))
    print('boundary sample CDF:')
    for j,vertices in enumerate((square,triangle,uneven)):
        t=.1*finite_threshold(vertices)
        got,want=sample_check(vertices,t,seed=2247+j)
        print('polygon',j,'observed',round(got,6),'formula',round(want,6))
    print('stability ratios:',stability_check())
    print('CHECKS_PASSED')

if __name__=='__main__':
    main()
