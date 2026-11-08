"""Finite numerical checks for shifted-square semigroup Apéry layers."""
from collections import Counter
from heapq import heappush, heappop
from math import isqrt

def min_square_counts(limit):
    d=[limit+1]*(limit+1)
    d[0]=0
    for n in range(1,limit+1):
        d[n]=1+min(d[n-j*j] for j in range(1,isqrt(n)+1))
    return d

def apery_distances(a):
    # Shortest paths in residues, using generator edges of weight below 5a.
    weights=[a+j*j for j in range(1,isqrt(4*a)+1)]
    distance=[10**12]*a
    distance[0]=0
    queue=[(0,0)]
    while queue:
        v,r=heappop(queue)
        if distance[r]!=v:
            continue
        for w in weights:
            rr=(r+w)%a
            vv=v+w
            if vv<distance[rr]:
                distance[rr]=vv
                heappush(queue,(vv,rr))
    return distance

def in_four_square_obstruction(n):
    while n%4==0:
        n//=4
    return n%8==7

pairs=0
residues=0
last=None
for a in list(range(3,101))+[127,128,200,255,256,300,384,500,512,777,1000,1500,2000]:
    c=min_square_counts(3*a)
    w=apery_distances(a)
    assert w[0]==0
    predicted=[0]+[min(c[r],1+c[a+r],2+c[2*a+r]) for r in range(1,a)]
    layers=[0]+[(w[r]-r)//a for r in range(1,a)]
    assert predicted==layers,(a,[(r,predicted[r],layers[r]) for r in range(1,a) if predicted[r]!=layers[r]][:2])
    assert all(w[r] == r+a*layers[r] for r in range(a))
    exceptional=set(r for r in range(1,a) if (c[r]<=2 or c[a+r]<=2 or c[2*a+r]==1))
    assert all(layers[r]==(4 if in_four_square_obstruction(r) else 3) for r in range(1,a) if r not in exceptional)
    genus=sum(layers)
    assert genus==sum((w[r]-r)//a for r in range(a))
    frob=max(w)-a
    assert frob <4*a
    counts=Counter(layers[1:])
    assert sum(counts.values())==a-1
    last=(a,genus,frob,dict(counts),len(exceptional))
    pairs+=1
    residues+=a-1
print('VERIFY_OK parameter_values=%d residue_classes=%d largest=%s' %(pairs,residues,last))
