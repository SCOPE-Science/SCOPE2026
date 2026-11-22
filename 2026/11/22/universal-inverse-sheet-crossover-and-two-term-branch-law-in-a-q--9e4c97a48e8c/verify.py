"""Exact symbolic and finite diagnostic checks of the sine-charge inverse theorem.
Run with Python 3 and SymPy installed; no network or external data required.
Finite diagnostics illustrate, but do not replace, the proof in RESULT.md.
"""
import math, random
import sympy as sp
x,q,V,a,w,b,R=sp.symbols('x q V a w b R',real=True)
phase=w*x*(1+b-b*q**2)
Phi=sp.expand(phase.subs(q,V-x))
assert sp.expand(Phi-w*(-b*x**3+2*b*V*x**2+(1+b-b*V**2)*x))==0
assert sp.expand(sp.diff(Phi,x)-w*(1+b-b*V**2+4*b*V*x-3*b*x*x))==0
assert sp.expand(Phi.subs(x,-R)-Phi.subs(x,R)-w*(2*b*R**3-2*(1+b-b*V**2)*R))==0
j11=a*w*(1+b-b*q*q)*sp.cos(phase)
j12=-2*a*w*b*q*x*sp.cos(phase)
assert sp.simplify((j11-j12).subs(q,V-x)-a*sp.cos(Phi)*sp.diff(Phi,x))==0

def crossing_count(lo,hi,t):
    if lo>hi:lo,hi=hi,lo
    al=math.asin(t)
    offsets = ([math.pi/2] if t==1 else [-math.pi/2] if t==-1 else [al,math.pi-al])
    ans=0
    for p in offsets:
        ans+=max(0,math.floor((hi-p)/(2*math.pi))-math.ceil((lo-p)/(2*math.pi))+1)
    return ans

def count_roots(A,omega,B,U,Vv,rad):
    def ph(t):return omega*t*(1+B-B*(Vv-t)**2)
    if abs(U)>A:return 0
    D=math.sqrt(Vv*Vv+3*(1+B)/B)
    stops=[-rad,rad]+[v for v in [(2*Vv-D)/3,(2*Vv+D)/3] if -rad<v<rad]
    stops=sorted(stops)
    count=sum(crossing_count(ph(L),ph(H),U/A) for L,H in zip(stops,stops[1:]))
    # Remove duplicate extrema exactly on a target phase level, if any.
    for p in stops[1:-1]:
        if abs(math.sin(ph(p))-U/A)<1e-11: count-=1
    return count

rng=random.Random(421)
for i in range(100):
    A=0.3+2*rng.random(); omega=0.4+2*rng.random(); B=0.1+2*rng.random()
    U=A*(2*rng.random()-1); Vv=5*(2*rng.random()-1)
    rad=5+40*rng.random()
    actual=count_roots(A,omega,B,U,Vv,rad)
    ph=lambda t:omega*t*(1+B-B*(Vv-t)**2)
    D=math.sqrt(Vv*Vv+3*(1+B)/B)
    stops=sorted([-rad,rad]+[v for v in [(2*Vv-D)/3,(2*Vv+D)/3] if -rad<v<rad])
    variation=sum(abs(ph(v)-ph(u)) for u,v in zip(stops,stops[1:]))
    assert abs(actual-variation/math.pi)<8,(actual,variation,A,omega,B,U,Vv,rad)
    actual_end=count_roots(A,omega,B,A,Vv,rad)
    assert abs(actual_end-variation/(2*math.pi))<6,(actual_end,variation)
for B in [0.001,0.01,0.1,1,3]:
    for rad in [50,100,300]:
        actual=count_roots(1,math.pi,B,0.237,1.15,rad)
        if rad>=5*math.sqrt((1+B)/B+1.15*1.15):
            approx=2*(B*rad**3-(1+B-B*1.15**2)*rad)
            # Fixed-parameter bounded remainder includes the central positive excursion.
            xc1=(2*1.15-math.sqrt(1.15**2+3*(1+B)/B))/3
            xc2=(2*1.15+math.sqrt(1.15**2+3*(1+B)/B))/3
            ph=lambda t:math.pi*t*(1+B-B*(1.15-t)**2)
            approx+=(2/math.pi)*(ph(xc2)-ph(xc1))
            assert abs(actual-approx)<8,(actual,approx)
def psi(t):
    t0=1/math.sqrt(3)
    return 2*(t-t**3) if t<=t0 else 2*(t**3-t+4/(3*math.sqrt(3)))
for B in [1e-3,1e-4,1e-5]:
    for t in [.2,.5,1/math.sqrt(3),.8,1,2]:
        rad=t/math.sqrt(B)
        c=count_roots(1,math.pi,B,.237,1.15,rad)
        target=psi(t)  # omega = pi
        err=abs(math.sqrt(B)*c-target)
        assert err<1.1*math.sqrt(B)+.03,(B,t,c,target,err)
print('PASS symbolic phase/derivative/Jacobian/endpoints, two-term inverse count and 18 crossover diagnostics')
