"""Independent generation of the claimed normal forms, direct graph-neighborhood checks."""
from itertools import combinations
from math import comb

def normal_forms(n):
    allidx=set(range(n))
    for m in range(1,n+1):
        for U_tuple in combinations(range(n), m):
            U=set(U_tuple)
            shared=allidx-U
            # A pure left block and right singleton blocks
            left=[frozenset(U)] + [frozenset([i,n+i]) for i in sorted(shared)]
            right=[frozenset([n+i]) for i in sorted(U)]
            yield left+right
            if m>=2:
                left=[frozenset([i]) for i in sorted(U)] + [frozenset([i,n+i]) for i in sorted(shared)]
                right=[frozenset(n+i for i in U)]
                yield left+right
            # Two large blocks: share precisely one deleted matching index.
            if m>=3:
                for x in sorted(U):
                    rest=sorted(U-{x})
                    for sz in range(1,m-1):
                        for ac in combinations(rest,sz):
                            A=set(ac)|{x};B=U-(A-{x})
                            left=[frozenset(A)] + [frozenset([i]) for i in sorted(U-A)]
                            right=[frozenset(n+i for i in B)] + [frozenset([n+i]) for i in sorted(U-B)]
                            yield [frozenset([i,n+i]) for i in sorted(shared)]+left+right

def valid(n, partition):
    color=[None]*(2*n)
    for i,block in enumerate(partition):
        for x in block:
            if color[x] is not None:return False
            color[x]=i
    if any(c is None for c in color):return False
    for i in range(n):
        for j in range(n):
            if i!=j and color[i]==color[n+j]: return False
    signatures=[]
    for v in range(2*n):
        side=v//n;idx=v%n
        signatures.append(frozenset(color[(1-side)*n+j] for j in range(n) if j!=idx))
    return all(color[i]!=color[j] or signatures[i]!=signatures[j] for i in range(2*n) for j in range(i))

for n in range(2,9):
    seen=set()
    for part in normal_forms(n):
        key=tuple(sorted(tuple(sorted(block)) for block in part))
        assert key not in seen,('duplicate',n,key)
        seen.add(key)
        assert len(part)==n+1 and valid(n,part),('invalid',n,key)
    expect=n*3**(n-1)-(n-2)*2**n-2
    assert len(seen)==expect,(n,len(seen),expect)
    print('n=',n,' constructions=',len(seen),' expected=',expect)
print('CONSTRUCTIVE_OK')
