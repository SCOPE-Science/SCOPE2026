#!/usr/bin/env python3
"""Self-contained arithmetic and finite-model checks for the two-part parity-tournament theorem."""
from collections import defaultdict
from itertools import permutations, product
from math import comb


def cross(a,b, rowbits, colbits, c):
    return tuple(tuple(c ^ rowbits[i] ^ colbits[j] for j in range(b)) for i in range(a))


def all_matrices(a,b):
    return {cross(a,b, (0,)+x, y, 0) for x in product((0,1), repeat=a-1)
            for y in product((0,1), repeat=b)}


def valid(M):
    a,b=len(M),len(M[0])
    return all((M[i][j] ^ M[i][v] ^ M[u][j] ^ M[u][v]) == 0
               for i in range(a) for u in range(i+1,a)
               for j in range(b) for v in range(j+1,b))


def formula(M):
    a,b=len(M),len(M[0]); n=a+b
    p=[comb(n,j) for j in range(n+1)]
    d=sum(M[0])
    e=sum(M[i][0] for i in range(a))
    for j in (d,b-d,e,a-e):p[j]+=1
    return tuple(p)


def direct(M):
    a,b=len(M),len(M[0]); n=a+b
    p=[0]*(n+1)
    for v in product((0,1),repeat=n):p[sum(v)]+=1  # new class
    for v in product((0,1),repeat=b):
        if all((M[i][j]^M[i][h]^v[j]^v[h])==0
               for i in range(a) for j in range(b) for h in range(j+1,b)):
            p[sum(v)]+=1   # joins first class
    for v in product((0,1),repeat=a):
        if all((M[i][j]^M[h][j]^v[i]^v[h])==0
               for j in range(b) for i in range(a) for h in range(i+1,a)):
            p[sum(v)]+=1   # joins second class
    return tuple(p)


def canon(M):
    a,b=len(M),len(M[0]); cand=[]
    for rows in permutations(range(a)):
        for cols in permutations(range(b)):
            cand.append(tuple(M[rows[i]][cols[j]] for i in range(a) for j in range(b)))
            if a==b:
                cand.append(tuple(1-M[cols[j]][rows[i]] for i in range(a) for j in range(b)))
    return min(cand)


def matching_profiles(q):
    e=[]
    for i,coeff in enumerate(q):e.extend([i]*coeff)
    assert len(e)==4
    out=set()
    for (i,j),(k,l) in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]:
        if e[i]+e[j] and e[k]+e[l]:
            out.add(tuple(sorted((e[i]+e[j],e[k]+e[l]))))
    return out


def main():
    checked=0
    global_max=0
    for n in range(2,8):
        fibers=defaultdict(set)
        for a in range(1,n//2+1):
            b=n-a
            for M in all_matrices(a,b):
                assert valid(M)
                p=formula(M)
                assert p==direct(M),(a,b,M,p,direct(M))
                checked+=1
                fibers[p].add((a,b,canon(M)))
        largest=max(map(len,fibers.values()))
        global_max=max(global_max,largest)
        for p,structures in fibers.items():
            q=tuple(p[j]-comb(n,j) for j in range(n+1))
            profiles={s[:2] for s in structures}
            assert profiles==matching_profiles(q),(n,p,profiles,matching_profiles(q))
            assert len(structures)<=6
        print('n=',n,'types=',sum(map(len,fibers.values())), 'polynomials=',len(fibers),
              'largest_fiber=',largest,'max_profiles=',max(len({s[:2] for s in v}) for v in fibers.values()))
        if n==2:assert largest==1
        if n==3:assert largest==2
        if n==4:assert max(len({s[:2] for s in v}) for v in fibers.values())==2
        if n<=5:assert max(len({s[:2] for s in v}) for v in fibers.values())<3
        if n==6:
            target=tuple(comb(6,j)+(1 if j in (0,1,2,3) else 0) for j in range(7))
            assert len(fibers[target])==6
            assert {s[:2] for s in fibers[target]}=={(1,5),(2,4),(3,3)}
            print('sixfold_witness_polynomial=',target)
    assert global_max==6
    print('VERIFY_OK matrices_checked=',checked,'complete_orders=2..7')

if __name__=='__main__':main()
