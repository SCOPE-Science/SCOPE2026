from itertools import combinations_with_replacement
from fractions import Fraction


def test(goods):
    n=len(goods)
    total=sum(goods)
    subset_sums=[sum(goods[i] for i in range(n) if mask>>i&1) for mask in range(1<<n)]
    optimum=max(s*(total-s) for s in subset_sums)
    checked=equal=0
    for mask,a in enumerate(subset_sums):
        b=total-a
        if a>b:
            continue
        B=[goods[i] for i in range(n) if not (mask>>i)&1]
        if not B or b-min(B)>a:
            continue
        checked+=1
        assert 9*a*b>=8*optimum, (goods,mask,a,b,optimum)
        if 9*a*b==8*optimum:
            equal+=1
            A=[goods[i] for i in range(n) if (mask>>i)&1]
            assert b==2*a and len(B)==2 and B[0]==B[1]
            assert any(2*sum(A[i] for i in range(len(A)) if mask2>>i&1)==a for mask2 in range(1<<len(A)))
    return checked,equal


def main():
    profiles=all_efx=equality=0
    for n in range(2,7):
        for goods in combinations_with_replacement(range(1,6),n):
            c,e=test(goods)
            profiles+=1
            all_efx+=c
            equality+=e
    assert (profiles,all_efx,equality)==(456,2939,4)
    assert test((2,2,1,1))[1]>0
    print('PASS:', profiles, 'profiles;', all_efx, 'EFX allocations;', equality, 'equality allocations')

if __name__=='__main__':
    main()
