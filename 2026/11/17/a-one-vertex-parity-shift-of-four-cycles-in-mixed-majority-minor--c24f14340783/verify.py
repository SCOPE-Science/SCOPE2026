#!/usr/bin/env python3
"""Exact independent microscopic check of conformist--contrarian clique dynamics.

Run with Python 3.10 or newer; no third-party libraries are required.
"""
from math import comb


def actual_step(s, m, k):
    n=m+k
    ones=s.bit_count()
    out=0
    for v in range(n):
        old=(s>>v)&1
        neighboring_ones=ones-old
        comparison=2*neighboring_ones-(n-1)
        if comparison==0:
            new=old
        elif v<m:
            new=int(comparison>0)
        else:
            new=int(comparison<0)
        out |= new<<v
    return out


def predicted(m,k):
    n=m+k
    if n%2==0:
        q=n//2
        b=comb(m,m//2)*comb(k,k//2) if m%2==0 and k%2==0 else 0
        fixed=2*int(m>k)
        two=b//2+int(m<k)
        four=int(m==k)
        e2=comb(n,q)-b-2*int(m==k)
    else:
        q=n//2
        fixed=2 if k<=q else 2*comb(k,q)
        two=int(k>=q+2)
        four=int(k==q+1)
        e2=(2*comb(n,q)-2*comb(m,q-k)) if k<=q else (2*comb(n,q)-2*comb(k,q)-2*int(k==q+1))
    e0=fixed+2*two+4*four
    e1=(1<<n)-e0-e2
    return {1:fixed,2:two,4:four}, {0:e0,1:e1,2:e2}


def classify(m,k):
    n=m+k
    successor=[actual_step(s,m,k) for s in range(1<<n)]
    # Following successors on the full labelled-state graph is distinct from
    # deriving the three/four-case quotient identities used in the proof.
    seen={}
    orbits={1:0,2:0,4:0}
    for x in range(1<<n):
        if x in seen:
            continue
        path=[]
        indices={}
        v=x
        while v not in seen and v not in indices:
            indices[v]=len(path)
            path.append(v)
            v=successor[v]
        if v in indices:
            offset=indices[v]
            length=len(path)-offset
            assert length in orbits, (m,k,length)
            orbits[length]+=1
            for s in path[offset:]:
                seen[s]=(0,length)
            path=path[:offset]
        for s in reversed(path):
            entry,period=seen[successor[s]]
            seen[s]=(entry+1,period)
    assert len(seen)==1<<n
    entries={0:0,1:0,2:0}
    for entry,period in seen.values():
        assert entry<=2,(m,k,entry)
        entries[entry]+=1
    return orbits,entries


def main():
    checked=0
    for n in range(3,16):
        for m in range(1,n):
            k=n-m
            actual=classify(m,k)
            expected=predicted(m,k)
            assert actual==expected,(m,k,actual,expected)
            checked+=1
        print(f'PASS size {n}: {n-1} type splits')
    print(f'PASS: {checked} graph/type pairs, every labelled state, orbit periods and first-entry counts')

if __name__=='__main__':
    main()
