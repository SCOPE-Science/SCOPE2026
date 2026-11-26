"""Independent finite diagnostics for circular-frustum orthographic shadows.

Run with Python 3 standard library: python3 checks/frustum_checker.py
The analytic proof is in RESULT.md; finite tests are diagnostics only.
"""
import math

CHECKS = 0

def near(actual, expected, atol=0.0004, rtol=0):
    global CHECKS
    CHECKS += 1
    if not math.isclose(actual, expected, abs_tol=atol, rel_tol=rtol):
        raise AssertionError((actual, expected, atol, rtol))

def simpson(f, lo, hi, n=2048):
    if n % 2: raise ValueError('even n required')
    h=(hi-lo)/n
    total=f(lo)+f(hi)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*f(lo+i*h)
    return total*h/3

def reference_area_perimeter(R,r,H,theta):
    """Explicit formulas, independently compared against polygonized silhouettes."""
    delta=R-r
    s,c=math.sin(theta),math.cos(theta)
    L=math.hypot(H,delta)
    q=lambda t:math.sqrt(max(0.0,1.0-s*s*math.cos(t)**2))
    baseline=R*simpson(q,0.0,2*math.pi)
    threshold=math.atan2(delta,H)
    if theta<=threshold:
        return math.pi*R*R*c,baseline
    if abs(c)<1e-12:
        return (R+r)*H,2*(R+r)+2*L
    alpha=math.acos(delta/(s*L))
    add=2*simpson(lambda t:H*s*math.cos(t)-delta*q(t),0,alpha)
    D=H*math.tan(theta)
    ell=math.sqrt(max(0.0,(D-delta)*(D+delta)))
    alpha_disk=math.atan2(ell,delta)
    area=c*(math.pi*R**2+(R+r)*(ell-delta*alpha_disk))
    return area,baseline+add

def convex_hull(points):
    pts=sorted(set(points))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def polygon_metrics(points):
    hull=convex_hull(points)
    area=0.0; perimeter=0.0
    for p,q in zip(hull,hull[1:]+hull[:1]):
        area+=p[0]*q[1]-q[0]*p[1]
        perimeter+=math.hypot(p[0]-q[0],p[1]-q[1])
    return abs(area)/2,perimeter

def discretized_shadow(R,r,H,theta,n=1500):
    c,s=math.cos(theta),math.sin(theta)
    points=[]
    for j in range(n):
        t=2*math.pi*j/n
        ct,st=math.cos(t),math.sin(t)
        points.append((R*c*ct,R*st))
        points.append((H*s+r*c*ct,r*st))
    return polygon_metrics(points)

def exact_cusps(R,r,H):
    d=R-r;L=math.hypot(H,d)
    return 4*math.sqrt(2)/3*L*math.sqrt(H/d), 2*math.sqrt(2)/3*(R+r)*L**2/math.sqrt(d*H)

def area_excess(R,r,H,theta):
    d=R-r;c=math.cos(theta);D=H*math.tan(theta)
    if D<=d:return 0.0
    ell=math.sqrt((D-d)*(D+d))
    # arctan is stable at the internal-tangency threshold
    alpha=math.atan2(ell,d)
    return c*(R+r)*(ell-d*alpha)

def perimeter_excess(R,r,H,theta):
    d=R-r;L=math.hypot(H,d);s=math.sin(theta)
    if s<=d/L:return 0.0
    alpha=math.acos(d/(s*L));q=lambda t:math.sqrt(1-s*s*math.cos(t)**2)
    return 2*simpson(lambda t:H*s*math.cos(t)-d*q(t),0,alpha,4096)

def run():
    sets=[(2.3,.8,2.7),(1.2,.25,.7),(1.9,1.2,.4),(3.4,3.1,8.0),(1.0,.2,2.0),(2.7,1.6,3.2)]
    for R,r,H in sets:
        d=R-r;L=math.hypot(d,H);tc=math.atan2(d,H)
        near(math.sin(tc),d/L,1e-13)
        for t in [0.0,0.4*tc,tc,tc+(math.pi/2-tc)*0.14,tc+(math.pi/2-tc)*0.48,math.pi/2]:
            area,p=reference_area_perimeter(R,r,H,t)
            ah,ph=discretized_shadow(R,r,H,t)
            near(area,ah,0.00012)
            near(p,ph,0.00012)
        _, p_ax=reference_area_perimeter(R,r,H,0)
        _, p_side=reference_area_perimeter(R,r,H,math.pi/2)
        near(p_ax,2*math.pi*R,1e-9)
        near(p_side,2*(R+r)+2*L,1e-9)
        cp,ca=exact_cusps(R,r,H)
        near(ca/cp,(R+r)*L/(2*H),1e-10)
        for eps in [0.0004,0.00015,0.00005]:
            if tc+eps>=math.pi/2: continue
            pe=perimeter_excess(R,r,H,tc+eps)
            ae=area_excess(R,r,H,tc+eps)
            near(pe/(cp*eps**1.5),1.0,0.010)
            near(ae/(ca*eps**1.5),1.0,0.010)
        Rrec=p_ax/(2*math.pi)
        Lrec=3*cp/(4*math.sqrt(2))*math.sqrt(math.tan(tc))
        near(Rrec,R,1e-10)
        near(Lrec*math.cos(tc),H,1e-10)
        near(Rrec-Lrec*math.sin(tc),r,1e-10)
        B=(p_side-4*R)/2
        L2=B/(1-math.sin(tc))
        near(L2,L,1e-10)
    print('PASS:',CHECKS,'independent finite analytic/convex-hull checks')

if __name__=='__main__': run()
