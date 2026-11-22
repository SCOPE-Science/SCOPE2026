"""Standalone numerical and symbolic diagnostics for the four-reading theorem.

The general theorem is proved analytically in RESULT.md. This script is
supplementary verification, not a substitute for proof.
"""
import math
import random
import sympy as sp

N = 0

def check(cond, msg):
    global N
    if not cond:
        raise AssertionError(msg)
    N += 1

def divided(y, t, i, j, k):
    return ((y[k]-y[j])/(t[k]-t[j]) - (y[j]-y[i])/(t[j]-t[i]))/(t[k]-t[i])

def invshape(t, q):
    r=[math.sqrt(x-q) for x in t]
    return (r[2]+r[3])*(r[1]+r[3])/((r[0]+r[1])*(r[0]+r[2]))

def rmax(t):
    r=[math.sqrt(x-t[0]) for x in t]
    return (r[2]+r[3])*(r[1]+r[3])/(r[1]*r[2])

def recover(t,y):
    e=divided(y,t,0,1,2)
    f=divided(y,t,1,2,3)
    if not(e<0 and f<0):
        return None
    rho=e/f
    if not(1<rho<rmax(t)):
        return None
    # Shape function is strictly increasing on (-inf,t1). Bracket by doubling.
    high=t[0]
    low=t[0]-max(1.0,t[-1]-t[0])
    while invshape(t,low)>rho:
        low=t[0]-2*(t[0]-low)
    for _ in range(110):
        mid=(low+high)/2
        if invshape(t,mid)>rho:
            high=mid
        else:
            low=mid
    q=(low+high)/2
    r=[math.sqrt(x-q) for x in t]
    S=-e*(r[0]+r[1])*(r[1]+r[2])*(r[0]+r[2])
    K=(y[1]-y[0])/(t[1]-t[0])-S/(r[0]+r[1])
    B=y[0]-S*r[0]-K*(t[0]-q)
    return (q,S,K,B)

# Exact symbolic identity for second divided difference using z_i=sqrt(t_i-q).
a,b,c=sp.symbols('a b c',positive=True)
# t_i=q+r_i^2
base=lambda x:x
s12=(b-a)/(b*b-a*a)
s23=(c-b)/(c*c-b*b)
sec=sp.factor((s23-s12)/(c*c-a*a))
check(sp.simplify(sec+1/((a+b)*(b+c)*(a+c)))==0,'symbolic secant identity')

# Exact-rational derivative identity in arbitrary positive root variables.
x1,x2,x3,x4=sp.symbols('x1 x2 x3 x4',positive=True)
dlog=sp.Rational(1,2)*(1/(x1*x2)+1/(x1*x3)-1/(x2*x4)-1/(x3*x4))
target=sp.Rational(1,2)*(1/x1-1/x4)*(1/x2+1/x3)
check(sp.simplify(dlog-target)==0,'symbolic logarithmic derivative')

rng=random.Random(481557)
# Mixed nonuniform observation times and interior positive physical parameters.
for rep in range(1200):
    t0=rng.uniform(-1,1)
    increments=[rng.uniform(0.3,2) for _ in range(4)]
    t=[]
    z=t0
    for delta in increments:
        z+=delta
        t.append(z)
    S=10**rng.uniform(-1,1)
    K=10**rng.uniform(-1,1)
    B=rng.uniform(-2,2)
    y=[B+S*math.sqrt(v-t0)+K*(v-t0) for v in t]
    solution=recover(t,y)
    check(solution is not None,f'missing solution at {rep}')
    if solution is None:continue
    Q,SS,KK,BB=solution
    check(abs(Q-t0)<1e-6*max(1,abs(t0)),f'onset at {rep}')
    check(abs(SS-S)<1e-6*max(1,abs(S)),f'sorptivity at {rep}')
    check(abs(KK-K)<1e-6*max(1,abs(K)),f'linear term at {rep}')
    check(abs(BB-B)<1e-5*max(1,abs(B)),f'baseline at {rep}')
    check(all(abs(y[i]-(BB+SS*math.sqrt(t[i]-Q)+KK*(t[i]-Q)))<1e-6*max(1,abs(y[i])) for i in range(4)),f'forward check {rep}')
    check(1<invshape(t,t0)<rmax(t),f'feasible ratio {rep}')
    qlow=t0-1
    qhigh=(t0+t[0])/2
    check(invshape(t,qlow)<invshape(t,t0)<invshape(t,qhigh),f'monotone {rep}')

# Three readings leave a local continuum. Check perturbation keeps S,K>0.
for rep in range(400):
    q=0.1
    t=[1.0,1.9,3.4]
    S=0.2+rng.random()*5
    K=0.3+rng.random()*5
    B=0.3
    y=[B+S*math.sqrt(v-q)+K*(v-q) for v in t]
    e=divided(y,t,0,1,2)
    for shift in (-1e-5,1e-5):
        qnew=q+shift
        r=[math.sqrt(v-qnew) for v in t]
        Snew=-e*(r[0]+r[1])*(r[1]+r[2])*(r[0]+r[2])
        Knew=(y[1]-y[0])/(t[1]-t[0])-Snew/(r[0]+r[1])
        Bnew=y[0]-Snew*r[0]-Knew*(t[0]-qnew)
        check(Snew>0 and Knew>0,'positive local family')
        check(max(abs(y[i]-(Bnew+Snew*r[i]+Knew*(t[i]-qnew))) for i in range(3))<1e-10,'same three observations')

# An observable record that is concave but has shape outside permissible range.
t=[1.,2.,3.,4.]
y=[0.,1.,1.1,1.19]
check(recover(t,y) is None,'infeasible sharp ratio')

print(f'{N} assertions passed')
print('example Rmax:',format(rmax([1.,2.,3.,4.]),'.14f'))
for q,S,K,B in [(0.,2.,1/3,.5)]:
    t=[1.,2.,3.,4.]
    y=[B+S*math.sqrt(z-q)+K*(z-q) for z in t]
    print('example observations:',[round(x,12) for x in y])
    print('example recovered:',recover(t,y))
