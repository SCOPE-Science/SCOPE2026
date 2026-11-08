"""Separate labelled-matrix and direct-extinction-moment crosscheck.
Uses no results imported from the main certificate.
"""
from itertools import permutations
from collections import defaultdict

def col_transform(rows, perm):
    return tuple(sorted(sum((1<<perm[j]) for j in range(len(perm)) if row&(1<<j)) for row in rows))
def direct_signature(rows, m):
    n=len(rows); mask=(1<<m)-1
    table=[]
    for r in range(m+1):
        vals=[sum(bool(row&(mask^extinct)) for row in rows)
              for extinct in range(1<<m) if extinct.bit_count()==r]
        table.append((sum(vals),sum(y*y for y in vals),tuple(vals.count(k) for k in range(n+1))))
    moment=tuple((a,b) for a,b,_ in table)
    law=tuple(x for *_,x in table)
    return moment,law

def connected(rows,m):
    p=len(rows)
    found_p={0}; found_m=set()
    for _ in range(p+m+1):
        nm=found_m|{j for i in found_p for j in range(m) if rows[i]&(1<<j)}
        np=found_p|{i for j in nm for i in range(p) if rows[i]&(1<<j)}
        if (nm,np)==(found_m,found_p):break
        found_p,found_m=np,nm
    return len(found_p)==p and len(found_m)==m

def check(p,m,expected_classes,expected_pairs):
    permutations_m=list(permutations(range(m)))
    canons=set()
    for mask in range(1<<(p*m)):
        rows=tuple((mask>>(i*m))&((1<<m)-1) for i in range(p))
        if 0 in rows or not connected(rows,m):continue
        canons.add(min(col_transform(rows,pi) for pi in permutations_m))
    groups=defaultdict(list)
    for rows in sorted(canons):
        sig,law=direct_signature(rows,m)
        groups[sig].append((rows,law))
    twins=[]
    for members in groups.values():
        for i,(a,x) in enumerate(members):
            for b,y in members[i+1:]:
                if x!=y:twins.append((a,b))
    assert len(canons)==expected_classes,(p,m,len(canons))
    assert len(twins)==expected_pairs,(p,m,len(twins))
    print('independent full labelled census:',p,m,'classes',len(canons),'moment-twin pairs',len(twins))
    return twins
if __name__=='__main__':
    x=check(4,4,150,4)
    y=check(5,3,76,1)
    for pair in x+y:print(pair)
    print('PASS')
