#!/usr/bin/env python3
"""Exact sixth Fourier moments for seven triangular-lattice sites.

Dependency-free verification: two independent constructions of the Laurent
coefficients, exact cyclotomic arithmetic, exhaustive normalized phase inputs.
"""
from collections import Counter, defaultdict
from functools import cmp_to_key
from itertools import product, combinations_with_replacement
from math import factorial

SITES=((0,0),(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1))
POLYS={2:(1,1),3:(1,1,1),4:(1,0,1),5:(1,1,1,1,1),6:(1,-1,1)}


def basis_power(q,k):
    f=POLYS[q]; degree=len(f)-1
    # Horner-like reduction of x^k in Z[x]/(f)
    poly=[1]+[0]*(degree-1)
    for _ in range(k%q):
        poly=[0]+poly
        hi=poly.pop()
        if hi:
            for j in range(degree): poly[j]-=hi*f[j]
    return tuple(poly)


def sum_vectors(vectors):
    return tuple(sum(z[j] for z in vectors) for j in range(len(vectors[0])))


def convolution_triples():
    # Ordered expansion: the coefficient of a point in P^3 is a sum of
    # exactly as many terms as ordered triples of the original frequencies.
    fibers=defaultdict(list)
    for i,j,k in product(range(7),repeat=3):
        point=(SITES[i][0]+SITES[j][0]+SITES[k][0],
               SITES[i][1]+SITES[j][1]+SITES[k][1])
        fibers[point].append((i,j,k))
    assert sum(len(x) for x in fibers.values())==343
    assert len(fibers)==37
    return fibers


def laurent_differences():
    # Independent unordered multinomial construction of the coefficients
    # of P^3, followed by expansion of its modulus square.
    fibers=defaultdict(Counter)
    for triple in combinations_with_replacement(range(7),3):
        pt=(sum(SITES[i][0] for i in triple),sum(SITES[i][1] for i in triple))
        m=6
        for v in Counter(triple).values():m//=factorial(v)
        fibers[pt][triple]=m
    assert len(fibers)==37
    spectrum=Counter()
    for terms in fibers.values():
        for a,ma in terms.items():
            for b,mb in terms.items():
                diff=tuple(a.count(i)-b.count(i) for i in range(3,7))
                spectrum[diff]+=ma*mb
    assert sum(spectrum.values())==5881
    return spectrum


def phase_moment_direct(fibers,q,sequence,roots):
    phases=(0,0,0)+sequence
    total=[0]*(len(POLYS[q])-1)
    for triples in fibers.values():
        counts=[0]*q
        for i,j,k in triples:
            counts[(phases[i]+phases[j]+phases[k])%q]+=1
        for r,nr in enumerate(counts):
            if not nr:continue
            for s,ns in enumerate(counts):
                if not ns:continue
                vec=roots[(r-s)%q]
                for i,v in enumerate(vec):total[i]+=nr*ns*v
    return tuple(total)


def phase_moment_laurent(spectrum,q,sequence,roots):
    total=[0]*(len(POLYS[q])-1)
    for e,count in spectrum.items():
        vec=roots[sum(v*w for v,w in zip(e,sequence))%q]
        for i,v in enumerate(vec):total[i]+=count*v
    return tuple(total)


def real_key(q,vec):
    if q==5:
        # Real subfield: M=A+B*(sqrt(5)-1)/2.
        # (A-B,0,-B,-B) is its representation mod Phi_5.
        assert len(vec)==4 and vec[1]==0 and vec[2]==vec[3]
        B=-vec[2];A=vec[0]+B
        return A,B
    assert all(v==0 for v in vec[1:]),(q,vec)
    return (vec[0],0)


def compare_keys(x,y):
    A=x[0]-y[0];B=x[1]-y[1]
    # Exact comparison of A+B*(sqrt(5)-1)/2 against zero.
    u=2*A-B
    if not u:return (B>0)-(B<0)
    if not B:return (u>0)-(u<0)
    if (u>0)==(B>0):return (u>0)-(u<0)
    return ((u>0)-(u<0)) if u*u>5*B*B else ((B>0)-(B<0))


EXPECTED={
    2:((649,0),3,(1081,0)),
    3:((913,0),6,(1084,0)),
    4:((649,0),3,(841,0)),
    5:((1417,-1038),6,(1387,-978)),
    6:((649,0),3,(757,0)),
}


def check():
    fibers=convolution_triples()
    spectrum=laurent_differences()
    results={}
    for q in (2,3,4,5,6):
        roots=[basis_power(q,r) for r in range(q)]
        hits=Counter()
        minimizers=defaultdict(list)
        for sequence in product(range(q),repeat=4):
            a=phase_moment_direct(fibers,q,sequence,roots)
            b=phase_moment_laurent(spectrum,q,sequence,roots)
            assert a==b,(q,sequence,a,b)
            k=real_key(q,a)
            hits[k]+=1
            minimizers[k].append(sequence)
        keys=sorted(hits,key=cmp_to_key(compare_keys))
        low,expected_count,second=EXPECTED[q]
        assert keys[0]==low and hits[low]==expected_count
        assert keys[1]==second
        assert keys[-1]==(5881,0) and hits[(5881,0)]==1
        assert sum(hits.values())==q**4
        results[q]={"minimum":low,"count_normalized":hits[low],
                    "second":second,"max":keys[-1],
                    "minimizers":sorted(minimizers[low]),
                    "distinct_values":len(hits)}
    assert results[5]['minimizers']==[
        (0,2,0,3),(0,3,0,2),(2,0,3,0),
        (2,3,3,2),(3,0,2,0),(3,2,2,3)]
    print('HEXAGON_SEVEN_L6_ALPHABETS_PASS')
    for q,v in results.items():print(q,v)
    return results

if __name__=='__main__':check()
