"""Exact finite-graph checks of the cubic-graph stochastic-resolvent curvature identity.
Uses only the Python standard library. These checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product,combinations

def inverse(a):
    n=len(a); b=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if b[i][k]); b[k],b[p]=b[p],b[k]
        d=b[k][k]; b[k]=[v/d for v in b[k]]
        for i in range(n):
            if i!=k:
                u=b[i][k];b[i]=[a-u*c for a,c in zip(b[i],b[k])]
    return [v[n:] for v in b]

def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def mul(A,x):return [dot(row,x) for row in A]

def verify(edges,n):
    E={tuple(sorted(e)) for e in edges}
    assert all(sum(i in e for e in E)==3 for i in range(n))
    theta=F(1,100*n)
    B=[[F(i==j)-F((min(i,j),max(i,j)) in E,12) if i!=j else F(1) for j in range(n)] for i in range(n)]
    W=[[F(3,4)*u for u in row] for row in inverse(B)]
    K=[[(1-theta)*W[i][j]+theta/F(n) for j in range(n)] for i in range(n)]
    Q=inverse(K)
    for row in K:
        assert all(v>=F(1,100*n*n) for v in row)
        assert sum(row)==1
    for i in range(n):
      for j in range(n):
        expected=(F(4,3)*F(i==j)-F((min(i,j),max(i,j)) in E,9) if i!=j else F(4,3)) / (1-theta) -theta/(n*(1-theta))
        assert Q[i][j]==expected
    bestcut=-1;bestscore=None;bestbal=None;hits=[]
    for s in product((-1,1),repeat=n):
        c=sum(s[i]!=s[j] for i,j in E); imbalance=abs(sum(s));score=dot(s,mul(Q,s))
        expected=(F(n)+F(4,9)*c-theta*F(imbalance**2,n))/(1-theta)
        assert score==expected
        if c>bestcut:bestcut=c;bestbal=imbalance
        elif c==bestcut:bestbal=min(imbalance,bestbal)
        if bestscore is None or score>bestscore:bestscore=score;hits=[s]
        elif score==bestscore:hits.append(s)
    assert bestscore==(F(n)+F(4,9)*bestcut-theta*F(bestbal**2,n))/(1-theta)
    assert all(sum(s[i]!=s[j] for i,j in E)==bestcut and abs(sum(s))==bestbal for s in hits)
    mu=1/bestscore
    assert round(F(9,4)*((1-theta)/mu-n))==bestcut
    for s in hits:
        y=mul(Q,s)
        assert all(a*b>0 for a,b in zip(s,y))
        assert sum(abs(a) for a in y)==bestscore
        assert dot(y,mul(K,y))==bestscore
    return n,len(E),bestcut,bestbal,mu,len(hits)

def run():
    K4=list(combinations(range(4),2))
    K33=[(i,j) for i in range(3) for j in range(3,6)]
    prism=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    cube=[(i,i^(1<<b)) for i in range(8) for b in range(3) if i<i^(1<<b)]
    for n,E in [(4,K4),(6,K33),(6,prism),(8,cube)]:
        print('CHECK',verify(E,n))
    print('ALL_EXACT_CHECKS_PASSED')
if __name__=='__main__':run()
