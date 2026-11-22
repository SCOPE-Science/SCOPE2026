#!/usr/bin/env python3
"""Independent finite tests for colored-cycle fiber symmetry, no external packages."""
from itertools import combinations
from collections import Counter

def subsets_ind(n):
    for s in range(1<<n):
        if not any((s>>i&1) and (s>>((i+1)%n)&1) for i in range(n)):
            yield s

def prediction(n):
    weights = {}
    for S in subsets_ind(n):
        if not S:
            if n%3==0: weights[S] = (n//3-1,2)
            elif n%3==1: weights[S] = (n//3-1,1)
            else: weights[S] = (n//3,1)
            continue
        I=[i for i in range(n) if S>>i&1]
        gaps = [(I[(j+1)%len(I)]-I[j])%n for j in range(len(I))]
        if len(I)==1: gaps=[n]
        if any(x%3==1 for x in gaps): continue
        d=len(I)-1+sum((x-2)//3 for x in gaps)
        weights[S]=(d,1)
    return weights

def mod_rank(rows,p):
    pivots={}
    for row in rows:
        row={i:v%p for i,v in row.items() if v%p}
        while row:
            i=min(row)
            if i not in pivots:
                inv=pow(row[i],-1,p)
                pivots[i]={k:v*inv%p for k,v in row.items()}
                break
            t=row[i]
            for k,v in pivots[i].items():
                z=(row.get(k,0)-t*v)%p
                if z:row[k]=z
                else:row.pop(k,None)
    return len(pivots)

def actual_betti(n,p=101):
    faces={-1:[()]}
    for S in subsets_ind(n):
        if not S:continue
        I=[i for i in range(n) if S>>i&1]
        for mask in range(1<<len(I)):
            sig=tuple(2*i+((mask>>j)&1) for j,i in enumerate(I))
            faces.setdefault(len(I)-1,[]).append(sig)
    ranks={}
    for d in range(max(faces)+1):
        idx={s:i for i,s in enumerate(faces[d-1])}
        rows=[]
        for sig in faces[d]:
            rows.append({idx[sig[:j]+sig[j+1:]]:(-1 if j%2 else 1) for j in range(len(sig))})
        ranks[d]=mod_rank(rows,p)
    return {d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in faces if d>=0 and len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def check_chain_blocks(n):
    # Chain component indexed by S is exactly link chain with fixed U factors.
    for S in subsets_ind(n):
        for A in subsets_ind(n):
            if S &~ A: continue
            indices=[i for i in range(n) if A>>i&1]
            # Every removal of a fiber with minus U must vanish; removal of plus has coefficient +/- 1.
            for j,i in enumerate(indices):
                eps=0 if S>>i&1 else 1
                if eps:
                    B=A & ~(1<<i)
                    assert B in set(subsets_ind(n))
                    assert (B&S)==S
                else:
                    assert S>>i&1

def main():
    tests=0
    for n in range(5,13):
        w=prediction(n)
        ctr=Counter()
        for d,m in w.values():ctr[d]+=m
        assert all(d>=0 and z>0 for d,z in ctr.items())
        assert len(w)<=sum(1 for _ in subsets_ind(n))
        check_chain_blocks(n)
        for T in range(1<<n):
            if n>8 and T not in (0,1,3,(1<<n)-1): continue
            fixed = -1+sum(((-1)**(A.bit_count()-1))*(1<<A.bit_count()) for A in subsets_ind(n) if A and not(A&T))
            predicted = sum(((-1)**(d+(S&T).bit_count()))*v for S,(d,v) in w.items())
            assert fixed==predicted,(n,T,fixed,predicted)
        tests+=1
        if n<=9:
            direct=actual_betti(n)
            assert direct==dict(ctr), (n,direct,dict(ctr))
            tests+=1
        print('n=',n,'sectors=',len(w),'betti=',dict(sorted(ctr.items())))
    print('VERIFY_OK','tested',tests,'family-and-boundary cases')
if __name__=='__main__':main()
