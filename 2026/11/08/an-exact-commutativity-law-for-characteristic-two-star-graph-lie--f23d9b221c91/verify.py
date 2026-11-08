"""Reproduce the commuting-pair count for graph-defined star Lie algebras in characteristic two.

Run: python3 verify.py
Dependencies: Python standard library only. No external input files.
The exhaustive tests enumerate the noncentral coordinates; central coordinates
are absent from brackets and cancel in commuting probabilities.
"""
from itertools import product
from fractions import Fraction

POLYS = {2: 0b11, 4: 0b111, 8: 0b1011}

def multiplication(q):
    assert q in POLYS
    degree=q.bit_length()-1
    mask=q-1
    poly=POLYS[q]
    table=[]
    for a in range(q):
        row=[]
        for b in range(q):
            aa=a; bb=b; v=0
            while bb:
                if bb&1: v ^=aa
                aa <<=1
                if aa&q: aa ^=poly
                bb >>=1
            row.append(v&mask)
        table.append(row)
    for a in range(1,q):
        assert sorted(table[a])==list(range(q))
    return table

def wedged(u,v,mul):
    return tuple(mul[u[i]][v[j]] ^ mul[u[j]][v[i]]
                 for i in range(len(u)) for j in range(i+1,len(u)))

def derived_formula(q,m):
    z=q**m
    count=2*q*q*(q+1)*z*z - q*q*(q+1)**2*z + q**4
    p=Fraction(count,q**(2+4*m))
    assert p==2*Fraction(q+1,q**(2*m))-Fraction((q+1)**2,q**(3*m))+Fraction(q*q,q**(4*m))
    return count,p

def fiber_enumeration(q,m):
    mul=multiplication(q)
    vs=list(product(range(q),repeat=m))
    hist={}
    for u in vs:
        for b in vs:
            z=wedged(u,b,mul)
            hist[z]=hist.get(z,0)+1
    origin=(0,)*(m*(m-1)//2)
    nzero=hist[origin]
    assert nzero==(q+1)*q**m-q
    assert all(count==q*(q*q-1) for z,count in hist.items() if z!=origin)
    # An arbitrary nonzero decomposable bivector uniquely determines a 2-plane.
    nonzero_count=(q**m-1)*(q**m-q)//(q*(q*q-1))
    assert len(hist)==nonzero_count+1
    zero_hub=sum(v*v for v in hist.values())
    nonzero_hub=(q*q-1)*q**m*nzero
    count,p=derived_formula(q,m)
    assert zero_hub+nonzero_hub==count
    return count, p, len(hist), len(vs)**2

def brute(q,m):
    mul=multiplication(q)
    vs=list(product(range(q),repeat=m)); zero=(0,)*m
    cache={(u,b):wedged(u,b,mul) for u in vs for b in vs}
    elements=list(product(range(q),vs,vs))
    total=0
    for t,u,a in elements:
        for s,v,b in elements:
            lhs=tuple(mul[t][v[i]]^mul[s][u[i]] for i in range(m))
            if lhs!=zero: continue
            if cache[(u,b)]==cache[(v,a)]:total+=1
    assert total==derived_formula(q,m)[0], (q,m,total,derived_formula(q,m)[0])
    return total, len(elements)**2

def main():
    direct_pairs=0
    fibers=0
    for q,m in [(2,2),(2,3),(2,4),(4,2)]:
        count,examined=brute(q,m)
        direct_pairs+=examined
        print('DIRECT',q,m,'pairs',examined,'commuting',count)
    for q,m in [(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3)]:
        count,p,images,examined=fiber_enumeration(q,m)
        fibers+=examined
        print('FIBER',q,m,'wedges',examined,'distinct_images',images,'commuting',count,'probability',p)
    for q in (2,4,8,16,32,64):
        for m in range(2,13):
            c,p=derived_formula(q,m)
            assert 0<c<=q**(2+4*m) and 0<p<=1
    print('VERIFY_OK direct_pairs=',direct_pairs,'wedge_pairs=',fibers,'formula_checks=',6*11)

if __name__=='__main__': main()
