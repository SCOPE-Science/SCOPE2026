"""Independent exact checks for the genus-four cyclic trigonal Cartier profile.

Pure Python; requires no third-party libraries.
"""
import itertools
from fractions import Fraction

IRR={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011,7:0b10000011,8:0b100011011}

def fm(a,b,n=2):
    mod=IRR[n]; r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a & (1<<n):a^=mod
    return r

def fp(a,n=2):
    return fm(a,a,n)

def powf(a,m,n):
    z=1
    while m:
        if m&1:z=fm(z,a,n)
        a=fm(a,a,n);m//=2
    return z

def inv(a,n=2):
    assert a
    return powf(a,(1<<n)-2,n)

def poly_trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def poly_rem(p,q):
    p=poly_trim(p[:]);q=poly_trim(q[:]);n=2
    while len(p)>=len(q) and p!=[0]:
        t=fm(p[-1],inv(q[-1],n),n); offset=len(p)-len(q)
        for j,v in enumerate(q):p[j+offset]^=fm(t,v,n)
        poly_trim(p)
    return p

def poly_gcd(p,q):
    while q!=[0]:p,q=q,poly_rem(p,q)
    if len(p)==1 and p[0]:return [1]
    return p

def gauss_rank(mat,n=2):
    a=[x[:] for x in mat]; nrow=len(a); ncol=len(a[0]);r=0
    for col in range(ncol):
        pivot=next((i for i in range(r,nrow) if a[i][col]),None)
        if pivot is None:continue
        a[pivot],a[r]=a[r],a[pivot]
        d=inv(a[r][col],n)
        for j in range(col,ncol):a[r][j]=fm(a[r][j],d,n)
        for i in range(nrow):
            if i==r or a[i][col]==0:continue
            c=a[i][col]
            for j in range(col,ncol):a[i][j]^=fm(c,a[r][j],n)
        r+=1
        if r==nrow:break
    return r

def mxmul(A,B,n=2):
    return [[__import__('functools').reduce(int.__xor__,(fm(A[i][k],B[k][j],n) for k in range(len(B))),0) for j in range(len(B[0]))] for i in range(len(A))]

def carmat(a,b):
    # basis U=dx/y, H=dx/y^2, W=x dx/y^2, J=x^2 dx/y^2
    A=[[0]*4 for _ in range(4)]
    A[1][0]=fp(b)
    A[2][0]=fp(a)
    A[3][0]=1
    A[0][2]=1
    return A

def rank_profile(a,b):
    A=carmat(a,b); B=A
    result=[]
    for _ in range(5):
        result.append(gauss_rank(B))
        B=mxmul(A,[[fp(x) for x in row] for row in B])
    return result

def poly_change(co,u,v):
    # exact x->u*x+v, normalized leading coefficient to 1 over GF(4)
    out=[0]*6
    for j,c in enumerate(co):
        for i in range(j+1):
            if (i&j)==i:
                t=fm(c,fm(powf(u,i,2),powf(v,j-i,2),2),2)
                out[i]^=t
    z=inv(powf(u,5,2),2)
    return [fm(x,z,2) for x in out]

cnt={0:0,2:0}; profile_cnt={}
for d,a,e,b,c in itertools.product(range(4),repeat=5):
    f=[c,b,e,a,d,1]
    derivative=[b,0,a,0,1]
    if poly_gcd(f,derivative)!=[1]:continue
    rank=0 if a==0 else 2
    cnt[rank]+=1
    prof=rank_profile(a,b)
    target=[2,1,0,0,0] if a==0 else [2,2,2,2,2]
    assert prof==target,(f,prof,target)
    profile_cnt[tuple(prof)]=profile_cnt.get(tuple(prof),0)+1
    for u in (1,2,3):
        for v in range(4):
            g=poly_change(f,u,v)
            assert g[3]==fm(a,inv(powf(u,2,2),2),2),(f,u,v,g)
assert cnt[0]>0 and cnt[2]>0
print('GF(4) monic squarefree quintics by 2-rank:',cnt)
print('All higher Cartier-rank profiles:',profile_cnt)
print('Affine coordinate-normalization checks:',12*sum(cnt.values()))

# Independently verify that mod-2 zeta-polynomial degrees match the 2-ranks
# for smooth models of f=x^5+x+1 and f=x^5+x^3+1 over F_2.
def curve_pointcount(n,a,b):
    q=1<<n
    cubes={powf(y,3,n) for y in range(q)} if n%2==0 else None
    ans=1  # exactly one point above infinity
    for x in range(q):
        v=powf(x,5,n)^fm(a,powf(x,3,n),n)^fm(b,x,n)^1
        ans+=1 if n%2 else (1 if v==0 else 3 if v in cubes else 0)
    return ans

def Lcoeff(a,b):
    N=[0]+[curve_pointcount(n,a,b) for n in range(1,9)]
    S=[0]+[(1<<n)+1-N[n] for n in range(1,9)]
    L=[1]
    for k in range(1,9):
        val=-sum(S[i]*L[k-i] for i in range(1,k+1))
        assert val%k==0
        L.append(val//k)
    return L

for name,a,b,expect in [('zero',0,1,0),('two',1,0,2)]:
    L=Lcoeff(a,b)
    d=max(i for i,x in enumerate(L) if x&1)
    assert d==expect,(name,L)
    print('F2 curve',name,'L-polynomial coefficients',L,'mod2 degree',d)
print('ALL_CHECKS_PASSED')
