"""Exact integer-modular tests for generalized Petersen coordinate control.

No external packages needed. Full row rank modulo a prime certifies full row rank
of the integral Kalman controllability matrix over the rationals.
A deficient modular rank alone is *not* a noncontrollability certificate.
"""
from fractions import Fraction
from itertools import permutations
from math import cos, pi

P=1000003

def graph_laplacian(n,k):
    if not (n >= 5 and 2 <= k and 2*k < n):
        raise ValueError((n,k))
    N=2*n
    L=[[0]*N for _ in range(N)]
    for i in range(n):
        for u,v in ((i,(i+1)%n),(n+i,n+(i+k)%n),(i,n+i)):
            L[u][u]+=1; L[v][v]+=1
            L[u][v]-=1; L[v][u]-=1
    assert all(L[i][i]==3 for i in range(N))
    assert all(sum(row)==0 for row in L)
    return L

def kalman_mod_rank(n,k,r,p=P):
    L=graph_laplacian(n,k); N=len(L)
    # Form N x (r*N) array of exact Kalman blocks with modular arithmetic.
    cols=[]
    block=[[1 if i==j else 0 for j in range(r)] for i in range(N)]
    for _ in range(N):
        cols.extend([[block[i][j] for i in range(N)] for j in range(r)])
        block=[[sum(L[i][v]*block[v][j] for v in range(N))%p for j in range(r)] for i in range(N)]
    A=[[c[i]%p for c in cols] for i in range(N)]
    rank=0
    for j in range(len(cols)):
        pivot=next((i for i in range(rank,N) if A[i][j]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        inv=pow(A[rank][j],-1,p)
        A[rank][j:]=[v*inv%p for v in A[rank][j:]]
        for i in range(rank+1,N):
            t=A[i][j]
            if t:
                A[i][j:]=[(a-t*b)%p for a,b in zip(A[i][j:],A[rank][j:])]
        rank+=1
        if rank==N:break
    return rank

def check_factor():
    # lambda=5 and k=2: (3-2x-5)*(5-4x*x-5)-1
    # equals (2x+1)*(4x*x+2x-1)
    for num in range(-9,10):
        x=Fraction(num,7)
        assert (3-2*x-5)*(5-4*x*x-5)-1 == (2*x+1)*(4*x*x+2*x-1)
    return 19

def norm_polynomial_for_gp11():
    """Exact resultant via multiplication in Z[u]/(u^5+u^4-4u^3-3u^2+3u+1).

    Each polynomial in the spectral variable is stored as ascending integer coefficients.
    This is a direct finite integer identity, without floating-point roots.
    """
    def add(a,b):
        c=[0]*max(len(a),len(b))
        for i,x in enumerate(a): c[i]+=x
        for i,x in enumerate(b): c[i]+=x
        return c
    def mult(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    def reduce_u_degree(d):
        v=[0]*(max(8,d+1));v[d]=1
        for q in range(len(v)-1,4,-1):
            z=v[q]
            if not z:continue
            # u^5 = -u^4+4u^3+3u^2-3u-1
            for t,c in enumerate((-1,-3,3,4,-1)):
                v[q-5+t]+=c*z
            v[q]=0
        return v[:5]
    f=[[14,-8,1],[-5,1],[-3,1],[1]]
    M=[[[0] for _ in range(5)] for _ in range(5)]
    for j in range(5):
        for q,coeff in enumerate(f):
            for row,b in enumerate(reduce_u_degree(q+j)):
                M[row][j]=add(M[row][j],[b*x for x in coeff])
    det=[0]
    for perm in permutations(range(5)):
        inv=sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))
        prod=[(-1)**inv]
        for i,j in enumerate(perm):prod=mult(prod,M[i][j])
        det=add(det,prod)
    while len(det)>1 and det[-1]==0:det.pop()
    assert det==[16951,-83215,169675,-191202,133122,-60301,18109,-3578,447,-32,1],det
    # Its reduction mod 2 has derivative (l+1)^4 and value 1 at l=1;
    # hence the resultant is squarefree over Q.
    r2=[a%2 for a in det]
    derivative=[(i*a)%2 for i,a in enumerate(r2)][1:]
    assert derivative==[1,0,0,0,1,0,0,0,0,0]
    assert sum(r2)%2==1
    assert sum(det[i]*0**i for i in range(len(det)))==16951
    assert sum(a*2**i for i,a in enumerate(det))==-11
    return len(det)

def numerical_predicted_min(n,k):
    eig=[]
    for j in range(n):
        x=cos(2*pi*j/n);y=cos(2*pi*k*j/n)
        a=3-x-y;b=((x-y)**2+1)**0.5
        eig.extend((a-b,a+b))
    eig.sort()
    group=1;mx=1
    for i in range(1,len(eig)):
        if abs(eig[i]-eig[i-1])<1e-8:group+=1
        else:group=1
        mx=max(mx,group)
    return mx

if __name__=='__main__':
    assert check_factor()==19
    assert norm_polynomial_for_gp11()==11
    cases=[(11,2),(5,2),(6,2),(7,2),(8,3),(9,2),(10,2),(11,3),(12,2),(13,3),(14,2),(15,2),(16,3),(17,2),(18,4),(20,2),(21,2),(25,2),(30,2)]
    for n,k in cases:
        r=numerical_predicted_min(n,k)
        R=kalman_mod_rank(n,k,r)
        assert R==2*n,(n,k,r,R)
        if n in (5,10,15,20,25,30) and k==2:
            low=kalman_mod_rank(n,k,r-1)
            assert low<2*n,(n,k,r,low)
            print('full modular rank',n,k,'r=',r,'full=',R,'previous=',low)
        else:
            print('full modular rank',n,k,'r=',r,'full=',R)
    assert kalman_mod_rank(11,2,2)==22  # exact finite witness: two adjacent outer coordinates suffice
    print('PASS: rational factor tests; all finite full-rank modular witnesses')
