from itertools import combinations,product
from math import comb

def rref_basis(rows,p):
    if not rows:return ()
    a=[list(row) for row in rows];nr=len(a);n=len(a[0]);at=0
    for c in range(n):
        s=next((i for i in range(at,nr) if a[i][c]%p),None)
        if s is None:continue
        a[at],a[s]=a[s],a[at]
        inv=pow(a[at][c],-1,p)
        a[at]=[(v*inv)%p for v in a[at]]
        for i in range(nr):
            if i==at:continue
            t=a[i][c]%p
            if t:a[i]=[(u-t*v)%p for u,v in zip(a[i],a[at])]
        at+=1
        if at==nr:break
    return tuple(tuple(row) for row in a[:at])

def all_subspaces(n,p):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(pivots[i]+1,n) if j not in pivots]
            for vals in product(range(p),repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,j in enumerate(pivots):rows[i][j]=1
                for (i,j),v in zip(free,vals):rows[i][j]=v
                yield tuple(tuple(row) for row in rows)

def bracket(u,v,m,p):
    z=sum(u[i]*v[m+i]-u[m+i]*v[i] for i in range(m))%p
    return (0,)*(2*m)+(z,)


def expected(q):
 H=q**3+q**2+q+1;P=(q*q+1)*(q*q+q+1);I=(q+1)*(q*q+1);G=(q*q-1)*(q*q-q);S=q*q*(q-1)
 E22=q**4*(P+2*q*q*I+q**3*I)//2
 T222=(q**4*G*(P+3*q*q*I+3*q**3*I)+q**9*I*S)//6
 return comb(H,3)+(q+1)*H*comb(q**3,2)+(P+q*q*I)*comb(q**3+q*q,2)+E22*(H-2*(q+1))+T222

def check(q):
 W=[w for w in all_subspaces(4,q) if 0<len(w)<4]
 weights=[1+q**len(w) if all(bracket((*u,0),(*v,0),2,q)[-1]==0 for u in w for v in w) else 1 for w in W]
 n=len(W)
 A=[[len(rref_basis([*W[i],*W[j]],q))==4 for j in range(n)] for i in range(n)]
 T=0; breakdown={}
 for i in range(n):
  for j in range(i+1,n):
   if not A[i][j]:continue
   for k in range(j+1,n):
    if A[i][k] and A[j][k]:
     count=weights[i]*weights[j]*weights[k];T+=count
     dims=tuple(sorted([len(W[i]),len(W[j]),len(W[k])]))
     breakdown[dims]=breakdown.get(dims,0)+count
 assert T==expected(q),(q,T,expected(q))
 print('q',q,'weighted_triangles',T,'breakdown',breakdown,'quotient_vertices',n)
for q in (2,3): check(q)
print('VERIFY_TRIANGLES_OK')
