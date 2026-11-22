"""Exact rational and numerical reproducibility checks for periodic unreliable departure clocks.
Scientific model: independent Bernoulli availability with a guaranteed scheduled departure.
No external dependencies. All computations use Python standard library.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from math import isclose


def hessian(p):
    n=len(p)
    H=[[Q(0) for _ in range(n)] for _ in range(n)]
    for mask in product((0,1),repeat=n):
        prob=Q(1)
        for flag,pr in zip(mask,p):
            prob*=pr if flag else 1-pr
        if prob==0: continue
        selected=[i for i,x in enumerate(mask) if x]
        assert selected  # at least one certain departure
        for at,now in enumerate(selected):
            after=selected[(at+1)%len(selected)]
            idx=[];k=now
            while True:
                idx.append(k)
                k=(k+1)%n
                if k==after or len(idx)==n:break
            for i in idx:
                for j in idx:H[i][j]+=prob
    return H


def evaluate(H,g):
    return sum(g[i]*H[i][j]*g[j] for i in range(len(g)) for j in range(len(g)))/2


def verify(p):
    assert len(p)>0 and all(Q(0)<x<=Q(1) for x in p) and Q(1) in p
    n=len(p);v=[x/(2-x) for x in p]; S=sum(v); w=[x/S for x in v]
    g=[(w[i]+w[(i+1)%n])/2 for i in range(n)]
    H=hessian(p)
    assert sum(g)==1 and all(x>0 for x in g)
    assert H==[list(x) for x in zip(*H)]
    assert all(sum(H[i][j]*g[j] for j in range(n))==1/S for i in range(n))
    assert evaluate(H,g)==Q(1)/(2*S)
    # Positive definiteness stronger than required because the all-success event is nonzero.
    assert all(H[i][i]==1 for i in range(n))
    # Check the exact completed-square identity at every tested simplex point.
    for i in range(n):
        delta=[Q(-1,n) for _ in range(n)];delta[i]+=1
        h=[g[j]+Q(1,25)*delta[j] for j in range(n)]
        assert all(x>=0 for x in h) and sum(h)==1
        quadratic=sum(delta[j]*H[j][k]*delta[k] for j in range(n) for k in range(n))/2
        assert evaluate(H,h)==evaluate(H,g)+Q(1,625)*quadratic
        if n>1:assert quadratic>0
    return S, g, evaluate(H,[Q(1,n)]*n),evaluate(H,g)


def main():
    total=0
    inputs=[
      (Q(1),),
      (Q(1),Q(1)),
      (Q(1),Q(1,2)),
      (Q(1),Q(1),Q(1,2)),
      (Q(1),Q(1),Q(1,2),Q(1,5)),
      (Q(1),Q(1,5),Q(1),Q(1,2)),
      (Q(1),Q(1,3),Q(1,2),Q(3,4),Q(2,5)),
      (Q(1),Q(1),Q(1,2),Q(1,3),Q(3,4),Q(2,5)),
      (Q(1),Q(1),Q(1,2),Q(1,3),Q(3,4),Q(2,5),Q(4,5)),
    ]
    for p in inputs:
      S,g,uniform,opt=verify(p);total+=1
      print('n',len(p),'p',list(map(str,p)),'S',S,'g',list(map(str,g)),'uniform',uniform,'optimal',opt)
    # Arbitrary cyclic reordering preserves the optimum value, but not the gap vector.
    q=(Q(1),Q(1),Q(1,2),Q(1,5))
    vals=set()
    for perm in set(permutations(q)):
      s,g,_,f=verify(perm)
      vals.add(f);total+=1
    assert len(vals)==1
    print('VERIFIED',total,'full exact rational configurations, including all distinct permutations of (1,1,1/2,1/5)')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
