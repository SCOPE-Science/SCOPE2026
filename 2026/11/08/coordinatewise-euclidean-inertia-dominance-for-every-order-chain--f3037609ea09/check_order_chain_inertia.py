"""Exact rational tests of order/chain-polytope inertia and conditional covariance."""
from fractions import Fraction
from itertools import combinations
import random

def extensions(predecessors):
    n=len(predecessors);out=[]
    def visit(prefix,chosen):
        if len(prefix)==n:
            out.append(tuple(prefix));return
        for v in range(n):
            if not(chosen>>v&1) and not(predecessors[v]&~chosen):
                visit(prefix+(v,), chosen|(1<<v))
    visit((),0)
    return out

def height(predecessors):
    h=[1]*len(predecessors)
    for v in range(len(predecessors)):
        h[v]=1+max([h[u] for u in range(v) if predecessors[v]>>u&1]+[0])
    return max(h,default=0)

def evaluate(predecessors):
    n=len(predecessors);N=n+1
    exts=extensions(predecessors);m=len(exts)
    ex=[0]*n;ey=[0]*n;ex2=[0]*n;ey2=[0]*n
    EL=[0]*n;EU=[0]*n;ELU=[0]*n
    for sigma in exts:
        rank={v:j+1 for j,v in enumerate(sigma)}
        for v in range(n):
            r=rank[v]
            lower=max((rank[u] for u in range(n) if predecessors[v]>>u &1),default=0)
            upper=min((rank[u] for u in range(n) if predecessors[u]>>v &1),default=N)
            d=r-lower
            ex[v]+=r; ey[v]+=d
            ex2[v]+=r*(r+1);ey2[v]+=d*(d+1)
            EL[v]+=lower;EU[v]+=upper; ELU[v]+=lower*(upper+1)
    diff=Fraction(0);total_cov=Fraction(0)
    for v in range(n):
        vx=Fraction(ex2[v],m*N*(N+1))-Fraction(ex[v],m*N)**2
        vy=Fraction(ey2[v],m*N*(N+1))-Fraction(ey[v],m*N)**2
        cov=Fraction(ELU[v],m*N*(N+1))-Fraction(EL[v]*EU[v],m*m*N*N)
        assert vx-vy==cov, ('identity failed', predecessors,v,vx,vy,cov)
        assert cov>=0,('negative',predecessors,v,cov)
        if (predecessors[v]!=0 and any(predecessors[u]>>v &1 for u in range(n))):
            assert cov>0,('non-strict internal',predecessors,v)
        else: assert cov==0,('nonzero boundary',predecessors,v)
        diff+=vx-vy;total_cov+=cov
    assert diff==total_cov and (diff>0)==(height(predecessors)>=3)
    return diff

def posets(n):
    edges=list(combinations(range(n),2));seen=set()
    for m in range(1<<len(edges)):
        p=[0]*n
        for j,(u,v) in enumerate(edges):
            if m>>j&1:p[v]|=1<<u
        for v in range(n):
            for u in range(v):
                if p[v]>>u&1:p[v]|=p[u]
        key=tuple(p)
        if key in seen:continue
        seen.add(key)
        yield key

def main():
    num=positive=zero=0
    for n in range(2,7):
        nn=np=nz=0
        for p in posets(n):
            gap=evaluate(p);nn+=1;np+=gap>0;nz+=gap==0
        num+=nn;positive+=np;zero+=nz
        print('n=%d, natural posets=%d, strict=%d, equal=%d'%(n,nn,np,nz))
    rng=random.Random(214703)
    tested=0
    for _ in range(250):
        n=7;p=[0]*n
        for u,v in combinations(range(n),2):
            if rng.randrange(3)==0:p[v]|=1<<u
        for v in range(n):
            for u in range(v):
                if p[v]>>u&1:p[v]|=p[u]
        evaluate(tuple(p));tested+=1
    assert evaluate((0,1,3))==Fraction(1,80)
    print('ORDER_CHAIN_INERTIA_FKG_CHECKS_PASSED',num,positive,zero,tested)
if __name__=='__main__':main()
