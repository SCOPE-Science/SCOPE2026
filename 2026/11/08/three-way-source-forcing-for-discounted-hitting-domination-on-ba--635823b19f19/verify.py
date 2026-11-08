"""Exact rational checks for discounted hitting domination on complete multipartite graphs.
Run with: python verify.py. Uses Python standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def solve(A,b):
    n=len(b)
    R=[list(map(F,A[i]))+[F(b[i])] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if R[i][j]),None)
        assert k is not None
        R[j],R[k]=R[k],R[j]
        pivot=R[j][j]
        R[j]=[v/pivot for v in R[j]]
        for i in range(n):
            if i!=j:
                q=R[i][j]
                if q:
                    R[i]=[R[i][t]-q*R[j][t] for t in range(n+1)]
    return [row[-1] for row in R]


def profile_potentials(parts,counts,lam):
    N=sum(parts)
    s=sum(counts)
    assert s>0 and all(0<=v<=n for n,v in zip(parts,counts))
    outside=[n-v for n,v in zip(parts,counts)]
    aa=[lam*u/F(N-n+lam*u) for n,u in zip(parts,outside)]
    B=sum((v*(1-a) for v,a in zip(counts,aa)),F(0))/(1-sum(aa,F(0)))
    vals=[lam*(B-v)/F(N-n+lam*u) for n,u,v in zip(parts,outside,counts)]
    return [vals[i] if outside[i] else F(1) for i in range(len(parts))]


def direct_potentials(parts,sources,lam):
    labels=[i for i,n in enumerate(parts) for _ in range(n)]
    n=len(labels)
    whites=[v for v in range(n) if v not in sources]
    if not whites: return [F(1)]*n
    idx={v:i for i,v in enumerate(whites)}
    A=[];rhs=[]
    for v in whites:
        neighbors=[w for w in range(n) if labels[w]!=labels[v]]
        d=len(neighbors)
        A.append([F(int(v==x))-(lam/F(d) if x in neighbors else F(0)) for x in whites])
        rhs.append(lam*sum(w in sources for w in neighbors)/F(d))
    q=solve(A,rhs)
    return [F(1) if v in sources else q[idx[v]] for v in range(n)]


def choose_source(parts,counts):
    S=set();k=0
    for size,sz in zip(parts,counts):
        S.update(range(k,k+sz));k+=size
    return S


def polynomial_profile(parts,lam,tau):
    out={}
    for counts in product(*(range(n+1) for n in parts)):
        if not sum(counts):continue
        vals=profile_potentials(parts,counts,lam)
        if all(v>=tau for v in vals):
            k=sum(counts)
            w=1
            for n,v in zip(parts,counts):w*=comb(n,v)
            out[k]=out.get(k,0)+w
    return out


def polynomial_direct(parts,lam,tau):
    N=sum(parts);out={}
    for bits in range(1,1<<N):
        S={i for i in range(N) if bits>>i&1}
        if min(direct_potentials(parts,S,lam))>=tau:
            out[len(S)]=out.get(len(S),0)+1
    return out


def thresholds(m,lam):
    A=m*(1-lam)+lam
    E=m*(2-lam-lam*lam)+3*lam*lam
    D=4*m*m-lam**3*(m-1)*(m-2)-lam*lam*(3*m*m-6*m+2)
    assert A>0 and E>0 and D>0
    eta111=lam/A
    eta210=lam*(2*lam*lam*(m-1)+lam*(5*m-2)+2*m)/D
    eta300=3*lam*lam/E
    assert eta111-eta210==lam*m*(1-lam)*(m*(2-lam-lam*lam)+lam*lam)/(A*D)
    assert eta111-eta300==2*lam*m*(1-lam)**2/(A*E)
    return eta111,eta210,eta300

if __name__=='__main__':
    count=0
    for parts in [(1,1),(1,2),(2,2),(1,1,1),(1,2,2),(2,2,2),(1,1,2,2),(1,3,3),(2,3,3)]:
        for lam,tau in [(F(1,2),F(1,4)),(F(3,4),F(1,2)),(F(2,5),F(1,3))]:
            a=polynomial_profile(parts,lam,tau)
            b=polynomial_direct(parts,lam,tau)
            assert a==b,(parts,lam,tau,a,b)
            count+=1
    print('INDEPENDENT_COMPLETE_POLYNOMIALS_OK',count)
    a=0
    for m in range(4,13):
        for lam in [F(1,7),F(1,3),F(1,2),F(3,4),F(9,10),F(99,100)]:
            eta,x,y=thresholds(m,lam)
            assert eta>max(x,y)
            for counts,expected in [((1,1,1),eta),((2,1,0),x),((3,0,0),y)]:
                S=choose_source([m]*3,counts)
                direct=min(direct_potentials([m]*3,S,lam))
                assert direct==expected,(m,lam,counts,direct,expected)
                a+=1
            # The theorem's exact phase has only the balanced triple.
            t=(eta+max(x,y))/2
            P={}
            for c in product(range(4),repeat=3):
                if sum(c) not in (1,2,3):continue
                if min(profile_potentials([m]*3,c,lam))>=t:
                    P[c]=True
            assert P=={(1,1,1):True},(m,lam,P)
    print('SHARP_THREE_WAY_PHASE_OK',a,'exact independent vertex-level solves')
    for lam in [F(1,7),F(1,3),F(1,2),F(3,4),F(9,10)]:
        eta=lam/(3*(1-lam)+lam)
        onepart=lam/(2-lam)
        assert onepart>eta
    print('SHARP_m_EQUALS_3_BOUNDARY_OK')
    print('VERIFY_OK')
