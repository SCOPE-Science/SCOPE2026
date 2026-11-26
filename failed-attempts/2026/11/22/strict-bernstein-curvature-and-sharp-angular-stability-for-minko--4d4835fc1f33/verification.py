"""Independent numerical spot checks for the ellipse mixed-area curvature theorem.

The theorem for all parameters is proved analytically in RESULT.md; this finite
checker tests independently derived formulas and representative boundary cases.
Requires only Python 3 standard library.
"""
import math

PI=math.pi

def simpson(f, lo, hi, n=4096):
    assert n % 2 == 0
    step=(hi-lo)/n
    total=f(lo)+f(hi)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(lo+j*step)
    return total*step/3

def geometry(a,b,c,d,angle):
    s=a*b/(c*d)
    base=a*a/(c*c)+b*b/(d*d)
    H=(a*a-b*b)*(1/(d*d)-1/(c*c))
    T=base+H*math.sin(angle)**2
    discriminant=math.sqrt(max(0.0,T*T-4*s*s))
    major2=(T+discriminant)/2
    minor2=(T-discriminant)/2
    perimeter=simpson(lambda t: math.sqrt(max(0.,major2*math.cos(t)**2+minor2*math.sin(t)**2)),0,2*PI)
    return PI*(a*b+c*d)+c*d*perimeter

def mixed_area(a,b,c,d,angle):
    def integrand(t):
        HA=math.hypot(a*math.cos(t),b*math.sin(t))
        u=t-angle
        HB=math.hypot(c*math.cos(u),d*math.sin(u))
        return HA*c*c*d*d/HB**3
    return PI*(a*b+c*d)+simpson(integrand,0,2*PI)

def shoelace_area(a,b,c,d,angle,n=8192):
    coords=[]
    for j in range(n):
        t=2*PI*j/n
        u=t-angle
        h1=math.hypot(a*math.cos(t),b*math.sin(t))
        h2=math.hypot(c*math.cos(u),d*math.sin(u))
        h=h1+h2
        hp=-(a*a-b*b)*math.sin(t)*math.cos(t)/h1-(c*c-d*d)*math.sin(u)*math.cos(u)/h2
        coords.append((h*math.cos(t)-hp*math.sin(t),h*math.sin(t)+hp*math.cos(t)))
    return .5*sum(coords[j][0]*coords[(j+1)%n][1]-coords[j][1]*coords[(j+1)%n][0] for j in range(n))

def laplace_perimeter(T,s):
    def integrand(v):
        if v==0: return 2*math.sqrt(2)*T
        if v==1: return 2*math.sqrt(2)
        t=(v/(1-v))**2
        x=2*t*T+4*s*s*t*t
        loss=-math.expm1(-.5*math.log1p(x))
        return math.sqrt(2)*2*loss/(v*v)
    return simpson(integrand,0,1,n=8192)

def direct_perimeter(T,s):
    root=math.sqrt(max(0.,T*T-4*s*s))
    hi=(T+root)/2
    low=(T-root)/2
    return simpson(lambda t:math.sqrt(max(0,hi*math.cos(t)**2+low*math.sin(t)**2)),0,2*PI)

n=0
for a,b,c,d in [(3,1,4,2),(10,1,10,1),(3,2,20,1),(2,1.95,1.3,1.1),(2,1,2,1)]:
    values=[]
    for u in (0,.05,.15,.3,.5,.7,.85,.95,1):
        angle=math.asin(math.sqrt(u))
        exact=geometry(a,b,c,d,angle)
        independent=mixed_area(a,b,c,d,angle)
        polygon=shoelace_area(a,b,c,d,angle)
        assert abs(exact-independent)<2e-7*max(1,exact), (a,b,c,d,angle,exact,independent)
        assert abs(exact-polygon)<1e-5*max(1,exact), (a,b,c,d,angle,exact,polygon)
        assert abs(exact-geometry(c,d,a,b,angle))<2e-8*max(1,exact)
        values.append((u,exact))
        n+=3
    bottom,top=values[0][1],values[-1][1]
    for u,value in values[1:-1]:
        gap=value-(1-u)*bottom-u*top
        assert gap>1e-9*max(1,top-bottom), (a,b,c,d,u,gap)
        n+=1
    for k in range(1,len(values)-1):
        u,val=values[k]
        ul,vl=values[k-1]; ur,vr=values[k+1]
        slope0=(val-vl)/(u-ul);slope1=(vr-val)/(ur-u)
        assert slope0>slope1, (a,b,c,d,u,slope0,slope1)
        n+=1
for s,T in [(1,2),(1,2.5),(1,3),(1,10),(.5,1.5),(2,10)]:
    lp=laplace_perimeter(T,s); pp=direct_perimeter(T,s)
    assert abs(lp-pp)<2e-6*max(1,pp), (s,T,lp,pp)
    n+=1
for a,b,c,d in [(2,2,5,1),(2,1,3,3),(2,2,3,3)]:
    vals=[geometry(a,b,c,d,j*PI/12) for j in range(7)]
    assert max(vals)-min(vals)<1e-8*max(vals)
    n+=1
print('ELLIPSE_MIXED_AREA_BERNSTEIN_PASS',n)
