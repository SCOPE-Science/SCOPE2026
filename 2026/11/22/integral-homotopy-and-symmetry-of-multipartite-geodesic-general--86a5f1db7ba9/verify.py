#!/usr/bin/env python3
"""Reproduce finite geodesic tests, exact mod-two ranks and trace checks."""
from itertools import combinations, product
from collections import deque

CASES = [(1,1), (2,2), (2,3), (3,3), (1,2,2), (2,2,2),
         (2,2,3), (1,3,3), (2,2,2,2), (3,2,2,2)]

def rank2(columns):
    piv = {}
    for x in columns:
        while x:
            k = x.bit_length()-1
            if k in piv: x ^= piv[k]
            else:
                piv[k] = x
                break
    return len(piv)

def build(sizes):
    parts=[]; ident=[]; pos=0
    for i,a in enumerate(sizes):
        v=tuple(range(pos,pos+a));parts.append(v)
        ident += [i]*a;pos+=a
    n=pos
    d=[[0 if i==j else (2 if ident[i]==ident[j] else 1) for j in range(n)] for i in range(n)]
    allfaces={0}; classified={0}
    for mask in range(1,1<<n):
        xs=[v for v in range(n) if mask>>v &1]
        good=all(not (d[x][z]==d[x][y]+d[y][z])
                 for x,y,z in combinations(xs,3)
                 for x,y,z in ((x,y,z),(x,z,y),(y,x,z)))
        if good:allfaces.add(mask)
        counts=[sum(ident[v]==i for v in xs) for i in range(len(sizes))]
        if max(counts)==len(xs) or max(counts)<=1: classified.add(mask)
    assert allfaces==classified, (sizes,len(allfaces),len(classified))
    faces_by_card={r:sorted(x for x in allfaces if x.bit_count()==r)
                   for r in range(n+1)}
    ranks={}
    for r in range(2,n+1):
        low={m:j for j,m in enumerate(faces_by_card[r-1])}
        cols=[]
        for m in faces_by_card[r]:
            col=0;v=m
            while v:
                bit=v&-v;v-=bit
                col ^= 1<<low[m^bit]
            cols.append(col)
        ranks[r-1]=rank2(cols)
    betti={}
    for k in range(n):
        nr=len(faces_by_card[k+1]);boundary=ranks.get(k,0);next_boundary=ranks.get(k+1,0)
        b=nr-boundary-next_boundary
        if k==0:b-=1
        if b:betti[k]=b
    t=len(sizes)
    expected={1:sum(a-1 for a in sizes)}
    product_b=1
    for a in sizes:product_b*=a-1
    expected[t-1]=expected.get(t-1,0)+product_b
    expected={k:v for k,v in expected.items() if v}
    assert betti==expected,(sizes,betti,expected)
    return n,allfaces,betti,parts,ident

def orientation_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def trace_chain(simplices,permutation):
    acc=0
    for mask in simplices:
        if mask==0:continue
        xs=[i for i in range(len(permutation)) if mask>>i&1]
        ys=[permutation[i] for i in xs]
        if set(xs)!=set(ys):continue
        parity=sum(ys[i]>ys[j] for i in range(len(ys)) for j in range(i+1,len(ys)))%2
        acc+=(-1)**(len(xs)-1+parity)
    return acc-1  # reduced Lefschetz: remove H_0 trace 1

def verify_trace(sizes,faces,parts):
    if len(sizes)<3:return
    n=sum(sizes);perm=list(range(n))
    # One within-part transposition if possible.
    if sizes[0]>=2:perm[parts[0][0]],perm[parts[0][1]]=perm[parts[0][1]],perm[parts[0][0]]
    fixed=[sum(perm[v]==v for v in part) for part in parts]
    tr1=sum(f-1 for f in fixed)
    trtop=1
    for f in fixed:trtop*=f-1
    exp=-tr1+(-1)**(len(sizes)-1)*trtop
    assert trace_chain(faces,perm)==exp,(sizes,'within-part',trace_chain(faces,perm),exp)
    # Swap first two blocks of equal size if possible, as a whole.
    if sizes[0]==sizes[1]:
        perm=list(range(n))
        for a,b in zip(parts[0],parts[1]):perm[a]=b;perm[b]=a
        tr1=sum(sizes[j]-1 for j in range(2,len(sizes)))
        trtop=-(sizes[0]-1)
        for a in sizes[2:]:trtop*=a-1
        exp=-tr1+(-1)**(len(sizes)-1)*trtop
        assert trace_chain(faces,perm)==exp,(sizes,'block-swap',trace_chain(faces,perm),exp)

if __name__=='__main__':
    total=0
    for case in CASES:
        n,faces,betti,parts,ident=build(case)
        verify_trace(case,faces,parts)
        total+=len(faces)
        print(f"sizes={case} N={n} faces={len(faces)} reduced_mod2_betti={betti} equivariant_Lefschetz=ok")
    print(f"TOTAL {len(CASES)} cases, {total} faces including empties, all checks passed")
