#!/usr/bin/env python3
"""Exact certificates for ternary Fourier convolution of signed permutation matrices.

Run: python3 check_signed_permutation.py [rank3_patterns_csv] [rank4_spectrum_csv]
Standard-library Python only; all computations use exact integers.
"""
import collections
import csv
import functools
import itertools
import math
import sys


def permanent_by_permutations(n, board_mask):
    ans=0
    for perm in itertools.permutations(range(n)):
        value=1
        for row,col in enumerate(perm):
            value *= 2 if (board_mask>>(row*n+col))&1 else -1
        ans+=value
    return ans


def rook_numbers(n, board_mask):
    # Each choice is either an unused row or a rook in an unoccupied column.
    rows=[((board_mask>>(row*n)) & ((1<<n)-1)) for row in range(n)]
    dp={(0,0):1}
    for row in range(n):
        new=collections.defaultdict(int)
        for (used,k),ways in dp.items():
            new[(used,k)]+=ways
            choices=rows[row]&~used
            while choices:
                bit=choices & -choices
                choices-=bit
                new[(used|bit,k+1)]+=ways
        dp=new
    return tuple(sum(v for (used,j),v in dp.items() if j==k) for k in range(n+1))


def permanent_by_rook_formula(n, board_mask):
    return sum((-1)**(n-k)*3**k*math.factorial(n-k)*r
               for k,r in enumerate(rook_numbers(n,board_mask)))


def weighted_spectrum(n):
    hist=collections.Counter();zeros=[]
    for mask in range(1 << (n*n)):
        p=permanent_by_rook_formula(n,mask)
        weight=2**(n*n-mask.bit_count())
        hist[p]+=weight
        if p==0:zeros.append(mask)
        # Independent permanent definition.
        assert p==permanent_by_permutations(n,mask),(n,mask,p)
    assert sum(hist.values())==3**(n*n)
    return hist,zeros


def direct_signed_perm_transform_n3():
    signed=[]
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((1,-1),repeat=3):
            v=[0]*9
            for i,j in enumerate(p):v[3*i+j]=signs[i]
            signed.append(v)
    assert len(signed)==48
    hist=collections.Counter()
    for char in itertools.product(range(3),repeat=9):
        # Exact cubic-cyclotomic coefficient counts.
        c=[0,0,0]
        for v in signed:
            c[sum(x*y for x,y in zip(v,char))%3]+=1
        # Sign symmetry forces equal non-real coefficients.
        assert c[1]==c[2]
        w=c[0]-c[1]
        mask=sum((char[i]==0)<<i for i in range(9))
        assert w==permanent_by_rook_formula(3,mask)
        hist[w]+=1
    return hist


def canonical(mask,n=3):
    perms=list(itertools.permutations(range(n)))
    copies=[]
    for r in perms:
        for c in perms:
            for transpose in (False,True):
                new=0
                for i in range(n):
                    for j in range(n):
                        rr,cc=(r[j],c[i]) if transpose else (r[i],c[j])
                        new|=((mask>>(rr*n+cc))&1) << (i*n+j)
                copies.append(new)
    return min(copies)


def orbit_summary(zeros):
    orbits=collections.defaultdict(list)
    for mask in zeros:orbits[canonical(mask)].append(mask)
    return sorted(((mask,len(elements),mask.bit_count()) for mask,elements in orbits.items()),
                  key=lambda v:(v[2],v[0]))


def main():
    h3,z3=weighted_spectrum(3)
    assert h3==direct_signed_perm_transform_n3()
    assert h3[0]==3816 and sum(h3.values())==19683
    orbits=orbit_summary(z3)
    assert sorted((size,k) for _,size,k in orbits)==[(9,1),(9,4),(18,7),(36,4)]
    assert len(z3)==72
    h4,z4=weighted_spectrum(4)
    assert h4[0]==0 and sum(h4.values())==43046721
    assert all(e % 9 == 6 for e in h4)
    assert min(abs(e) for e in h4)==3 and max(h4)==384
    assert len(h4)==27
    # n=5 is covered by the general congruence, without exhaustive enumeration.
    assert math.factorial(5)%9==3
    assert math.factorial(4)%9==6
    if len(sys.argv)>1:
        with open(sys.argv[1],newline='',encoding='utf-8') as f:
            rows=list(csv.reader(f))
        assert rows[0]==['board_mask','zero_sites','value','orbit_canonical','character_multiplicity']
        assert rows[1:]==[[str(m),str(m.bit_count()),'0',str(canonical(m)),str(2**(9-m.bit_count()))]
                          for m in sorted(z3)]
    if len(sys.argv)>2:
        with open(sys.argv[2],newline='',encoding='utf-8') as f:
            rows=list(csv.reader(f))
        assert rows[0]==['multiplier','frequency_multiplicity']
        assert rows[1:]==[[str(w),str(m)] for w,m in sorted(h4.items())]
    print('SIGNED_PERMUTATION_TERNARY_PASS',h3[0],19683-h3[0],len(z3),
          [(size,k) for _,size,k in orbits],h4[0],len(h4),min(map(abs,h4)),max(h4))

if __name__=='__main__':main()
