"""Reproducible exact checks of cyclic screened-Green landmark identities.

Python 3 standard library only.  The universal result rests on the written proof;
finite verification independently checks identities and optimizer classifications.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def mat_inverse(A):
    n=len(A)
    if not n: return []
    aug=[[Q(x) for x in A[i]]+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if aug[i][j]);aug[j],aug[p]=aug[p],aug[j]
        v=aug[j][j];aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i!=j:
                s=aug[i][j]
                if s: aug[i]=[a-s*b for a,b in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def det(A):
    n=len(A)
    if not n:return Q(1)
    B=[[Q(x) for x in r] for r in A]; out=Q(1)
    for j in range(n):
        p=next((i for i in range(j,n) if B[i][j]),None)
        if p is None:return Q(0)
        if p!=j: B[j],B[p]=B[p],B[j];out=-out
        v=B[j][j];out*=v
        for i in range(j+1,n):
            s=B[i][j]/v
            for t in range(j+1,n):B[i][t]-=s*B[j][t]
    return out


def cycle_precision(n,mu):
    A=[[Q(mu+2) if i==j else Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        j=(i+1)%n;A[i][j]-=1;A[j][i]-=1
    return A


def sub(A,S):return [[A[i][j] for j in S] for i in S]


def ff(mu,n):
    F=[Q(1),Q(mu+2)]
    for _ in range(2,n+1):F.append((mu+2)*F[-1]-F[-2])
    Fp=[Q(0),Q(1)]
    for j in range(2,n+1):Fp.append(F[j-1]+(mu+2)*Fp[j-1]-Fp[j-2])
    return F,Fp


def gaps(n,S):
    S=tuple(sorted(S));return tuple((S[(i+1)%len(S)]-S[i])%n or n for i in range(len(S)))


def check():
    count=0
    for mu in [Q(1,3),Q(1),Q(5,2)]:
        for n in range(3,11):
            F,Fp=ff(mu,n)
            f=[Fp[i]/F[i] for i in range(n+1)]
            for m in range(1,n):
                assert f[m+1]-2*f[m]+f[m-1]>0;count+=1
                assert F[m]*F[m]-F[m-1]*F[m+1]==1;count+=1
            for k in range(1,n+1):
                vals=[];detvals=[];winners=[]
                for S in combinations(range(n),k):
                    lengths=[g-1 for g in gaps(n,S)]
                    E=sum((f[m] for m in lengths),Q(0))
                    D=Q(1)
                    for m in lengths:D*=F[m]
                    vals.append(E);detvals.append(D)
                    if max(lengths)-min(lengths)<=1:winners.append(S)
                    count+=1
                bestE=min(vals);bestD=max(detvals)
                assert {i for i,v in enumerate(vals) if v==bestE}=={i for i,v in enumerate(detvals) if v==bestD};count+=1
                assert sum(v==bestE for v in vals)==len(winners);count+=1
                q,r=divmod(n,k)
                assert bestE==r*f[q]+(k-r)*f[q-1];count+=1
                assert bestD==F[q]**r*F[q-1]**(k-r);count+=1
                assert len(winners)*k==n*comb(k,r);count+=1
                if r==0 and 2<=k<n:
                    runnerE=min(v for v in vals if v>bestE)
                    runnerD=max(v for v in detvals if v<bestD)
                    assert runnerE-bestE==f[q]+f[q-2]-2*f[q-1];count+=1
                    assert runnerD/bestD==1-Q(1,F[q-1]**2);count+=1
                    assert sum(v==runnerE for v in vals)==n*(k-1);count+=1
                    assert sum(v==runnerD for v in detvals)==n*(k-1);count+=1
    # Check full covariance, Schur complement and complementary minor directly.
    for mu in [Q(1,3),Q(2)]:
        for n in range(3,8):
            A=cycle_precision(n,mu)
            G=mat_inverse(A);dA=det(A)
            F,Fp=ff(mu,n)
            for k in range(1,n+1):
                for S in combinations(range(n),k):
                    T=tuple(i for i in range(n) if i not in S)
                    lengths=[g-1 for g in gaps(n,S)]
                    detS=det(sub(G,S))
                    prod=Q(1)
                    for m in lengths:prod*=F[m]
                    assert detS==prod/dA;count+=1
                    E=sum((Fp[m]/F[m] for m in lengths),Q(0))
                    ATinv=mat_inverse(sub(A,T))
                    assert E==sum((ATinv[i][i] for i in range(len(T))),Q(0));count+=1
                    # Direct Schur complement independent of Jacobi identity
                    SS=sub(G,S);Tinv=mat_inverse(SS)
                    Sch=Q(0)
                    for i in T:
                        Sch+=G[i][i]
                        for aa,a in enumerate(S):
                            for bb,b in enumerate(S):
                                Sch-=G[i][a]*Tinv[aa][bb]*G[b][i]
                    assert Sch==E;count+=1
    n=6
    opt2=[s for s in combinations(range(n),2) if len(set(gaps(n,s)))==1]
    opt3=[s for s in combinations(range(n),3) if len(set(gaps(n,s)))==1]
    assert all(not set(a).issubset(b) for a in opt2 for b in opt3);count+=1
    print('PASS',count,'exact rational checks including all subsets at n<=10; independent n<=7 direct covariance comparisons')

if __name__=='__main__':check()
