#!/usr/bin/env python3
"""Standalone arithmetic and finite Fourier-generator checks for two-dimensional angular-tumble transport."""
from fractions import Fraction as Q

N=0

def check(cond, label):
    global N
    N+=1
    if not cond: raise AssertionError(label)

def cheby(n,x):
    if n==0:return Q(1)
    if n==1:return x
    u,v=Q(1),x
    for k in range(2,n+1):u,v=v,2*x*v-u
    return v

def endpoints(m):
    q=(Q(3)+m)/4
    yl=(5*m+3)/(4*(m+1))
    # lower third moment support {-1, yl}
    pl=(yl-m)/(yl+1)
    # upper third moment support {-3/4, +1}
    yu=Q(-3,4)
    pu=(m-yu)/(1-yu)
    return ([(Q(-1),pl),(yl,1-pl)],[(yu,1-pu),(Q(1),pu)])

def harmonics(law,n):
    return sum((p*cheby(n,x) for x,p in law), Q(0))

def rates(law):
    a=1-harmonics(law,1)
    b=1-harmonics(law,2)
    c=1-harmonics(law,3)
    k2=Q(1)/a
    k4=3*(a-2*b)/(a**3*b)
    k6=Q(45,2)*(a**3-a*a*c-6*a*b*c+8*b*b*c)/(a**5*b*b*c)
    return a,b,c,k2,k4,k6

def char_poly(x,p,a,b,c):
    # Exact 4-mode characteristic equation of the cosine Fourier hierarchy.
    return x*((x+a)*((x+b)*(x+c)-p/4)-p*(x+c)/4)-p*((x+b)*(x+c)-p/4)/2

def eigenroot(p,a,b,c):
    # Direct positive eigenvalue root, independently of formal series.
    a,b,c,p=map(float,(a,b,c,p))
    lo,hi=0.0, 2*p/min(a,b,c)+2*p**0.5+1
    for _ in range(110):
        mid=(lo+hi)/2
        if char_poly(mid,p,a,b,c)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

# 1. Direct exact moment reconstruction and cancellation bounds.
for m in [Q(-3,4),Q(-11,15),Q(-5,7),Q(-7,10),Q(-1,2),Q(0),Q(1,2),Q(9,10)]:
    q=(3+m)/4
    lo,hi=endpoints(m)
    for name,law in [('lower',lo),('upper',hi)]:
        check(sum(p for x,p in law)==1,(m,name,'total mass'))
        check(all(0<=p<=1 and -1<=x<=1 for x,p in law),(m,name,'physical support'))
        check(harmonics(law,1)==m,(m,name,'first harmonic'))
        check(sum(p*x*x for x,p in law)==q,(m,name,'second moment'))
        check(harmonics(law,2)==(1+m)/2,(m,name,'fourth cancellation'))
        a,b,c,k2,k4,k6=rates(law)
        check(k4==0,(m,name,'quartic rate'))
        check(k2>0 and a>0 and b>0 and c>0,(m,name,'positive rates'))
        check((k6>0)==(harmonics(law,3)>(1+m)/2) or k6==0,
              (m,name,'sextic sign'))
    wlo=harmonics(lo,3); whi=harmonics(hi,3)
    check(wlo==(9*m*m+2*m-3)/(4*(1+m)),(m,'lower bound'))
    check(whi==(m+3)/4,(m,'upper bound'))
    check(wlo<=whi,(m,'bound order'))
    check((wlo<(1+m)/2)==(m>Q(-5,7)),(m,'threshold ordering'))
    check(whi>(1+m)/2,(m,'strict upper sign'))
    if m>Q(-5,7):
        weight=((1+m)/2-wlo)/(whi-wlo)
        combo=[(x,p*(1-weight)) for x,p in lo]+[(x,p*weight) for x,p in hi]
        check(0<weight<1,(m,'interior mixture'))
        check(rates(combo)[4]==0 and rates(combo)[5]==0,(m,'both exact cancellations'))

# 2. Unique threshold distribution: 3/7 at pi, 2/7 each at +/- 2pi/3.
law=[(Q(-1),Q(3,7)),(Q(-1,2),Q(4,7))]
check(harmonics(law,1)==Q(-5,7),'threshold first harmonic')
check(harmonics(law,2)==Q(1,7),'threshold second harmonic')
check(harmonics(law,3)==Q(1,7),'threshold third harmonic')
check(rates(law)[4]==0 and rates(law)[5]==0,'threshold cumulants')

