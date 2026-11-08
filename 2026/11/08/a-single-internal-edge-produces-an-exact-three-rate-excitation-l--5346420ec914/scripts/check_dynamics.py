"""Independent direct dynamics and counting for an internal-edge-augmented biclique.

Usage: python check_dynamics.py
No third-party dependencies.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

def counts(p,q):
    r=p-2
    t=lambda n:3**n-3*2**n+3
    z=3*(3**p+3**q)-9-6*3**r+3*(2**p-2)*(2**q-2)
    h=6*3**r*(3**q-2**q)+t(p)*t(q)-6*(3**r-2**r)*t(q)
    return Counter({Fraction(0):z,Fraction(3,4):3**(p+q)-z-h,Fraction(1):h})

def orbit_rate(p,q,initial,which):
    N=p+q
    neighbor=[set(range(p,N)) for _ in range(p)]+[set(range(p)) for _ in range(q)]
    neighbor[0].add(1);neighbor[1].add(0)
    state=initial
    seen={};activities=[]
    while state not in seen:
        seen[state]=len(activities)
        if which=='CCA':
            future=tuple((x+1)%3 if any(state[j]==(x+1)%3 for j in neighbor[i]) else x
                         for i,x in enumerate(state))
            active=sum(x!=y for x,y in zip(state,future))
        else:
            future=tuple((x+1)%3 if x or any(state[j]==1 for j in neighbor[i]) else 0
                         for i,x in enumerate(state))
            active=sum(x==0 and future[i]==1 for i,x in enumerate(state))
        activities.append(active);state=future
        assert len(activities)<=100
    mu=seen[state];period=len(activities)-mu
    return Fraction(sum(activities[mu:]),N*period)

def main():
    total=0
    for p,q in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4)]:
        cc=Counter();gh=Counter()
        for s in product(range(3),repeat=p+q):
            a=orbit_rate(p,q,s,'CCA');b=orbit_rate(p,q,s,'GHM')
            assert a==3*b,(p,q,s,a,b)
            cc[a]+=1;gh[b]+=1;total+=1
        assert cc==+counts(p,q),(p,q,cc,counts(p,q))
        assert sum(cc.values())==3**(p+q)
        print('p=%d q=%d: N_0=%d N_3/4=%d N_1=%d, checked=%d' %
              (p,q,cc[Fraction(0)],cc[Fraction(3,4)],cc[Fraction(1)],sum(cc.values())))
    print('Direct CCA and GHM trajectories checked for',total,'initial configurations; all passed.')

if __name__=='__main__':main()
