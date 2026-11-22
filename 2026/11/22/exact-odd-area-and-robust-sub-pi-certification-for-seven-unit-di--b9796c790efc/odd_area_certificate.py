#!/usr/bin/env python3
"""Exact rational enclosures for an odd-area seven-unit-disk configuration.

Only the Python standard library is used. No floating point is used in the
interval certificate; the independent polar quadrature at the end uses floats.
"""
from fractions import Fraction as F
from math import isqrt, comb, pi, sin, cos, sqrt

PREC = 10 ** 28

def interval(a,b=None):
    if b is None: b=a
    return (F(a),F(b))

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y]
    return (min(v),max(v))
def scale(x,t): return mul(x,interval(t))
def div(x,t):
    assert t[0]>0 or t[1]<0
    return mul(x,(1/t[1],1/t[0]))
def root(q):
    q=F(q)
    assert q>=0
    lo=isqrt(q.numerator*PREC*PREC//q.denominator)
    return (F(lo,PREC),F(lo+1,PREC))

def arctan_bounds(q,n=26):
    """Alternating Taylor bounds for 0 < q < 1."""
    q=F(q); assert 0<q<1
    s=sum(((-1)**j*q**(2*j+1)/F(2*j+1)) for j in range(n))
    rem=q**(2*n+1)/F(2*n+1)
    return (s, s+rem) if n%2==0 else (s-rem,s)

PI=sub(scale(arctan_bounds(F(1,5), 28),16),scale(arctan_bounds(F(1,239), 8),4))
RT3=root(3)
HALF=interval(F(1,2))

def asin_bounds(x,n=10):
    """Nonnegative Taylor coefficients and explicit positive tail bound."""
    assert 0<=x[0]<=x[1]<1
    def part(t):
        return sum(F(comb(2*j,j), 4**j*(2*j+1))*t**(2*j+1) for j in range(n))
    tail=x[1]**(2*n+1)/(1-x[1]*x[1])
    return (part(x[0]),part(x[1])+tail)

# Coordinates in the exact form (u*sqrt(3)/24,v/8).
SITES=[(0,0),(4,0),(-2,2),(-2,-2),(1,1),(-2,0),(1,-1)]
NAMES=['O','V0','V1','V2','M0','M1','M2']
QCHOICES=(4,12,16,36,48)
TH={q:root(F(q,768)) for q in QCHOICES}  # cos(half intersection angle)
AS={q:asin_bounds(TH[q]) for q in QCHOICES}

# (cos alpha,sin alpha) for the 12 exact 30-degree directions.
C60=HALF; S60=div(RT3,interval(2))
DIRECTIONS=[(interval(1),interval(0)), (S60,C60),(C60,S60),
 (interval(0),interval(1)),(neg(C60),S60),(neg(S60),C60),
 (interval(-1),interval(0)),(neg(S60),neg(C60)),(neg(C60),neg(S60)),
 (interval(0),interval(-1)),(C60,neg(S60)),(S60,neg(C60))]

def heading(du,dv):
    if dv==0:return 0 if du>0 else 6
    if du==0:return 3 if dv>0 else 9
    if du==3*dv:return 1 if du>0 else 7
    if du==dv:return 2 if du>0 else 8
    if du==-dv:return 4 if dv>0 else 10
    if du==-3*dv:return 5 if dv>0 else 11
    raise AssertionError(('non-special direction',du,dv))

def site_xy(j):
    u,v=SITES[j]
    return scale(RT3,F(u,24)),interval(F(v,8))

def theta_bounds(j,k,pm):
    u,v=SITES[j];U,V=SITES[k]
    du,dv=U-u,V-v
    z=heading(du,dv)
    q=du*du+3*dv*dv
    assert q in QCHOICES
    beta=sub(scale(PI,F(1,2)),AS[q])
    t=add(scale(PI,F(z,6)),scale(beta,pm))
    TWO_PI=scale(PI,2)
    # The interval is narrower than 10^(-20); adjust by full turns.
    while t[1]<0:t=add(t,TWO_PI)
    while t[0]>TWO_PI[1]:t=sub(t,TWO_PI)
    assert t[0]>=0 and t[1]<=TWO_PI[1]
    co,si=DIRECTIONS[z]
    tail=root(1-F(q,768))
    sine=add(mul(si,TH[q]),scale(mul(co,tail),pm))
    cosine=sub(mul(co,TH[q]),scale(mul(si,tail),pm))
    x,y=site_xy(j)
    primitive=add(t,sub(mul(x,sine),mul(y,cosine)))
    return t,primitive,z,q

def sign_at_zero(j):
    u,v=SITES[j]
    covered=0
    for k,(U,V) in enumerate(SITES):
        if k==j:continue
        du,dv=u-U,v-V
        q=du*du+3*dv*dv
        excess=add(scale(RT3,16*du),interval(q))
        if excess[1]<0:covered+=1
        else:assert excess[0]>0
    return (-1)**covered

def green_interval(j):
    ev=[]
    for k in range(7):
        if k==j:continue
        for pm in (-1,1):
            theta,primitive,z,q=theta_bounds(j,k,pm)
            ev.append((theta,primitive,k,pm,z,q))
    ev.sort(key=lambda e: (e[0][0]+e[0][1])/2)
    for e,f in zip(ev,ev[1:]): assert e[0][1]<f[0][0],('ambiguous crossings',j)
    sig=sign_at_zero(j)
    # I = 2*pi*sig - sum delta-sign times F(event), F=theta+x*sin(theta)-y*cos(theta).
    integral=scale(PI,2*sig)
    for theta,primitive,k,pm,z,q in ev:
        delta=-2*sig
        integral=sub(integral,scale(primitive,delta))
        sig=-sig
    assert sig==sign_at_zero(j)
    return integral,[(NAMES[e[2]],e[3]) for e in ev]

def output_bounds(a): return (str(float(a[0])),str(float(a[1])))

I0,ORDER0=green_interval(0)
I1,ORDER1=green_interval(1)
I4,ORDER4=green_interval(4)
area=scale(add(I0,add(scale(I1,3),scale(I4,3))),F(1,2))

# A fully simplified exact expression for area - pi.
R=add(add(add(scale(root(15),F(-3,4)),scale(root(183),F(-3,16))),
          add(scale(root(3),F(-1,16)),scale(root(191),F(1,16)))),
      add(scale(root(47),F(1,4)),scale(root(7),F(9,8))))
U=add(add(scale(AS[4],12),scale(AS[12],24)),
      add(add(scale(AS[16],12),scale(AS[36],-12)),scale(AS[48],-12)))
closed_delta=add(R,U)
delta=sub(area,PI)
assert max(delta[0],closed_delta[0])<=min(delta[1],closed_delta[1])
assert F(-33502,1000000)<delta[0]<delta[1]<F(-33500,1000000)
assert F(310809,100000)<area[0]<area[1]<F(310810,100000)
print('Rational proof certificate: PASS')
print('Three complete crossing orders:')
for name,order in [('O',ORDER0),('V0',ORDER1),('M0',ORDER4)]:
 print(name, ' '.join(k+('+' if pm==1 else '-') for k,pm in order))
print('GREEN odd-area enclosure:',output_bounds(area))
print('CLOSED area-minus-pi enclosure:',output_bounds(closed_delta))
print('STRICT inequality area < pi: PASS')

# Independent check using radial exits, not boundary arc integration.
# Every disk contains the origin, so sorting exit radii gives odd intervals.
from math import fsum
coords=[(u*sqrt(3)/24, v/8) for u,v in SITES]
for N in (8192,65536):
 accum=0.0
 for h in range(N):
    angle=2*pi*(h+.5)/N
    ux,uy=cos(angle),sin(angle)
    exits=[]
    for x,y in coords:
      proj=x*ux+y*uy
      exits.append(proj+sqrt(1-x*x-y*y+proj*proj))
    exits.sort()
    accum+=sum((1 if k%2==0 else -1)*r*r for k,r in enumerate(exits))
 radial=pi*accum/N
 print('Independent midpoint polar quadrature',N,':',format(radial,'.13f'))
 assert abs(radial-(float(area[0])+float(area[1]))/2) < (0.000005 if N==8192 else 0.0000001)

# Exact formal identity check in a rational multiquadratic ring.
# Angle symbols are pi and asin(sqrt(q/768)); surds use squarefree radicands.
def square_reduce(n):
    root=1
    d=2
    while d*d<=n:
        while n%(d*d)==0:
            n//=d*d
            root*=d
        d+=1
    return n,root

def s_poly(n=1,coefficient=F(1)):
    r,t=square_reduce(n)
    return {('s',r):coefficient*t} if coefficient else {}

def p_add(*values):
    result={}
    for d in values:
        for key,value in d.items():result[key]=result.get(key,F(0))+value
    return {key:value for key,value in result.items() if value}

def p_neg(x):return {k:-v for k,v in x.items()}
def p_scale(x,t):return {k:v*t for k,v in x.items() if v*t}
def p_mul_surd(x,y):
    result={}
    for (a,ra),ca in x.items():
        for (b,rb),cb in y.items():
            assert a==b=='s'
            sq,coef=square_reduce(ra*rb)
            key=('s',sq)
            result[key]=result.get(key,F(0))+ca*cb*coef
    return {k:v for k,v in result.items() if v}

def pure_trig(z):
    half=s_poly(1,F(1,2)); rt=s_poly(3,F(1,2)); one=s_poly()
    zero={}
    cs=[one,rt,half,zero,p_neg(half),p_neg(rt),p_neg(one),p_neg(rt),p_neg(half),zero,half,rt]
    sn=[zero,half,rt,one,rt,half,zero,p_neg(half),p_neg(rt),p_neg(one),p_neg(rt),p_neg(half)]
    return cs[z],sn[z]

def symbolic_event(j,k,pm):
    u,v=SITES[j];U,V=SITES[k]
    du,dv=U-u,V-v
    q=du*du+3*dv*dv;z=heading(du,dv)
    angle_range,_,_,_=theta_bounds(j,k,pm)
    shift=0
    base=z*F(1,6)+pm*F(1,2)
    if pm<0 and z<=2: shift=1
    if pm>0 and z>=10:shift=-1
    theta=p_add({('pi',0):base+2*shift},{('asin',q):F(-pm)})
    alpha_cos,alpha_sin=pure_trig(z)
    t=s_poly(3*q,F(1,48))
    st=s_poly(3*(768-q),F(1,48))
    sint=p_add(p_mul_surd(alpha_sin,t),p_scale(p_mul_surd(alpha_cos,st),pm))
    cost=p_add(p_mul_surd(alpha_cos,t),p_scale(p_mul_surd(alpha_sin,st),-pm))
    cx=s_poly(3,F(u,24));cy=s_poly(1,F(v,8))
    return p_add(theta,p_mul_surd(cx,sint),p_neg(p_mul_surd(cy,cost)))

def symbolic_integral(j):
    es=[]
    for k in range(7):
        if k!=j:
            for pm in (-1,1):
                ti,_,_,_=theta_bounds(j,k,pm)
                es.append((ti,k,pm))
    es.sort(key=lambda e:e[0][0])
    result={('pi',0):F(2*sign_at_zero(j))}
    sg=sign_at_zero(j)
    for ti,k,pm in es:
        result=p_add(result,p_scale(symbolic_event(j,k,pm),2*sg))
        sg=-sg
    return result

exact_area=p_scale(p_add(symbolic_integral(0),p_scale(symbolic_integral(1),3),p_scale(symbolic_integral(4),3)),F(1,2))
expected={('pi',0):F(1), ('asin',4):F(12),('asin',12):F(24),('asin',16):F(12),
          ('asin',36):F(-12),('asin',48):F(-12),
          ('s',15):F(-3,4),('s',183):F(-3,16),('s',3):F(-1,16),
          ('s',191):F(1,16),('s',47):F(1,4),('s',7):F(9,8)}
assert exact_area==expected,('exact closed-form identity mismatch',exact_area,expected)
print('Exact symbolic identity in pi, arcsines and radicals: PASS')
