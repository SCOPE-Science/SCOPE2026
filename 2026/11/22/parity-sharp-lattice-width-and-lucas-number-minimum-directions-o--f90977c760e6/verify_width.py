#!/usr/bin/env python3
"""Independent bounded exhaustive checks for a circulant lattice-simplex width theorem.

The output enumerates all primitive affine-lattice directions with coordinate
range <=3, for n=3..8, w=2..5. This bounded check does not prove the theorem.
"""
from itertools import product
from math import gcd

def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a

def canonical_binary(u):
    # Directions are considered modulo addition of a constant and sign.
    if max(u)-min(u) != 1: return False
    t=tuple(x-min(u) for x in u)
    n=len(u)
    if n%2==0:
        return all(t[i]!=t[(i+1)%n] for i in range(n))
    has00=any(t[i]==t[(i+1)%n]==0 for i in range(n))
    has11=any(t[i]==t[(i+1)%n]==1 for i in range(n))
    return has00 != has11


def run():
    tested=0; equal=0
    for n in range(3,9):
        for w in range(2,6):
            expected=w if n%2 else w-1
            minimizers=set()
            for u in product(range(4), repeat=n):
                if min(u)!=0 or max(u)==0 or gcd(*u)!=1:
                    continue
                f=[u[i]+w*u[(i+1)%n] for i in range(n)]
                width=max(f)-min(f)
                tested+=1
                assert width>=expected,(n,w,u,width,expected)
                is_min=(width==expected)
                assert is_min==canonical_binary(u),(n,w,u,width)
                if is_min:
                    # choose one representative per unoriented equivalence class
                    norm=tuple(u)
                    comp=tuple(max(u)-x for x in u)
                    minimizers.add(min(norm,comp))
                    equal+=1
            count=lucas(n)-1 if n%2 else 1
            assert len(minimizers)==count,(n,w,len(minimizers),count)
            print('n=%d w=%d width=%d unoriented=%d'%(n,w,expected,count))
    print('PASS: %d bounded primitive direction instances checked, %d minimum instances'%(tested,equal))
if __name__=='__main__': run()
