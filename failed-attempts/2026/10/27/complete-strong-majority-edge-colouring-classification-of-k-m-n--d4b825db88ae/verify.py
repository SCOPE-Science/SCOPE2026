#!/usr/bin/env python3
"""Verify explicit strong-majority edge colourings of complete bipartite graphs.
Scientific definitions and exhaustive finite checks only.
"""
from itertools import product
from math import comb

K44 = [[0,1,0,0],[2,2,0,1],[0,1,1,2],[2,2,1,0]]
K45 = [[3,3,2,3,0],[2,0,1,2,1],[3,0,1,1,2],[1,3,1,2,0]]
K47 = [[2,1,1,2,2,0,0],[0,1,2,0,2,1,1],[1,0,0,1,0,2,2],[2,0,0,2,0,1,1]]

def admissible(a):
    m, n = len(a), len(a[0]); bound = (m+n-2)//2
    for i in range(m):
        for j in range(n):
            neighbours = [a[i][v] for v in range(n) if v != j] + [a[u][j] for u in range(m) if u != i]
            if any(neighbours.count(c) > bound for c in set(neighbours)):
                return False
    return True

def cyclic(m,n):
    return [[(i+j)%3 for j in range(n)] for i in range(m)]

def k2n(n):
    # Every column is monochromatic, with color groups as equal as possible.
    return [[j%3 for j in range(n)] for _ in range(2)]

def test_all():
    for m in range(2,16):
        for n in range(m,24):
            if m==2:
                if n%2==0:
                    # Two balanced column groups.
                    a = [[j%2 for j in range(n)] for _ in range(2)]
                else:
                    a = k2n(n)
            elif (m,n)==(3,4):
                a = [[j for j in range(4)] for _ in range(3)]
            elif (m,n)==(4,4): a=K44
            elif (m,n)==(4,5): a=K45
            elif (m,n)==(4,7): a=K47
            else: a=cyclic(m,n)
            assert admissible(a), ('construction fails',m,n,a)
            if m==2 and n%2==0: assert len(set(sum(a,[])))==2
            if (m,n) in ((3,4),(4,5)): assert len(set(sum(a,[])))==4
            if (m,n) not in ((3,4),(4,5)) and (m!=2 or n%2!=0): assert len(set(sum(a,[])))==3
    assert admissible(K44) and admissible(K45) and admissible(K47)
    # Exhaustive canonical K_{3,4} three-colour obstruction (independent of literature proof).
    count=0
    for first in ((0,0,1,1),(0,0,1,2)):
        for second in product(range(3),repeat=4):
            for third in product(range(3),repeat=4):
                count+=1
                assert not admissible((first,second,third))
    assert count==2*3**8
    # Exhaustive row-mask check for individual admissible single-colour classes in K_{4,5}.
    best=0; topcount=0
    for rows in product(range(32),repeat=4):
        rd=[r.bit_count() for r in rows]
        if sum(rd)<best: continue
        cd=[sum((row>>j)&1 for row in rows) for j in range(5)]
        valid=all(rd[i]+cd[j] <= (5 if rows[i]>>j&1 else 3) for i in range(4) for j in range(5))
        if valid:
            sz=sum(rd)
            if sz>best:best=sz;topcount=1
            elif sz==best:topcount+=1
    assert best==6,(best,topcount)
    print('K_{4,5} color-class maximum: 6')
    print('K_{3,4} exhaustive canonical 3-color matrices:',count,'none valid')
    print('Finite construction checks: 2<=m<=15, m<=n<=23, all passed')
    print('Exceptional named matrices: K_{4,4}, K_{4,5}, K_{4,7} pass')
    print('VERIFY_OK')

if __name__=='__main__': test_all()
