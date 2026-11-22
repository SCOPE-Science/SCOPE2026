"""Reproduce finite-field tests for maximal elementwise square-zero subspaces of exterior E_3.
Requires only Python 3 standard library. Calculations use prime fields F_3 and F_5.
"""
from itertools import product, combinations
from collections import Counter

def rank(rows,q):
    if not rows:return 0
    a=[list(x) for x in rows]
    m,n=len(a),len(a[0]); k=0
    for j in range(n):
        i=next((i for i in range(k,m) if a[i][j]%q),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k]
        t=pow(a[k][j]%q,-1,q);a[k]=[(x*t)%q for x in a[k]]
        for i in range(m):
            if i!=k and a[i][j]:
                t=a[i][j];a[i]=[(x-t*y)%q for x,y in zip(a[i],a[k])]
        k+=1
        if k==m:break
    return k

def rref(rows,q):
    if not rows:return ()
    a=[list(x) for x in rows]; m,n=len(a),len(a[0]);k=0
    for j in range(n):
        i=next((i for i in range(k,m) if a[i][j]%q),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k]
        t=pow(a[k][j]%q,-1,q);a[k]=[(x*t)%q for x in a[k]]
        for i in range(m):
            if i!=k and a[i][j]:
                t=a[i][j];a[i]=[(x-t*y)%q for x,y in zip(a[i],a[k])]
        k+=1
        if k==m:break
    return tuple(tuple(x) for x in a[:k])

def subspaces(n,r,q):
    for piv in combinations(range(n),r):
        free=[(i,j) for i in range(r) for j in range(piv[i]+1,n) if j not in piv]
        for v in product(range(q),repeat=len(free)):
            rows=[[int(j==piv[i]) for j in range(n)] for i in range(r)]
            for (i,j),a in zip(free,v):rows[i][j]=a
            yield tuple(map(tuple,rows))

def dot(a,b,q):return sum(x*y for x,y in zip(a,b))%q

def cross(u,v,q):return ((u[1]*v[2]-u[2]*v[1])%q,(u[2]*v[0]-u[0]*v[2])%q,(u[0]*v[1]-u[1]*v[0])%q)

def nullspace(rows,n,q):
    R=rref(rows,q);p=[next(i for i,x in enumerate(row) if x) for row in R];out=[]
    for j in range(n):
        if j in p:continue
        w=[0]*n;w[j]=1
        for i,row in enumerate(R):w[p[i]]=(-row[j])%q
        out.append(tuple(w))
    return out

def solve_dual(U,targets,q):
    for b in product(range(q),repeat=3):
        if all(dot(u,b,q)==t for u,t in zip(U,targets)):
            return b
    raise RuntimeError('missing solution')

def family(q):
    allspaces={};strata=Counter()
    for r in range(4):
        for U in subspaces(3,r,q):
            K=nullspace(U,3,q)
            for coeff in product(range(q),repeat=r*(r-1)//2):
                B=[[0]*r for _ in range(r)];i=0
                for a in range(r):
                    for b in range(a+1,r):
                        B[a][b]=coeff[i];B[b][a]=-coeff[i]%q;i+=1
                bs=[solve_dual(U,[B[j][i] for j in range(r)],q) for i in range(r)]
                W=[tuple(u)+tuple(b)+(0,) for u,b in zip(U,bs)]
                W += [(0,0,0)+tuple(b)+(0,) for b in K]
                W += [(0,0,0,0,0,0,1)]
                canonical=rref(W,q)
                assert len(canonical)==4
                assert canonical not in allspaces
                for x in W:
                    assert dot(x[:3],x[3:6],q)==0
                for x,y in combinations(W,2):
                    assert (dot(x[:3],y[3:6],q)+dot(y[:3],x[3:6],q))%q==0
                products=[(0,0,0)+cross(x[:3],y[:3],q)+(0,) for x,y in combinations(W,2)]
                closed=all(rank(W+[p],q)==4 for p in products)
                assert closed==(r<=2)
                assert rank(products,q)==(0 if r<=1 else (1 if r==2 else 3))
                allspaces[canonical]=r;strata[(r,closed)]+=1
    v=q*q+q+1; total=2*(q**3+q*q+q+1)
    assert len(allspaces)==total,(q,len(allspaces),total)
    assert strata=={(0,True):1,(1,True):v,(2,True):q*v,(3,False):q**3}
    W=list(allspaces);counts=Counter();deg=Counter();
    for i,j in combinations(range(len(W)),2):
        x,y=W[i],W[j]
        intr=8-rank(list(x)+list(y),q)
        assert intr in (1,2,3)
        a,b=allspaces[x]%2,allspaces[y]%2
        assert (intr==2)==(a==b)
        counts[intr]+=1
        if intr==3:deg[i]+=1;deg[j]+=1
    assert all(deg[i]==v for i in range(len(W)))
    expected={2:2*total//2*(total//2-1)//2,3:(total//2)*v,1:(total//2)*(total//2-v)}
    assert counts==expected,(counts,expected)
    print('parameter enumeration',q,'strata',dict(strata),'maximal spaces',len(W),'pairs',dict(counts),'degree',v)
    return set(W)

def independent_exhaustion(q,target):
    # All 3-dimensional subspaces of hyperbolic F_q^6, independently of the U/beta parameterization
    num=0;singular=set();N=0
    for rows in subspaces(6,3,q):
        N+=1
        if all(dot(x[:3],x[3:],q)==0 for x in rows) and all((dot(x[:3],y[3:],q)+dot(y[:3],x[3:],q))%q==0 for x,y in combinations(rows,2)):
            singular.add(rref([r+(0,) for r in rows]+[(0,0,0,0,0,0,1)],q))
    assert singular==target
    print('independent exhaustive isotropic Grassmannian',q,'candidate 3-spaces',N,'singular 3-spaces',len(singular),'PASS')

if __name__=='__main__':
    a=family(3)
    independent_exhaustion(3,a)
    family(5)
    print('ALL CHECKS PASS')
