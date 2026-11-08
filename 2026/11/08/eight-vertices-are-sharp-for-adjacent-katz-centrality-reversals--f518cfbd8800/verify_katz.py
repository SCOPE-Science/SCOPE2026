"""Exact matching-polynomial/Bernstein enumeration for finite simple trees."""
from itertools import combinations
from fractions import Fraction
from math import comb
import networkx as nx

def exact_data(graph):
    n=len(graph); E=list(graph.edges()); b=[(1<<u)|(1<<v) for u,v in E]
    m=[0]*(n//2+1)
    for mask in range(1<<len(E)):
        used=0
        for j, e in enumerate(b):
            if mask>>j&1:
                if used & e:break
                used |= e
        else:m[mask.bit_count()]+=1
    D=[0]*(n+1)
    for k, val in enumerate(m):D[2*k]=(-1)**k*val
    deg=[[] for _ in range(n)]
    for u,v in E: deg[u].append(v);deg[v].append(u)
    W=[];w=[1]*n
    for k in range(n):
        W.append(w)
        w=[sum(w[v] for v in deg[u]) for u in range(n)]
    nums=[[sum(D[j]*W[k-j][u] for j in range(k+1)) for k in range(n)] for u in range(n)]
    return D,nums

def choose_R(D,den=1000):
    n=len(D)-1
    # first rational witness det(I-rA)<=0
    for a in range(1,den+1):
        v=sum(d*a**i*den**(n-i) for i,d in enumerate(D))
        if v==0:return a,den,v
        if v<0:
            lo=Fraction(a-1,den);hi=Fraction(a,den)
            for _ in range(32):
                mid=(lo+hi)/2
                val=sum(di*mid**i for i,di in enumerate(D))
                if val==0:return mid.numerator,mid.denominator,0
                if val>0:lo=mid
                else:hi=mid
            return hi.numerator,hi.denominator,-1
    raise AssertionError('no signed determinant bracket')

def certificate(h,a,b):
    if not any(h): return True, []
    while h[-1]==0:h.pop()
    h=h[next(i for i,c in enumerate(h) if c):]
    d=len(h)-1
    q=[sum(h[k]*a**k*b**(d-k)*comb(d-k,j-k) for k in range(j+1)) for j in range(d+1)]
    return all(c>=0 for c in q) or all(c<=0 for c in q), q

def poly_eval(c, x):
    return sum(z*x**k for k,z in enumerate(c))

def score_difference(G,u,v,x):
    D,N=exact_data(G)
    return poly_eval([a-b for a,b in zip(N[u],N[v])],x)/poly_eval(D,x)

def run():
    expected={2:(1,1,0,0),3:(1,2,2,0),4:(2,6,5,0),5:(3,12,12,0),6:(6,30,28,0),7:(11,66,66,0),8:(23,161,157,2)}
    seen=[]
    for n in range(2,9):
        Gs=list(nx.nonisomorphic_trees(n))
        edges=nonzero=0; bad=[]
        for idx,G in enumerate(Gs):
            D,nums=exact_data(G)
            a,b,_=choose_R(D)
            assert poly_eval(D, Fraction(a,b))<=0
            for u,v in G.edges():
                edges+=1
                h=[x-y for x,y in zip(nums[u],nums[v])]
                nonzero+=int(any(h))
                ok,_=certificate(h[:],a,b)
                if not ok:bad.append((idx,u,v))
        observed=(len(Gs),edges,nonzero,len(bad))
        assert observed==expected[n],(n,observed)
        if n==8:seen=bad
        print('n=',n,'trees,edges,nonidentical,exceptions=',observed)
    assert seen==[(4,0,5),(12,0,5)],seen
    for idx,u,v,tlo,thi,vlo,vhi,bound in [
       (4,0,5,Fraction(1,3),Fraction(3,7),Fraction(-17,137),Fraction(1191,7169),25),
       (12,0,5,Fraction(1,4),Fraction(1,3),Fraction(-2,31),Fraction(3,29),32)]:
        G=list(nx.nonisomorphic_trees(8))[idx]
        assert score_difference(G,u,v,tlo)==vlo
        assert score_difference(G,u,v,thi)==vhi
        # Bound rho(A)^4 by the maximum row sum of A^4.
        adj=[list(G.neighbors(i)) for i in range(8)]
        w=[1]*8
        for _ in range(4):w=[sum(w[j] for j in adj[i]) for i in range(8)]
        assert max(w)==bound and bound*thi**4 < 1
        print('witness',idx,'edge',(u,v),'endpoint values',(vlo,vhi),'four-walk-bound',bound)
    print('EXACT_CERTIFICATE_OK')
if __name__=='__main__':run()
