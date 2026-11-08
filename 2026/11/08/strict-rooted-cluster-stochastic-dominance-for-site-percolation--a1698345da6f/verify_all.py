#!/usr/bin/env python3
"""Compare every integer entry from independently specified counting algorithms."""
from math import comb
from verify_masks import histogram,make_rook,make_shrikhande,evaluate
from verify_boundaries import count_by_boundary,adjacency_rook,adjacency_shrikhande

def main():
    A=histogram(make_rook());B=histogram(make_shrikhande())
    C=count_by_boundary(adjacency_rook());D=count_by_boundary(adjacency_shrikhande())
    assert A==C and B==D
    delta=evaluate()
    assert delta==[[B[k][s]-A[k][s] for s in range(17)] for k in range(17)]
    # 16th-degree Bernstein coefficients of exact mean cluster-size difference.
    coefficients=[sum(s*delta[k][s] for s in range(17)) for k in range(17)]
    expected=[0,0,0,0,12,96,234,126,24]+[0]*8
    assert coefficients==expected
    # The p=1/2 numerator, since every 16-bit site mask then has weight 2^-16.
    assert sum(coefficients)==492
    # For every threshold the full microcanonical Bernstein coefficients
    # of the survival-function difference must be nonnegative.
    for t in range(1,17):
        tail=[sum(delta[k][s] for s in range(t,17)) for k in range(17)]
        assert min(tail)>=0
        if t in range(4,9):
            assert max(tail)>0
        else:
            assert max(tail)==0
    print('PASS: all 578 root histograms agree; exact strict site-cluster stochastic order')

if __name__=='__main__':main()
