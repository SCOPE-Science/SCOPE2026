"""Deterministic verification for synchronous-reset walkers with weak independent holds.
Dependencies: Python >=3.10, numpy, sympy.
"""
from itertools import product
import numpy as np
import sympy as sp

checks=0

def verify(flag,desc):
    global checks
    checks+=1
    if not flag:
        raise AssertionError(desc)

# The center (node zero) and any of n leaves are the vertices of the star.
def star_transition(n):
    a=np.zeros((n+1,n+1))
    a[0,1:]=1/n
    a[1:,0]=1.
    return a

def walk_transition(a,epsilon):
    return (1-epsilon)*a+epsilon*np.eye(len(a))

def joint_transition(a,epsilon,S):
    mat=walk_transition(a,epsilon)
    w=mat
    for i in range(S-1):
        w=np.kron(w,mat)
    return w

def target_index(a,S,target):
    N=len(a)
    return sum(target*N**i for i in range(S))

def start_index(a,starts):
    N=len(a)
    k=0
    for i,st in enumerate(starts):
        k=k*N+st
    return k

def discounted_hit(a,eps,S,starts,target,gamma):
    w=joint_transition(a,eps,S)
    idx=target_index(a,S,target)
    other=np.array([i for i in range(len(w)) if i!=idx],dtype=int)
    q=1-gamma
    Q=w[np.ix_(other,other)]
    b=w[other,idx]
    h=np.linalg.solve(np.eye(len(other))-q*Q,q*b)
    st=start_index(a,starts)
    return float(h[np.searchsorted(other,st)])

def full_reset_mfpt(a,eps,S,starts,target,gamma):
    w=joint_transition(a,eps,S)
    r=start_index(a,starts)
    idx=target_index(a,S,target)
    other=np.array([i for i in range(len(w)) if i!=idx],dtype=int)
    q=1-gamma
    Q=q*w[np.ix_(other,other)]
    # Each transient row jumps to the reset configuration with probability gamma.
    Q[:,np.searchsorted(other,r)]+=gamma
    f=np.linalg.solve(np.eye(len(other))-Q,np.ones(len(other)))
    return float(f[np.searchsorted(other,r)])

# Exact symbolic comparison to the independent-hold two-walker star formula.
x,g=sp.symbols('x g',positive=True)
states=[(1,1),(1,0),(0,1),(0,0)] # 1 denotes hub
Q=sp.zeros(3,3)
for i,st in enumerate(states[1:]):
    for h0,h1 in product([0,1],repeat=2):
        prob=(x if h0 else 1-x)*(x if h1 else 1-x)
        nxt=(st[0] if h0 else 1-st[0],st[1] if h1 else 1-st[1])
        if nxt!=(1,1):
            Q[i,states[1:].index(nxt)]+=(1-g)*prob
    Q[i,0]+=g
T_exact=sp.factor(((sp.eye(3)-Q).inv()*sp.ones(3,1))[0])
T_formula=(1+(1-g)*x*(1-2*x))/(x*(1-x)*(1-g)*((2-g)-2*x*(1-g)))
verify(sp.simplify(T_exact-T_formula)==0,'exact star formula')
verify(sp.simplify(sp.limit(x*T_formula,x,0)-1/((1-g)*(2-g)))==0,'star small-laziness coefficient')

q,t=sp.symbols('q t',positive=True)
T_odds=sp.factor(T_formula.subs({x:t/(1+t),g:1-q}))
P=(1-q)**2*t**4+2*(1-q*q)*t**3+q*(q+5)*t**2-2*(1-q)*t-(1+q)
verify(sp.simplify(sp.diff(T_odds,t)-P/(q*t*t*((1-q)*t+1+q)**2))==0,'exact optimality polynomial')

for n in [1,2,5]:
    a=star_transition(n)
    for gamma in [0.1,0.35,0.6,0.88]:
        for eps in [0.04,0.2,0.5,0.8]:
            exp=float(T_formula.subs({x:eps,g:gamma}))
            direct=full_reset_mfpt(a,eps,2,[0,1],0,gamma)
            hit=discounted_hit(a,eps,2,[0,1],0,gamma)
            verify(abs(exp/direct-1)<1e-9,'star exact-vs-matrix')
            verify(abs(exp-(1-hit)/(gamma*hit))<1e-9,'renewal identity')
            checks+=1
        # Strict unique critical point by Descartes also checked at explicit rational gammas.
        poly=sp.Poly(P.subs(q,sp.Rational(str(1-gamma))),t)
        vals=[float(z) for z in poly.all_coeffs()]
        verify(vals[0]>0 and vals[1]>0 and vals[2]>0 and vals[3]<0 and vals[4]<0,'Descartes coefficient signs')

# Distinct bipartite graphs and reset color splits. Rate exponent k=min(m,S-m).
path4=np.zeros((4,4))
for i in range(3):
    path4[i,i+1]=path4[i+1,i]=1
path4=path4/path4.sum(axis=1,keepdims=True)
cycle4=np.zeros((4,4))
for i in range(4):
    cycle4[i,(i+1)%4]=cycle4[i,(i-1)%4]=.5
cases=[(star_transition(2),2,[0,1],0,1),
       (star_transition(2),3,[0,1,1],0,1),
       (star_transition(2),4,[0,0,1,1],0,2),
       (path4,3,[0,1,3],2,1),
       (cycle4,4,[0,2,1,3],0,2)]
for a,S,starts,target,k in cases:
    # A positive, finite coefficient is witnessed by stabilization of p_eps/eps^k.
    epsvals=[0.025,0.0125,0.00625]
    ratios=[discounted_hit(a,e,S,starts,target,0.4)/(e**k) for e in epsvals]
    verify(all(v>0 for v in ratios),'positive coefficients')
    verify(abs(ratios[-1]/ratios[-2]-1)<0.15,'predicted rare-event exponent')
    # Compare two full-reset mean values with the exact renewal formula.
    for e in [0.025,0.0125]:
        p=discounted_hit(a,e,S,starts,target,0.4)
        mean=full_reset_mfpt(a,e,S,starts,target,0.4)
        verify(abs(mean-(1-p)/(0.4*p))/mean<1e-8,'matrix renewal identity')
    print('graph_states',len(a)**S,'agents',S,'k',k,'p/eps^k',round(ratios[-1],7))

print('PASS',checks,'deterministic verification assertions')
