"""verify.py — independent checker: given orbit reps, expand to 70 blocks,
check STS(21) axioms, sigma-invariance, fixed-point count, Pasch count,
Pasch-switch twin test placeholder. Reads FIRST solution rows when available."""
import sys
from itertools import combinations

def sig(x): return x^1 if x<18 else x

def expand(fix_rows, mix_rows, p3_rows):
    blocks=set()
    blocks.add((18,19,20))
    for (f,i) in fix_rows:
        a,b=2*i,2*i+1
        blocks.add(tuple(sorted((18+f,a,b))))
    for (F,x,y) in mix_rows:
        blocks.add(tuple(sorted((F,x,y))))
        blocks.add(tuple(sorted((sig(F),sig(x),sig(y)))))
    for (x,y,z) in p3_rows:
        blocks.add(tuple(sorted((x,y,z))))
        blocks.add(tuple(sorted((sig(x),sig(y),sig(z)))))
    return blocks

def check(blocks):
    assert len(blocks)==70, len(blocks)
    cov={}
    for b in blocks:
        for p in combinations(b,2):
            assert p not in cov, ("dup pair",p)
            cov[p]=b
    assert len(cov)==210
    # sigma invariance
    for b in blocks:
        assert tuple(sorted((sig(b[0]),sig(b[1]),sig(b[2])))) in blocks
    fixed=[b for b in blocks if tuple(sorted((sig(b[0]),sig(b[1]),sig(b[2]))))==b]
    print("fixed blocks:",len(fixed),fixed)
    # Pasch count
    bset=set(blocks)
    bl=list(blocks)
    n=len(bl)
    pasch=0; first=None
    for i in range(n):
        for j in range(i+1,n):
            if len(set(bl[i])&set(bl[j]))!=2: continue
            # opposite pair: remaining points
            a=tuple(sorted(set(bl[i])|set(bl[j])))
            if len(a)!=4: continue
            # find blocks on other two pairs
            import itertools
            rest=[tuple(sorted(p)) for p in combinations(a,2) if set(p)!=set(bl[i]) or True]
    # standard: Pasch = 4 blocks on 6 points, each pair of blocks shares 2... use K6 4-triple config
    # brute force over 6-sets? C(21,6)=54264, fine
    for s6 in combinations(range(21),6):
        s=set(s6)
        inside=[b for b in blocks if set(b)<=s]
        if len(inside)==4:
            # check it is a Pasch (opposite pair partition: union of any two = ... ) — 4 triples on 6 pts with each pair in exactly... verify pairwise intersections
            pasch+=1
            if first is None: first=(s6,inside)
    print("num Pasch:",pasch)
    if first: print("first Pasch 6-set:",first[0],"blocks:",first[1])
    return pasch

if __name__=="__main__":
    print("checker ready (no solution yet)")
