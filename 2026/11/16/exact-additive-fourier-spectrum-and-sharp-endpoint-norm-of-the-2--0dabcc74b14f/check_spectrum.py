"""Independent integer and Fourier checks for the 2x2x2 Segre-cone projection.

The test enumerates rank-one tensors in three prime fields and in F4,
checks their complete Fourier multiplicity distribution, and enumerates
projective kernel intersections with the 2x2 rank-one quadric.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
import numpy as np


def predicted(q):
    gl2 = (q*q-1)*(q*q-q)
    ans = Counter()
    ans[0] = q*q*(q-1)**2*gl2//2
    ans[1] = (q+1)**2*(q-1)*gl2
    ans[2] = q*q*(q+1)**2*gl2//2
    ans[q+1] = 2*(q+1)*gl2 + q*(q*q-1)**2
    ans[2*q+1] = (q+1)**2*(q*q-1)
    ans[(q+1)**2] = 1
    assert sum(ans.values()) == q**8
    return Counter({q*(q*b-q-2): n for b,n in ans.items()})


def predicted_norm(q):
    return Fraction(q**8-q**7+q**6+6*q**5-11*q**4-5*q**3+14*q**2-4,q**6)


def rank_one_tensor(c, mul):
    u,v,w=c
    return tuple(mul(mul(a,b),d) for a in u for b in v for d in w)


def gf4_mul(a,b):
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: z^=1<<(i+j)
    if z&8: z^=0b1100  # x^3 = x^2+x mod x^2+x+1
    if z&4: z^=0b111   # x^2 = x+1
    return z


def measure(q):
    if q==4:
        mul=gf4_mul
    else:
        mul=lambda a,b:(a*b)%q
    elems=range(q)
    vectors=list(product(elems,repeat=2))
    C={rank_one_tensor((u,v,w),mul) for u in vectors for v in vectors for w in vectors}
    assert len(C)==q**4+2*q**3-2*q
    if q==4:
        data=np.zeros(1<<16,dtype=np.int64)
        for x in C:
            k=sum(int(xi)<<(2*i) for i,xi in enumerate(x))
            data[k]=1
        # Exact integer Walsh-Hadamard on the binary representation.
        for bit in range(16):
            block=1<<bit
            ar=data.reshape(-1,block*2)
            left=ar[:,:block].copy()
            right=ar[:,block:].copy()
            ar[:,:block]=left+right
            ar[:,block:]=left-right
        values=Counter(map(int,data))
    else:
        data=np.zeros((q,)*8,dtype=np.int64)
        for x in C:data[x]=1
        spectrum=np.fft.fftn(data)
        assert max(abs(z.imag) for z in spectrum.flat)<1e-7
        values=Counter(int(round(float(z.real))) for z in spectrum.flat)
        assert max(abs(z.real-round(z.real)) for z in spectrum.flat)<1e-7
    expected=predicted(q)
    assert values==expected,(q,values,expected)
    norm=Fraction(sum(abs(x)*n for x,n in values.items()),q**8)
    assert norm==predicted_norm(q),(q,norm,predicted_norm(q))
    assert sum(x*n for x,n in values.items())==q**8
    assert sum(x*x*n for x,n in values.items())==q**8*len(C)
    print(f'FIELD q={q} size={len(C)} levels={sorted(values.items())} endpoint={norm} support={q**8-values.get(0,0)} PASS')


def rowspace_pairs(q):
    # All 2-subspaces as RREF row pairs in Fq^4.
    for p in range(4):
        for r in range(p+1,4):
            free1=[j for j in range(p+1,4) if j!=r]
            free2=list(range(r+1,4))
            for a in product(range(q),repeat=len(free1)+len(free2)):
                x=[0]*4;y=[0]*4
                x[p]=1;y[r]=1
                for j,t in zip(free1,a[:len(free1)]):x[j]=t
                for j,t in zip(free2,a[len(free1):]):y[j]=t
                yield tuple(x),tuple(y)


def projective_points(q):
    for p in range(4):
        for rest in product(range(q),repeat=3-p):
            yield (0,)*p+(1,)+rest


def check_geometry(q):
    Q=[v for v in projective_points(q) if (v[0]*v[3]-v[1]*v[2])%q==0]
    assert len(Q)==(q+1)**2
    def B(u):
        return sum(all(sum(a*b for a,b in zip(r,x))%q==0 for r in u) for x in Q)
    rank2=Counter(B(pair) for pair in rowspace_pairs(q))
    allp=list(projective_points(q))
    rank1=Counter(B((h,)) for h in allp)
    expected2=Counter({0:q*q*(q-1)**2//2,1:(q+1)**2*(q-1),2:q*q*(q+1)**2//2,q+1:2*(q+1)})
    expected1=Counter({q+1:q*(q*q-1),2*q+1:(q+1)**2})
    assert rank2==expected2,(q,rank2,expected2)
    assert rank1==expected1,(q,rank1,expected1)
    print(f'GEOMETRY q={q} line_sections={dict(sorted(rank2.items()))} plane_sections={dict(sorted(rank1.items()))} PASS')


if __name__=='__main__':
    for q in (2,3,4,5):measure(q)
    for q in (2,3,5,7):check_geometry(q)
    print('SEGRE_FULL_SPECTRUM_AND_ENDPOINT_CHECKS_PASS')
