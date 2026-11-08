from itertools import product,combinations
from math import prod

def gauss(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def s(n,k,q):
    return sum(gauss(n,i,q)*gauss(n,k-i,q) for i in range(n+1))

def t(n,u,q):
    # Number of ordered disjoint A-invariant subspaces of dimensions u and 2n-1-u.
    out=0
    for i in range(n+1):
        j=u-i
        if not 0<=j<=n:continue
        if i<n:
            out+=gauss(n,i,q)*gauss(n-i,1,q)*q**(i*(n-i-1))*gauss(n,j,q)*q**(j*(n-j))
        if j<n:
            out+=gauss(n,i,q)*q**(i*(n-i))*gauss(n,j,q)*gauss(n-j,1,q)*q**(j*(n-j-1))
    return out

def predicted(n,q):
    m=2*n; d=m+1
    if q%2==0:return [gauss(d,r,q)*q**(r*(d-r)) for r in range(d+1)]
    ans=[]
    for r in range(d+1):
        A=(s(n,m-r,q)*q**(r*(m-r+1))) if r<=m else 0
        B=(s(n,r-1,q)*q**(r*(m-r+1))) if 1<=r else 0
        # first exponent WRONG? type A exponent r(m-r)+r=r(m-r+1)
        C=((q-1)*q**m*t(n,r-1,q)) if 1<=r<=m else 0
        ans.append(A+B+C)
    return ans

def bracket(x,y,q):
    d=len(x); out=[0]*d
    for j in range(1,d):
        sign=1 if j<=((d-1)//2) else (q-1)
        out[j]=sign*(x[0]*y[j]-y[0]*x[j])%q
    return out

def linear(a,x,d,q):
    return [sum(a[i*d+k]*x[k] for k in range(d))%q for i in range(d)]

def rank(a,d,q):
    mat=[list(a[i*d:(i+1)*d]) for i in range(d)]; r=0
    for c in range(d):
        pivot=next((i for i in range(r,d) if mat[i][c]),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        inv=pow(mat[r][c],-1,q)
        mat[r]=[v*inv%q for v in mat[r]]
        for i in range(d):
            if i!=r:
                t=mat[i][c]
                mat[i]=[(mat[i][j]-t*mat[r][j])%q for j in range(d)]
        r+=1
    return r

def satisfies(a,d,q):
    for i in range(d):
        for j in range(d):
            if sum(a[i*d+k]*a[k*d+j] for k in range(d))%q!=a[i*d+j]:return False
    cols=[[a[i*d+j] for i in range(d)] for j in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            ei=[int(k==i) for k in range(d)]; ej=[int(k==j) for k in range(d)]
            pi,pj=cols[i],cols[j]
            l=bracket(pi,pj,q)
            x=bracket(pi,ej,q); y=bracket(ei,pj,q)
            z=linear(a,bracket(ei,ej,q),d,q)
            rhs=linear(a,[(x[k]+y[k]-z[k])%q for k in range(d)],d,q)
            if l!=rhs:return False
    return True

def brute(n,q):
    d=2*n+1; got=[0]*(d+1)
    for matrix in product(range(q),repeat=d*d):
        if satisfies(matrix,d,q):got[rank(matrix,d,q)]+=1
    return got


def rref_subspaces(d,k,q):
    for pivots in combinations(range(d),k):
        free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,d) if j not in pivots]
        for vals in product(range(q),repeat=len(free)):
            rows=[[0]*d for _ in pivots]
            for i,p in enumerate(pivots):rows[i][p]=1
            for (i,j),v in zip(free,vals):rows[i][j]=v
            yield tuple(map(tuple,rows)),pivots

def contains(sub, piv, x,q):
    v=list(x)
    for row,p in zip(sub,piv):
        t=v[p]
        if t:
            for j in range(p,len(v)):v[j]=(v[j]-t*row[j])%q
    return not any(v)

def closed(sub,piv,q,n):
    for ii in range(len(sub)):
        for jj in range(ii+1,len(sub)):
            x,y=sub[ii],sub[jj]
            z=[0]+[(x[0]*y[j]-y[0]*x[j])*(1 if j<=n else q-1)%q for j in range(1,2*n+1)]
            if not contains(sub,piv,z,q):return False
    return True

def complementary(u,w,q,d):
    # row rank of concatenated bases
    A=[list(row) for row in u+w];r=0
    for c in range(d):
        pivot=next((i for i in range(r,d) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inverse=pow(A[r][c],-1,q)
        for j in range(c,d):A[r][j]=(A[r][j]*inverse)%q
        for i in range(r+1,d):
            t=A[i][c]
            if t:
                for j in range(c,d):A[i][j]=(A[i][j]-t*A[r][j])%q
        r+=1
        if r==d:return True
    return r==d


def verify():
    for n,q in ((1,2),(1,3),(1,5)):
        actual=brute(n,q)
        expected=predicted(n,q)
        print("direct torsion matrix enumeration",n,q,actual,flush=True)
        assert actual==expected
    for n,q in ((2,2),(2,3)):
        d=2*n+1
        sub=[]
        for k in range(d+1):
            sub.append([b for b,p in rref_subspaces(d,k,q) if closed(b,p,q,n)])
        actual=[sum(complementary(u,w,q,d) for u in sub[k] for w in sub[d-k]) for k in range(d+1)]
        expected=predicted(n,q)
        print("independent subspace-pair enumeration",n,q,actual,flush=True)
        assert actual==expected
    # Check the symmetry under P -> I-P and characteristic-two collapse.
    for n in range(1,6):
        for q in (2,3,5):
            counts=predicted(n,q)
            assert counts==counts[::-1]
            assert counts[0]==counts[-1]==1
            if q==2:
                assert counts==[gauss(2*n+1,r,q)*q**(r*(2*n+1-r)) for r in range(2*n+2)]
    print('VERIFY_OK')

if __name__=='__main__': verify()
