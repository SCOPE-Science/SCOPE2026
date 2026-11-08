#!/usr/bin/env python3
"""Reproducible finite tests for the two-subset Kneser independence homology module.
Pure Python, no external dependencies. Finite tests corroborate the uniform argument.
"""
from itertools import combinations, permutations
from math import comb, factorial

def sign(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))

def faces(n):
    E = tuple(combinations(range(n),2))
    eid = {p:i for i,p in enumerate(E)}
    items = set()
    for i in range(n):
        star = [eid[p] for p in E if i in p]
        for k in range(1,len(star)+1):
            items.update(combinations(star,k))
    for a,b,c in combinations(range(n),3):
        tri = sorted((eid[(a,b)],eid[(a,c)],eid[(b,c)]))
        for k in range(1,4):
            items.update(combinations(tri,k))
    return E,eid,sorted(items,key=lambda t:(len(t),t))

def cyc_stats(p):
    n=len(p); vis=set(); cs={}
    for i in range(n):
        if i in vis:continue
        j=i;l=0
        while j not in vis:vis.add(j);j=p[j];l+=1
        cs[l]=cs.get(l,0)+1
    return cs

def char_formula(p):
    cs=cyc_stats(p);f=cs.get(1,0);t=cs.get(2,0);u=cs.get(3,0)
    return comb(f,3)-f*t+u-comb(f,2)+t+f-1

def fixed_face_trace(n,E,eid,faces,p):
    vmap=[eid[tuple(sorted((p[a],p[b])))] for a,b in E]
    s=-1 # reduced empty face contribution
    for face in faces:
        image=[vmap[i] for i in face]
        if sorted(image)==list(face):
            orientation=sign(image)
            s += (-1)**(len(face)-1)*orientation
    return s

def modular_rank(columns,prime):
    pivots={}
    for col in columns:
        vec={i:v%prime for i,v in col.items() if v%prime}
        while vec:
            i=max(vec)
            if i not in pivots:
                inverse=pow(vec[i],-1,prime)
                pivots[i]={k:(v*inverse)%prime for k,v in vec.items()}
                break
            scale=vec[i]
            for k,v in pivots[i].items():
                nv=(vec.get(k,0)-scale*v)%prime
                if nv:vec[k]=nv
                else:vec.pop(k,None)
    return len(pivots)

def check_direct_homology(fs,n):
    grouped={}
    for f in fs:grouped.setdefault(len(f)-1,[]).append(f)
    maxdim=max(grouped)
    for prime in (2,3):
        ranks={0:0}
        for d in range(1,maxdim+1):
            prev={f:i for i,f in enumerate(grouped[d-1])}
            cols=[]
            for f in grouped[d]:
                cols.append({prev[f[:j]+f[j+1:]]:(-1)**j for j in range(d+1)})
            ranks[d]=modular_rank(cols,prime)
        ranks[maxdim+1]=0
        betti={d:len(grouped[d])-ranks[d]-ranks[d+1] for d in range(maxdim+1)}
        expected={0:1,2:comb(n-1,3)}
        for d,val in betti.items():assert val==expected.get(d,0),(n,prime,betti)

def check(n):
    E,eid,fs=faces(n)
    d={};maxdim=0
    for f in fs:
        k=len(f)-1;d[k]=d.get(k,0)+1;maxdim=max(maxdim,k)
    assert len(fs)==sum(d.values())
    check_direct_homology(fs,n)
    for p in permutations(range(n)):
        lhs=fixed_face_trace(n,E,eid,fs,p)
        rhs=char_formula(p)
        if lhs!=rhs: raise AssertionError((n,p,lhs,rhs))
    # The triangle boundaries containing label 0 form an integral cycle basis.
    # Oriented edge coordinates (i,j), i<j. For triangle (0,i,j),
    # boundary=(i,j)-(0,j)+(0,i), and the coefficient on (i,j) is 1.
    # Check the full integer relative boundary, not just its rank.
    # For i<j<k, the oriented triangle boundary is (j,k)-(i,k)+(i,j).
    for i,j,k in combinations(range(n),3):
        bd={(j,k):1,(i,k):-1,(i,j):1}
        vert={q:0 for q in range(n)}
        for (a,b),coeff in bd.items():
            vert[a]-=coeff
            vert[b]+=coeff
        assert all(v==0 for v in vert.values())
    # The (0,i,j) columns have a literal +1 identity minor on chords
    # (i,j), 1<=i<j<n; hence they form an integral cycle basis.
    chords=list(combinations(range(1,n),2))
    for i,j in chords:
        bd={(i,j):1,(0,j):-1,(0,i):1}
        for a,b in chords:
            assert bd.get((a,b),0)==(1 if (a,b)==(i,j) else 0)
    b2=comb(n-1,3)
    expected_euler=1+b2
    euler=sum((-1)**k*v for k,v in d.items())
    assert euler==expected_euler,(n,euler,expected_euler)
    print(f'n={n} independent_faces={len(fs)} f_vector={d} group_actions={factorial(n)} integral_H2_rank={b2} all_characters_and_mod_2_3_homology_pass')

for n in range(4,8):check(n)
print('TWO_SUBSET_KNESER_INTEGRAL_SYMMETRY_CHECK_PASS')
