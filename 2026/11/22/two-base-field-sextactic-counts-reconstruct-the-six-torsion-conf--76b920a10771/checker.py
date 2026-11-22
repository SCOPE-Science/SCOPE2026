#!/usr/bin/env python3
"""Exact finite torsion/geometry checks for universal cubic sextactic configurations.
Python 3 standard library only; no external software or unpublished records required.
"""
import csv, sys, itertools
from collections import Counter, defaultdict

# Chinese-remainder coordinates for E[6] = F_2^2 x F_3^2.
P=[(a,b,c,d) for a,b in ((0,1),(1,0),(1,1))
   for c in range(3) for d in range(3)]
INDEX={p:i for i,p in enumerate(P)}

def addzero(indices):
    return (sum(P[i][0] for i in indices)%2 == 0 and
            sum(P[i][1] for i in indices)%2 == 0 and
            sum(P[i][2] for i in indices)%3 == 0 and
            sum(P[i][3] for i in indices)%3 == 0)

# The unique cubic line through 3 distinct sextactic points exists iff sum=0.
LINE={frozenset(t) for t in itertools.combinations(range(27),3) if addzero(t)}
# The unique conic through 6 distinct sextactic points exists iff sum=0.
CONIC={frozenset(t) for t in itertools.combinations(range(27),6) if addzero(t)}
# A conic is geometrically reducible iff it is a union of two distinct trisecants.
RED=set()
for a,b in itertools.combinations(LINE,2):
    if not (a&b):
        RED.add(a|b)
assert len(LINE)==81 and len(CONIC)==8244
assert RED<=CONIC and len(RED)==2268
SMOOTH=CONIC-RED
assert len(SMOOTH)==5976

def gl_classes(p):
    matrices=[(a,b,c,d) for a,b,c,d in itertools.product(range(p),repeat=4)
              if (a*d-b*c)%p]
    def mul(A,B):
        a,b,c,d=A;e,f,g,h=B
        return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
    def inv(A):
        a,b,c,d=A;z=pow((a*d-b*c)%p,-1,p)
        return (d*z%p,-b*z%p,-c*z%p,a*z%p)
    remaining=set(matrices)
    reps=[]
    while remaining:
        r=min(remaining)
        C={mul(mul(b,r),inv(b)) for b in matrices}
        assert C<=remaining or not C.isdisjoint(remaining)
        remaining-=C
        reps.append((r,len(C)))
    assert sum(c for r,c in reps)==len(matrices)
    return reps
C2=gl_classes(2)
C3=gl_classes(3)
assert len(C2)==3 and len(C3)==8
assert sum(z for a,z in C2)==6 and sum(z for a,z in C3)==48

def induced(A,B):
    a,b,c,d=A;e,f,g,h=B
    return [INDEX[((a*u+b*v)%2,(c*u+d*v)%2,(e*x+f*y)%3,(g*x+h*y)%3)]
            for u,v,x,y in P]

def cyc(F,sets):
    arr=sorted(sets,key=lambda s:tuple(sorted(s)))
    loc={s:i for i,s in enumerate(arr)}
    f=[loc[frozenset(F[j] for j in s)] for s in arr]
    seen=set(); lengths=Counter()
    for i in range(len(arr)):
        if i in seen:continue
        x=i; length=0
        while x not in seen:
            seen.add(x);length+=1;x=f[x]
        assert x==i
        lengths[length]+=1
    assert sum(k*v for k,v in lengths.items())==len(arr)
    return tuple(sorted(lengths.items()))

def numfix(cycles,n):
    return sum(k*v for k,v in cycles if n%k==0)

def notation(cycles):
    return ' '.join('%d^%d'%(length,mult) for length,mult in cycles)

rows=[]; spectral_to_key={}; key_to_spectral={}
for i,(A,n2) in enumerate(C2):
    for j,(B,n3) in enumerate(C3):
        F=induced(A,B)
        pt=cyc(F,{frozenset((x,)) for x in range(27)})
        line=cyc(F,LINE)
        conic=cyc(F,CONIC)
        red=cyc(F,RED)
        smooth=cyc(F,SMOOTH)
        det=(B[0]*B[3]-B[1]*B[2])%3
        p1,l1,c1,r1,s1=(numfix(C,1) for C in [pt,line,conic,red,smooth])
        assert c1==r1+s1
        # Full scheme spectrum, not a name of a conjugacy class.
        spec=(pt,line,conic,red,smooth)
        key=(det,p1,c1)
        old=key_to_spectral.setdefault(key,spec)
        assert old==spec, ('reconstruction failed', key, i,j)
        spectral_to_key.setdefault(spec,key)
        rows.append(dict(id='%d-%d'%(i,j),matrix2=''.join(map(str,A)),matrix3=''.join(map(str,B)),
             class2=n2,class3=n3,det3=det,pts1=p1,lines1=l1,conics1=c1,
             reducible1=r1,smooth1=s1,pts_cycles=notation(pt),lines_cycles=notation(line),
             conics_cycles=notation(conic),red_cycles=notation(red),smooth_cycles=notation(smooth),
             pts2=numfix(pt,2),conics2=numfix(conic,2)))
assert len(rows)==24
assert len(set((r['det3'],r['pts1'],r['conics1']) for r in rows))==19
assert len({(r['pts_cycles'],r['lines_cycles'],r['conics_cycles'],r['red_cycles'],r['smooth_cycles']) for r in rows})==19
assert len(set(r['pts1'] for r in rows))<19
assert len(set(r['conics1'] for r in rows))<19
# The fermat-cubic specializations are independent sanity anchors (all with nine lines).
assert any(r['pts1']==27 and r['lines1']==81 and r['smooth1']==5976 for r in rows)
assert any(r['pts1']==0 and r['lines1']==9 and r['smooth1']==0 for r in rows)
assert any(r['pts1']==3 and r['lines1']==9 and r['smooth1']==22 for r in rows)
if len(sys.argv)>1:
    with open(sys.argv[1],'w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)
print('UNIVERSAL_SEXTACTIC_24_CLASS_19_SPECTRUM_RECONSTRUCTION_VERIFIED')
print('geometric:',len(P),len(LINE),len(CONIC),len(RED),len(SMOOTH))
print('conjugacy classes:',len(C2),len(C3),'representative pairs:',len(rows),'distinct spectra:',len(spectral_to_key))
