#!/usr/bin/env python3
"""Exact finite checks for dihedral actions on cycle Boolean cell complexes.

Only standard-library Python is required. Computes cells from injective words,
incidence maps, and signed actions without using the transfer-matrix formulas.
"""
import itertools
import math
from collections import defaultdict


def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a


def path_partition(n):
    a,b=1,0
    for _ in range(n):a,b=a+b,-a-2*b
    return a+b


def key_of_word(n,word):
    loc={v:i for i,v in enumerate(word)}
    support=sum(1<<v for v in word)
    # Store directed edges, not binary orientation codes, so this model is
    # independent of an arbitrarily chosen global orientation of the cycle.
    ed=frozenset((a,b) if loc[a]<loc[b] else (b,a)
        for a in range(n) for b in [(a+1)%n]
        if a in loc and b in loc)
    return (support,ed)


def cells(n):
    faces={}
    for k in range(1,n+1):
        for word in itertools.permutations(range(n),k):
            key=key_of_word(n,word)
            if key not in faces:faces[key]=word
    bydim=defaultdict(list)
    for key in faces:bydim[key[0].bit_count()-1].append(key)
    return faces,bydim


def sign_perm(vals):
    return -1 if sum(vals[i]>vals[j] for i in range(len(vals))
                for j in range(i+1,len(vals)))%2 else 1


def act(n,g,key):
    mask,es=key
    support=[v for v in range(n) if mask>>v&1]
    newmask=sum(1<<g[v] for v in support)
    return (newmask,frozenset((g[a],g[b]) for a,b in es)), sign_perm([g[v] for v in support])


def boundary(n,faces,key):
    word=faces[key]
    # Independent of representative, and signs refer to sorted cell vertices.
    support=sorted(word)
    d=defaultdict(int)
    for j,v in enumerate(support):
        if len(word)>1:
            sub=tuple(x for x in word if x!=v)
            d[key_of_word(n,sub)]+=(-1)**j
    return {k:v for k,v in d.items() if v}


def check_d2(n,faces,bydim):
    for dim in range(2,n):
        for key in bydim[dim]:
            comp=defaultdict(int)
            for face,c in boundary(n,faces,key).items():
                for sub,d in boundary(n,faces,face).items():comp[sub]+=c*d
            assert all(z==0 for z in comp.values()),(n,dim,key)


def check_equivariance(n,faces,bydim,g):
    for dim in range(1,n):
        for key in bydim[dim]:
            img,sgn=act(n,g,key)
            lhs={x:sgn*c for x,c in boundary(n,faces,img).items()}
            rhs=defaultdict(int)
            for face,c in boundary(n,faces,key).items():
                target,s=act(n,g,face)
                rhs[target]+=c*s
            assert {k:v for k,v in lhs.items() if v}=={k:v for k,v in rhs.items() if v},(n,g,key)


def gf_rank(columns,pr=1000003):
    pivots={}
    for col in columns:
        x={r:(v%pr) for r,v in col.items() if v%pr}
        while x:
            r=min(x)
            if r not in pivots:
                inv=pow(x[r],-1,pr)
                pivots[r]={a:b*inv%pr for a,b in x.items()}
                break
            scalar=x[r]
            for rr,z in pivots[r].items():
                xx=(x.get(rr,0)-scalar*z)%pr
                if xx:x[rr]=xx
                else:x.pop(rr,None)
    return len(pivots)


def expected_rot(n,k):
    d=math.gcd(n,k)
    if d<=2:return (-1)**n
    return (-1)**(n-d)*(lucas(d)-2)


def expected_ref(n,a):
    if n%2:return -path_partition((n-1)//2)
    return path_partition(n//2+1) if a%2==0 else path_partition(n//2-2)


def signed_trace(n,bydim,g):
    tr=0
    for dim,arr in bydim.items():
        for key in arr:
            mapped,s=act(n,g,key)
            if mapped==key:tr+=(-1)**(n-1-dim)*s
    # alternating top homology character = signed trace on nonempty chains
    # plus the empty-cell reduced augmentation contribution.
    return tr+(-1)**n


def check(n):
    faces,bydim=cells(n)
    check_d2(n,faces,bydim)
    if n<=6:
        for k in (1,2):
            g=[(i+k)%n for i in range(n)]
            check_equivariance(n,faces,bydim,g)
        for a in (0,1):
            g=[(a-i)%n for i in range(n)]
            check_equivariance(n,faces,bydim,g)
    # Top rational homology is top-chain kernel because there is no upper chain.
    if n<=7:
        lower={k:i for i,k in enumerate(bydim[n-2])}
        cols=[{lower[face]:c for face,c in boundary(n,faces,key).items()}
              for key in bydim[n-1]]
        rank1=gf_rank(cols,1000003)
        rank2=gf_rank(cols,1000033)
        assert rank1==rank2
        betti=len(cols)-rank1
        assert betti==lucas(n)-2,(n,betti,rank1)
    chars=[]
    for k in range(n):
        g=[(i+k)%n for i in range(n)]
        tr=signed_trace(n,bydim,g)
        assert tr==expected_rot(n,k),(n,k,tr,expected_rot(n,k))
        chars.append(tr)
    refl=[]
    for a in range(n):
        g=[(a-i)%n for i in range(n)]
        tr=signed_trace(n,bydim,g)
        assert tr==expected_ref(n,a),(n,a,tr,expected_ref(n,a))
        refl.append(tr)
    inv=(sum(chars)+sum(refl))//(2*n)
    assert inv*(2*n)==sum(chars)+sum(refl)
    return f'n={n} cells={len(faces)} top={len(bydim[n-1])} rotations={chars} reflections={refl} full_invariants={inv}'

if __name__=='__main__':
    for n in range(3,9):print(check(n))
    print('BOOLEAN_CYCLE_DIHEDRAL_INTEGRAL_CELL_CHECK_PASS')
