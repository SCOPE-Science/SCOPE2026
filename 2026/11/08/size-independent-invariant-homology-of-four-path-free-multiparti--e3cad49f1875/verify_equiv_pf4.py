#!/usr/bin/env python3
"""Exact face and signed-character checks for four-path-free multipartite complexes.

No external libraries are required.  Finite tests corroborate, but do not replace,
the general proof from the relative chain sequence.
"""
from itertools import combinations, permutations, product
from math import comb


def path4_on_support(s, part):
    for v in permutations(s,4):
        if all(part[v[j]] != part[v[j+1]] for j in range(3)):
            return True
    return False

def faces(parts):
    p = tuple(i for i,n in enumerate(parts) for _ in range(n))
    vs = range(len(p))
    return {r:[s for s in combinations(vs,r) if not path4_on_support(s,p)]
            for r in range(1,len(p)+1)}

def sign_perm(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def signed_euler_trace(fc,g):
    v = 0
    for r,fs in fc.items():
        for s in fs:
            gs = tuple(g[x] for x in s)
            if set(gs)==set(s):
                v += (-1)**(r-1)*sign_perm(gs)
    return v-1

def predicted(parts,g):
    off=0; fixes=[]
    for n in parts:
        fixes.append(sum(g[i]==i for i in range(off,off+n)))
        off+=n
    e2=sum(a*b for a,b in combinations(fixes,2))
    e3=sum(a*b*c for a,b,c in combinations(fixes,3))
    return e3+e2-(len(parts)-1)*(sum(fixes)-1)

def all_perms(parts):
    ranges=[];o=0
    for n in parts:
        ranges.append(list(range(o,o+n)));o+=n
    for tup in product(*(permutations(block) for block in ranges)):
        yield tuple(x for bl in tup for x in bl)

def main():
    count_cases=0;checks=0;maxfaces=0
    from itertools import product as iterprod
    for m in [3,4]:
        for parts in iterprod(range(1,4), repeat=m):
            if sum(parts)>8:continue
            count_cases+=1
            fc=faces(parts)
            maxfaces=max(maxfaces,sum(map(len,fc.values())))
            traces=[]
            for g in all_perms(parts):
                direct=signed_euler_trace(fc,g)
                formula=predicted(parts,g)
                assert direct==formula,(parts,g,direct,formula)
                checks+=1
                traces.append(direct)
            assert sum(traces)==len(traces)*comb(m-1,3),(parts,sum(traces),len(traces))
    print('multipartite part-size cases',count_cases)
    print('part-preserving automorphisms checked',checks)
    print('largest total number nonempty faces',maxfaces)
    print('sample PF4(2,2,2), identity trace',predicted((2,2,2),tuple(range(6))))
    print('all invariant dimensions equal binomial(part_count-1,3)')
    print('sample PF4(2,2,2), three swaps trace',predicted((2,2,2),(1,0,3,2,5,4)))
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