# 3. Independent four-mode determinant vs sixth-order Taylor prediction.
for a,b,c in [(Q(1),Q(1),Q(1)),(Q(1),Q(1,2),Q(3,4)),
              (Q(3,2),Q(1,3),Q(5,4)),(Q(8,7),Q(4,7),Q(6,7))]:
    L2=Q(1,2)/a
    L4=(a-2*b)/(8*a**3*b)
    L6=(a**3-a*a*c-6*a*b*c+8*b*b*c)/(32*a**5*b*b*c)
    # Formal-series coefficients of characteristic polynomial are exactly zero through p^3.
    # Use exact polynomial arithmetic in p for x=L2p+L4p²+L6p³.
    def mul(x,y):
        z=[Q(0)]*4
        for i,s in enumerate(x):
            for j,t in enumerate(y):
                if i+j<=3:z[i+j]+=s*t
        return z
    def add(*xs):return [sum(x[i] for x in xs) for i in range(4)]
    def scale(x,c):return [c*v for v in x]
    x=[Q(0),L2,L4,L6]; ap=[a,L2,L4,L6]; bp=[b,L2,L4,L6];cp=[c,L2,L4,L6]
    p=[Q(0),Q(1),Q(0),Q(0)];p2=[Q(0),Q(0),Q(1),Q(0)]
    # Reconstruct directly: x*((x+a)*((x+b)*(x+c)-p/4)-p*(x+c)/4)-p*((x+b)*(x+c)-p/4)/2
    inner=add(mul(bp,cp),scale(p,Q(-1,4)))
    det=add(mul(x,add(mul(ap,inner),scale(mul(p,cp),Q(-1,4)))),
            scale(mul(p,inner),Q(-1,2)))
    check(det==[Q(0)]*4,('series determinant',a,b,c,det))
    for k in [0.05,0.09]:
        p=Q(str(k*k))
        numeric=eigenroot(p,a,b,c)
        series=float(L2*p+L4*p*p+L6*p*p*p)
        # next term is O(p^4), use conservative bound on this parameter family
        check(abs(numeric-series)<100*(float(p)**4),('root expansion',a,b,c,k,numeric,series))

# 4. Exact moment feasibility tests for random rational two-point distributions.
for j in range(1,25):
    m=Q(-3,4)+Q(j,50) # up to m=-.27
    l,u=endpoints(m)
    w=(Q(j,25))
    mix=[(x,p*(1-w)) for x,p in l]+[(x,p*w) for x,p in u]
    m1=harmonics(mix,1); w2=harmonics(mix,2);w3=harmonics(mix,3)
    check(m1==m and w2==(1+m)/2,(j,'mixed moments'))
    check(rates(mix)[4]==0,(j,'mixed fourth cancellation'))
    check(w3==harmonics(l,3)*(1-w)+harmonics(u,3)*w,(j,'mixed third interpolation'))


# 5. An independent finite-time moment ODE (not the spectral determinant):
# d/dt E[X^j exp(in theta)] = -gamma_n E[...] + j v/2 (n-1,n+1) + D j(j-1) lower j.
# For j <= 6, no angle modes beyond |n|<=j are needed.
def transient_cumulants(law,T=180.0,dt=0.08):
    gamma=[float(1-harmonics(law,n)) for n in range(7)]
    y=[[0.0]*7 for j in range(7)]
    y[0][0]=1.0
    steps=round(T/dt);dt=T/steps
    def derivative(Y):
        A=[[0.0]*7 for j in range(7)]
        for j in range(1,7):
            for n in range(j+1):
                A[j][n]=-gamma[n]*Y[j][n]+0.5*j*(Y[j-1][abs(n-1)]+(Y[j-1][n+1] if n+1<=6 else 0.0))
        return A
    def add(Y,A,c):
        return [[Y[j][n]+c*A[j][n] for n in range(7)] for j in range(7)]
    for _ in range(steps):
        k1=derivative(y)
        k2=derivative(add(y,k1,dt/2))
        k3=derivative(add(y,k2,dt/2))
        k4=derivative(add(y,k3,dt))
        y=[[y[j][n]+dt*(k1[j][n]+2*k2[j][n]+2*k3[j][n]+k4[j][n])/6 for n in range(7)] for j in range(7)]
    m2,m4,m6=y[2][0],y[4][0],y[6][0]
    return ((m4-3*m2*m2)/T,(m6-15*m4*m2+30*m2**3)/T)

lower,upper=endpoints(Q(0))
for law,targetsign in [(lower,-1),(upper,1)]:
    k4,k6=transient_cumulants(law)
    check(abs(k4)<0.2,('transient quartic relaxation',k4))
    check(k6*targetsign>90,('transient sextic sign',k6,targetsign))
crit=[(Q(-1),Q(3,7)),(Q(-1,2),Q(4,7))]
k4,k6=transient_cumulants(crit)
check(abs(k4)<.1 and abs(k6)<1,('critical double cancellation transient',k4,k6))
print(f'PASS: {N} exact algebraic, Fourier-generator and transient-ODE checks')
