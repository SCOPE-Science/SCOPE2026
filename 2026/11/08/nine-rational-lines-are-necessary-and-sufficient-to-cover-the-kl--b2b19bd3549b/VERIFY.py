#!/usr/bin/env python3
"""Exact finite-field certificate for the Klein quartic over F_31.
No third-party packages, network requests, external data, or precomputed tables.
Usage: python3 VERIFY.py
"""
from itertools import product
P=31
WITNESS=[(0,1,30),(1,0,11),(1,1,26),(1,5,25),(1,13,3),
         (1,16,26),(1,18,27),(1,23,23),(1,26,0)]

def normalize(coords):
    for a in coords:
        if a:
            s=pow(a,-1,P)
            return tuple((v*s)%P for v in coords)
    raise ValueError('zero vector')

# Every F_31-rational projective point/line has one unique normalized triple.
projective=sorted({normalize(v) for v in product(range(P),repeat=3) if any(v)})
assert len(projective)==P*P+P+1==993
curve=[(x,y,z) for x,y,z in projective if (pow(x,3,P)*y+pow(y,3,P)*z+pow(z,3,P)*x)%P==0]
assert len(curve)==32

# Exhaustive incidence of all 993 rational lines with all 32 rational curve points.
linebits={}
for a,b,c in projective:
    mask=sum((1<<i) for i,(x,y,z) in enumerate(curve)
             if (a*x+b*y+c*z)%P==0)
    linebits[(a,b,c)]=mask
spectrum={t:sum(mask.bit_count()==t for mask in linebits.values()) for t in range(5)}
assert spectrum=={0:354,1:334,2:256,3:18,4:31},spectrum
assert sum(spectrum.values())==993

# Explicit nine-line cover: every curve point lies on at least one displayed line.
assert all(w in linebits for w in WITNESS)
assert len(WITNESS)==9
covered=0
for line in WITNESS:
    covered|=linebits[line]
assert covered==(1<<32)-1

# A cover by 8 lines would use eight pairwise disjoint 4-secants.
# This exact exhaustive depth-first search enumerates every such disjoint family,
# choosing indices strictly increasingly and restricting to disjoint successors.
quads=[mask for mask in linebits.values() if mask.bit_count()==4]
assert len(quads)==31
successors=[sum(1<<j for j in range(i+1,len(quads))
                if not (mask & quads[j])) for i,mask in enumerate(quads)]
counts=[0]*32

def search(available,depth):
    counts[depth]+=1
    while available:
        low=available & -available
        i=low.bit_length()-1
        available^=low
        search(available & successors[i],depth+1)

search((1<<len(quads))-1,0)
assert counts[:8]==[1,31,270,804,805,207,3,0],counts
assert sum(counts)==2121
print('KLEIN_F31_FULL_PROJECTIVE_INCIDENCE_OK: 993 lines, 32 curve points')
print('FOUR_SECANT_PACKING_CERTIFICATE_OK: 31 four-secants, maximum disjoint family 6')
print('MINIMUM_RATIONAL_LINE_COVER_OK: 9 explicit lines, 8 impossible')
