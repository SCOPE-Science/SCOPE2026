#!/usr/bin/env python3
"""Verify finite cases of the cyclic no-three-equal bit-flip component theorem.

No finite check is used as a proof for arbitrary length.
"""
from collections import Counter, deque
from math import comb
import argparse


def admissible(x, n):
    for i in range(n):
        a=(x >> i) & 1
        if a == ((x >> ((i + 1) % n)) & 1) == ((x >> ((i + 2) % n)) & 1):
            return False
    return True


def equal_edges(x, n):
    return sum(((x >> i) & 1) == ((x >> ((i + 1) % n)) & 1)
               for i in range(n))


def direct_components(n):
    verts={x for x in range(1 << n) if admissible(x,n)}
    todo=set(verts)
    components=[]
    while todo:
        start=todo.pop()
        q=deque([start])
        seen={start}
        nedges=0
        while q:
            x=q.popleft()
            for j in range(n):
                y=x ^ (1 << j)
                if y in verts:
                    nedges+=1
                    if y not in seen:
                        seen.add(y)
                        todo.remove(y)
                        q.append(y)
        counts={equal_edges(x,n) for x in seen}
        assert len(counts)==1, (n,counts)
        components.append((next(iter(counts)),len(seen),nedges//2))
    return sorted(components)


def predicted_components(n):
    ans=[]
    for k in range(n//2+1):
        if (n-k)%2:
            continue
        if k==0:
            ans.extend([(0,1,0)]*2)
        elif 2*k==n:
            ans.extend([(k,1,0)]*4)
        else:
            v=2*n*comb(n-k-1,k-1)//k
            e=2*n*comb(n-k-2,k-1)
            ans.append((k,v,e))
    return sorted(ans)


def crosscheck_particle_counts(n):
    for k in range(n//2+1):
        if (n-k)%2:
            continue
        independent=0
        for d in range(1<<n):
            if d.bit_count()!=k:
                continue
            if not any((d>>i&1) and (d>>((i+1)%n)&1) for i in range(n)):
                independent+=1
        if k>0:
            target=n*comb(n-k-1,k-1)//k
            assert independent == target,(n,k,independent,target)
        else:
            assert independent==1


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-n',type=int,default=18)
    args=ap.parse_args()
    assert args.max_n>=3
    for n in range(3,args.max_n+1):
        got=direct_components(n)
        exp=predicted_components(n)
        assert got==exp,(n,got,exp)
        if n<=13:crosscheck_particle_counts(n)
        print(f'n={n} components={len(got)} vertices={sum(v for _,v,_ in got)} edges={sum(e for _,_,e in got)} OK')
    print('PASS: direct Hamming-flip components, sector sizes, and edge counts')

if __name__=='__main__':main()
