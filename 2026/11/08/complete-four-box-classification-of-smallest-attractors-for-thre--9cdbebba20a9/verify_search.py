#!/usr/bin/env python3
"""Independent exhaustive branch-and-cover search for Tribonacci attractors.

Enumerates distinct factors via their *position coverage* masks and branches
only at positions that hit a currently unhit factor. This is complete for
hitting sets of size three. Standard library only.
"""
from itertools import product
from verify_direct import BOXES, COUNTS, FACTORS, LENGTHS, tribonacci, explicit_boxes


def position_coverages(word):
    n = len(word)
    cov = {}
    for length in range(1,n+1):
        for start in range(n-length+1):
            label=(length,word[start:start+length])
            cov[label] = cov.get(label,0) | (((1<<length)-1)<<start)
    return sorted(cov.values(),key=int.bit_count)


def branch_search(word):
    masks=position_coverages(word)
    n=len(word)
    hits=[0]*n
    for fid, mask in enumerate(masks):
        while mask:
            least=mask & -mask
            at=least.bit_length()-1
            hits[at]|=1<<fid
            mask-=least
    full=(1<<len(masks))-1
    found=set()
    leaves=0
    def dfs(chosen, covered):
        nonlocal leaves
        if covered == full:
            if len(chosen)==3:
                found.add(tuple(sorted(chosen)))
            return
        if len(chosen)==3:
            leaves+=1
            return
        remaining=full & ~covered
        first=(remaining & -remaining).bit_length()-1
        choices=masks[first]
        while choices:
            bit=choices & -choices
            p=bit.bit_length()-1
            choices-=bit
            if p not in chosen:
                dfs(chosen+(p,), covered|hits[p])
    dfs((),0)
    return len(masks),found,leaves


def main():
    for order in (8,9,10):
        word=tribonacci(order)
        assert len(word)==LENGTHS[order]
        factor_count,actual,failures=branch_search(word)
        assert factor_count==FACTORS[order]
        assert actual==explicit_boxes(order)
        assert len(actual)==COUNTS[order]
        print(f'order={order} length={len(word)} factors={factor_count} '
              f'optimal_triples={len(actual)} pruned_terminal_branches={failures} PASS')

if __name__=='__main__':main()
