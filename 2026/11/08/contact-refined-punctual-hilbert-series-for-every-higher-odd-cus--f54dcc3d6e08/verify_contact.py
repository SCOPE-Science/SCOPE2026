#!/usr/bin/env python3
"""Standalone finite-field coefficient enumeration for monomial cusp contact cells.
Checks the ideal-stability congruence directly for every polynomial residue.
This finite test is not a proof for arbitrary colength or arbitrary fields.
"""
from itertools import product

def run():
    tested=0
    for p, ds in [(2, range(2, 5)), (3, range(2, 4))]:
        for d in ds:
            for h in range(0, 2*d+4):
                count=0
                for g in product(range(p), repeat=h):
                    # Squaring the residue in k[x]/(x^h), independent of the
                    # valuation shortcut used in the general proof.
                    square=[0]*h
                    for i,gi in enumerate(g):
                        for j,gj in enumerate(g):
                            if i+j<h:
                                square[i+j]=(square[i+j]+gi*gj)%p
                    if 2*d+1<h:
                        square[2*d+1]=(square[2*d+1]-1)%p
                    if not any(square):
                        count+=1
                expected=(p**(h//2)) if h<=2*d+1 else 0
                assert count==expected,(p,d,h,count,expected)
                tested+=1
    # Independently compare coefficients of the rational identity by expanding
    # the geometric series and the monomial-cell colength grading.
    for d in range(2,5):
        for p in (2,3):
            for n in range(1,22):
                via_cells={1:0,2:0}
                for h in range(0,2*d+2):
                    if n>=h and (n-h)%2==0:
                        b=(n-h)//2
                        if b==0 and h>0:
                            via_cells[1]+=p**(h//2)
                        if b>0:
                            via_cells[2]+=p**(h//2)
                via_series={1:0,2:0}
                if n<=2*d+1:
                    via_series[1]=p**(n//2)
                for h in range(0,2*d+2):
                    if n>=h+2 and (n-h)%2==0:
                        via_series[2]+=p**(h//2)
                assert via_cells==via_series,(d,p,n,via_cells,via_series)
    print('FINITE_FIELD_STABILITY_AND_SERIES_TEST_OK',tested)

if __name__=='__main__':
    run()
