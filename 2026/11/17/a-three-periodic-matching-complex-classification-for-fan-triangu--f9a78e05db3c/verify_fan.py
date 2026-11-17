#!/usr/bin/env python3
"""Independent small-case boundary ranks and exact counting checks for a fan graph theorem.
No nonstandard Python packages are needed. All arithmetic is integral or in F_2.
"""
from collections import defaultdict

def predicted(n):
    q, r = divmod(n, 3)
    if r == 0:
        return {q - 1: q + 1}
    if r == 1:
        return {q: q}
    return {q: 2 * q + 2}

def fan_edges(n):
    return [(i, i + 1) for i in range(1, n)] + [(0, i) for i in range(1, n + 1)]

def all_matchings(edges):
    by = defaultdict(list)
    def visit(j,used,chosen):
        if j == len(edges):
            if chosen: by[chosen.bit_count()-1].append(chosen)
            return
        visit(j+1,used,chosen)
        a,b=edges[j]
        if not (used & ((1<<a)|(1<<b))):
            visit(j+1,used|(1<<a)|(1<<b),chosen|(1<<j))
    visit(0,0,0)
    return by

def rank_gf2(vectors):
    pivots={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k not in pivots:
                pivots[k]=v
                break
            v ^= pivots[k]
    return len(pivots)

def reduced_betti(edges):
    faces=all_matchings(edges)
    ranks={0:1 if faces.get(0) else 0}  # augmented d_0: each vertex goes to the empty simplex
    for k in range(1,max(faces)+1):
        row_index={f:j for j,f in enumerate(faces[k-1])}
        columns=[]
        for f in faces[k]:
            v=0; t=f
            while t:
                bit=t & -t
                v ^= 1 << row_index[f ^ bit]
                t-=bit
            columns.append(v)
        ranks[k]=rank_gf2(columns)
    return {k:len(s)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,s in faces.items() if len(s)-ranks.get(k,0)-ranks.get(k+1,0)}, sum(len(s) for s in faces.values())

def path_matching_number_at_minus_one(m):
    # P_m has m vertices. Matchings satisfy J_m=J_{m-1}-J_{m-2} at activity -1.
    if m in (0,1): return 1
    a=b=1
    for j in range(2,m+1):
        a,b=b,b-a
    return b

def signed_euler_fan(n):
    # Empty face contributes 1 to the independence polynomial at -1.
    return path_matching_number_at_minus_one(n)-sum(
        path_matching_number_at_minus_one(i-1)*path_matching_number_at_minus_one(n-i)
        for i in range(1,n+1))

def check():
    tested=0; total=0
    for n in range(3,19):
        got, nonempty_faces = reduced_betti(fan_edges(n))
        want=predicted(n)
        assert got == want,(n,got,want)
        assert -signed_euler_fan(n) == sum(((-1)**k)*v for k,v in got.items())
        tested+=1;total+=nonempty_faces
        print(f'n={n:2d} nonempty_faces={nonempty_faces:6d} mod2_reduced_betti={got}')
    for n in range(3,301):
        want=predicted(n)
        assert -signed_euler_fan(n)==sum(((-1)**k)*v for k,v in want.items()),n
        # Exactly the spokes with noncontractible links match the residue count.
        count=sum((i-1)%3!=2 and (n-i)%3!=2 for i in range(1,n+1))
        q,r=divmod(n,3)
        assert count==({0:q,1:q+1,2:2*q+2}[r]),(n,count)
    print(f'CHECK_OK: {tested} complete mod-two boundary complexes, {total} nonempty simplices, 298 exact signed-Euler/link-count parameter checks')

if __name__=='__main__':check()
