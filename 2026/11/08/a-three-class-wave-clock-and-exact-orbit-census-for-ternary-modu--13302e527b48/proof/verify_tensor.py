#!/usr/bin/env python3
"""Exact-integer recurrence check for modular Hamming adjacency Jordan counts."""
for m in range(3,31,3):
    a,b,c=1,0,0
    for d in range(1,41):
        a,b,c=(m-2)*a+b,a+(m-2)*b,b+m*c
        af=((m-1)**d+(m-3)**d)//2
        bf=((m-1)**d-(m-3)**d)//2
        cf=(m**d-af-2*bf)//3
        assert (a,b,c)==(af,bf,cf) and a+2*b+3*c==m**d
        assert a>=0 and b>=0 and c>=0
print('ALL INTEGER TENSOR CHECKS PASSED: 10 alphabet sizes x 40 dimensions')
