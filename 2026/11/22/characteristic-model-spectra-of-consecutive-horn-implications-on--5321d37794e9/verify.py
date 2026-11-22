#!/usr/bin/env python3
"""Reproducible independent finite tests for the path/ring Horn characteristic-model spectrum.

Run with Python 3 standard library: python3 verify.py
"""
from collections import Counter


def closed(n, bits, ring=False):
    if not ring:
        return all(not ((bits >> j)&1 and (bits >> (j+1))&1 and not (bits >> (j+2))&1)
                   for j in range(n-2))
    assert n >= 3
    return all(not ((bits >> j)&1 and (bits >> ((j+1)%n))&1 and not (bits >> ((j+2)%n))&1)
               for j in range(n))


def brute_irreducibles(n, ring=False):
    # Checks meet irreducibility from the definition: intersection of every
    # pair of strict closed supersets must strictly contain the candidate.
    valid=[bits for bits in range(1<<n) if closed(n,bits,ring)]
    result=set()
    for bits in valid:
        if bits==(1<<n)-1:
            continue
        upper=[z for z in valid if z!=bits and z&bits==bits]
        if all((x&y)!=bits for k,x in enumerate(upper) for y in upper[k+1:]):
            result.add(bits)
    return result


def path_pred(n):
    out=set()
    for omitted in range(n):
        for prefix in range(1 << omitted):
            if prefix & (prefix << 1):
                continue
            if any(not ((prefix >> v) & 1) and
                   not (v and ((prefix>>(v-1))&1)) and
                   not (v<omitted-1 and ((prefix>>(v+1))&1))
                   for v in range(omitted)):
                continue
            suffix = ((1<<n)-1) ^ ((1<<(omitted+1))-1)
            out.add(prefix|suffix)
    return out


def cycle_pred(n):
    out=set()
    for bits in range(1<<n):
        if bits==(1<<n)-1:
            continue
        if any((bits>>j)&1 and (bits>>((j+1)%n))&1 for j in range(n)):
            continue
        free=sum(not ((bits>>j)&1) and not ((bits>>((j-1)%n))&1)
                 and not ((bits>>((j+1)%n))&1) for j in range(n))
        if free<=1:out.add(bits)
    return out


def polynomial_coefficients(max_n):
    # These are coefficients of the two claimed *rational generating functions*.
    # Integer polynomials are represented by Counters indexed by degree of q.
    d=[Counter() for _ in range(max_n+1)]
    d[0][0]=1
    for k in range(1,max_n+1):
        if k>=2:
            for degree,coeff in d[k-2].items():d[k][degree+1]+=coeff
        if k>=3:
            for degree,coeff in d[k-3].items():d[k][degree+2]+=coeff
    path=[Counter() for _ in range(max_n+1)]
    for n in range(max_n+1):
        for shift,degree in [(1,1),(2,1),(3,2)]:
            for k in range(n-shift+1):
                for j,v in d[k].items():path[n][j+degree]+=v

    # C_n(q) = n [t^n](-log(1-f)+q^3 t^4/(1-f)),
    # f=qt^2+q^2t^3. Instead of logs evaluate by cycle tile compositions.
    cycle=[Counter() for _ in range(max_n+1)]
    for n in range(3,max_n+1):
        for r in range(1,n+1):
            # gap tuple lengths 2 and 3: count ordered tuples via DP
            blocks=[Counter() for _ in range(n+1)]
            blocks[0][0]=1
            for _ in range(r):
                next_blocks=[Counter() for _ in range(n+1)]
                for length in range(n+1):
                    for j,v in blocks[length].items():
                        if length+2<=n:next_blocks[length+2][j+1]+=v
                        if length+3<=n:next_blocks[length+3][j+2]+=v
                blocks=next_blocks
            for j,v in blocks[n].items():
                assert (n*v)%r==0
                cycle[n][j]+=(n*v)//r
            # exactly one 4-block: r possible positions for special block
            for length in range(n-3):
                if length+4!=n:continue
                # coefficient of (q t²+q²t³)^(r-1), then multiply q³t⁴
                if r==1:
                    if length==0:cycle[n][3]+=n
                else:
                    blocks=[Counter() for _ in range(n+1)]
                    blocks[0][0]=1
                    for _ in range(r-1):
                        tmp=[Counter() for _ in range(n+1)]
                        for ll in range(n+1):
                            for j,v in blocks[ll].items():
                                if ll+2<=n:tmp[ll+2][j+1]+=v
                                if ll+3<=n:tmp[ll+3][j+2]+=v
                        blocks=tmp
                    for j,v in blocks[length].items():cycle[n][j+3]+=n*v
    return path,cycle


def main():
    P,C=polynomial_coefficients(12)
    brute_tested=0
    for n in range(0,12):
        observed=brute_irreducibles(n,False)
        assert observed==path_pred(n),(n,'path membership', observed ^ path_pred(n))
        assert Counter(n-x.bit_count() for x in observed)==P[n],(n,'path distribution')
        brute_tested+=1<<n
    for n in range(3,12):
        observed=brute_irreducibles(n,True)
        assert observed==cycle_pred(n),(n,'cycle membership',observed ^ cycle_pred(n))
        assert Counter(n-x.bit_count() for x in observed)==C[n],(n,'cycle distribution')
        brute_tested+=1<<n
    # Check the all-closed-set enumerators independently of characteristic models.
    fib=[0,1]
    for _ in range(17):fib.append(sum(fib[-2:]))
    for n in range(0,12):
        assert sum(closed(n,x) for x in range(1<<n))==fib[n+3]-1
        if n>=3:
            assert sum(closed(n,x,True) for x in range(1<<n))==fib[n-1]+fib[n+1]+1
    print('VERIFY_OK raw_lattice_subsets=%d; path_orders=0..11; ring_orders=3..11' % brute_tested)
    print('path counts:',[sum(P[n].values()) for n in range(12)])
    print('ring counts:',[sum(C[n].values()) for n in range(3,12)])

if __name__=='__main__':
    main()
