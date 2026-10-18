import math

SQ2=math.sqrt(2.0)
R=SQ2-1.0
TOL=5e-12

V=[(1.0,R),(R,1.0),(-R,1.0),(-1.0,R),(-1.0,-R),(-R,-1.0),(R,-1.0),(1.0,-R)]
F=[(1.0,0.0),(-1.0,0.0),(0.0,1.0),(0.0,-1.0),(1.0/SQ2,1.0/SQ2),(-1.0/SQ2,-1.0/SQ2),(1.0/SQ2,-1.0/SQ2),(-1.0/SQ2,1.0/SQ2)]

def dual(a):
    return max(abs(x*a[0]+y*a[1]) for x,y in V)

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])

def N(z):
    x,y=z
    return max(abs(x),abs(y),(abs(x)+abs(y))/SQ2)

pairs=[]
for f in F:
    for g in F:
        pairs.append((dual(add(f,g)),dual(sub(f,g))))

expected=[(2.0,0.0),(0.0,2.0),(2.0,2.0*R),(2.0*R,2.0),(SQ2,SQ2)]
for a,b in pairs:
    assert any(abs(a-c)<TOL and abs(b-d)<TOL for c,d in expected),(a,b)
for c,d in expected:
    assert any(abs(a-c)<TOL and abs(b-d)<TOL for a,b in pairs),(c,d)

support_checks=0
for k in range(4001):
    t=k/4000.0
    target=2.0*(1.0+R*t)
    for a,b in pairs:
        assert a+t*b <= target+TOL
        support_checks += 1

u=(1.0,R); v=(-R,1.0)
chord_checks=0
for k in range(4001):
    t=k/4000.0
    ap=N((u[0]+t*v[0],u[1]+t*v[1]))
    am=N((u[0]-t*v[0],u[1]-t*v[1]))
    target=1.0+R*t
    assert abs(ap-target)<2e-12 and abs(am-target)<2e-12
    chord_checks += 1

ps=[1.0,1.25,1.5,2.0,3.0,4.0,8.0,20.0,float('inf')]
profile_checks=0
for p in ps:
    if p==1.0:
        val=1.0; tstar=0.0
    elif math.isinf(p):
        val=1.0+R; tstar=1.0
    else:
        q=p/(p-1.0)
        val=(1.0+R**q)**(1.0/q)
        tstar=R**(1.0/(p-1.0))
    def quot(t):
        den=1.0 if math.isinf(p) else (1.0+t**p)**(1.0/p)
        return (1.0+R*t)/den
    assert abs(quot(tstar)-val)<2e-11,(p,tstar,quot(tstar),val)
    for k in range(3001):
        t=k/3000.0
        assert quot(t)<=val+2e-11,(p,t,quot(t),val)
        profile_checks+=1

print(f"VERIFY_OK support_pairs={len(pairs)} support_checks={support_checks} chord_checks={chord_checks} profile_checks={profile_checks} endpoints=1,sqrt2")
