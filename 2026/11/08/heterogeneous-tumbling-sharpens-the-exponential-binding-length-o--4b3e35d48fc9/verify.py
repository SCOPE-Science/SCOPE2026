"""Reproduce exact algebra and stationary checks for a two-swimmer attractive fluid model.

Requires sympy and numpy (and no network). Use: python3 verify.py.
"""
import math
import random

import numpy as np
import sympy as sp

G1,G2,g,v,z=sp.symbols('G1 G2 g v z',positive=True)
states=((1,1),(1,-1),(-1,1),(-1,-1))
Q=sp.zeros(4)
for i,(a,b) in enumerate(states):
    for j,(c,d) in enumerate(states):
        if (c,d)==(-a,b): Q[i,j]=G1
        if (c,d)==(a,-b): Q[i,j]=G2
    Q[i,i]=-G1-G2
W=sp.diag(*[-2*g+v*(b-a) for a,b in states])
s=G1+G2
p=G1*G2
P=(4*g*g*(v*v-g*g)*z**3
   +4*g*s*(v*v-2*g*g)*z**2
   +(s*s*(v*v-4*g*g)-4*g*g*p)*z
   -4*g*s*p)
assert sp.expand((Q.T+z*W).det()+4*z*P)==0
h_rate=sp.symbols('h_rate',positive=True)
assert sp.expand(P.subs({G1:h_rate,G2:h_rate})-4*(h_rate+g*z)**2*((v*v-g*g)*z-2*g*h_rate)) == 0
checks=0

def calc(vv,gg,rate1,rate2):
    global checks
    S=rate1+rate2
    product=rate1*rate2
    def poly(t):
        return (4*gg**2*(vv**2-gg**2)*t**3
                +4*gg*S*(vv**2-2*gg**2)*t**2
                +(S*S*(vv**2-4*gg**2)-4*gg*gg*product)*t
                -4*gg*S*product)
    hi=max(1.0,2*S*gg/(vv*vv-gg*gg))
    assert poly(0)<0
    assert poly(hi)>0
    lo=0.0
    for _ in range(130):
        m=(lo+hi)/2
        if poly(m)>0:hi=m
        else:lo=m
    lam=(lo+hi)/2
    assert abs(poly(lam))<1.e-7*max(1., abs(4*gg*S*product))
    q=np.array(Q.subs({G1:rate1,G2:rate2}),dtype=float)
    speeds=np.array([float(W[i,i].subs({g:gg,v:vv})) for i in range(4)])
    eigenvalues,eigenvectors=np.linalg.eigh(q.T+lam*np.diag(speeds))
    assert abs(eigenvalues[-1])<1e-9
    h=eigenvectors[:,-1]
    if h.sum()<0: h=-h
    assert np.min(h)>1e-12
    assert np.linalg.norm(q.T@h+lam*speeds*h,np.inf)<1e-9
    U=np.where(speeds<0)[0]
    out=np.where(speeds>0)[0]
    assert len(U)==3 and len(out)==1
    mb=np.zeros(4)
    mb[U]=np.linalg.solve(-q[np.ix_(U,U)].T,-speeds[U]*h[U])
    assert np.min(mb[U])>0
    assert max(abs(q.T@mb-speeds*h))<1e-7
    norm=(h.sum()/lam)+mb.sum()
    c=1.0/norm
    assert abs(c*(mb.sum()+h.sum()/lam)-1)<1e-10
    assert np.linalg.norm(c*(mb+h/lam)-np.ones(4)/4,np.inf)<1e-9
    bound=S*gg/(vv*vv-gg*gg)
    assert lam<=bound+1e-9
    if abs(rate1-rate2)>1e-9:assert lam<bound-1e-10
    checks+=1
    return lam, c*mb.sum(), c*h.sum()/lam**2

for vv in (1.05,1.3,1.7,1.99,2.0,2.01,3.0,7.0):
    for gg in (1.0,):
        vals=[]
        for rate1 in (0.02,0.1,0.25,0.5,0.8,1.0):
            lam, atom, EY=calc(vv,gg,rate1,2.0-rate1)
            vals.append(lam)
            assert 0<atom<1 and EY>0
        assert all(x<y for x,y in zip(vals,vals[1:]))

# The rare-flipper boundary: exact lower envelope and its critical scales.
for vv in (1.25,1.75,2.0,3.0):
    small=1.e-7
    lam,_,_=calc(vv,1.0,small,2.0-small)
    if vv<2.0:
        lower=2.0*(2.0-vv)/(2.0*(vv-1.0))
        assert abs(lam-lower)<3e-6
    elif vv==2.0:
        assert abs(lam/math.sqrt(small*(2.0-small)/2.0)-1)<1e-3
    else:
        approx=4.0*small*(2-small)/(2.0*(vv**2-4.0))
        assert abs(lam/approx-1)<1e-3

# Independent event-time integration for the workload process. No time discretization.
def simulate(vv,gg,r1,r2,n=950000,burn=100000):
    rand=random.Random(15314)
    y=0.0
    state=[1,1]
    area=idle=total=0.0
    for i in range(n):
        dt=rand.expovariate(r1+r2)
        speed=vv*(state[1]-state[0])-2*gg
        if speed>=0:
            integ=y*dt+0.5*speed*dt*dt
            ny=y+speed*dt
            zero=0.0
        else:
            hit=y/(-speed)
            if hit>=dt:
                integ=y*dt+0.5*speed*dt*dt
                ny=y+speed*dt
                zero=0.0
            else:
                integ=y*hit/2
                ny=0.0
                zero=dt-hit
        if i>=burn:
            total+=dt;area+=integ;idle+=zero
        y=max(0.,ny)
        if rand.random()<r1/(r1+r2):state[0]*=-1
        else:state[1]*=-1
    return area/total,idle/total
for pars in [(3.,1.,.5,1.5),(1.5,1.,.5,1.5),(2.5,1.,1.,1.)]:
    lam,atom,mean=calc(*pars)
    observed_mean,observed_atom=simulate(*pars)
    print('case',pars,'lambda',lam,'predicted_mean',mean,'observed_mean',observed_mean,
        'predicted_atom',atom,'observed_atom',observed_atom)
    assert abs(observed_mean/mean-1)<0.10
    assert abs(observed_atom-atom)<0.035
print('PASS: symbolic determinant, symmetric factorization,',checks,
      'root/monotonicity/stationarity parameter cases, and three independent event-driven simulations.')
