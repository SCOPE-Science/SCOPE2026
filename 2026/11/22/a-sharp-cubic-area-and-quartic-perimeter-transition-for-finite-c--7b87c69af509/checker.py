#!/usr/bin/env python3
"""Independent polygonal and limiting checks for finite circular-involute hull formulas."""
import math

ALPHA = 4.4934094579090641753

def z(t): return complex(math.cos(t)+t*math.sin(t), math.sin(t)-t*math.cos(t))

def ff(d):return (d-math.sin(d))/(1-math.cos(d))

def contact(T):
    if T<=ALPHA:return 0.,T
    l,r=ALPHA,2*math.pi-1e-6
    while ff(r)<T:r=(r+2*math.pi)/2
    for _ in range(90):
        m=(l+r)/2
        if ff(m)<T:l=m
        else:r=m
    d=(l+r)/2
    return T-d,d

def hull_formula(T):
    s,d=contact(T)
    A=(T**3-s**3)/6-((1+s*T)*math.sin(d)-d*math.cos(d))/2
    P=(T*T-s*s)/2+abs(z(T)-z(s))
    return s,A,P

def hull(vertices):
    pts=sorted(vertices)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def discrete(T,N):
    verts=[(z(T*i/N).real,z(T*i/N).imag,i) for i in range(N+1)]
    h=hull(verts)
    area=abs(sum(h[i][0]*h[(i+1)%len(h)][1]-h[(i+1)%len(h)][0]*h[i][1] for i in range(len(h))))/2
    perimeter=sum(math.hypot(h[i][0]-h[(i+1)%len(h)][0],h[i][1]-h[(i+1)%len(h)][1]) for i in range(len(h)))
    return area,perimeter,min(q[2] for q in h)*T/N,len(h)

def main():
    count=0
    for T in (0.25,1.,3.,4.0,ALPHA,4.5,5.,8.,10.,20.,50.):
        s,A,P=hull_formula(T)
        a,p,min_t,v=discrete(T,7000)
        assert abs(a/A-1)<0.00013,(T,'area',a,A)
        assert abs(p/P-1)<0.00013,(T,'perimeter',p,P)
        assert abs(min_t-s)<min(0.09,T/40),(T,'contact',min_t,s)
        count+=3
        print(f'T={T:.9f}, s={s:.9f}, area={A:.9f}, perimeter={P:.9f}, discrete_error=({a/A-1:+.2e},{p/P-1:+.2e}), hull_vertices={v}')
    rho=math.sqrt(1+ALPHA**2)
    k=1-1/rho
    cA=(rho+1)*k**3/12
    cP=k**4/24
    print('ALPHA',ALPHA,'rho',rho,'k',k,'cubic-area',cA,'quartic-perimeter',cP)
    assert abs(math.tan(ALPHA)-ALPHA)<2e-12
    count+=1
    for e in (0.2,0.1,0.04,0.01,0.002):
        T=ALPHA+e
        s,A,P=hull_formula(T)
        A0=T**3/6 + (T*math.cos(T)-math.sin(T))/2
        P0=T*T/2+abs(z(T)-z(0))
        ratA=(A-A0)/(cA*e**3)
        ratP=-(P-P0)/(cP*e**4)
        assert abs(ratA-1)<1.3*e
        if e>=.01:assert abs(ratP-1)<3*e
        print(f'eps={e} ratios: area={ratA:.8f} perimeter={ratP:.8f} contact={s/e:.8f}')
        count+=2
    print('PASSED',count,'tests; discrete polygon approximations are supplemental, not proof')
if __name__=='__main__': main()
