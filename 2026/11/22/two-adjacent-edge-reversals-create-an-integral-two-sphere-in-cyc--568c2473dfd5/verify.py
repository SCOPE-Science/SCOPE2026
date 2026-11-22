#!/usr/bin/env python3
"""Independent finite checks for two short-arc reversals of cyclic tournaments.
Run with Python 3 standard library: python verify.py
"""
from itertools import combinations


def face_set_tournament(m, reversed_starts):
    n=2*m+1
    outgoing=[{(i+j)%n for j in range(1,m+1)} for i in range(n)]
    for i in reversed_starts:
        j=(i+1)%n
        assert j in outgoing[i]
        outgoing[i].remove(j)
        outgoing[j].add(i)
    bad_by_largest=[[] for _ in range(n)]
    for a,b,c in combinations(range(n),3):
        cyc=(b in outgoing[a] and c in outgoing[b] and a in outgoing[c]) or (c in outgoing[a] and b in outgoing[c] and a in outgoing[b])
        if cyc:bad_by_largest[c].append((1<<a)|(1<<b))
    valid=bytearray(1<<n);valid[0]=1
    faces=set()
    for mask in range(1,1<<n):
        top=mask.bit_length()-1
        lower=mask^(1<<top)
        if valid[lower] and all(lower&pair!=pair for pair in bad_by_largest[top]):
            valid[mask]=1
            faces.add(mask)
    return faces


def base_interval_faces(m):
    n=2*m+1
    faces=set()
    for i in range(n):
        interval=[(i+j)%n for j in range(m+1)]
        for subset in range(1,1<<(m+1)):
            face=0
            for j in range(m+1):
                if subset&(1<<j):face|=1<<interval[j]
            faces.add(face)
    return faces


def check_collapse(m,base):
    n=2*m+1
    remain=set(base)
    pairs=0
    for s in range(m,1,-1):
        for i in range(n):
            edge=(1<<i)|(1<<((i+s)%n))
            pivot=1<<((i+1)%n)
            others=[(i+j)%n for j in range(2,s)]
            batches=[]
            for bits in range(1<<len(others)):
                lower=edge
                for j,v in enumerate(others):
                    if bits&(1<<j):lower|=1<<v
                batches.append(lower)
            for lower in sorted(batches,key=lambda t:-t.bit_count()):
                upper=lower|pivot
                assert lower in remain and upper in remain
                cofaces=[lower|(1<<j) for j in range(n) if not lower&(1<<j) and (lower|(1<<j)) in remain]
                assert cofaces==[upper],(m,s,i,lower,cofaces,upper)
                remain.remove(lower);remain.remove(upper);pairs+=1
    cycle={1<<i for i in range(n)}|{(1<<i)|(1<<((i+1)%n)) for i in range(n)}
    assert remain==cycle,(m,len(remain),len(cycle))
    assert pairs==n*(2**(m-1)-1)
    return pairs


def rank_mod2(masks_low,masks_high,n):
    rows={f:i for i,f in enumerate(masks_low)}
    pivots={}
    for f in masks_high:
        col=0
        for i in range(n):
            if f&(1<<i):col^=1<<rows[f^(1<<i)]
        while col:
            j=col.bit_length()-1
            if j in pivots:col^=pivots[j]
            else:pivots[j]=col;break
    return len(pivots)


def betti_mod2(faces,n):
    bydim={k:[f for f in faces if f.bit_count()==k+1] for k in range(n)}
    boundary={d:rank_mod2(bydim[d-1],bydim[d],n) for d in range(1,n) if bydim[d]}
    return {d:len(fs)-boundary.get(d,0)-boundary.get(d+1,0)-(1 if d==0 else 0)
            for d,fs in bydim.items() if fs and len(fs)-boundary.get(d,0)-boundary.get(d+1,0)-(1 if d==0 else 0)}


def main():
    cases=0
    for m in range(2,8):
        n=2*m+1
        base=base_interval_faces(m)
        assert base==face_set_tournament(m,()),n
        collapse_pairs=check_collapse(m,base)
        print('BASE',n,'faces',len(base),'collapse_pairs',collapse_pairs)
        for d in range(2,m+1):
            actual=face_set_tournament(m,(0,d))
            t0=sum(1<<j for j in (0,1,m+1))
            td=sum(1<<j for j in (d,d+1,(d+m+1)%n))
            expected=base|{t0,td}
            if d==m:
                expected.add(sum(1<<j for j in (0,1,m,m+1)))
            assert actual==expected,('face classification',n,d,sorted(actual-expected),sorted(expected-actual))
            if m<=5:
                betti=betti_mod2(actual,n)
                assert betti==({} if d==m else {2:1}),(n,d,betti)
            cases+=1
            print('DOUBLE',n,d,'faces',len(actual),'homology',('acyclic' if d==m else 'beta2=1'))
    print('ALL CHECKS PASS',cases,'double-reversal cases; base ranks and all intermediate free faces checked')

if __name__=='__main__':main()
