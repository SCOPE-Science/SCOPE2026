"""Reproducibility diagnostics for the Jordan Ritt cluster law (standard library)."""
import math

def g(x):
    return math.sqrt(1.0+(x/2.0)**2)+x/2.0

def f(c,t):
    return t*math.exp(-t)*g(c*abs(t-1.0))

def critical(c,side):
    lo,hi=(0.0,1.0) if side=='left' else (1.0,3.0)
    for _ in range(90):
        t=(lo+hi)/2
        d=1.0/t-1.0 + ((-1 if side=='left' else 1)*c/math.sqrt(4.0+c*c*(t-1)**2))
        if d>0: lo=t
        else: hi=t
    return (lo+hi)/2

def scalar_exact(c,q,n,j):
    e=q**j
    r=1-e
    d=n*e*r**n
    b=n*c*e*r**(n-1)*((n+1)*e-1)
    return math.hypot(d,b/2)+abs(b)/2

def H(c,q,u):
    tl,tr=critical(c,'left'),critical(c,'right')
    vals=[]
    for t in (tl,tr):
        k=math.floor(math.log(t/u)/math.log(q))
        vals.extend([f(c,u*q**k),f(c,u*q**(k+1))])
    return max(vals)

def brute(c,q,u):
    return max(f(c,u*q**j) for j in range(-25,26))

assertions=0
for c in (0.1,0.4,1.0,1.5,5.0):
    tl,tr=critical(c,'left'),critical(c,'right')
    assert 0<tl<1<tr<(3+math.sqrt(5))/2
    assert f(c,tr)>f(c,tl)>f(c,1)
    assertions+=3
    for q in (.23,.5,.82):
        for m in range(101):
            u=q**(-m/100)
            assert abs(H(c,q,u)-brute(c,q,u))<1e-11
            assertions+=1
        for n in (1,2,3,5,50,100,1000,3000,10000):
            # finite block norms computed from explicit entry formula and from singular-value expression
            for j in range(1,15):
                e=q**j; r=1-e
                diag=n*e*r**n
                off=n*c*e*r**(n-1)*((n+1)*e-1)
                lhs=math.sqrt(diag**2+off**2/4)+abs(off)/2
                rhs=scalar_exact(c,q,n,j)
                assert abs(lhs-rhs)<1e-12
                assertions+=1
            if n>=1000:
                D=max(scalar_exact(c,q,n,j) for j in range(1,230))
                z=math.log(n)/math.log(1/q)
                theta=z-math.floor(z)
                u=q**(-theta)
                assert abs(D-H(c,q,u))<.012, (c,q,n,D,H(c,q,u))
                assertions+=1
print('JORDAN_RITT_DIAGNOSTICS_OK', assertions)

def threshold_roots(c):
    tl,tr=critical(c,'left'),critical(c,'right')
    z=math.exp(-1)
    lo,hi=0.0,tl
    for _ in range(90):
        m=(lo+hi)/2
        if f(c,m)<z:lo=m
        else:hi=m
    a=(lo+hi)/2
    lo,hi=tr,50.0
    for _ in range(90):
        m=(lo+hi)/2
        if f(c,m)>z:lo=m
        else:hi=m
    b=(lo+hi)/2
    return a,b

for c in (0.1,0.5,1.0,3.0):
    a,b=threshold_roots(c)
    q1=a/b
    q2=min(a,1/b)
    assert 0<q1<q2<1 and abs(f(c,a)-math.exp(-1))<1e-12 and abs(f(c,b)-math.exp(-1))<1e-12
    assertions+=3
    for q,regime in ((q1*.8,'below'),((q1+q2)/2,'plateau'),((1+q2)/2,'above')):
        vals=[H(c,q,q**(-i/600)) for i in range(601)]
        m=min(vals)
        if regime=='below':assert m<math.exp(-1)-1e-5, (c,q,m)
        elif regime=='above':assert m>math.exp(-1)+1e-5, (c,q,m)
        else:assert abs(m-math.exp(-1))<1e-11,(c,q,m)
        assertions+=1
print('JORDAN_RITT_PLATEAU_DIAGNOSTICS_OK', assertions)
