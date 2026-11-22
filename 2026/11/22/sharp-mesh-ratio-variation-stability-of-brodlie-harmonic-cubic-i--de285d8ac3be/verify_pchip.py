#!/usr/bin/env python3
"""Reproduce finite-cell checks of the nonuniform harmonic-mean Hermite variation law.
This tests numeric cases and the near-flat witnesses; the all-grid result uses the proof.
Python standard library only.
"""
import math, random

def harmonic(a,b,hl,hr):
    if a*b<=0: return 0.0
    return 3*(hl+hr)*a*b/((2*hr+hl)*b+(hr+2*hl)*a)

def slopes(h, d):
    m=[0.]*(len(d)+1)
    for k in range(1,len(d)):
        m[k]=harmonic(d[k-1],d[k],h[k-1],h[k])
    return m

def q_integral_abs(c0,c1,c2):
    # derivative polynomial q(t)=c0+c1*t+c2*t*t on [0,1]
    cuts=[0.,1.]
    if abs(c2)<1e-14:
        if abs(c1)>1e-14:
            t=-c0/c1
            if 0<t<1: cuts.append(t)
    else:
        disc=c1*c1-4*c2*c0
        if disc>0:
            root=math.sqrt(disc)
            for t in [(-c1-root)/(2*c2),(-c1+root)/(2*c2)]:
                if 0<t<1: cuts.append(t)
    cuts=sorted(set(cuts))
    F=lambda t: c0*t+c1*t*t/2+c2*t*t*t/3
    return sum(abs(F(b)-F(a)) for a,b in zip(cuts,cuts[1:]))

def totalvar(h,d):
    m=slopes(h,d)
    s=0.
    for k, (hk,dk) in enumerate(zip(h,d)):
        a=dk-m[k]
        b=dk-m[k+1]
        # d/du = h*(6u-6u²)*d + h*mleft*(1-4u+3u²) + h*mright*(-2u+3u²)
        s+=hk*q_integral_abs(m[k],6*dk-4*m[k]-2*m[k+1],-6*dk+3*m[k]+3*m[k+1])
    return s

def differencevar(h,d,e):
    m=slopes(h,d); p=slopes(h,e)
    s=0.
    for k,hk in enumerate(h):
        dd=d[k]-e[k]; a=m[k]-p[k]; b=m[k+1]-p[k+1]
        s+=hk*q_integral_abs(a,6*dd-4*a-2*b,-6*dd+3*a+3*b)
    return s

def coeff(h):
    def phi(r):return 3*r*(1+r)/(1+2*r)
    qs=[]
    for j,x in enumerate(h):
        v=(phi(h[j-1]/x) if j>0 else 0)+(phi(h[j+1]/x) if j+1<len(h) else 0)
        qs.append(v)
    return 1+8*max(qs)/27,qs

def test():
    rng=random.Random(20261119)
    trials=0
    for n in range(2,13):
        for _ in range(280):
            h=[math.exp(rng.uniform(-2.5,2.5)) for j in range(n-1)]
            d=[rng.uniform(-3,3) for j in range(n-1)]
            e=[rng.uniform(-3,3) for j in range(n-1)]
            vd=sum(hk*abs(a-b) for hk,a,b in zip(h,d,e))
            K,_=coeff(h)
            assert abs(totalvar(h,d)-sum(hk*abs(x) for hk,x in zip(h,d)))<2e-8*max(1,sum(hk*abs(x) for hk,x in zip(h,d)))
            assert differencevar(h,d,e)<=K*vd+1e-8*max(1,vd)
            trials+=1
    witnesses=[]
    for h in ([1,1,1],[2,1,3],[0.4,1.7,0.3,8.2,0.1],[1,2],[5,0.2,5]):
        K,qs=coeff(h)
        j=max(range(len(qs)),key=qs.__getitem__)
        zero=[0.]*len(h)
        for k in [j-1,j+1]:
            if 0<=k<len(h):zero[k]=1.
        near=zero.copy(); near[j]=1e-7
        ratio=differencevar(h,near,zero)/(h[j]*1e-7)
        assert abs(ratio-K)<5e-5,(h,ratio,K)
        witnesses.append((h,round(K,9),round(ratio,9)))
    # Analytic corner nonnegativity, basis variation.
    assert abs(q_integral_abs(0,6,-6)-1)<1e-12
    assert abs(q_integral_abs(1,-4,3)-8/27)<1e-12
    assert abs(q_integral_abs(0,-2,3)-8/27)<1e-12
    print('PASS: random data / arbitrary positive meshes:',trials)
    print('PASS: sharp near-plateau witnesses:',witnesses)
    print('PASS: Hermite basis variation identities')
if __name__=='__main__':test()
