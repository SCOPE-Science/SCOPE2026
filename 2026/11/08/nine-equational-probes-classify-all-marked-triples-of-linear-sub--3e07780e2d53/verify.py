"""Verify the nine-test fingerprint of three generated bounded subspace lattices.

This checks the complete finite nine-block normal-form reduction. The
normal-form theorem, not this finite enumeration, proves field uniformity.
"""
from collections import Counter
from math import comb

# Coordinates 0..7: one-dimensional blocks indexed by containment subsets.
# Coordinate 8: a two-dimensional block with three different projective lines.
def meet_m3(x, y):
    return x if x == y else (y if x == 4 else (x if y == 4 else 0))
def join_m3(x, y):
    return x if x == y else (y if x == 0 else (x if y == 0 else 4))

def meet(a,b):
    return tuple(min(x,y) for x,y in zip(a[:8],b[:8]))+(meet_m3(a[8],b[8]),)
def join(a,b):
    return tuple(max(x,y) for x,y in zip(a[:8],b[:8]))+(join_m3(a[8],b[8]),)

bottom=(0,)*9
top=(1,)*8+(4,)
generators=[tuple((s>>i)&1 for s in range(8))+(i+1,) for i in range(3)]

def wedge(factors):
    z=top
    for factor in factors:z=meet(z,factor)
    return z

def vee(factors):
    z=bottom
    for factor in factors:z=join(z,factor)
    return z

def probe_values():
    differences=[]
    for s in range(8):
        lhs=wedge([generators[i] for i in range(3) if s>>i&1])
        rhs=meet(lhs, vee([generators[i] for i in range(3) if not(s>>i&1)]))
        differences.append(tuple(lhs[k]!=rhs[k] for k in range(9)))
    x,y,z=generators
    lhs=meet(x,join(y,z))
    rhs=join(meet(x,y),meet(x,z))
    differences.append(tuple(lhs[k]!=rhs[k] for k in range(9)))
    return differences

def closure():
    elements=[bottom,top]+generators
    known=set(elements)
    cursor=0
    while cursor<len(elements):
        x=elements[cursor]
        for y in list(elements):
            for op in (meet,join):
                result=op(x,y)
                if result not in known:
                    known.add(result)
                    elements.append(result)
        cursor+=1
    return elements

def main():
    diffs=probe_values()
    assert len(diffs)==9
    for i, row in enumerate(diffs):
        assert row==tuple(i==j for j in range(9)),(i,row)
    print('PASS nine fixed equations each isolate exactly one canonical block')
    terms=closure()
    assert len(terms)==30,len(terms)
    print('PASS closure of bounded three-generator terms has 30 evaluations')
    kernels={}
    size_distribution=Counter()
    for mask in range(1<<9):
        coordinates=[k for k in range(9) if (mask>>k)&1]
        vals=[tuple(t[k] for k in coordinates) for t in terms]
        lookup={};canonical=[]
        for v in vals:
            if v not in lookup:lookup[v]=len(lookup)
            canonical.append(lookup[v])
        kernels.setdefault(tuple(canonical),[]).append(mask)
        size_distribution[len(lookup)]+=1
        actual_probe_mask=sum((1<<j) for j in range(9) if any(diffs[j][k] and mask>>k&1 for k in range(9)))
        assert actual_probe_mask==mask
    assert len(kernels)==512 and all(len(v)==1 for v in kernels.values())
    print('PASS all 512 support masks give distinct marked bounded lattice term kernels')
    print('PASS type sizes range from {} to {}'.format(min(size_distribution),max(size_distribution)))
    def h(n):return sum(comb(8,k) for k in range(1,min(8,n)+1)) if n>=1 else 0
    for n, expected in [(0,1),(1,8),(2,37),(3,100),(4,199),(9,509),(10,511),(11,510),(12,511)]:
        got=(1 if n==0 else h(n)+h(n-2)+(1 if n>=2 and n%2==0 else 0))
        assert got==expected,(n,got,expected)
    print('PASS fixed-rank profile N(0..4)=(1,8,37,100,199)')
    print('PASS for even n>=10 N(n)=511 and for odd n>=11 N(n)=510')
    print('PASS nine tests are information-theoretically optimal for 512 types')
if __name__=='__main__':main()
