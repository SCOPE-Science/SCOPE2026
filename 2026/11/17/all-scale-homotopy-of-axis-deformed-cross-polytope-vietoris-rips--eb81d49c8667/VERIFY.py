#!/usr/bin/env python3
"""Independent mod-two boundary-matrix checks for Euclidean axis-cross vertex Rips stages."""
from itertools import combinations, product
import random

def predicted(weights, t):
    n=len(weights)
    edges={(i,j) for i in range(n) for j in range(i+1,n) if weights[i]+weights[j]<=t}
    active={i for a,b in edges for i in (a,b)}
    if t >= 4*min(weights):
        c=(1 if edges else 0)+sum(1 if 4*w<=t else 2 for i,w in enumerate(weights) if i not in active)
        return {0:c-1} if c>1 else {}
    def rec(ids):
        if not ids:
            return {-1:1}
        e={(i,j) for i,j in edges if i in ids and j in ids}
        if not e: return {0:2*len(ids)-1}
        a={i for i,j in e for i in (i,j)}
        s=len(ids)-len(a)
        v=min(a,key=lambda i:(weights[i],i))
        assert all((min(v,j),max(v,j)) in e for j in a if j!=v), ('bad universal',weights,t,e)
        p={k+1:x for k,x in rec(a-{v}).items()}
        if s:p[0]=p.get(0,0)+2*s
        return p
    return {k:v for k,v in rec(set(range(n))).items() if v}

def computed(weights, t):
    n=len(weights);N=2*n
    # i=2*axis + sign
    pairs=set()
    for u in range(N):
        for v in range(u+1,N):
            i,j=u//2,v//2
            d=4*weights[i] if i==j else weights[i]+weights[j]
            if d<=t:pairs.add((u,v))
    # enumerate each clique recursively (not powerset filter)
    fs=[[] for _ in range(N)]
    def extend(face, eligible):
        for k,v in enumerate(eligible):
            newface=face+(v,)
            fs[len(newface)-1].append(newface)
            extend(newface,[w for w in eligible[k+1:] if (min(v,w),max(v,w)) in pairs])
    extend((),list(range(N)))
    fs=[x for x in fs if x]
    ranks={}
    for k in range(1,len(fs)):
        lower={f:i for i,f in enumerate(fs[k-1])}
        piv={}
        for f in fs[k]:
            b=0
            for ix in range(len(f)):
                b ^= 1 << lower[f[:ix]+f[ix+1:]]
            while b:
                j=b.bit_length()-1
                if j in piv:b ^= piv[j]
                else:
                    piv[j]=b
                    break
        ranks[k]=len(piv)
    out={}
    for k,f in enumerate(fs):
        b=len(f)-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0:b-=1
        if b:out[k]=b
    return out,tuple(map(len,fs))

def run():
    R=random.Random(8082026)
    tests=[]
    for d in range(1,8):
        cases=[]
        for j in range(9):
            w=sorted(R.randint(1,9)**2 for _ in range(d))
            cases.append(w)
        cases += [list(range(1,d+1)),[1]*d,[4]*d,[1]+[4]*(d-1)]
        for w in cases:
            tvals=sorted({0,*[4*x for x in w],*[w[i]+w[j] for i in range(d) for j in range(i+1,d)]})
            for t in tvals:
                # for larger d, compute select stages only
                if d>=7 and t>4*w[0] and t!=tvals[-1]:continue
                p=predicted(w,t)
                c,fs=computed(w,t)
                assert p==c, (d,w,t,p,c,fs)
                tests.append((d,w,t,fs))
    print('PASS',len(tests),'exact stages',len(set(tuple(x[1]) for x in tests)),'side-length vectors')
    for d in (3,4,5,6,7):
        arr=[x for x in tests if x[0]==d]
        print('dim',d,'stages',len(arr),'max_faces',max(sum(x[3]) for x in arr))
    examples=[([1,1,1],2),([1,1,1],3),([1,4,4,4],5),([1,4,4,4],4),([1,1,4,4],5)]
    for w,t in examples:
        print('example',w,t,predicted(w,t))
    print('VERIFY_OK')
if __name__=='__main__':run()
