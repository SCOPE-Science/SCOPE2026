"""Standalone finite verification of a signed homology basis for quadrilateral bouquets.

The universal argument is mathematical; these checks are independent finite corroboration.
"""
from itertools import combinations, product
from math import comb


def vertices(i):
    return (1 + 3*i, 2 + 3*i, 3 + 3*i)  # leaf, distal, leaf


def alpha_without_c(W, m):
    total = 0
    middle_count = 0
    for i in range(m):
        a, b, d = vertices(i)
        ends = ((W >> a) & 1) + ((W >> d) & 1)
        middle = (W >> b) & 1
        total += max(ends, middle)
        middle_count += middle
    return total, middle_count


def is_face(W, m, k):
    a, b = alpha_without_c(W, m)
    return a <= k-1 and (not (W & 1) or b <= k-2)


def star_faces(I, m):
    D = [vertices(i)[1] for i in I]
    E = [(vertices(i)[0], vertices(i)[2]) for i in I]
    ans = set()
    for ds in product((0, 1), repeat=len(I)):
        for es in product((0, 1, 2), repeat=len(I)):
            W = 0
            for j, keep in enumerate(ds):
                if keep: W |= 1 << D[j]
            for j, choice in enumerate(es):
                if choice: W |= 1 << E[j][choice-1]
            ans.add(W)
    return ans


def sign_permutation(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))) % 2 else 1


def top_cycle(I):
    D = [vertices(i)[1] for i in I]
    out = {}
    for eps in product((0,1),repeat=len(I)):
        L = [vertices(i)[0 if e==0 else 2] for i,e in zip(I,eps)]
        ordered = D+L
        canonical = tuple(sorted(ordered))
        out[canonical] = (-1)**sum(eps) * sign_permutation(ordered)
    return out


def apply_chain(chain, p):
    out={}
    for face, coeff in chain.items():
        img=[p[v] for v in face]
        ordered=tuple(sorted(img))
        out[ordered]=out.get(ordered,0)+coeff*sign_permutation(img)
    return {x:c for x,c in out.items() if c}


def generators(m):
    n=3*m+1
    idp=list(range(n))
    flips=[]
    for i in range(m):
        p=idp.copy(); a,_,d=vertices(i);p[a],p[d]=p[d],p[a]
        flips.append((f'flip_{i}',p,lambda I,i=i: I, lambda I,i=i: -1 if i in I else 1))
    p=idp.copy()
    if m>=2:
        for v,w in zip(vertices(0),vertices(1)):p[v],p[w]=p[w],p[v]
    trans=('swap_0_1',p,lambda I:tuple(sorted(1 if j==0 else 0 if j==1 else j for j in I)), lambda I:1)
    p=idp.copy()
    for i in range(m):
        for off,v in enumerate(vertices(i)):p[v]=vertices((i+1)%m)[off]
    rot=('rotate',p,lambda I:tuple(sorted((j+1)%m for j in I)),lambda I:1)
    return flips+[trans,rot]


def trace_by_faces(m,k,p):
    n=1+3*m
    trace=0
    for W in range(1<<n):
        if not is_face(W,m,k):continue
        face=[i for i in range(n) if (W>>i)&1]
        img=[p[v] for v in face]
        if sorted(img)!=face: continue
        trace+=(-1)**len(face)*sign_permutation(img)
    return trace


def trace_by_basis(m,k,p):
    r=k-1
    res=0
    for I in combinations(range(m),r):
        img=tuple(sorted((p[vertices(i)[1]]-2)//3 for i in I))
        if img!=I:continue
        flips=sum(p[vertices(i)[0]]==vertices((p[vertices(i)[1]]-2)//3)[2] for i in I)
        res+=(-1)**flips
    return res


def check(m,k):
    r=k-1
    X={W for W in range(1<<(3*m+1)) if not(W&1) and is_face(W,m,k)}
    L={W for W in X if is_face(W|1,m,k)}
    D={}
    for I in combinations(range(m),r):
        Z=star_faces(I,m)
        assert Z <= X
        middle_mask=sum(1<<vertices(i)[1] for i in I)
        assert {W for W in Z if W&middle_mask!=middle_mask}==Z&L
        for W in Z-L:
            assert W not in D,(m,k,W)
            D[W]=I
        cyc=top_cycle(I)
        bound={}
        for face,coef in cyc.items():
            for j in range(len(face)):
                face2=face[:j]+face[j+1:]
                W=sum(1<<v for v in face2)
                if W in L:continue
                bound[face2]=bound.get(face2,0)+(-1)**j*coef
        assert all(x==0 for x in bound.values()), (m,k,I,bound)
        for name,p,where,sgn in generators(m):
            transformed=apply_chain(cyc,p)
            target=top_cycle(where(I))
            assert transformed=={f:v*sgn(I) for f,v in target.items()},(m,k,I,name)
    assert set(D)==(X-L)
    traces=[]
    for name,p,_,_ in generators(m):
        first=trace_by_faces(m,k,p)
        second=trace_by_basis(m,k,p)
        assert first==second,(m,k,name,first,second)
        traces.append((name,first))
    assert len(list(combinations(range(m),r)))==comb(m,r)
    return len(X),len(L),len(D),traces


if __name__=='__main__':
    count=0
    for m in range(3,6):
        for k in range(4,m+2):
            nx,nl,nd,traces=check(m,k)
            print(f'm={m}, k={k}: deletion_faces={nx}, link_faces={nl}, relative_faces={nd}, generators={traces}')
            count+=1
    print(f'SIGNED_BOUQUET_INTEGRAL_MODULE_CHECK_PASS cases={count}')
