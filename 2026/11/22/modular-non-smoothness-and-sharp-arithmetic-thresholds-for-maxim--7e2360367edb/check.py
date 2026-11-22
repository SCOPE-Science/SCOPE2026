#!/usr/bin/env python3
"""Independent finite-field checks of normalized maximal-index evolution-algebra automorphisms and infinitesimal tangent spaces.
The multiplication and constraints are constructed independently from displayed group-scheme formulas.
"""
import itertools, math

def table(n, entries, p):
    a=[[0]*n for _ in range(n)]
    for i in range(n-1): a[i][i+1]=1
    for (i,j),v in entries.items():
        assert 0<=i<j-1 and j<n-1
        a[i][j]=v%p
    return a

def product(x,y,a,p):
    n=len(a)
    return [sum((x[i]*y[i]*a[i][j] for i in range(n)),0)%p for j in range(n)]

def det_nonzero(M,p):
    M=[row[:] for row in M]; n=len(M); r=0
    for c in range(n):
        pivot=next((i for i in range(r,n) if M[i][c]%p),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        v=pow(M[r][c],-1,p); M[r]=[(x*v)%p for x in M[r]]
        for i in range(n):
            if i==r:continue
            k=M[i][c]
            M[i]=[(u-k*v)%p for u,v in zip(M[i],M[r])]
        r+=1
    return r==n

def is_automorphism(M,a,p):
    n=len(a)
    if not det_nonzero(M,p):return False
    for i in range(n):
        for j in range(i,n):
            lhs=[sum(M[r][k]*a[i][k] for k in range(n))%p for r in range(n)] if i==j else [0]*n
            x=[M[k][i] for k in range(n)]; y=[M[k][j] for k in range(n)]
            if product(x,y,a,p)!=lhs:return False
    return True

def modular_rank(A,p):
    A=[[x%p for x in row] for row in A]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        k=next((i for i in range(r,m) if A[i][c]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][c],-1,p); A[r]=[(v*inv)%p for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                t=A[i][c]
                A[i]=[(x-t*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def derivation_dim(a,p):
    n=len(a); equations=[]
    for i in range(n):
        for j in range(i,n):
            for r in range(n):
                coefficients=[0]*(n*n)
                for k in range(n):
                    coefficients[r*n+k]=(coefficients[r*n+k]+a[i][k]*(i==j))%p
                # D(e_i)*e_j: coefficient of D(e_i) at e_j times a_jr
                coefficients[j*n+i]=(coefficients[j*n+i]-a[j][r])%p
                coefficients[i*n+j]=(coefficients[i*n+j]-a[i][r])%p
                equations.append(coefficients)
    return n*n-modular_rank(equations,p)

def expected(n,b,p):
    weights=[2**j-2**(i+1) for (i,j),v in b.items() if v%p] # 0-index w=2^(j)-2^(i+1)
    g=math.gcd(*weights) if weights else 0
    dim=2 if not weights or g%p==0 else 1
    points=p*(p-1 if not weights else math.gcd(p-1,g))
    return (g,dim,points)

def derived_maps(n,b,p):
    a=table(n,b,p); g,dd,pp=expected(n,b,p)
    cnt=0
    for t in range(1,p):
        for u in range(p):
            M=[[0]*n for _ in range(n)]
            for i in range(n):M[i][i]=pow(t,2**i,p)
            M[n-1][0]=u
            if is_automorphism(M,a,p):cnt+=1
    return cnt

def brute_binary_4(b):
    n=4;p=2;a=table(n,b,p)
    cnt=0
    for data in itertools.product(range(p),repeat=n*n):
        M=[list(data[r*n:(r+1)*n]) for r in range(n)]
        if is_automorphism(M,a,p):cnt+=1
    return cnt

if __name__=='__main__':
    cases=[(4,{},2),(4,{(0,2):1},2),(4,{(0,2):1},3),
           (5,{(0,3):1},3),(5,{(0,2):1,(0,3):1},3),
           (6,{(0,4):1},7),(7,{(0,5):1},5),
           (7,{(0,2):1,(0,5):1},5),
           (5,{(0,2):1,(1,3):1},2),
           (5,{(0,2):1,(1,3):1},3)]
    for n,b,p in cases:
        g,dd,pp=expected(n,b,p)
        got_dim=derivation_dim(table(n,b,p),p)
        got_points=derived_maps(n,b,p)
        assert got_dim==dd,(n,b,p,g,dd,got_dim)
        assert got_points==pp,(n,b,p,g,pp,got_points)
        print('PASS',n,'p',p,'support',sorted(b),'g',g,'Der dimension',got_dim,'parametrized automorphisms',got_points)
    for b in ({},{(0,2):1}):
        direct=brute_binary_4(b)
        exp=expected(4,b,2)[2]
        assert direct==exp,(b,direct,exp)
        print('PASS exhaustive all 2^16 matrices, n=4 p=2 support',sorted(b),'automorphisms',direct)

# Independent infinitesimal witness over K[eps]/(eps^2): these checks
# use dual-number arithmetic and do not rely on finite-field point counts.
def dadd(x,y,p): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def dmul(x,y,p): return (x[0]*y[0]%p,(x[0]*y[1]+x[1]*y[0])%p)
def dsquare(x,p):return dmul(x,x,p)
def dcheck(n,entry,p):
    # t=1+eps and all off-diagonal coordinates zero
    a=table(n,{entry:1},p)
    t=(1,1); powers=[t]+[(1,0)]*(n-1)
    for i in range(1,n):powers[i]=dsquare(powers[i-1],p)
    # scalar diagonal images preserve all products iff each skipped term matches
    ok=True
    for i in range(n):
      for j in range(n):
        for r in range(n):
          lhs=dmul((a[i][r],0),powers[r],p) if i==j else (0,0)
          rhs=dmul(dmul(powers[i],powers[j],p),(a[i][r],0),p) if i==j else (0,0)
          if lhs!=rhs:ok=False
    g=expected(n,{entry:1},p)[0]
    assert ok == (g%p==0)
    print('PASS dual-numbers', 'n',n,'p',p,'g',g,'nontrivial infinitesimal automorphism',ok)

if __name__=='__main__':
    dcheck(4,(0,2),2)
    dcheck(4,(0,2),3)
    dcheck(5,(0,3),3)
    dcheck(7,(0,5),5)
