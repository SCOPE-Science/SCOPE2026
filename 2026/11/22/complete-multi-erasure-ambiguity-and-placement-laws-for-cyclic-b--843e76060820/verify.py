#!/usr/bin/env python3
"""Exact finite tests for cyclic binary pair-sum erasures (self-contained)."""
from collections import Counter
from itertools import combinations, product
from math import comb
from fractions import Fraction


def path_sizes(n, erased):
    er = set(erased)
    # An erased edge i separates vertices i and i+1; follow every gap
    edges = sorted(er)
    assert edges
    sizes = [((edges[(j+1) % len(edges)]-edges[j]-1) % n)+1 for j in range(len(edges))]
    assert sum(sizes) == n
    return sizes


def mul_poly(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def predicted(n, erased):
    out=[1]
    for v in path_sizes(n,erased):
        out=mul_poly(out,[2**v-2,1])
    return out


def brute(n, erased):
    kept=[i for i in range(n) if i not in erased]
    fibers=Counter()
    for x in product(range(2),repeat=n):
        y=tuple(x[i]+x[(i+1)%n] for i in kept)
        fibers[y]+=1
    result=[0]*(len(erased)+1)
    for size in fibers.values():
        assert size > 0 and size & (size-1)==0
        result[size.bit_length()-1]+=1
    return result


def composition_sum_polynomial(n,e):
    # Sum over positive ordered compositions v_1+...+v_e=n.
    total=[0]*(e+1)
    def recur(part,left):
        if len(part)==e-1:
            sizes=part+[left]
            p=[1]
            for v in sizes:p=mul_poly(p,[2**v-2,1])
            for i,a in enumerate(p):total[i]+=a
            return
        for v in range(1,left-(e-len(part)-1)+1):recur(part+[v],left-v)
    recur([],n)
    # Mark an erased edge; each mask counted e times after choosing n anchors.
    assert all((n*x)%e==0 for x in total)
    return [n*x//e for x in total]


def arithmetic_extremes(n,e):
    a,r=divmod(n,e)
    return (2**(n-e+1)-1,(2**a-1)**(e-r)*(2**(a+1)-1)**r)


def main():
    direct_cases=0
    word_instances=0
    isolated_mask_cases=0
    for n in range(3,11):
        for e in range(1,n+1):
            collective=[0]*(e+1)
            capacities=[]
            for er in combinations(range(n),e):
                pred=predicted(n,er)
                direct=brute(n,set(er))
                assert pred==direct,(n,er,pred,direct)
                for i,x in enumerate(pred):collective[i]+=x
                capacities.append(sum(pred))
                assert sum((2**i)*count for i,count in enumerate(pred))==2**n
                assert pred[-1]==1
                has_singletons=pred[0]>0
                no_adjacent=all((i+1)%n not in er for i in er)
                assert has_singletons==no_adjacent
                isolated_mask_cases += not no_adjacent
                direct_cases+=1
                word_instances+=2**n
            expected=composition_sum_polynomial(n,e)
            assert collective==expected,(n,e,collective,expected)
            no_neighbor_masks=sum(all((i+1)%n not in E for i in E) for E in combinations(range(n),e))
            expected_masks=n*comb(n-e-1,e-1)//e if 2*e<=n else 0
            assert no_neighbor_masks==expected_masks,(n,e,no_neighbor_masks,expected_masks)
            low,high=arithmetic_extremes(n,e)
            assert min(capacities)==low and max(capacities)==high,(n,e,min(capacities),max(capacities),low,high)
            # The whole distribution across masks has the correct number of outputs and source mass.
            assert sum(2**i*count for i,count in enumerate(collective))==comb(n,e)*2**n
    print(f'VERIFY_OK n=3..10 all_masks={direct_cases} direct_source_instances={word_instances} adjacent_erasures={isolated_mask_cases} algebraic_sums_extrema_and_birthday_counts=all')

if __name__=='__main__':main()
