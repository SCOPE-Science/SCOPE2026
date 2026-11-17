"""Independent two-pentagon contraction of the classical spin-one state sum."""
from itertools import product
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text())
ring=list(product((-1,0,1),repeat=5))
outer=[];inner=[]
for s in ring:
    k=sum(a*a for a in s);m=sum(s)
    eo=sum(s[i]*s[(i+1)%5] for i in range(5))
    ei=sum(s[i]*s[(i+2)%5] for i in range(5))
    outer.append((s,eo,k,m));inner.append((s,ei,k,m))
C=defaultdict(int)
for a,eo,ka,ma in outer:
    for b,ei,kb,mb in inner:
        e=eo+ei+sum(a[i]*b[i] for i in range(5))
        C[e,ka+kb,ma+mb]+=1
assert sum(C.values())==3**10 and len(C)==318
mi={}
for (e,k,m),count in C.items():
    if m<0:continue
    if (k,m) not in mi or mi[k,m][0]>e:mi[k,m]=[e,count]
    elif mi[k,m][0]==e:mi[k,m][1]+=count
assert len(mi)==36
for r in cert['sector_bounds']:
    assert mi[r['u'],r['m']]==[r['e'],r['count']]
for key,d in [('zero_d_3_4',Fraction(3,4)),('zero_d_1',Fraction(1))]:
    val=min(Fraction(e)+d*k for e,k,m in C)
    assert sum(c for (e,k,m),c in C.items() if Fraction(e)+d*k==val)==cert['zero_field_boundary'][key]['degeneracy']
print('PASS: independent 243 x 243 outer/inner pentagon convolution reproduces all 318 sectors, 36 minima, and critical degeneracies.')
