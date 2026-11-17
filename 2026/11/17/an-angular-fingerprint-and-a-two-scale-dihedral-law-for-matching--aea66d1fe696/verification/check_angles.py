"""Exact rational verification of facet-normal Gram spectra for matching-deleted complete-graph Laplacian simplices."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

def matmul(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def gram(n,m):
    # explicit pseudoinverse from the n- and (n-2)-eigenspaces
    I=[[Q(i==j) for j in range(n)] for i in range(n)]
    J=[[Q(1,n) for j in range(n)] for i in range(n)]
    P=[[I[i][j]-J[i][j] for j in range(n)] for i in range(n)]
    W=[[Q(0) for j in range(n)] for i in range(n)]
    for k in range(m):
        i,j=2*k,2*k+1
        for a,b,z in ((i,i,1),(j,j,1),(i,j,-1),(j,i,-1)): W[a][b]+=Q(z,2)
    Lplus=[[P[i][j]/n+Q(2,n*(n-2))*W[i][j] for j in range(n)] for i in range(n)]
    # original Laplacian reconstructed as complete graph minus m independent edges
    L=[[Q(n*(i==j)-1) for j in range(n)] for i in range(n)]
    for k in range(m):
        i,j=2*k,2*k+1
        L[i][i]-=1;L[j][j]-=1;L[i][j]+=1;L[j][i]+=1
    assert matmul(L,Lplus)==P
    G=matmul(Lplus,Lplus)
    c=Q(1,n-1); kapp=1+Q(2*n,(n-2)**2)
    types={'UU':0,'UM':0,'MM_diff':0,'MM_mates':0}
    for i,j in combinations(range(n),2):
        t='UU' if i>=2*m and j>=2*m else 'UM' if (i>=2*m)!=(j>=2*m) else 'MM_mates' if i//2==j//2 else 'MM_diff'
        if t=='UU':norm=c*c
        elif t=='UM':norm=c*c/kapp
        elif t=='MM_diff':norm=c*c/kapp**2
        else:norm=((c+kapp-1)/kapp)**2
        observed=G[i][j]**2/(G[i][i]*G[j][j])
        assert observed==norm and G[i][j]<0,(n,m,i,j,t,observed,norm)
        types[t]+=1
    s=n-2*m
    assert types=={'UU':comb(s,2),'UM':2*m*s,'MM_diff':2*m*(m-1),'MM_mates':m}
    if m:
        mates=[(i,i+1) for i in range(0,2*m,2)]
        assert all(G[i][j]**2/(G[i][i]*G[j][j])>c*c for i,j in mates)
    return types

if __name__=='__main__':
    total=0;groups={}
    for n in range(3,17):
        for m in range(0,n//2+1):
            if n==2 and m==1:continue
            typ=gram(n,m)
            total+=1
            for k,v in typ.items():groups[k]=groups.get(k,0)+v
    print(f'MATCHING_DELETED_LAPLACIAN_ANGLE_PASS configurations={total} exact_ridges={sum(groups.values())} by_type={groups}')
