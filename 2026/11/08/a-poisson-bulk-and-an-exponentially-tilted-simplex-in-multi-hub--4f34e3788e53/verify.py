"""Finite independent checks for a degree-weighted zero-range stationary law.

Usage: python verify.py.  Requires Python 3 standard library only.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, factorial


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for tail in compositions(total-i, parts-1):
                yield (i,)+tail


def degrees_and_edges(n, h):
    r=len(h)
    degrees = [n+x for x in h]+[r]*n+[1]*sum(h)
    edges = set()
    for i in range(r):
        for j in range(n):
            edges.add(tuple(sorted((i,r+j))))
    a=r+n
    for i,num in enumerate(h):
        for j in range(num):
            edges.add(tuple(sorted((i,a))))
            a+=1
    assert len(degrees) == a
    assert all(sum(i in edge for edge in edges)==degrees[i] for i in range(len(degrees)))
    return degrees, sorted(edges)


def exact_weight(degrees, v):
    p=1
    for d, m in zip(degrees,v):
        p*=d**m
    return p


def compressed_masses(n, h, M):
    r=len(h)
    H=sum(h)
    degrees,edges=degrees_and_edges(n,h)
    counts={}
    for s in range(M+1):
        for ell in range(M-s+1):
            # all compositions among n bulk sites, h leaf sites
            if H==0 and ell>0: continue
            bw=comb(n+s-1,s)*r**s
            lw=(comb(H+ell-1,ell) if H else 1)
            for u in compositions(M-s-ell,r):
                mass=bw*lw
                for v,hi in zip(u,h): mass*=(n+hi)**v
                counts[(s,ell,u)]=mass
    return counts


def direct_masses(n,h,M):
    r=len(h)
    deg,_=degrees_and_edges(n,h)
    ans={}
    for x in compositions(M,len(deg)):
        u=x[:r]
        s=sum(x[r:r+n]); ell=sum(x[r+n:])
        key=(s,ell,u)
        ans[key]=ans.get(key,0)+exact_weight(deg,x)
    return ans


def detailed_balance_checks(n,h,M):
    deg,edges=degrees_and_edges(n,h)
    ct=0
    for x in compositions(M,len(deg)):
        for a,b in edges:
            if x[a]>0:
                y=list(x); y[a]-=1; y[b]+=1
                assert Fraction(exact_weight(deg,x),deg[a]) == Fraction(exact_weight(deg,y),deg[b])
                ct+=1
            if x[b]>0:
                y=list(x); y[b]-=1; y[a]+=1
                assert Fraction(exact_weight(deg,x),deg[b]) == Fraction(exact_weight(deg,y),deg[a])
                ct+=1
    return ct


def exact_s_distribution(n,h,M):
    assert h==(1,0)
    # Separate the n degree-2 peripheral sites, one degree-1 leaf,
    # and the two high-degree vertices, with weights n+1 and n.
    A=[1];E=[0]
    for t in range(1,M+1):
        A.append(n*A[-1]+(n+1)**t)
        E.append(n*E[-1]+t*(n+1)**t)
    PA=[];PE=[]
    for t in range(M+1):
        PA.append(A[t]+(PA[-1] if PA else 0))
        PE.append(E[t]+(PE[-1] if PE else 0))
    numer=[comb(n+s-1,s)*2**s*PA[M-s] for s in range(M+1)]
    Z=sum(numer)
    probs={s:Fraction(v,Z) for s,v in enumerate(numer)}
    hub1=sum(comb(n+s-1,s)*2**s*PE[M-s] for s in range(M+1))
    return probs,Fraction(hub1,Z*M)

def exact_three_hub(n,M):
    # K_{3,n} with a single pendant at hub 0. Two other hubs have degree n.
    A=[1]; E=[0]; T=[1]; Q=[0]
    for t in range(1,M+1):
        A.append(n*A[-1]+(n+1)**t)
        E.append(n*E[-1]+t*(n+1)**t)
        T.append(n*T[-1]+A[t])
        Q.append(n*Q[-1]+E[t])
    PT=[];PQ=[]
    for t in range(M+1):
        PT.append(T[t]+(PT[-1] if PT else 0))
        PQ.append(Q[t]+(PQ[-1] if PQ else 0))
    masses=[comb(n+s-1,s)*3**s*PT[M-s] for s in range(M+1)]
    Z=sum(masses)
    mean1=sum(comb(n+s-1,s)*3**s*PQ[M-s] for s in range(M+1))
    return {s:Fraction(v,Z) for s,v in enumerate(masses)}, Fraction(mean1,M*Z)


def check():
    total=0
    for n,h,M in [(2,(0,0),3),(2,(1,0),3),(3,(0,1),3),(2,(1,1),3),
                  (2,(1,0,0),2),(3,(0,0,0),3),(2,(2,0),3),(4,(1,0),3)]:
        direct=direct_masses(n,h,M)
        reduced=compressed_masses(n,h,M)
        assert direct == reduced,(n,h,M)
        total+=len(reduced)
        total+=detailed_balance_checks(n,h,M)
    for n in [20,40,80,160,320]:
        h=(1,0);M=n
        probs,mean1=exact_s_distribution(n,h,M)
        mean_bulk=sum(s*float(p) for s,p in probs.items())
        limit_mean=exp(1)/(exp(1)-1)-1
        assert abs(mean_bulk-2)<16/n,(n,mean_bulk)
        assert abs(float(mean1)-limit_mean)<8/n,(n,mean1)
        p0=float(probs.get(0,0))
        assert abs(p0-exp(-2))<5/n,(n,p0)
        total+=3
    for n in (20,40,80,160,320):
        probs,mean=exact_three_hub(n,n)
        target=(3-exp(1))/(exp(1)-2)
        assert abs(sum(s*float(p) for s,p in probs.items())-3)<20/n
        assert abs(float(mean)-target)<8/n
        assert abs(float(probs[0])-exp(-3))<5/n
        total+=3
    print('PASS',total,'finite exact identities, detailed-balance comparisons and asymptotic bound checks')


if __name__=='__main__':check()
