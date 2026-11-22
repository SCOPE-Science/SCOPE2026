"""Exact-rational independent transition-kernel checks for finite edge-environment dynamics."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations

def model_step(P, n, edges, p, q, omega):
    """Independent construction of the entire 2^m-state Markov kernel by vertex updates."""
    m=len(edges); out=defaultdict(F)
    for state,weight in P.items():
        out[state]+=weight*(1-omega)
        for v in range(n):
            affected=[j for j,(a,b) in enumerate(edges) if a==v or b==v]
            partial={state:F(1)}
            for j in affected:
                nxt=defaultdict(F)
                for z,pr in partial.items():
                    old=(z>>j)&1
                    flip=q if old else p
                    nxt[z]+=pr*(1-flip)
                    nxt[z^(1<<j)]+=pr*flip
                partial=nxt
            for z,pr in partial.items(): out[z]+=weight*omega*pr/n
    assert sum(out.values(),F(0))==1
    return out

def moments(P,m):
    mean=sum(pr*state.bit_count() for state,pr in P.items())
    var=sum(pr*(state.bit_count()-mean)**2 for state,pr in P.items())
    return mean,var

def formula(n,edges,p,q,omega,t,initial=0):
    m=len(edges); s=p+q; pi=p/s; z=F(initial)-pi
    a=1-2*omega*s/n
    b0=1-4*omega*s/n
    b1=b0+omega*s*s/n
    wedge=sum(bool(set(e)&set(f)) for e,f in combinations(edges,2))
    mu=pi+a**t*z
    cav=z*z*(b1**t-a**(2*t))
    dis=z*z*(b0**t-a**(2*t))
    var=m*mu*(1-mu)+2*wedge*cav+2*(m*(m-1)//2-wedge)*dis
    return m*mu,var,(a,b0,b1,wedge,cav,dis)

def run(n,edges,p,q,omega,tmax=4,initial=0):
    P={(2**len(edges)-1 if initial else 0):F(1)}
    for t in range(tmax+1):
        act=moments(P,len(edges)); exp=formula(n,edges,p,q,omega,t,initial)
        assert act==exp[:2],(n,edges,t,act,exp)
        if t<tmax:P=model_step(P,n,edges,p,q,omega)
    return exp

if __name__=='__main__':
    # Valid in the source paper's parameter ordering: p0=9/10>p1=4/5>p2=7/10;
    # q0=9/10<q1=19/20<q2=99/100.
    p=q=F(9,10);omega=F(19,20)
    for n in (4,5,6):
        star=[(0,j) for j in range(1,n)]
        path=[(j,j+1) for j in range(n-1)]
        for edges in (star,path):
            for ini in (0,1):
                run(n,edges,p,q,omega,3,ini)
        for t in (1,2,3):
            vs=formula(n,star,p,q,omega,t)[1]
            vp=formula(n,path,p,q,omega,t)[1]
            print('n=',n,'t=',t,'V_star-V_path=',vs-vp,'decimal=',float(vs-vp))
            assert (vs-vp>0) == ((t%2==1) or (n==6)), (n,t)
    # Check a nonextremal five-vertex tree and a cyclic graph, to test the full invariant.
    run(5, [(0,1),(1,2),(1,3),(3,4)], p, q, omega, 3)
    run(4, [(0,1),(1,2),(2,3),(3,0)], p, q, omega, 3)
    # Repeat in nonalternating regime and at varied parameters and graph shapes.
    for n in range(3,7):
        path=[(j,j+1) for j in range(n-1)]
        for pp,qq,ww in [(F(1,4),F(1,3),F(1,2)),(F(3,5),F(1,4),F(4,5)),(F(4,5),F(9,10),F(2,3))]:
            run(n,path,pp,qq,ww,3)
    print('PASS: full finite-state transition law independently matches moments and variance.')
