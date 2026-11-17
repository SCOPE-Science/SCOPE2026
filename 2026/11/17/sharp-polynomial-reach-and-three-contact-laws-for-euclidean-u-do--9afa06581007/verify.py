"""Finite, independent checks for U-domain Euclidean outer parallel volume.
Python standard library only. Numerical evidence does not establish infinite claims.
"""
from math import pi, sqrt, acos, hypot

def primitive_disk(t,x):
    return (x*sqrt(max(0.,t*t-x*x))+t*t*__import__('math').asin(min(1.,x/t)))/2

def E(q,t):
    d=t-q
    if d<=0:return 0.
    return t*d-(primitive_disk(t,d)-primitive_disk(t,0.))

def gamma_onset(g,q,t):
    m=g/2
    if t<=m:return 0.
    if t>=g or (q>m and t>=q):
        raise ValueError('onset formula used outside its proved interval')
    capheight=sqrt(t*t-m*m)
    lower=max(0.,t-q)
    # Part above top H, not covered by the base rectangle's radius-t offset.
    cap=2*(primitive_disk(t,capheight)-primitive_disk(t,lower)-m*(capheight-lower)) if lower<capheight else 0.
    rect=2*(t-m)*max(0.,q-t)
    return cap+rect

def u_formula(a,b,g,q,t):
    W=2*a+g;H=b+q;m=g/2
    P=(2*W+4*H-2*b)*t+(3*pi/2-2)*t*t
    # Formula valid for t before the second of q and m, and slightly after the first.
    if t<=min(q,m):return P
    if q<m and t<m: return P+2*E(q,t) # two independent notch-tip corrections
    if q>=m and t<min(q if q>m else g,g):
        return P-gamma_onset(g,q,t)
    raise ValueError('outside local verification interval')

def dist_rect(x,y,x1,y1,x2,y2):
    dx=max(x1-x,x-x2,0.)
    dy=max(y1-y,y-y2,0.)
    return hypot(dx,dy)

def u_direct(a,b,g,q,t,N=480):
    W=2*a+g;H=b+q
    left=-t;bottom=-t;dx=(W+2*t)/N;dy=(H+2*t)/N
    inside=0
    for i in range(N):
        x=left+(i+.5)*dx
        for j in range(N):
            y=bottom+(j+.5)*dy
            if min(dist_rect(x,y,0,0,W,b),dist_rect(x,y,0,0,a,H),dist_rect(x,y,a+g,0,W,H))<=t:
                inside+=1
    S_area=W*b+2*a*q
    return dx*dy*inside-S_area

def run():
    checks=0
    for a,b,g,q in [(1,1,2,.6),(1,1,2,1),(1,1,2,1.4),(.2,.8,2,.65),(1.5,.3,1,1),(.4,.8,3,2)]:
        m=min(q,g/2)
        for t in [.22*m,.65*m,.95*m,1.02*m,1.08*m]:
            formula=u_formula(a,b,g,q,t)
            approximate=u_direct(a,b,g,q,t,N=380)
            assert abs(formula-approximate)<.015*(1+a+b+g+q+t),(a,b,g,q,t,formula,approximate)
            checks+=1
            P=(2*(2*a+g)+4*(b+q)-2*b)*t+(3*pi/2-2)*t*t
            if t<m:assert abs(formula-P)<1e-12
            elif q<g/2: assert formula>P
            else:assert formula<P
            checks+=1
    for g,q in [(2.,.7),(2.,1.),(2.,1.4),(1.,.8),(3.,1.5)]:
        m=min(q,g/2)
        target=1/(3*q) if q<g/2 else -(4/3)*sqrt(g) if q==g/2 else -2*(q-g/2)
        for d in [m*.001,m*.005,m*.01]:
            t=m+d
            p=(2*(2*1+g)+4*(1+q)-2*1)*t+(3*pi/2-2)*t*t
            val=u_formula(1,1,g,q,t)-p
            test=val/d**3 if q<g/2 else val/d**1.5 if q==g/2 else val/d + (4/3)*sqrt(g)*sqrt(d)
            err=abs(test-target)
            tolerance=(.3 if q==g/2 else .075)*max(1,abs(target))
            assert err<tolerance,(g,q,d,test,target,err)
            checks+=1
    print('PASS',checks,'grid/area comparisons and first-contact asymptotic checks')

if __name__=='__main__':run()
