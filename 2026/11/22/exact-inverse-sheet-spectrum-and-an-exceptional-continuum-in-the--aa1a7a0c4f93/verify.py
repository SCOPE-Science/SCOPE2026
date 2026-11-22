"""Standalone exact inverse-count and numerical reconstruction checker.
All exact statements are justified by integer-interval counting in RESULT.md.
"""
import math
from fractions import Fraction

def psi(w):
    return w-w**3/6

def invert_psi(y):
    lo,hi=0.,1.
    for _ in range(65):
        z=(lo+hi)/2
        if psi(z)<y:lo=z
        else:hi=z
    return (lo+hi)/2

def frac(x):
    return x-math.floor(x)

def branches(m, U, V, W, enumerate_preimages=True):
    a=m*(64+U+V)/64
    s=max(0,math.ceil(5*a/6-W))
    count=0; inverse=[]; singular=False
    for k in range(s):
        w=invert_psi((W+k)/a)
        delta=frac(V-w*(1+U*U))
        t=U-w
        # Away from boundary or very-near-boundary numerical ambiguity,
        # this matches the closed-form count exactly.
        if abs(delta)<1e-12 and abs(t)<1e-12:
            singular=True
            continue
        increment=(frac(t)>1e-12 and frac(t)<=delta+1e-12)
        count+=m*(m-1)//2+m*int(increment)
        if enumerate_preimages:
            for j in range(m):
                Q=delta+j
                if abs(Q)<1e-12:continue
                lo=math.floor(-t)+1
                hi=math.floor(Q-t+1e-12)
                for ell in range(lo,hi+1):
                    u=1-(t+ell)/Q
                    v=Q/m
                    if -1e-10<=u<1+1e-10:
                        inverse.append((u,v,w))
    return s,count,inverse,singular

def F(m,u,v,w):
    U=frac(m*v*(1-u)+w)
    V=frac(m*v+w*(1+U*U))
    W=frac((m/64)*(U+V+64)*psi(w))
    return U,V,W

# Separate exact integer inequalities verify the compact per-row formula.
for m in range(1,13):
    for d_num in range(0,21):
        delta=Fraction(d_num,23)
        for t_num in range(-17,19):
            t=Fraction(t_num,19)
            H=int(0 < t-math.floor(t) <= delta)
            direct=sum(sum(1 for l in range(-3,m+4)
                 if 0<t+l<=delta+j) for j in range(m))
            formula=m*(m-1)//2+m*H
            assert direct==formula,(m,delta,t,direct,formula)

# Verify arithmetic root sheets and actual forward preimages of the full map.
checks=[(2,.31,.64,.24),(3,.42,.23,.57),(4,.73,.18,.81),
        (7,.13,.83,.37),(8,.77,.44,.12),(64,.23,.61,.44),
        (64,.73,.14,.81),(64,.27,.39,.93)]
for m,U,V,W in checks:
    s,number,pre,singular=branches(m,U,V,W)
    assert not singular
    assert len(pre)==number,(m,U,V,W,s,len(pre),number)
    assert s==max(0,math.ceil(5*(m/64)*(64+U+V)/6-W))
    for u,v,w in pre:
        U1,V1,W1=F(m,u,v,w)
        assert abs(U1-U)<1e-8 and abs(V1-V)<1e-8 and abs(W1-W)<1e-8, (m,(u,v,w),(U1,V1,W1))
    if m==64:
        assert 53<=s<=55 and 106848<=number<=114400
    print(f'm={m} target=({U},{V},{W}) sheets={s} count={number}')

# Infinite fibers: all u on v=0 share the same output at chosen w.
for m in (2,64):
    for w in (.2,.5,.9):
        outputs=[F(m,u,0,w) for u in (.1,.3,.8)]
        assert outputs[0]==outputs[1]==outputs[2]
print('INVERSE_GEOMETRY_VERIFY_OK')
