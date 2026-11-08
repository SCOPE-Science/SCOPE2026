"""Exhaustive finite-preorder C2 census, using the Python standard library only.
Run: python verify_preorders.py
"""
from collections import Counter, defaultdict
from itertools import permutations

MAX_N=8

def iso(a,b):
    n=len(a)
    if n!=len(b): return False
    if a==b: return True
    def signature(rows,i):
        return ((rows[i]).bit_count(),sum((row>>i)&1 for row in rows), (rows[i]>>i)&1)
    sa=[signature(a,i) for i in range(n)];sb=[signature(b,i) for i in range(n)]
    if sorted(sa)!=sorted(sb):return False
    buckets={k:[j for j in range(n) if sb[j]==k] for k in set(sa)}
    order=sorted(range(n),key=lambda i:(len(buckets[sa[i]]),-sa[i][0],-sa[i][1]))
    chosen={};occupied=set()
    def walk(t):
        if t==n: return True
        i=order[t]
        for j in buckets[sa[i]]:
            if j in occupied:continue
            if any(((a[i]>>u)&1)!=((b[j]>>v)&1) or ((a[u]>>i)&1)!=((b[v]>>j)&1) for u,v in chosen.items()):continue
            chosen[i]=j;occupied.add(j)
            if walk(t+1):return True
            occupied.remove(j);del chosen[i]
        return False
    return walk(0)

def key(rows):
    n=len(rows)
    return tuple(sorted(((rows[i]).bit_count(),sum((row>>i)&1 for row in rows), (rows[i]>>i)&1) for i in range(n)))

def ideals(rows):
    n=len(rows)
    for z in range(1<<n):
        if all(not(z>>x&1) or (z>>y&1) or not(rows[y]>>x&1) for x in range(n) for y in range(n)):
            yield z

def posets_by_size():
    p={0:[()]}
    for n in range(1,MAX_N+1):
        seen=defaultdict(list)
        for rows in p[n-1]:
            for I in ideals(rows):
                new=tuple((rows[i] | (((I>>i)&1)<<(n-1))) if i<n-1 else 0 for i in range(n))
                k=key(new)
                if not any(iso(new,x) for x in seen[k]):seen[k].append(new)
        p[n]=[x for a in seen.values() for x in a]
        print('POSET',n,len(p[n]),flush=True)
    assert [len(p[i]) for i in range(1,MAX_N+1)] == [1,2,5,16,63,318,2045,16999]
    return p

def compositions(n,k):
    if k==1: yield (n,);return
    for x in range(1,n-k+2):
        for other in compositions(n-x,k-1):yield (x,)+other

def expand(rows,weights):
    verts=[i for i,w in enumerate(weights) for _ in range(w)]
    return tuple(sum((1<<j) for j,v in enumerate(verts) if u==v or (rows[u]>>v)&1) for u in verts)

def profile_census(p,n):
    desc=[]
    for k in range(1,n+1):
        for poset in p[k]:
            for w in compositions(n,k):
                desc.append((poset,w,expand(poset,w)))
    old=[[0]*n for _ in desc]
    for depth in range(n+1):
        signatures=[]
        for (poset,w,a),c in zip(desc,old):
            sigs=[]
            for x in range(n):
                sigs.append((c[x],tuple(sorted(Counter((((a[x]>>y)&1),((a[y]>>x)&1),int(x==y),c[y]) for y in range(n)).items()))))
            signatures.extend(sigs)
        palette={sig:i for i,sig in enumerate(sorted(set(signatures)))}
        new=[[palette[signatures[i*n+x]] for x in range(n)] for i in range(len(desc))]
        if new==old:break
        old=new
    groups=defaultdict(list)
    for i,c in enumerate(old):groups[tuple(sorted(Counter(c).items()))].append(i)
    exceptions=[];typenum=0
    for bucket in groups.values():
        reps=[]
        for idx in bucket:
            a=desc[idx][2]
            if not any(iso(a,desc[j][2]) for j in reps):reps.append(idx)
        typenum+=len(reps)
        if len(reps)>1:exceptions.append(tuple(reps))
    expected=[1,3,9,33,139,718,4535,35979][n-1]
    assert typenum==expected,(n,typenum,expected)
    assert len(groups)==typenum-(2 if n==8 else 0)
    if n==8:
        assert len(exceptions)==2 and all(len(x)==2 for x in exceptions)
        assert all(all(all(w==1 for w in desc[i][1]) for i in ex) for ex in exceptions)
    else:assert not exceptions
    print('CENSUS',n,'descriptions',len(desc),'preorders',typenum,'C2_classes',len(groups),'exception_pairs',len(exceptions),flush=True)
    for e in exceptions:
        print('PAIR',[(desc[i][0],desc[i][1]) for i in e],flush=True)

if __name__=='__main__':
    p=posets_by_size()
    for n in range(1,MAX_N+1):profile_census(p,n)
    print('VERIFY_OK preorders_8=35979 c2_classes_8=35977',flush=True)
