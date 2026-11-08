#!/usr/bin/env python3
"""Reproduce integral homology and rational symmetry characters of a six-vertex cyclic digraph multipath complex. Stdlib only."""
from collections import Counter
from itertools import product
from hashlib import sha256

P=1009
VERTICES=range(6)
ARCS=tuple((u,v) for u in VERTICES for v in VERTICES if v//2==(u//2+1)%3)
N=len(ARCS)
assert N==12

def valid_walk(mask):
    in_d=[0]*6;out_d=[0]*6;succ={}
    for i,(u,v) in enumerate(ARCS):
        if mask>>i&1:
            in_d[v]+=1;out_d[u]+=1;succ[u]=v
            if in_d[v]>1 or out_d[u]>1:return False
    for u in succ:
        seen=set();v=u
        while v in succ:
            if v in seen:return False
            seen.add(v);v=succ[v]
    return True

def valid_forest(mask):
    inn=[0]*6;out=[0]*6;root=list(range(6))
    def rep(x):
        while root[x]!=x:x=root[x]
        return x
    for i,(u,v) in enumerate(ARCS):
        if not(mask>>i&1):continue
        inn[v]+=1;out[u]+=1
        if inn[v]>1 or out[u]>1:return False
        a,b=rep(u),rep(v)
        if a==b:return False
        root[a]=b
    return True

F={s for s in range(1,1<<N) if valid_walk(s)}
assert all(valid_walk(s)==valid_forest(s) for s in range(1<<N))
assert len(F)==278
L={k:sorted(f for f in F if f.bit_count()==k+1) for k in range(5)}
assert [len(L[k]) for k in range(5)]==[12,54,104,84,24]
assert sum((-1)**k*len(L[k]) for k in L)==2
facets=[s for s in F if not any(s!=t and s&t==s for t in F)]
assert Counter(s.bit_count() for s in facets)=={4:24,5:24}

# Simplicial oriented boundary: signed coefficients indexed by deleted arc position.
I={k:{f:i for i,f in enumerate(L[k])} for k in L}
D={}
for k in range(1,5):
    D[k]=[]
    for s in L[k]:
        bits=[i for i in range(N) if s>>i&1]
        D[k].append({I[k-1][s^(1<<bit)]:(-1)**j for j,bit in enumerate(bits)})
for k in range(2,5):
    for col in D[k]:
        z={}
        for row,v in col.items():
            for t,w in D[k-1][row].items():z[t]=z.get(t,0)+v*w
        assert not any(z.values())

# Integral elementary chain cancellations: a unit pivot gives an integral chain-homotopy equivalence.
def chain_cancel(order):
    B={k:{(r,c):val for c,vec in enumerate(D[k]) for r,val in vec.items()} for k in range(1,5)}
    bases={k:set(range(len(L[k]))) for k in L};counts=Counter()
    for k in (4,3,2,1):
        M=B[k]
        while True:
            units=[key for key,val in M.items() if abs(val)==1]
            if not units:break
            a,b=(min(units) if order=='forward' else max(units));unit=M[a,b]
            cv={r:v for (r,c),v in M.items() if c==b and r!=a}
            rv={c:v for (r,c),v in M.items() if r==a and c!=b}
            for r,x in cv.items():
                for c,y in rv.items():
                    new=M.get((r,c),0)-unit*x*y
                    if new:M[r,c]=new
                    else:M.pop((r,c),None)
            for key in list(M):
                if key[0]==a or key[1]==b:del M[key]
            bases[k].remove(b);bases[k-1].remove(a);counts[k]+=1
            if k>1:
                for key in list(B[k-1]):
                    if key[1]==a:del B[k-1][key]
            if k<4:
                for key in list(B[k+1]):
                    if key[0]==b:del B[k+1][key]
        assert not M
    assert all(not M for M in B.values())
    rank=[len(bases[k]) for k in range(5)]
    assert rank==[1,0,1,4,4]
    assert [counts[k] for k in (1,2,3,4)]==[11,43,60,20]
    return counts,rank
for direction in ('forward','reverse'):chain_cancel(direction)

# A natural ambient complex without the directed-cycle exclusion is the join of three chessboard complexes M(K_{2,2}).
def degree_only(mask):
    ins=[0]*6;outs=[0]*6
    for i,(u,v) in enumerate(ARCS):
        if mask>>i&1:
            ins[v]+=1;outs[u]+=1
            if ins[v]>1 or outs[u]>1:return False
    return True
Y={s for s in range(1,1<<N) if degree_only(s)}
assert F<=Y
# In each block, the two 0-sphere representatives lie in different connected components of M(K_2,2).
O=((0,1),(4,5),(11,9))
for pair in O:
    a,b=pair
    assert ARCS[a][0]//2==ARCS[b][0]//2
    assert (ARCS[a][0]%2==ARCS[a][1]%2)!=(ARCS[b][0]%2==ARCS[b][1]%2)
for t in product(*O):
    assert sum(1<<a for a in t) in F
# Their join is an octahedral two-sphere, generating H_2(Y)=Z; hence the map H_2(F)->H_2(Y) is an isomorphism.

# Group G=(C2)^3 rtimes C3 acts by independent twin swaps and cyclic rotation of blocks.
E={e:i for i,e in enumerate(ARCS)}
GROUP=[]
for shift in range(3):
    for flips in product(range(2),repeat=3):
        vm={2*j+b:2*((j+shift)%3)+(b^flips[j]) for j in range(3) for b in range(2)}
        em=tuple(E[(vm[u],vm[v])] for u,v in ARCS)
        GROUP.append((shift,flips,em))
assert len(GROUP)==24 and len({q[2] for q in GROUP})==24

def sign_perm(A):
    return -1 if sum(A[i]>A[j] for i in range(len(A)) for j in range(i+1,len(A)))%2 else 1

def act_face(f,em):
    ff=[em[i] for i in range(N) if f>>i&1]
    return sum(1<<x for x in ff),sign_perm(ff)
for shift,flips,em in GROUP:
    assert all(act_face(f,em)[0] in F for f in F)

def pivcols(cols):
    seen={};keep=[]
    for j,vec in enumerate(cols):
        x={i:v%P for i,v in vec.items() if v%P}
        while x:
            i=min(x)
            if i in seen:
                c=x[i]
                for a,b in seen[i].items():
                    z=(x.get(a,0)-c*b)%P
                    if z:x[a]=z
                    else:x.pop(a,None)
            else:
                inv=pow(x[i],-1,P)
                seen[i]={a:b*inv%P for a,b in x.items()};keep.append(j);break
    return keep

def invert(A):
    n=len(A);X=[[v%P for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        ii=next(i for i in range(j,n) if X[i][j])
        X[ii],X[j]=X[j],X[ii]
        z=pow(X[j][j],-1,P);X[j]=[v*z%P for v in X[j]]
        for i in range(n):
            if i==j:continue
            z=X[i][j]
            if z:X[i]=[(a-z*b)%P for a,b in zip(X[i],X[j])]
    return [v[n:] for v in X]

BD={}
for k in range(1,5):
    ci=pivcols(D[k]);basis=[D[k][i] for i in ci]
    row_vectors=[{j:v.get(i,0) for j,v in enumerate(basis) if v.get(i,0)} for i in range(len(L[k-1]))]
    ri=pivcols(row_vectors)
    assert len(ci)==len(ri)==[0,11,43,60,20][k]
    left=invert([[c.get(i,0) for c in basis] for i in ri]);BD[k]=(ci,ri,left)

def image_trace(k,em):
    ci,ri,inv=BD[k];r=len(ci);out=0
    for j,col_idx in enumerate(ci):
        dst,sg=act_face(L[k][col_idx],em);col=D[k][I[k][dst]]
        out+=sum(inv[j][t]*sg*col.get(ri[t],0) for t in range(r))
    return out%P

def signed(a):
    a%=P
    return a if a<=P//2 else a-P

def permutation_4_character(shift,flips):
    if shift:return 1
    if flips==(0,0,0) or flips==(1,1,1):return 4
    return 0
TRACES=[]
for shift,flips,em in GROUP:
    trC=[sum(sign for f in L[k] for dst,sign in [act_face(f,em)] if dst==f) for k in range(5)]
    trB={k:image_trace(k,em) for k in range(1,5)}
    trH=tuple(signed(trC[k]-trB.get(k,0)-trB.get(k+1,0)) for k in range(5))
    q=permutation_4_character(shift,flips)
    epsilon=(-1)**sum(flips)
    assert trH==(1,0,1,q,q*epsilon),(shift,flips,trH)
    TRACES.append(trH)
assert [sum(t[k] for t in TRACES)//24 for k in (2,3,4)]==[1,1,0]
print('multipath faces (nonempty): 278; f-vector: (12,54,104,84,24)')
print('maximal facets: 24 tetrahedra and 24 four-simplices')
print('elementary integral cancellations in boundary degrees 1..4: (11,43,60,20)')
print('remaining integral boundary matrices: all zero')
print('reduced integral homology ranks in degrees 2,3,4: (1,4,4); all free')
print('embedded octahedral S2 generates ambient join H2')
print('group order 24; H2 trivial, H3 four-coset permutation, H4 parity twist')
print('rational invariant ranks in degrees 2,3,4: (1,1,0)')
print('CYCLIC_TRIPARTITE_MULTIPATH_INTEGRAL_CHARACTER_VERIFIED')
