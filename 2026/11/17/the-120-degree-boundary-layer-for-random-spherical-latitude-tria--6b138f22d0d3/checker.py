"""Independent checks of three-point spherical 120-degree latitude sampling.
Only standard-library arithmetic. Numerical checks support, not replace, the proof.
"""
from math import sin, cos, acos, atan, atan2, tan, pi, sqrt, isclose

def psi(c, a):
    return atan2(cos(a), c*sin(a))

def formula_angles(c, g):
    f=[psi(c,x) for x in g]
    return [f[(i-1)%3]+f[i] for i in range(3)]

def vector_angles(c,g):
    import math
    s=sqrt(1-c*c)
    phi=[0,2*g[0],2*(g[0]+g[1])]
    pts=[(s*cos(t),s*sin(t),c) for t in phi]
    dot=lambda x,y:sum(a*b for a,b in zip(x,y))
    ret=[]
    for i in range(3):
        p=pts[i];q=pts[(i-1)%3];r=pts[(i+1)%3]
        a=dot(p,q);b=dot(p,r);d=dot(q,r)
        val=(d-a*b)/sqrt((1-a*a)*(1-b*b))
        ret.append(acos(max(-1,min(1,val))))
    return ret

def simpson(f,a,b,n=40000):
    h=(b-a)/n
    v=f(a)+f(b)
    for j in range(1,n):v+=(4 if j%2 else 2)*f(a+j*h)
    return v*h/3

def p_exact(c):
    beta=2*pi/3
    def f(a):
        y=beta-psi(c,a)
        b0=atan2(1,c*tan(y)) if y < pi/2 else 0.
        return max(0.,(pi-a)/2-max(a,b0))
    return 12/pi**2*simpson(f,1e-12,pi/3,30000)

if __name__=='__main__':
    for c in (.01,.1,.5,.999):
        for g in ((.2,.4,pi-.6),(.1,1.3,pi-1.4),(.95,1.,pi-1.95)):
            a=formula_angles(c,g);b=vector_angles(c,g)
            assert max(abs(x-y) for x,y in zip(a,b))<1e-9,(c,g,a,b)
    for c in (.2,.5,.8,1):
        p=p_exact(c)
        print('exact',c,p)
    for c in (.1,.05,.02,.01):
        p=p_exact(c)
        print('equator coefficient',c,p/c**2,'target',4/pi**2)
        assert abs(p/c**2-4/pi**2)<.035
    assert abs(p_exact(1)-2/3)<1e-9
    print('SPHERICAL_LATITUDE_120_LAW_CHECKS_OK')
