#!/usr/bin/env python3
"""Exact Rayleigh certificates for one-defect random-cluster K_{3,3}.
Usage: python verify.py [CERTIFICATE.json]
Requires Python 3.9+ standard library only.
"""
import itertools,json,sys
from collections import defaultdict
from pathlib import Path
from fractions import Fraction

EDGES=[(i,j) for i in range(3) for j in range(3,6)]

def components(mask):
    parent=list(range(6))
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for index,(i,j) in enumerate(EDGES):
        if mask&(1<<index):
            parent[root(i)]=root(j)
    return len({root(i) for i in range(6)})

COMPONENTS=tuple(components(mask) for mask in range(512))

def product(a,b):
    out=defaultdict(int)
    for (q,v,w),x in a.items():
        for (r,s,t),y in b.items():
            out[(q+r,v+s,w+t)]+=x*y
    return {e:c for e,c in out.items() if c}

def rayleigh(e,f):
    # Four constrained sums with activities of the two marked edges removed.
    blocks=[defaultdict(int) for _ in range(4)]
    for mask,k in enumerate(COMPONENTS):
        xy=((mask>>e)&1)+2*((mask>>f)&1)
        vcount=(mask & ~((1<<e)|(1<<f)|1)).bit_count()
        wcount=((mask&1)!=0) if 0 not in (e,f) else 0
        blocks[xy][(k,vcount,int(wcount))]+=1
    difference=defaultdict(int,product(blocks[1],blocks[2]))
    for ex,c in product(blocks[0],blocks[3]).items():
        difference[ex]-=c
    difference={ex:c for ex,c in difference.items() if c}
    # Exact coefficient division by q^2(1-q) in Z[q,v,w].
    by_vw=defaultdict(dict)
    for (q,v,w),c in difference.items():
        by_vw[v,w][q]=c
    quotient={}
    for (v,w),qpoly in by_vw.items():
        running=0
        for degree in range(max(qpoly)-1):
            running+=qpoly.get(degree+2,0)
            if running:
                quotient[(degree,v,w)]=running
    reconstructed=defaultdict(int)
    for (q,v,w),c in quotient.items():
        reconstructed[q+2,v,w]+=c
        reconstructed[q+3,v,w]-=c
    assert {ex:c for ex,c in reconstructed.items() if c}==difference, (e,f,'factorization')
    assert quotient and all(c>0 for c in quotient.values()),(e,f,'positivity')
    return quotient

def table():
    grouped={}
    for e in range(9):
        for f in range(e+1,9):
            polynomial=rayleigh(e,f)
            key=tuple(sorted(polynomial.items()))
            grouped.setdefault(key,[]).append([e,f])
    rows=[]
    for orbit,(key,pairs) in enumerate(grouped.items(),1):
        rows.append({'orbit':orbit,'representative':pairs[0], 'pairs':pairs,
                     'positive_monomials':len(key),
                     'coefficients':[[*powers,value] for powers,value in key]})
    return {'model':'Random-cluster K3,3, marked edge 0, other edges equal activity',
            'variable_order':['q','v','w'],
            'factor':'F10*F01-F00*F11=q^2*(1-q)*C',
            'edge_index':[list(edge) for edge in EDGES],'pair_count':36,'orbits':rows}

def count_exact_numerator(q,v,w,e,f):
    # Independent exact weighted probabilities using 512 raw configurations.
    Z=E=F=EF=Fraction(0)
    x=[w]+[v]*8
    for mask,k in enumerate(COMPONENTS):
        wt=q**k
        for i in range(9):
            if mask&(1<<i): wt*=x[i]
        Z+=wt
        if mask&(1<<e): E+=wt
        if mask&(1<<f): F+=wt
        if mask&(1<<e) and mask&(1<<f): EF+=wt
    return E*F-EF*Z,Z

def evaluate(poly,q,v,w):
    return sum(c*q**a*v**b*w**d for (a,b,d),c in poly.items())

def main():
    actual=table()
    source=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('CERTIFICATE.json')
    if len(sys.argv)>1 and sys.argv[1]=='--generate':
        Path('CERTIFICATE.json').write_text(json.dumps(actual,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
        return
    reference=json.loads(source.read_text())
    assert actual==reference,'Certificate differs from full exact enumeration'
    assert len(actual['orbits'])==8
    assert sorted(len(g['pairs']) for g in actual['orbits'])==[2,2,4,4,4,4,8,8]
    checks=0
    for e,f in itertools.combinations(range(9),2):
        poly=rayleigh(e,f)
        for q,v,w in [(Fraction(1,3),Fraction(2,5),Fraction(3,4)),
                      (Fraction(1,2),Fraction(3,2),Fraction(1,4)),
                      (Fraction(2,3),Fraction(1,2),Fraction(4,3))]:
            numerator,Z=count_exact_numerator(q,v,w,e,f)
            assert Z>0 and numerator>0
            assert numerator==([w]+[v]*8)[e]*([w]+[v]*8)[f]*q**2*(1-q)*evaluate(poly,q,v,w)
            checks+=1
    print('K33_ONE_DEFECT_SYMBOLIC_CERTIFICATE_PASSED 36 PAIRS 8 ORBITS',checks,'RATIONAL_MOMENT_CHECKS')

if __name__=='__main__':
    main()
