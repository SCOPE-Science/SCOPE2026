#!/usr/bin/env python3
"""Reproducible exact finite-field barcode check of layered-poset formulas.

No external dependencies. Independently enumerates the poset's chains, computes
furtherness from principal downsets, and reduces the filtered boundary matrix.
"""
from itertools import combinations, product
from collections import Counter

PRIME=101

def raw_barcodes(sizes,center):
    layers=[]; v=0
    for size in sizes:
        layers.append(tuple(range(v,v+size))); v+=size
    level={x:i for i,layer in enumerate(layers) for x in layer}
    elements=[x for layer in layers for x in layer]
    U={y:{z for z in elements if level[z]<level[y] or z==y} for y in elements}
    weight={y:len(U[y]-U[center]) for y in elements}
    # Order complex contains at most one vertex in each layer.
    faces=[]
    for k in range(1,len(layers)+1):
        for indices in combinations(range(len(layers)),k):
            for face in product(*(layers[i] for i in indices)):
                faces.append(tuple(sorted(face)))
    faces.sort(key=lambda f:(max(weight[x] for x in f),len(f),f))
    cols={f:i for i,f in enumerate(faces)}
    matrix_reduced={}; pairs={}; zero_births=[]
    for j,f in enumerate(faces):
        col={cols[f[:i]+f[i+1:]]:(-1 if i%2 else 1) % PRIME for i in range(len(f))} if len(f)>1 else {}
        while col:
            pivot=max(col)
            if pivot not in matrix_reduced:
                matrix_reduced[pivot]=col
                pairs[pivot]=j
                break
            prior=matrix_reduced[pivot]
            coeff=col[pivot]*pow(prior[pivot],-1,PRIME)%PRIME
            for row,value in prior.items():
                nv=(col.get(row,0)-coeff*value)%PRIME
                if nv:col[row]=nv
                else:col.pop(row,None)
        if not col: zero_births.append(j)
    bars=Counter()
    for j in zero_births:
        f=faces[j]; degree=len(f)-1
        b=max(weight[x] for x in f)
        if j in pairs:
            death_face=faces[pairs[j]]
            d=max(weight[x] for x in death_face)
            if b<d:bars[(degree,b,d)]+=1
        else:bars[(degree,b,'inf')]+=1
    return bars

def expected(sizes,i):
    r=len(sizes); bars=Counter({(0,0,'inf'):1})
    multiplicity=1
    for j in range(1,r+1):
        multiplicity*=sizes[j-1]-1
        if j<i:continue
        birth=1 if j==i else sum(sizes[i-1:j-1])
        death='inf' if j==r else sum(sizes[i-1:j])
        bars[(j-1,birth,death)]+=multiplicity
    return bars

def reconstruct_from_bottom(bars):
    highest=max(k[0] for k in bars)
    r=highest+1
    c=[]; widths=[]
    for j in range(1,r):
        selected=[(k,v) for k,v in bars.items() if k[0]==j-1 and k[2]!='inf']
        assert len(selected)==1
        (dim,b,d),mult=selected[0]
        c.append(mult)
        if j==1:
            assert b==1
            widths.append(d)
        else:
            widths.append(d-b)
    top=[(k,v) for k,v in bars.items() if k[0]==r-1 and k[2]=='inf']
    assert len(top)==1
    top_mult=top[0][1]
    assert top_mult%c[-1]==0
    widths.append(1+top_mult//c[-1])
    return tuple(widths)

def check(sizes):
    layers=[]; start=0
    for m in sizes:
        layers.append(range(start,start+m));start+=m
    for i,layer in enumerate(layers,1):
        for center in (layer[0],layer[-1]):
            actual=raw_barcodes(sizes,center)
            wanted=expected(sizes,i)
            assert actual==wanted,(sizes,i,center,actual,wanted)
    assert reconstruct_from_bottom(raw_barcodes(sizes,layers[0][0]))==tuple(sizes)
    # Top-bar bottleneck and directional separation are exact.
    D=sum(sizes[:-1]); bottom=expected(sizes,1); top=expected(sizes,len(sizes))
    b1=next(k[1] for k in bottom if k[0]==len(sizes)-1)
    b2=next(k[1] for k in top if k[0]==len(sizes)-1)
    assert b1==D and b2==1 and abs(b1-b2)==D-1
    return len(layers)*2

if __name__=='__main__':
    cases=[(2,2),(3,2),(2,3),(3,3),(2,2,2),(2,3,2),(3,2,3),
           (2,2,2,2),(2,3,2,2),(2,2,3,2),(2,2,2,2,2)]
    count=0
    for prime in (2,3,101):
        PRIME=prime
        count+=sum(check(c) for c in cases)
    print('PASS:',len(cases),'layer-size patterns;',count,'root-by-prime calculations; exact boundary reduction mod (2,3,101)')
    for sz in [(2,3,2),(2,2,2,2),(3,2,3)]:
        print('example',sz, 'bottom root',sorted((str(k),v) for k,v in expected(sz,1).items()))
