"""Finite reproducibility checks of gyroelongated square-bipyramid inballs.
Only Python standard library is required; these checks supplement the proof.
Run: python3 verify.py
"""
import math

s = math.sqrt(2)
B = 3-2*s
A = 4-2*s
h0 = s-1
hvol = (math.sqrt(10+6*s)-1)/(3*(1+s))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(x): return math.sqrt(dot(x,x))

def vertices(h):
    r=math.sqrt(1-h*h)
    return [(0.,0.,1.),(0.,0.,-1.)]+[(r*math.cos(math.pi/8+j*math.pi/4),r*math.sin(math.pi/8+j*math.pi/4),(-1)**j*h) for j in range(8)]

def hull_faces(vertices):
    """Enumerate every supporting plane through a triple; deduplicate faces."""
    out={}
    n=len(vertices)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                p=cross(sub(vertices[j],vertices[i]),sub(vertices[k],vertices[i]))
                pn=norm(p)
                if pn<1e-12: continue
                offset=dot(p,vertices[i]); errs=[dot(p,v)-offset for v in vertices]
                if max(errs)<1e-9*pn:pass
                elif min(errs)>-1e-9*pn:
                    p=tuple(-v for v in p);offset=-offset;errs=[-e for e in errs]
                else:continue
                assert offset>0
                face=frozenset(i for i,e in enumerate(errs) if abs(e)<1e-9*pn)
                out[face]=(tuple(e/pn for e in p),offset/pn)
    return out

def area(v,face,n):
    p=[v[i] for i in face];c=tuple(sum(x[k] for x in p)/len(p) for k in range(3))
    u=sub(p[0],c);un=norm(u);u=tuple(x/un for x in u);w=cross(n,u)
    p.sort(key=lambda x: math.atan2(dot(sub(x,c),w),dot(sub(x,c),u)))
    return sum(dot(n,cross(sub(p[i],c),sub(p[(i+1)%len(p)],c)))/2 for i in range(len(p)))

def cap(h):return math.sqrt((1+h)/(3-h))
def belt(h):return 1/math.sqrt(A*A/(1-h*h)+B*B/(h*h))
def inball(h):return min(cap(h),belt(h))
def volume(h):return (4/3)*(1-h*h)*(1+(1+s)*h)

assert 0<B<h0<hvol<1
assert abs(cap(h0)-belt(h0))<1e-14
assert abs(cap(h0)-math.sqrt((1+2*s)/7))<1e-14
checks=0
for k in range(201):
    h=B+(1-B)*(k+.25)/202
    v=vertices(h);fs=hull_faces(v)
    assert len(fs)==16 and all(len(f)==3 for f in fs)
    distances=[d for _,d in fs.values()]
    assert abs(min(distances)-inball(h))<2e-9,(h,distances)
    checks+=2
    val=sum(d*area(v,f,n) for f,(n,d) in fs.items())/3
    assert abs(val-volume(h))<3e-9,(h,val,volume(h))
    checks+=1
for h in [B+.00001,h0,hvol,.4,.5,.8,.99]:
    f=hull_faces(vertices(h))
    assert len(f)==16
    assert abs(min(d for _,d in f.values())-inball(h))<2e-9
    checks+=2
assert all(inball(B+(1-B)*i/10000)<inball(h0)+1e-12 for i in range(1,10000))
assert inball(hvol)<inball(h0) and volume(hvol)>volume(h0)
assert abs(volume(hvol)-2.2187111315)<2e-10
checks+=3
print('PASS',checks,'geometric consistency checks')
print('height at best inball:',repr(h0))
print('inradius:',repr(inball(h0)))
print('height at volume optimum:',repr(hvol))
print('volume at inball optimum:',repr(volume(h0)))
