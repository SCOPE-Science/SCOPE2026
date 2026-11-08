"""Finite sample checker for counting-free fixed-variable theories of disjoint chains."""
from itertools import product
from collections import defaultdict
from functools import lru_cache

@lru_cache(None)
def partitions(n,top=None):
    if n==0:return ((),)
    top=n if top is None else min(n,top)
    return tuple((p,)+rest for p in range(top,0,-1) for rest in partitions(n-p,p))

def structures(nmax):
    return [parts for n in range(1,nmax+1) for parts in partitions(n)]

def poset(parts):
    size=sum(parts); A=[[0]*size for _ in range(size)]; a=0
    for ell in parts:
        for i in range(ell):
            for j in range(i+1,ell):
                A[a+i][a+j]=1
        a+=ell
    return A

def pred(parts,k):
    return tuple(sorted((ell,min(parts.count(ell),k)) for ell in set(parts)))

def theory_classes(parts_list,k):
    mat=[poset(p) for p in parts_list]; ts=[list(product(range(len(A)),repeat=k)) for A in mat]
    maps=[{t:i for i,t in enumerate(tuples)} for tuples in ts]
    colors=[]; keys=[]
    for A,tuples in zip(mat,ts):
        keys.append([tuple((int(t[i]==t[j]), A[t[i]][t[j]], A[t[j]][t[i]]) for i in range(k) for j in range(i+1,k)) for t in tuples])
    uniq={s:i for i,s in enumerate(sorted(set(sum(keys,[]))))}
    colors=[[uniq[s] for s in ks] for ks in keys]
    for rnd in range(100):
        keys2=[]
        for A,tuples,ids,cc in zip(mat,ts,maps,colors):
            ks=[]
            for t,old in zip(tuples,cc):
                opts=[]
                for j in range(k):
                    opts.append(tuple(sorted({cc[ids[t[:j]+(v,)+t[j+1:]]] for v in range(len(A))})))
                ks.append((old,tuple(opts)))
            keys2.append(ks)
        uniq={s:i for i,s in enumerate(sorted(set(sum(keys2,[]))))}
        nxt=[[uniq[s] for s in ks] for ks in keys2]
        old_classes=[tuple(sorted(set(c))) for c in colors]
        new_classes=[tuple(sorted(set(c))) for c in nxt]
        # colors can be renumbered globally; stable iff no cell of tuple partition split
        if all(len(set(zip(c,n)))==len(set(c)) for c,n in zip(colors,nxt)):
            colors=nxt;break
        colors=nxt
    else: raise RuntimeError('refinement exceeded cap')
    signatures=[tuple(sorted(set(cc))) for cc in colors]
    return signatures,rnd+1

def verify(nmax,k):
    cases=structures(nmax); found,rounds=theory_classes(cases,k)
    bad=[]
    for i in range(len(cases)):
        for j in range(i):
            if (found[i]==found[j]) != (pred(cases[i],k)==pred(cases[j],k)):
                bad.append((cases[i],cases[j]))
    return {'k':k,'max_order':nmax,'structures':len(cases),'comparisons':len(cases)*(len(cases)-1)//2,'refinement_rounds':rounds,'predicted_classes':len({pred(p,k) for p in cases}),'observed_classes':len(set(found)),'disagreements':len(bad),'examples':bad[:4]}

if __name__=='__main__':
    import json
    tests=[(8,2),(7,3),(6,4)]
    for n,k in tests:
        result=verify(n,k)
        print(json.dumps(result,sort_keys=True))
        assert result['disagreements']==0
    print('VERIFY_OK')
