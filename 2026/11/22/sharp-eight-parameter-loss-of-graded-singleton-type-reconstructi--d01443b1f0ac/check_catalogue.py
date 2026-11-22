"""Exact validation of all displayed eight-point collision certificates."""
import json
from pathlib import Path

def fingerprint(g,n=8):
    a=[[0]*n for _ in range(n)]
    k=0
    for i in range(1,n):
        for j in range(i+1,n):
            a[i][j]=a[j][i]=(g>>k)&1
            k+=1
    p=[0]*(n*(n-1)//2+1)
    for s in range(1<<(n-1)):
        deg=s.bit_count()
        for i in range(1,n):
            for j in range(i+1,n):
                deg+=a[i][j]^((s>>(i-1))&1)^((s>>(j-1))&1)
        p[deg]+=1
    d=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i][j]^a[j][k]^a[i][k]:
                    d[i]+=1;d[j]+=1;d[k]+=1
    return [[k,c] for k,c in enumerate(p) if c], sorted(d)

rows=json.loads(Path('collision_catalogue.json').read_text(encoding='utf8'))['collision_groups']
assert len(rows)==21
assert sum(len(r['representative_masks'])==2 for r in rows)==18
assert sum(len(r['representative_masks'])==3 for r in rows)==3
pairs=set();distinct=set()
for row in rows:
    degrees=set()
    for g,d in zip(row['representative_masks'],row['sorted_coherent_triple_vertex_degrees']):
        p2,d2=fingerprint(g)
        assert p2==row['nonzero_coefficients'] and d2==d
        assert g not in distinct
        distinct.add(g);degrees.add(tuple(d))
    assert len(degrees)==len(row['representative_masks'])
    poly=tuple(tuple(v) for v in row['nonzero_coefficients'])
    assert poly not in pairs;pairs.add(poly)
assert len(distinct)==45
print('CATALOGUE_VERIFY_OK groups=21 representatives=45 pair_groups=18 triple_groups=3')
