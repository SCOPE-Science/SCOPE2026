"""Independent deterministic diagnostics for the paired-departure theorem.

Use: python3 verify.py
Requires Python 3 standard library only. Finite diagnostics do not replace the proof.
"""
from fractions import Fraction as F
from random import Random


def closed_mean(p, q, r, x):
    return (2*p*q*x*x - 2*r*x - p-q+r+2)/(2*(p+q-r))


def first_event_integral(p, q, r, x):
    """Separate forward-first-event recurrence, integrating each arrival phase."""
    h=1-p-q+r
    # V is remaining wait just past the second scheduled opportunity.
    V=((1-x)+(1-p)*x)/(1-h)
    left=x*x/2 + x*(1-q)*V
    right=(1-x)**2/2+(1-x)*((1-p)*x+h*V)
    return left+right


def horizon_survival_integral(p,q,r,x,K):
    """Truncate the no-arrival survival sum after K complete future blocks."""
    h=1-p-q+r
    Vpartial=((1-x)+(1-p)*x)*sum(h**j for j in range(K))
    left=x*x/2+x*(1-q)*Vpartial
    right=(1-x)**2/2+(1-x)*((1-p)*x+h*Vpartial)
    return left+right


def finite_sample(p,q,r,x,N=200000,seed=7):
    """Pathwise squared-headway renewal-reward estimate, separate from forward recursion."""
    rng=Random(seed)
    events=[]
    for n in range(N+10):
        u=rng.random()
        if u<r: a,b=True,True
        elif u<r+p-r: a,b=True,False
        elif u<p+q-r: a,b=False,True
        else: a,b=False,False
        if a: events.append(n)
        if b: events.append(n+x)
    events.sort()
    return sum((events[j+1]-events[j])**2 for j in range(len(events)-1)
               if 5<=events[j]<N+5)/(2*N)


def run():
    checks=0
    for i in range(1,10):
        for j in range(1,10):
            p,q=F(i,10),F(j,10)
            for k in range(max(0,i+j-10),min(i,j)+1):
                r=F(k,10)
                if not (max(0,p+q-1)<=r<=min(p,q)):
                    continue
                opt=min(F(1),r/(2*p*q))
                for v in range(21):
                    x=F(v,20)
                    w=closed_mean(p,q,r,x)
                    alt=first_event_integral(p,q,r,x)
                    assert w==alt,(p,q,r,x,w,alt)
                    assert w>=closed_mean(p,q,r,opt),(p,q,r,x,opt)
                    # Unique exact minimum at grid equality.
                    assert (w==closed_mean(p,q,r,opt))==(x==opt)
                    checks+=3
                # Independent pathwise limit for a sparse subset (stochastic, not certification).
                if i in (3,7) and j in (4,8) and k in (max(0,i+j-10),min(i,j)):
                    x=F(2,5)
                    n=300000
                    w_sim=finite_sample(float(p),float(q),float(r),float(x),N=n,seed=i*100+j*10+k)
                    assert abs(w_sim-float(closed_mean(p,q,r,x)))<0.055,(p,q,r,w_sim)
                    checks+=1
    # Exact rational illustrations and endpoint critical cases.
    p=q=r=F(2,5)
    assert min(F(1),r/(2*p*q))==1
    assert closed_mean(p,q,r,F(1,2))-closed_mean(p,q,r,F(1))==F(1,5)
    checks+=2
    p,q,r=F(3,5),F(2,5),F(1,5)
    assert min(F(1),r/(2*p*q))==F(5,12)
    assert closed_mean(p,q,r,F(5,12))==F(67,96)
    checks+=2
    print(f'PASS: {checks} diagnostics (exact rational checks plus supplementary simulations).')


if __name__=='__main__':run()
