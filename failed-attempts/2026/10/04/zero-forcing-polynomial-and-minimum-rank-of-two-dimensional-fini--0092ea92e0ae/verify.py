#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def gf_elements(q):
    if q in (2,3,5):
        return list(range(q))
    if q==4:
        return list(range(4))
    raise ValueError

def add(a,b,q):
    if q in (2,3,5):
        return (a+b)%q
    if q==4:
        return a^b
    raise ValueError

def mul(a,b,q):
    if q in (2,3,5):
        return (a*b)%q
    if q==4:
        # GF(4)=F2[w]/(w^2+w+1), bits encode a+bw.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)          # w^2=w+1 contributes 1
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)
    raise ValueError

def dot(x,y,q):
    return add(mul(x[0],y[0],q),mul(x[1],y[1],q),q)

def graph(q):
    E=gf_elements(q)
    V=[(a,b) for a in E for b in E if (a,b)!=(0,0)]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if dot(x,V[j],q)==0:
                N[i].add(j);N[j].add(i)
    return V,N

def comps(N):
    seen=set(); out=[]
    for v in range(len(N)):
        if v in seen: continue
        st=[v];seen.add(v);C=[]
        while st:
            x=st.pop();C.append(x)
            for y in N[x]:
                if y not in seen:
                    seen.add(y);st.append(y)
        out.append(C)
    return out

def zero_forces(C,N):
    blue=set(C)
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W)); break
        if move is None:
            return len(blue)==len(N)
        blue.add(move)

def polynomial(N):
    n=len(N); d={}
    for k in range(n+1):
        c=0
        for C in combinations(range(n),k):
            if zero_forces(C,N): c+=1
        if c:d[k]=c
    return d

def predicted(q):
    if q==2:
        return {2:2,3:1}
    s=q-1
    a=(q+1)*(q-2)
    # expand u^a (u+s)^(q+1)
    from math import comb
    return {a+j:comb(q+1,j)*(s**(q+1-j)) for j in range(q+2)}

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0;c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1;continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

def rank_witness(N):
    C=comps(N); n=len(N)
    A=[[0]*n for _ in range(n)]
    expected=0
    for comp in C:
        m=len(comp)
        # classify clique or balanced biclique.
        is_clique=all((j in N[i]) for a,i in enumerate(comp) for j in comp[a+1:])
        if is_clique:
            if m==1:
                continue
            expected+=1
            for i in comp:
                for j in comp:
                    A[i][j]=1
        else:
            # infer bipartition by nonneighbors inside component.
            root=comp[0]
            left={root}|({x for x in comp if x!=root and x not in N[root]})
            right=set(comp)-left
            assert len(left)==len(right)
            assert all((j in N[i]) for i in left for j in right)
            assert all((j not in N[i]) for i in left for j in left if i!=j)
            assert all((j not in N[i]) for i in right for j in right if i!=j)
            if len(left)==1:
                expected+=1
                i=next(iter(left));j=next(iter(right))
                A[i][i]=A[j][j]=1;A[i][j]=A[j][i]=1
            else:
                expected+=2
                for i in left:
                    for j in right:
                        A[i][j]=A[j][i]=1
    for i in range(n):
        for j in range(i+1,n):
            assert ((A[i][j]!=0)==(j in N[i]))
    assert rank_fraction(A)==expected
    return expected

for q in (2,3,4,5):
    V,N=graph(q)
    cs=comps(N)
    sizes=sorted(len(c) for c in cs)
    s=q-1
    if q==2:
        assert sizes==[1,2]
        expected_mr=1
    else:
        assert all(m in (s,2*s) for m in sizes)
        # Each clique contributes one projective line, each biclique two.
        assert sum(1 if m==s else 2 for m in sizes)==q+1
        expected_mr=q+1
    mr=rank_witness(N)
    assert mr==expected_mr
    if len(V)<=15:
        brute=polynomial(N)
        assert brute==predicted(q),(q,brute,predicted(q))
        print(f"q={q}: |V|={len(V)}, components={sizes}, polynomial={brute}, witness_rank={mr}")
    else:
        print(f"q={q}: |V|={len(V)}, components={sizes}, predicted_polynomial={predicted(q)}, witness_rank={mr}")

print("VERIFY_OK")
