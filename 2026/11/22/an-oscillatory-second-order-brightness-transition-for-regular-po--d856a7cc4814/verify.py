"""Independent numerical checks for regular-pyramid brightness identities.
Only Python standard library. Numerical tests are not proofs.
"""
import math
import random
import itertools

PI=math.pi

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def unit(a):
    t=norm(a)
    return tuple(x/t for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def pyramid(n,h):
    return [(math.cos(2*PI*j/n),math.sin(2*PI*j/n),0.0) for j in range(n)]+[(0.,0.,h)]

def hull_area(pts):
    pts=sorted(pts)
    def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in pts:
        while len(low)>1 and cr(low[-2],low[-1],p)<=1e-13:low.pop()
        low.append(p)
    high=[]
    for p in reversed(pts):
        while len(high)>1 and cr(high[-2],high[-1],p)<=1e-13:high.pop()
        high.append(p)
    hull=low[:-1]+high[:-1]
    return abs(sum(hull[j][0]*hull[(j+1)%len(hull)][1]-hull[j][1]*hull[(j+1)%len(hull)][0] for j in range(len(hull))))/2

def projected_area(n,h,u):
    u=unit(u)
    b=unit(cross(u,(1.,0.,0.)) if abs(u[0])<.8 else cross(u,(0.,1.,0.)))
    c=cross(u,b)
    return hull_area([(dot(p,b),dot(p,c)) for p in pyramid(n,h)])

def brightness(n,h,u):
    a=PI/n; s=math.sin(a)*math.cos(a)
    total=abs(n*s*u[2])
    total+=sum(abs(h*math.sin(a)*(math.cos((2*j+1)*a)*u[0]+math.sin((2*j+1)*a)*u[1])+s*u[2]) for j in range(n))
    return total/2

def max_formula(n,h):
    a=PI/n;s=math.sin(a)*math.cos(a)
    return math.sqrt(max(h*h*math.sin(k*a)**2+k*k*s*s for k in range((n+1)//2,n+1)))

def threshold(n):
    a=PI/n;s=math.sin(a)*math.cos(a)
    return min((n*n-k*k)*s*s/(math.sin(k*a)**2) for k in range((n+1)//2,n))

def exhaustive_max(n,h):
    a=PI/n;s=math.sin(a)*math.cos(a)
    q=[(h*math.sin(a)*math.cos((2*j+1)*a), h*math.sin(a)*math.sin((2*j+1)*a),s) for j in range(n)]
    best=0.
    for mask in range(1<<n):
        v=[sum(q[j][r] for j in range(n) if mask & (1<<j)) for r in range(3)]
        best=max(best,norm(v))
    return best

def root_constants():
    def f(x):return x+PI*(1-x*x)/math.tan(PI*x)
    lo,hi=.5,.999
    for j in range(85):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    x=(lo+hi)/2
    ss=math.sin(PI*x)
    R=(1-x*x)/ss**2
    fp=1-2*PI*x/math.tan(PI*x)-PI*PI*(1-x*x)/ss**2
    Rpp=-2*fp/ss**2
    t0=PI*PI*R
    return x,t0,PI*PI*Rpp/2,-4*PI*PI*t0/3

def run():
    rng=random.Random(217706)
    checks=0
    for n in [5,6,7,8,10,13,24,41]:
        for h in [.24,.87,1.55,2.0,2.5,3.15,5.0]:
            for j in range(50):
                u=unit((rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)))
                a=projected_area(n,h,u)
                b=brightness(n,h,u)
                assert abs(a-b)<1e-9*max(1,a,b),(n,h,a,b)
                checks+=1
            if n<=10:
                e=exhaustive_max(n,h)
                m=max_formula(n,h)
                assert abs(e-m)<1e-9,(n,h,e,m)
                checks+=1
    x,t0,coef,base=root_constants()
    assert .5889<x<.5891 and 6.976<t0<6.978
    for n in [100,170,251,400,1000]:
        t=threshold(n)
        pred=t0+(base+coef*min(abs(n*x-k) for k in range(n+1))**2)/n**2
        assert abs(t-pred)<20/n**3,(n,t,pred)
        checks+=1
    print('PASS',checks,'numerical checks; critical x=',x,'cone t=',t0,'coef=',coef,'base=',base)

if __name__=='__main__':run()
