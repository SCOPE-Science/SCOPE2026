"""Independent finite-diagram verifier for matching-cover type enumeration.
The structure here is a 3-colour graph R,S,T with equivalence classes of size 2,
and each pair of different classes joined by a perfect S matching.
No runtime or operational context is needed to execute this program.
"""
import itertools
from math import comb, factorial


def predicted(f,s,r):
    m=f+s
    total=0
    for j in range(min(s,r)+1):
        occ=comb(r,j)*factorial(s)//factorial(s-j)
        t=r-j
        for p in range(t//2+1):
            q=t-2*p
            k=t-p
            total+=occ*(factorial(t)//(2**p*factorial(p)*factorial(q)))*2**(m*k+comb(k,2))
    return total


def partitions_pair_single(rest):
    if not rest:
        yield []
        return
    first=rest[0]
    for tail in partitions_pair_single(rest[1:]):
        yield [(first,)]+tail
    for v in rest[1:]:
        rr=tuple(x for x in rest[1:] if x!=v)
        for tail in partitions_pair_single(rr):
            yield [(first,v)]+tail


def direct(f,s,r,old_signs=0):
    # The first f old R-fibres have two named members and the next s have one.
    m=f+s
    old=[]
    for i in range(m):
        old.append((i,0))
        if i<f: old.append((i,1))
    old_edges=list(itertools.combinations(range(m),2))
    old_bit={e:(old_signs>>i)&1 for i,e in enumerate(old_edges)}
    unique=set()
    for j in range(min(s,r)+1):
        for old_positions in itertools.combinations(range(r),j):
            for assigned_old in itertools.permutations(range(f,m),j):
                existing={pos:(fiber,1) for pos,fiber in zip(old_positions,assigned_old)}
                remaining=tuple(x for x in range(r) if x not in existing)
                for blocks in partitions_pair_single(remaining):
                    k=len(blocks)
                    # One canonical orientation of each newly visible R fibre suffices.
                    # For pairs, first member layer 0, second member layer 1.
                    # For singles, choose layer 0. All alternative choices can be
                    # absorbed into free independent E-bits at its incident edges.
                    newer={}
                    for h,block in enumerate(blocks):
                        for layer,pos in enumerate(block):
                            newer[pos]=(m+h,layer)
                    x=[existing.get(p,newer.get(p)) for p in range(r)]
                    new_edges=[(u,v) for u in range(m+k) for v in range(u+1,m+k)
                               if v>=m]
                    for bits in range(1<<len(new_edges)):
                        e=old_bit.copy()
                        e.update({pair:(bits>>i)&1 for i,pair in enumerate(new_edges)})
                        def color(a,b):
                            ia,pa=a;ib,pb=b
                            if ia==ib:return 0 # R
                            edge=e[(min(ia,ib),max(ia,ib))]
                            return 1 if edge==(pa==pb) else 2 # S or T
                        signature=tuple(color(x0,x1) for x0,x1 in itertools.product(x,old))
                        signature+=tuple(color(x0,x1) for x0,x1 in itertools.combinations(x,2))
                        unique.add(signature)
    return len(unique)


def check():
    runs=[]
    for f in range(3):
        for s in range(3):
            if f+s>3:continue
            for r in range(4):
                for old_bits in ([0, 5] if f+s>=3 else [0]):
                    d=direct(f,s,r,old_bits)
                    p=predicted(f,s,r)
                    assert d==p,(f,s,r,old_bits,d,p)
                    runs.append((f,s,r,old_bits,d))
    # Additional symbolic cross-check via independent formal EGF assembly.
    for f in range(6):
        for s in range(6):
            m=f+s
            coeff=[0]*8
            # Ordinary polynomial convolution of (1+z)^s with the weighted
            # pair/single SET series, using exact factorial denominators.
            from fractions import Fraction
            h=[Fraction(0) for _ in range(8)]
            for k in range(8):
                # coefficient of z^t in (z+z^2/2)^k/k!
                for p in range(k+1):
                    t=k+p
                    if t>7:continue
                    h[t]+=Fraction(2**(m*k+comb(k,2))*comb(k,p),2**p*factorial(k))
            for r in range(8):
                val=sum(Fraction(comb(s,j))*h[r-j] for j in range(min(s,r)+1))*factorial(r)
                assert val.denominator==1
                assert int(val)==predicted(f,s,r)
    assert [predicted(0,0,r) for r in range(6)]==[1,1,3,14,118,1784]
    assert all(2**m+m < 2**(m+1) for m in range(1,80))
    print('EXACT_MATCHING_COVER_TYPE_SPECTRUM_OK')
    print('direct_diagram_checks',len(runs),'formal_egf_checks',36*8)
    print('empty_base', [predicted(0,0,r) for r in range(6)])
    print('examples',[(f,s,[predicted(f,s,r) for r in range(4)]) for f,s in ((0,1),(1,0),(1,1),(0,2),(2,0),(1,2))])
if __name__=='__main__': check()
