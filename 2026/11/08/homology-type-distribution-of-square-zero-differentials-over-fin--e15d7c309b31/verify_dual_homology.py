"""Directly verify R-module homology type of square-zero R-linear differential matrices.
R = F_q[e]/e^2, H = ker(X)/im(X). Computes epsilon-action on H from
actual 2n x 2n matrices and compares to a distinct flag count formula.
"""
from itertools import product
from collections import Counter
from math import prod
from verify_dual_differentials import ops,rank,matmul

def gauss(M,q,add,mul):
    A=[list(row) for row in M]; k=0; piv=[]; cols=len(A[0])
    for j in range(cols):
        t=next((i for i in range(k,len(A)) if A[i][j]),None)
        if t is None:continue
        A[k],A[t]=A[t],A[k]
        inv=next(u for u in range(1,q) if mul(u,A[k][j])==1)
        A[k]=[mul(inv,x) for x in A[k]]
        for i in range(len(A)):
            if i==k or A[i][j]==0:continue
            fac=A[i][j]
            A[i]=[add(x,mul((-fac)%q,y)) if q!=4 else add(x,mul(fac,y)) for x,y in zip(A[i],A[k])]
        piv.append(j);k+=1
        if k==len(A):break
    return A,piv

def kernel(M,q,add,mul):
    A,piv=gauss(M,q,add,mul); cols=len(M[0]);free=[j for j in range(cols) if j not in piv];out=[]
    for j in free:
        v=[0]*cols;v[j]=1
        for i,p in enumerate(piv):v[p]=(-A[i][j])%q if q!=4 else A[i][j]
        out.append(v)
    return out

def invs(n,q):
    add,mul=ops(q); N=n*n; zero=[0]*N;cnt=Counter()
    for aa in product(range(q),repeat=N):
        if matmul(aa,aa,n,add,mul)!=zero:continue
        A=[list(aa[n*i:n*(i+1)]) for i in range(n)]
        r=rank(A,q,add,mul)
        for bb in product(range(q),repeat=N):
            ab=matmul(aa,bb,n,add,mul);ba=matmul(bb,aa,n,add,mul)
            if any(add(x,y) for x,y in zip(ab,ba)):continue
            X=[A[i]+[0]*n for i in range(n)]+[list(bb[n*i:n*(i+1)])+A[i] for i in range(n)]
            s=rank(X,q,add,mul)
            ker=kernel(X,q,add,mul)
            # epsilon * (v0,v1) = (0,v0)
            ev=[[0]*n+list(v[:n]) for v in ker]
            # sum of im X and epsilon(ker X) via column span
            stacked=[X[i]+[v[i] for v in ev] for i in range(2*n)]
            u=rank(stacked,q,add,mul)-s
            v=2*n-2*s-2*u
            assert v>=0 and v%2==0,(n,q,r,s,u,v)
            cnt[(r,s,u,v)]+=1
    return cnt

def predicted(n,q):
    def g(n,r):return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))
    def gl(r):return prod(q**r-q**i for i in range(r))
    out=Counter()
    for r in range(n//2+1):
        h=n-2*r
        for s in range(h+1):
            a=h-s
            for c in range(min(a,s)+1):
                u=a-c;v=2*c;total_rank=2*r+s
                count=g(n,r)*g(n-r,r)*gl(r)*q**(2*r*(n-r))
                count*=g(h,a)*g(a,c)*g(s,s-c)*q**((a-c)*(s-c))*gl(s)
                out[(r,total_rank,u,v)]+=count
    return out

def main():
    for n,q in [(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)]:
        act=invs(n,q);theory=predicted(n,q)
        assert act==theory,(n,q,act-theory,theory-act)
        print('DIRECT_HOMOLOGY_MATCH',n,q,'types',len(act),'total',sum(act.values()),'spectrum',sorted(act.items()) if n<=2 else 'omitted')
    for n in range(1,9):
        for q in (2,3,4,5):
            arr=predicted(n,q)
            assert all(v%2==0 for (_r,_rank,_u,v) in arr)
    print('HOMOLOGY_TYPE_COUNTS_AND_PARITY_OK')
if __name__=='__main__':main()
