"""Exact finite verification of two-forbidden-triangle colored extension counts."""
from itertools import combinations, product
from collections import Counter
COL = ('R', 'G', 'B')

def valid_coloring(nodes, edges):
    for a,b,c in combinations(range(nodes),3):
        cs = (edges[a,b], edges[a,c], edges[b,c])
        if cs[0] == cs[1] == cs[2] and cs[0] != 'B':
            return False
    return True

def pattern_weight(r, edge_colors):
    """By direct enumeration, not the analytical pair-state formulas."""
    m = 2 + r
    edges = {}
    edges[0,1]='R'
    for i,j in combinations(range(r),2):
        edges[2+i,2+j]=edge_colors[i,j]
    free = [(a,b) for a in (0,1) for b in range(2,m)]
    count = 0
    for vals in product(COL, repeat=len(free)):
        for key,val in zip(free,vals):edges[key]=val
        if valid_coloring(m,edges):count+=1
    return count

def enumeration(r, m):
    old = 2*m
    n=old+r
    edges = {(2*j,2*j+1):'R' for j in range(m)}
    # Old edges crossing blocks are B.
    for i,j in combinations(range(old),2): edges.setdefault((i,j),'B')
    new_pairs=list(combinations(range(old,n),2))
    cross=[(i,j) for i in range(old) for j in range(old,n)]
    ans=Counter()
    for ics in product(COL, repeat=len(new_pairs)):
        for p,c in zip(new_pairs,ics):edges[p]=c
        if not valid_coloring(r,{(i,j):edges[old+i,old+j] for i,j in combinations(range(r),2)}):continue
        for v in product(COL,repeat=len(cross)):
            for p,c in zip(cross,v):edges[p]=c
            if valid_coloring(n,edges):ans[ics]+=1
    return ans

def run():
    assert pattern_weight(2,{(0,1):'R'})==56
    assert pattern_weight(2,{(0,1):'G'})==47
    assert pattern_weight(2,{(0,1):'B'})==64
    star={(0,1):'R',(0,2):'R',(1,2):'B'}
    assert pattern_weight(3,star)==400
    assert pattern_weight(3,{(0,1):'R',(0,2):'G',(1,2):'B'})==324
    assert pattern_weight(3,{(0,1):'G',(0,2):'G',(1,2):'B'})==301
    for r,m in [(2,1),(2,2),(3,1)]:
        got=enumeration(r,m)
        for colors, val in got.items():
            d=dict(zip(combinations(range(r),2),colors))
            assert val==pattern_weight(r,d)**m,(r,m,colors,val)
        assert len(got)==(3 if r==2 else 25)
        print('DIRECT_PROFILE_PASS',r,m,'profiles',len(got),'total',sum(got.values()))
    print('ALL_CHECKS_PASS')
if __name__=='__main__':run()
