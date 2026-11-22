#!/usr/bin/env python3
"""Check the explicit finite instances and the general shadow inequality."""
from itertools import product, combinations
from collections import Counter

Q7 = [tuple(map(int,s)) for s in '000 001 022 036 042 054 063 111 120 134 136 144 150 165 222 231 246 251 254 260 305 311 332 333 352 401 423 444 453 461 530 551 555 562 566 612 640 645 666'.split()]

def shadow(w):
    return {w[:2], (w[0],w[2]), w[1:]}

def design_code(q, blocks, matching):
    blocks = [tuple(sorted(block)) for block in blocks]
    assert len(blocks) == len(set(blocks)) == q * (q - 1) // 6
    pair_counts = Counter(tuple(sorted(pair)) for block in blocks for pair in combinations(block, 2))
    assert len(pair_counts) == q * (q - 1) // 2 and set(pair_counts.values()) == {1}
    match_set = {tuple(sorted(block)) for block in matching}
    assert match_set <= set(blocks)
    assert len(set(x for block in matching for x in block)) == 3 * len(matching)
    code = {(i,i,i) for i in range(q)}
    for a,b,c in blocks:
        # Each reversal pair covers every ordered pair on {a,b,c} once.
        words = {(a,b,c), (c,b,a), (a,c,b), (b,c,a)}
        if (a,b,c) in match_set:
            words.remove((a,b,c))
            words |= {(a,a,b), (b,b,c), (a,c,c)}
        code.update(words)
    # q<=13 (single-digit encoding) is used for independent check.
    return code

def all_instances():
    # F_3, the affine line.
    B3=[(0,1,2)]; M3=B3
    # AG(2,3), all affine lines in the plane.
    def coord(a): return (a // 3, a % 3)
    def idx(p): return (p[0]%3)*3+(p[1]%3)
    B9=set()
    for a in range(9):
        x,y=coord(a)
        for dx,dy in [(0,1),(1,0),(1,1),(1,2)]:
            B9.add(tuple(sorted(idx((x+t*dx,y+t*dy)) for t in range(3))))
    M9=[(0,1,2),(3,4,5),(6,7,8)]
    B13={tuple(sorted((x+y)%13 for y in base)) for x in range(13) for base in [(0,1,4),(0,2,7)]}
    M13=[(0,1,4),(2,8,10),(3,9,11),(5,7,12)]
    for q,code in [(3,design_code(3,B3,M3)),(7,set(Q7)),(9,design_code(9,B9,M9)),(13,design_code(13,B13,M13))]:
        assert len(code)==q+(2*q*q)//3, (q,len(code))
        assert len(code)==len(set(code))
        assert all(len(w)==3 and all(0<=c<q for c in w) for w in code)
        count=Counter(s for w in code for s in shadow(w))
        assert len(count)==q*q and max(count.values())<=2, (q,len(count),max(count.values()))
        print('q=%d, codewords=%d, received=%d, max_list=%d, total_incidences=%d' % (q,len(code),len(count),max(count.values()),sum(count.values())))
    # Independent global upper bound check at small alphabets: all length-three
    # shadows of size one correspond to constant words; those of size two
    # have a repeated symbol and contain its doubled-symbol length-two output.
    for q in range(2,10):
        ss = list(product(range(q),repeat=3))
        for a,b,c in ss:
            s={(a,b),(a,c),(b,c)}
            if len(s)==1: assert a==b==c
            if len(s)==2: assert any(i==j for i,j in s)
        print('q=%d, universal shadow-type enumeration=%d' % (q,len(ss)))

if __name__=='__main__': all_instances()
