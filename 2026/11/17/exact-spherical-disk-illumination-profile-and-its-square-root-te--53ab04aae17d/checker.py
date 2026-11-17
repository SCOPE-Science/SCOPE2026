"""Independent numerical consistency checks for a spherical-cap illumination formula.

Requires only Python standard library. This is not a substitute for the proof.
Run: python checker.py
"""
import math

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(v): return math.sqrt(dot(v,v))
def sph_tri(a,b,c):
    num=abs(dot(a,cross(b,c)))
    den=1+dot(a,b)+dot(b,c)+dot(c,a)
    return 2*math.atan2(num,den)
def lift(q,M,E,F):
    v=tuple(M[j]+q[0]*E[j]+q[1]*F[j] for j in range(3))
    nv=norm(v)
    return tuple(x/nv for x in v)
def hull(pts):
    ps=sorted(set(pts))
    def orient(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in ps:
        while len(lower)>=2 and orient(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(ps):
        while len(upper)>=2 and orient(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]
def geom_added_area(r,t,n=800):
    alpha=(t-r)/2
    M=(math.sin(alpha),0.,math.cos(alpha))
    E=(math.cos(alpha),0.,-math.sin(alpha))
    F=(0.,1.,0.)
    pts=[]
    for i in range(n):
        ph=2*math.pi*i/n
        v=(math.sin(r)*math.cos(ph),math.sin(r)*math.sin(ph),math.cos(r))
        d=dot(v,M)
        pts.append((dot(v,E)/d,dot(v,F)/d))
    P=(math.sin(t),0.,math.cos(t))
    pts.append((dot(P,E)/dot(P,M),dot(P,F)/dot(P,M)))
    phull=hull(pts)
    center=(sum(p[0] for p in phull)/len(phull),sum(p[1] for p in phull)/len(phull))
    z=lift(center,M,E,F)
    vs=[lift(p,M,E,F) for p in phull]
    area=sum(sph_tri(z,vs[i],vs[(i+1)%len(vs)]) for i in range(len(vs)))
    return area-2*math.pi*(1-math.cos(r))
def formula(r,t):
    if not (0<r<math.pi/2 and r<t<math.pi-r): raise ValueError('domain')
    u=math.acos(max(-1,min(1,math.tan(r)*math.cos(t)/math.sin(t))))
    v=math.asin(min(1,math.sin(r)/math.sin(t)))
    return 2*(math.cos(r)*u+v)-math.pi
def deriv(r,t):
    return 2*math.sin(r)*(math.cos(r)-math.cos(t))/(math.sin(t)*math.sqrt(math.sin(t)**2-math.sin(r)**2))
def integration(r,t,n=6000):
    # z^2 substitution removes the square-root singularity at s=r
    h=t-r
    def g(z):
        if z==0: return 0.
        return deriv(r,r+h*z*z)*2*h*z
    s=g(0)+g(1)
    for i in range(1,n): s+=(4 if i%2 else 2)*g(i/n)
    return s/(3*n)

def checks():
    counts=0
    for r,t in [(.12,.35),(.12,1.9),(.5,.9),(.5,1.8),(.5,2.3),(1.1,1.4),(1.1,1.9)]:
        val=formula(r,t)
        assert 0<val<2*math.pi*math.cos(r)
        direct=geom_added_area(r,t,n=1000)
        assert abs(direct-val)<6e-6,(r,t,direct,val)
        numeric=integration(r,t)
        assert abs(numeric-val)<1e-6,(r,t,numeric,val)
        counts+=3
    for r in [.15,.5,1.1]:
        h=1e-4
        a=formula(r,r+h)/h**1.5
        a0=2/3*math.sqrt(2*math.tan(r))
        b=(2*math.pi*math.cos(r)-formula(r,math.pi-r-h))/math.sqrt(h)
        b0=4*math.sqrt(2/math.tan(r))
        assert abs(a/a0-1)<.003,(r,a/a0)
        assert abs(b/b0-1)<.003,(r,b/b0)
        counts+=2
    print('PASS:',counts,'numerical comparisons; spherical polygons are independently projected and triangulated')
if __name__=='__main__': checks()
