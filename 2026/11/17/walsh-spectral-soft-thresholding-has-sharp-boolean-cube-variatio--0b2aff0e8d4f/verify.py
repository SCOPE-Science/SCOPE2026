"""Exact rational verifier of hypercube Walsh soft-threshold variation bounds.
Run with Python >=3.9; no external packages.
"""
from fractions import Fraction
from itertools import combinations
import random

def parity(x):return x.bit_count()%2

def vals(mask,d):
    N=1<<d
    return [sum((-1)**parity(s&x) for s in range(1,N) if (mask>>(s-1))&1) for x in range(N)]

def projection(mask,vec,d):
    N=1<<d
    cf=[sum((-1)**parity(s&x)*vec[x] for x in range(N)) for s in range(1,N)]
    return [Fraction(sum(((-1)**parity(s&x))*cf[s-1] for s in range(1,N) if (mask>>(s-1))&1),N) for x in range(N)]

def variation(vec,d):
    N=1<<d
    return sum(abs(vec[x]-vec[x^(1<<i)]) for x in range(N) for i in range(d) if x<(x^(1<<i)))

def exact_cut_exhaust(d):
    N=1<<d
    best=Fraction(0)
    bestparams=None
    cuts=[ [int((B>>x)&1) for x in range(N)] for B in range(1,(1<<N)-1) ]
    for mask in range(1<<(N-1)):
        for B,cut in enumerate(cuts,1):
            val=variation(projection(mask,cut,d),d)/variation(cut,d)
            if val>best:best,bestparams=val,(mask,B)
    return best,bestparams

def soft(mask,base,pert,d,lamb=Fraction(1)):
    N=1<<d
    coeff=[sum(Fraction(((-1)**parity(s&x)))*pert[x] for x in range(N))/N for s in range(N)]
    c=[base[s]+coeff[s] for s in range(N)]
    out=[ (c[s]-lamb if c[s]>lamb else c[s]+lamb if c[s]<-lamb else 0) if s else c[s] for s in range(N)]
    return [sum(Fraction((-1)**parity(s&x))*out[s] for s in range(N)) for x in range(N)]

def main():
    for d in range(1,4):
        best,(mask,B)=exact_cut_exhaust(d)
        N=1<<d
        # Verify attained exactly with two inputs lying in same active spectral chamber.
        data=[Fraction(int((B>>x)&1),1000) for x in range(N)]
        base=[Fraction(0)]+[Fraction(2) if mask>>(s-1)&1 else Fraction(0) for s in range(1,N)]
        initial=soft(mask,base,[Fraction(0)]*N,d)
        shifted=soft(mask,base,data,d)
        ratio=variation([a-b for a,b in zip(shifted,initial)],d)/variation(data,d)
        assert ratio==best,(d,best,ratio)
        assert best >= 1 and best*best <= N
        print('EXACT_ALL_MASKS_ALL_CUTS_AND_NONLINEAR_ATTAINMENT_PASS',d,str(best),mask,B)
    # Mask and single-vertex witnesses: exact integer arithmetic for d=4 through 9.
    rng=random.Random(20261114)
    for d in (4,5,6,7,8,9):
        N=1<<d
        top=Fraction(0); bestmask=0
        for j in range(110 if d<7 else 40):
            mask=rng.getrandbits(N-1)
            k=vals(mask,d)
            edge_sum=sum(abs(k[x]-k[x^(1<<i)]) for x in range(N) for i in range(d) if x<(x^(1<<i)))
            ratio=Fraction(edge_sum,N*d)
            if ratio>top:top,bestmask=ratio,mask
            assert ratio*ratio<=N
        if d>=5:
            assert top>1,(d,top)
        print('EXACT_BINARY_MASK_IMPULSE_BV_WITNESSES_PASS',d,str(top),bestmask.bit_count())
    print('ALL_WALSH_CUBE_BV_CHECKS_PASS')
if __name__=='__main__':main()
