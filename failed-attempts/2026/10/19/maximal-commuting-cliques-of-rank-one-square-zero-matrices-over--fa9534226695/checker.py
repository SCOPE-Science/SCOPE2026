"""Standalone exhaustive checks of rank-one square-zero commuting-clique formulas.

Run: python rank_one_clique_checker.py
Requires only the Python 3 standard library.
"""
from itertools import product
from math import factorial

def matmul(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def mat(u,phi,q):
    return tuple(x*y%q for x in u for y in phi)

def vectors(n,q):
    return list(product(range(q), repeat=n))

def normalized_lines(n,q):
    ans=[]
    for u in vectors(n,q):
        if not any(u):continue
        a=next(v for v in u if v)
        u=tuple(x*pow(a,-1,q)%q for x in u)
        if u not in ans:ans.append(u)
    return ans

def matrices(n,q):
    all_vec=vectors(n,q)
    return sorted({mat(u,phi,q) for u in normalized_lines(n,q) for phi in all_vec if any(phi) and sum(x*y for x,y in zip(u,phi))%q==0})

def rank(M,q):
    if not M:return 0
    T=[list(row) for row in M]
    nrow=len(T); ncol=len(T[0]); r=0
    for j in range(ncol):
        p=next((k for k in range(r,nrow) if T[k][j]%q),None)
        if p is None:continue
        T[r],T[p]=T[p],T[r]
        a=pow(T[r][j],-1,q)
        T[r]=[x*a%q for x in T[r]]
        for k in range(nrow):
            if k!=r:
                t=T[k][j]
                T[k]=[(x-t*y)%q for x,y in zip(T[k],T[r])]
        r+=1
        if r==nrow:break
    return r

def canonical_span(vecs,n,q):
    if not vecs:return frozenset({(0,)*n})
    basis=[]
    for coefs in product(range(q),repeat=len(vecs)):
        basis.append(tuple(sum(a*v[i] for a,v in zip(coefs,vecs))%q for i in range(n)))
    return frozenset(basis)

def all_subspaces(n,q):
    S={frozenset({(0,)*n})}
    zero=(0,)*n
    for v in vectors(n,q):
        if v==zero:continue
        prev=list(S)
        for old in prev:
            if v in old:continue
            new=frozenset(tuple((x[i]+a*v[i])%q for i in range(n)) for x in old for a in range(q))
            S.add(new)
    return S

def qbin(n,k,q):
    if k<0 or k>n:return 0
    num=1;den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(k-i)-1
    return num//den

def factfall(x,k):
    r=1
    for j in range(k):r*=x-j
    return r

def clique_formula(n,q,k):
    total=0
    for r in range(1,n):
        inner=sum((-1)**(r-j)*q**((r-j)*(r-j-1)//2)*qbin(r,j,q)*factfall(((q**j-1)//(q-1))*(q**(n-r)-1),k) for j in range(r+1))
        total+=qbin(n,r,q)*inner
    assert total%factorial(k)==0
    return total//factorial(k)

def maximal_cliques(neighbors):
    found=set()
    def bk(R,P,X):
        if not P and not X:
            found.add(frozenset(R));return
        union=P|X
        pivot=max(union,key=lambda u:len(P&neighbors[u])) if union else None
        candidates=sorted(P-neighbors[pivot]) if pivot is not None else sorted(P)
        for v in candidates:
            bk(R|{v},P&neighbors[v],X&neighbors[v])
            P.remove(v);X.add(v)
    bk(set(),set(neighbors),set())
    return found

def count_k_cliques(neighbors,k):
    def rec(P,remaining):
        if remaining==0:return 1
        total=0
        for v in sorted(P):
            P.remove(v)
            total+=rec(P&neighbors[v],remaining-1)
        return total
    return rec(set(neighbors),k)

def test(n,q):
    matrices_list=matrices(n,q)
    neighbors={i:set() for i in range(len(matrices_list))}
    for i,A in enumerate(matrices_list):
        assert matmul(A,A,n,q)==(0,)*(n*n)
        assert rank([A[j*n:(j+1)*n] for j in range(n)],q)==1
        for j in range(i):
            B=matrices_list[j]
            AB=matmul(A,B,n,q);BA=matmul(B,A,n,q)
            if AB==BA:
                assert AB==(0,)*(n*n)
                neighbors[i].add(j);neighbors[j].add(i)
    predicted=[]
    for w in all_subspaces(n,q):
        sz=len(w)
        r=0
        while sz>1:
            assert sz%q==0
            sz//=q;r+=1
        if not 0<r<n:continue
        curr=set()
        for j,A in enumerate(matrices_list):
            cols=[tuple(A[i*n+k] for i in range(n)) for k in range(n)]
            if all(v in w for v in cols) and all(sum(A[i*n+k]*u[k] for k in range(n))%q==0 for u in w for i in range(n)):
                curr.add(j)
        assert len(curr)==((q**r-1)//(q-1))*(q**(n-r)-1)
        predicted.append(frozenset(curr))
    actual=maximal_cliques(neighbors)
    assert actual==set(predicted),(n,q,len(actual),len(predicted),list(actual-set(predicted))[:2])
    max_clique=max(map(len,actual))
    for k in range(1,min(max_clique,4)+1):
        exact=count_k_cliques(neighbors,k)
        predicted_count=clique_formula(n,q,k)
        assert exact==predicted_count,(n,q,k,exact,predicted_count)
    assert len(actual)==sum(qbin(n,r,q) for r in range(1,n))
    print('PASSED',n,q,'vertices',len(matrices_list),'maximal',len(actual),'maximum',max_clique)

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(3,2),(3,3),(4,2)]:test(n,q)
    print('ALL_EXACT_CHECKS_PASSED')
