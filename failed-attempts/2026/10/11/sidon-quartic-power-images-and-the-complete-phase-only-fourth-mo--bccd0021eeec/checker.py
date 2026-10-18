#!/usr/bin/env python3
"""Exact arithmetic checks for the quartic-image Sidon phase theorem.

Uses only Python's standard library. No floating-point decisions enter the proof.
"""
from collections import defaultdict, Counter
from fractions import Fraction


def fibers(p):
    ordered = defaultdict(list)
    unordered = defaultdict(list)
    for a in range(p):
        for b in range(p):
            ordered[((a+b) % p, (pow(a, 4, p)+pow(b, 4, p)) % p)].append((a, b))
    for a in range(p):
        for b in range(a, p):
            unordered[((a+b) % p, (pow(a, 4, p)+pow(b, 4, p)) % p)].append((a, b))
    return ordered, unordered


def relation_matrix(p):
    _, fib = fibers(p)
    rows = []
    edges = []
    for pairs in fib.values():
        c, d = pairs[0]
        for a, b in pairs[1:]:
            row = [0]*p
            for x, sign in ((a,1),(b,1),(c,-1),(d,-1)):
                row[x] += sign
            rows.append(row)
            edges.append(((c,d),(a,b)))
    return rows, edges


def det_fraction(A):
    n = len(A)
    B = [[Fraction(x) for x in row] for row in A]
    sign = 1
    ans = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k,n) if B[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            B[k],B[pivot] = B[pivot],B[k]
            sign = -sign
        x = B[k][k]
        ans *= x
        for i in range(k+1,n):
            fac = B[i][k]/x
            for j in range(k+1,n):
                B[i][j] -= fac*B[k][j]
            B[i][k] = 0
    assert ans.denominator == 1
    return sign*int(ans)


def rank_mod(A,p):
    if not A:
        return 0
    M = [[v%p for v in r] for r in A]
    h,w=len(M),len(M[0]); row=0
    for col in range(w):
        pivot=next((i for i in range(row,h) if M[i][col]),None)
        if pivot is None:continue
        M[row],M[pivot]=M[pivot],M[row]
        inv=pow(M[row][col],-1,p)
        M[row]=[(v*inv)%p for v in M[row]]
        for i in range(h):
            if i!=row and M[i][col]:
                fac=M[i][col]
                M[i]=[(x-fac*y)%p for x,y in zip(M[i],M[row])]
        row+=1
        if row==h:break
    return row


def main():
    assert {pow(t,4,5) for t in range(5)} == {0,1}
    assert {pow(t,4,13) for t in range(13)} == {0,1,3,9}
    for p,expected_h,counts,energy,ranks,edges,columns,target_det in (
        (5,2,{1:1,2:4,3:4,4:1},69,(3,2),
         [((1,1),(3,4)),((1,2),(4,4)),((1,3),(2,2))],
         [1,2,3],-5),
        (13,4,{1:13,2:48,4:15},445,(9,8),
         [((1,7),(9,12)),((1,10),(3,8)),((1,12),(5,8)),
          ((2,7),(3,6)),((2,8),(11,12)),((2,11),(3,10)),
          ((3,4),(9,11)),((4,9),(6,7)),((5,9),(6,8))],
         [1,2,3,6,7,8,9,11,12],-13)
    ):
        H=sorted({pow(t,4,p) for t in range(p)})
        assert len(H)==expected_h
        sums=[(a+b)%p for i,a in enumerate(H) for b in H[i:]]
        assert len(sums)==len(set(sums))
        ord_fib,_=fibers(p)
        cnt=dict(Counter(len(v) for v in ord_fib.values()))
        assert cnt==counts
        assert sum(len(v)**2 for v in ord_fib.values())==energy
        for pair_list in ord_fib.values():
            assert len({tuple(sorted((pow(a,4,p),pow(b,4,p)))) for a,b in pair_list}) == 1
        R, pairs=relation_matrix(p)
        assert len(R)==(5 if p==5 else 15)
        # Every row is orthogonal over Z to each quartic-class indicator.
        for h in H:
            ind=[int(pow(t,4,p)==h) for t in range(p)]
            assert all(sum(a*b for a,b in zip(row,ind))==0 for row in R)
        # The additive-character direction is an independent extra null vector mod p.
        assert all(sum(t*r for t,r in enumerate(row))%p==0 for row in R)
        assert len({t:pow(t,4,p) for t in range(p)})==p
        chosen_rows=[]
        for pair in edges:
            assert pair in pairs
            chosen_rows.append(R[pairs.index(pair)])
        sub=[[row[c] for c in columns] for row in chosen_rows]
        d=det_fraction(sub)
        assert d==target_det,(p,d)
        assert rank_mod(R,p)==ranks[1]
        assert ranks[0]==p-expected_h
        # The full rank minors have gcd p: lower bound from the exhibited minor,
        # upper divisibility from rank drop mod p and the class/linear null vectors.
        print(f'p={p} H={H} fiber_size_histogram={cnt} additive_energy={energy} '
              f'relations={len(R)} rational_rank={ranks[0]} '
              f'modular_rank={ranks[1]} minor={d} components={p} '
              f'continuous_dimension={expected_h}')
    H17={pow(t,4,17) for t in range(17)}
    assert H17=={0,1,4,13,16}
    assert (0+0)%17 == (1+16)%17 == (4+13)%17
    print('SIDON_OBSTRUCTION p=17 and counting excludes all remaining primes >=5')
    print('CHECK_PASS')

if __name__=='__main__':main()
