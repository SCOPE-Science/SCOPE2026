#!/usr/bin/env python3
"""Exact inverse-diameter census for six-element triple sumsets.
All integer sets are translated to include 0 as the least point.
"""
from itertools import combinations
import time

def profile(k,D):
    m={}; witness={}; maxext=[]; examined=0
    for five in combinations(range(1,D+1), k-1):
        A=(0,)+five
        bits=sum(1<<x for x in A)
        two=0
        for x in A: two |= bits<<x
        three=0
        for x in A: three |= two<<x
        size=three.bit_count()
        examined+=1
        if size not in m or A[-1]<m[size]:
            m[size]=A[-1]; witness[size]=A
        if size==k*(k+1)*(k+2)//6 and A[-1]==D:
            maxext.append(A)
    return m,witness,examined,maxext

if __name__=='__main__':
    t=time.monotonic()
    m,w,exam,ext=profile(6,45)
    assert exam==1221759, exam
    assert sorted(m)==[16]+list(range(18,57))
    expect=[5,6,6,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,13,13,14,15,14,15,16,17,18,19,19,21,21,24,24,27,30,33,38,45]
    assert [m[s] for s in sorted(m)]==expect,[(s,m[s]) for s in sorted(m)]
    assert ext==[(0,2,11,26,42,45),(0,3,19,34,43,45)]
    assert m[40]==15 and m[41]==14
    print('SIX_EXACT',exam,'spectra',len(m),'N_3_6',max(m.values())+1,'optimal_endpoint',max(m.values()),'extremizers',ext,'time_s',round(time.monotonic()-t,3))
    # Controls: small cardinality profiles, including a known non-monotone case at k=4.
    for k,D in ((3,4),(4,11),(5,23)):
        mm,_,num,_=profile(k,D)
        print('SMALL_ORDER_CONTROL',k,'n_sets',num,'n_spectra',len(mm),'inverse_profile', sorted(mm.items()))
    print('VERIFY_OK exact_finite_enumeration=True global_spectrum_from_Rajagopal=True')
