#!/usr/bin/env python3
"""Independent finite checks of collinearity-plane atomic extension profiles.
All arithmetic is exact over the prime fields in this script.
"""
from itertools import combinations, product
from collections import defaultdict
import json

def affine(p):
    points=list(product(range(p), repeat=2))
    def C(a,b,c):
        return ((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))%p == 0
    return points,C

def projective(p):
    points=[]
    for x in product(range(p),repeat=3):
        if x==(0,0,0):continue
        j=next(i for i in range(3) if x[i])
        if x[j]!=1:continue
        points.append(x)
    def C(a,b,c):
        return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%p==0
    return points,C

def profile(points, collinear):
    n=len(points)
    # Precompute collinearity for three *distinct* indices.
    C={tuple(sorted((i,j,k))) for i,j,k in combinations(range(n),3) if collinear(points[i],points[j],points[k])}
    def typ(xs):
        # equality among positions, plus collinear flags of position triples
        m=len(xs)
        eq=tuple(xs[i]==xs[j] for i,j in combinations(range(m),2))
        triple=tuple(len({xs[i],xs[j],xs[k]})<3 or tuple(sorted((xs[i],xs[j],xs[k]))) in C for i,j,k in combinations(range(m),3))
        return (eq,triple)
    # Dictionary keyed by quantifier-free type of stationary triple.
    out=defaultdict(set)
    seen=set()
    for x,y,z in product(range(n),repeat=3):
        s=(x,y,z); key=typ(s)
        seen.add(key)
        for w in range(n):
            out[key].add(typ(s+(w,)))
    # Canonical JSON-friendly serialization for comparison.
    def key(t):return ''.join('1' if x else '0' for a in t for x in a)
    serial={key(k):sorted(map(key,v)) for k,v in out.items()}
    return {'n':n,'stationary_types':len(seen),'extension_types':sum(map(len,out.values())),'catalog':serial,
            'collinear_3':any(len({i,j,k})==3 and tuple(sorted((i,j,k))) in C for i,j,k in product(range(n),repeat=3)),
            'collinear_4':any(all(tuple(sorted(t)) in C for t in combinations(quad,3)) for quad in combinations(range(n),4))}

if __name__=='__main__':
    runs=[]
    for model,p in [('AG',2),('PG',2),('AG',3),('PG',3),('AG',5),('PG',5)]:
        pts,C=affine(p) if model=='AG' else projective(p)
        r=profile(pts,C)
        expected=('A' if model=='AG' and p==2 else 'B' if (model=='PG' and p==2) or (model=='AG' and p==3) else 'C')
        runs.append({'model':model+str(p),'class':expected,**r})
    classes=defaultdict(list)
    for r in runs:classes[r['class']].append(r)
    for cls,group in classes.items():
        assert all(r['catalog']==group[0]['catalog'] for r in group)
        assert all((r['collinear_3'],r['collinear_4'])==(group[0]['collinear_3'],group[0]['collinear_4']) for r in group)
    assert len({json.dumps(group[0]['catalog'],sort_keys=True) for group in classes.values()})==3
    assert {r['class']:(r['collinear_3'],r['collinear_4']) for r in runs}=={'A':(False,False),'B':(True,False),'C':(True,True)}
    print('PASS exact stationary-type extension catalogue comparisons')
    for r in runs:
        print(r['model'], 'vertices',r['n'],'class',r['class'],'types',r['stationary_types'],'extensions',r['extension_types'])
    print('PASS all six models agree precisely within their predicted class')
    print('LIMIT finite prime-field examples only; abstract theorem requires proof')
