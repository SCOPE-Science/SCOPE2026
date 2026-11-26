"""Independent prime-field Leibniz solver and rank-spectrum enumerator."""
from itertools import product
from collections import Counter
from math import prod

def rankmod(M,p):
    if not M:return 0
    a=[x[:] for x in M];R=len(a);C=len(a[0]);r=0
    for c in range(C):
        k=next((i for i in range(r,R) if a[i][c]%p),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        t=pow(a[r][c],-1,p)
        for j in range(c,C):a[r][j]=(a[r][j]*t)%p
        for i in range(R):
            if i==r:continue
            t=a[i][c]
            if t:
                for j in range(c,C):a[i][j]=(a[i][j]-t*a[r][j])%p
        r+=1
        if r==R:break
    return r

def kernel_basis(rows,p,nvars):
    a=[list(map(lambda x:x%p,row)) for row in rows]
    r=0;piv=[]
    for c in range(nvars):
        k=next((i for i in range(r,len(a)) if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        t=pow(a[r][c],-1,p)
        a[r]=[(u*t)%p for u in a[r]]
        for i in range(len(a)):
            if i==r:continue
            t=a[i][c]
            if t:a[i]=[(u-t*v)%p for u,v in zip(a[i],a[r])]
        piv.append(c);r+=1
        if r==len(a):break
    free=[c for c in range(nvars) if c not in piv]
    basis=[]
    for c in free:
        v=[0]*nvars;v[c]=1
        for i,k in enumerate(piv):v[k]=-a[i][c]%p
        basis.append(v)
    return basis

def leibniz_basis(parts,p):
    N=sum(parts); nvar=N*N
    group=[i for i,n in enumerate(parts) for _ in range(n)]
    w=[[int(group[b]!=group[a]) for b in range(N)] for a in range(N)]
    eq=[]
    for a in range(N):
      for b in range(a,N):
       for k in range(N):
        row=[0]*nvar
        if a==b:
          for j in range(N):
            if w[a][j]:row[k*N+j]+=1
          row[a*N+a]-=2*w[a][k]
        else:
          row[b*N+a]+=w[b][k]
          row[a*N+b]+=w[a][k]
        if any(x%p for x in row):eq.append(row)
    return kernel_basis(eq,p,nvar)

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def sym_polynomial(m,q):
    ans={}
    for k in range(m+1):
      N=q**(k*(k+1)//2)
      numerator=prod(q**(2*i-1)-1 for i in range(1,(k+1)//2+1))
      denom=q**sum(2*i-1 for i in range(1,(k+1)//2+1))
      N=N*numerator//denom
      ans[k]=gaussian(m,k,q)*N
    return ans

def alt_polynomial(m,q):
    ans={}
    for r in range(m//2+1):
      ans[2*r]=gaussian(m,2*r,q)*q**(r*(r-1))*prod(q**(2*i-1)-1 for i in range(1,r+1))
    return ans

def convolve(P,Q):
    R=Counter()
    for i,a in P.items():
      for j,b in Q.items():R[i+j]+=a*b
    return dict(R)

def expected(parts,p):
    f=sym_polynomial if p==2 else alt_polynomial
    res={0:1}
    for a in parts:res=convolve(res,f(a-1,p))
    return res

def actual(parts,p):
    N=sum(parts);basis=leibniz_basis(parts,p)
    assert p**len(basis)<=100000,'test too large'
    out=Counter()
    for alphas in product(range(p),repeat=len(basis)):
      C=[sum(alpha*b[i] for alpha,b in zip(alphas,basis))%p for i in range(N*N)]
      M=[[C[i*N+j] for j in range(N)] for i in range(N)]
      out[rankmod(M,p)]+=1
    return dict(out),len(basis)

def run():
 for parts,p in [((1,1),2),((1,1),3),((2,2),2),((2,3),2),((3,3),2),((2,2,2),2),((1,2,3),2),((2,3),5),((3,3),5),((3,3,3),5),((3,2),7),((2,2,2),5)]:
  if p!=2 and (p==3 or any(a%p==0 for a in parts)):continue
  a,dim=actual(parts,p);e=expected(parts,p)
  assert a=={k:v for k,v in e.items() if v},(parts,p,a,e)
  print('PASS',parts,p,'derivation dimension',dim,'spectrum',a)
 print('VERIFY_OK')
if __name__=='__main__':run()
