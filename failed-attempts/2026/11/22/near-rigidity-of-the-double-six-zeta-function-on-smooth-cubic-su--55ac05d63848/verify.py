#!/usr/bin/env python3
"""Exact finite Schlaefli configuration and W(E6) conjugacy-class checker.
Standard library only. Run: python3 verify.py [certificate.csv]"""
from collections import Counter, deque, defaultdict
from itertools import combinations
import csv, os, sys

# All 27 exceptional curves of the blowup of P^2 in six points.
# Vectors (d,m1,...,m6) mean dH - sum m_i E_i.
E=[(0,)+tuple(-int(i==j) for i in range(6)) for j in range(6)]
L=[(1,)+tuple(int(k==i or k==j) for k in range(6)) for i,j in combinations(range(6),2)]
Q=[(2,)+tuple(int(k!=i) for k in range(6)) for i in range(6)]
curves=E+L+Q
assert len(curves)==len(set(curves))==27

def intersect(u,v): return u[0]*v[0]-sum(a*b for a,b in zip(u[1:],v[1:]))
assert all(intersect(c,c)==-1 for c in curves)
roots=[(0,)+tuple(-1 if j==i else 1 if j==i+1 else 0 for j in range(6)) for i in range(5)]
roots.append((1,1,1,1,0,0,0))
assert all(intersect(a,a)==-2 for a in roots)

def refl(v,r): return tuple(a+intersect(v,r)*b for a,b in zip(v,r))
generators=[tuple(curves.index(refl(c,r)) for c in curves) for r in roots]
identity=tuple(range(27))
def mul(a,b): return tuple(a[b[i]] for i in range(27))
assert all(mul(g,g)==identity for g in generators)

# Generate W(E6) exactly by right multiplication.
all_g={identity}; queue=deque([identity]); elements=[]
while queue:
 g=queue.popleft(); elements.append(g)
 for h in generators:
  t=mul(g,h)
  if t not in all_g: all_g.add(t); queue.append(t)
assert len(all_g)==len(elements)==51840

# Independent geometric construction: every sixer is a 6-clique in
# the disjointness graph. Its complementary half is the unique set
# of six curves meeting exactly five of its six members.
skew={(i,j) for i in range(27) for j in range(i+1,27) if intersect(curves[i],curves[j])==0}
sixers={frozenset(t) for t in combinations(range(27),6) if all((i,j) in skew for i,j in combinations(t,2))}
assert len(sixers)==72
partners={}
for a in sixers:
 b=frozenset(j for j in range(27) if sum(intersect(curves[i],curves[j])==1 for i in a)==5)
 assert len(b)==6 and b in sixers and b!=a
 assert {i for j in b for i in a if intersect(curves[i],curves[j])==0}==set(a)
 partners[a]=b
assert all(partners[partners[a]]==a for a in sixers)
double_sixes={frozenset((a,b)) for a,b in partners.items()}
assert len(double_sixes)==36
# Independent orbit-method verification of the 36 double-sixes.
canon=frozenset(range(6)); mate=frozenset(range(21,27))
assert partners[canon]==mate
orbit={frozenset((frozenset(g[i] for i in canon),frozenset(g[i] for i in mate))) for g in elements}
assert orbit==double_sixes

ds=sorted(double_sixes,key=lambda p:tuple(sorted(tuple(sorted(x)) for x in p)))
si={x:i for i,x in enumerate(ds)}

def dsperm(g):
 return tuple(si[frozenset(frozenset(g[j] for j in a) for a in pair)] for pair in ds)

def cycle_type(p):
 seen=set();freq=Counter()
 for i in range(len(p)):
  if i not in seen:
   j=i; n=0
   while j not in seen: seen.add(j); j=p[j]; n+=1
   freq[n]+=1
 return tuple(sorted(freq.items()))

def encoded(c):return ','.join(f'{a}^{b}' for a,b in c)
def fixed(c,n=1):return sum(a*b for a,b in c if n%a==0)

# All conjugacy classes, without reliance on a character table.
def rational_rank(a):
 from fractions import Fraction
 b=[[Fraction(v) for v in row] for row in a]
 n=len(b);m=len(b[0]);rank=0
 for j in range(m):
  pivot=next((i for i in range(rank,n) if b[i][j]),None)
  if pivot is None:continue
  b[rank],b[pivot]=b[pivot],b[rank]
  z=b[rank][j];b[rank]=[v/z for v in b[rank]]
  for i in range(n):
   if i!=rank and b[i][j]:
    z=b[i][j];b[i]=[u-z*v for u,v in zip(b[i],b[rank])]
  rank+=1
 return rank

def picard_data(g):
 k=(-3,)+(-1,)*6
 es=[curves[g[i]] for i in range(6)]
 hs_num=[sum(e[j] for e in es)-k[j] for j in range(7)]
 assert all(u%3==0 for u in hs_num)
 h=tuple(u//3 for u in hs_num)
 columns=[h]+[tuple(-u for u in e) for e in es]
 m=[[columns[j][i] for j in range(7)] for i in range(7)]
 return sum(m[i][i] for i in range(7)),7-rational_rank([[m[i][j]-int(i==j) for j in range(7)] for i in range(7)])

seen=set();rows=[]
for g in elements:
 if g in seen:continue
 q=deque([g]);seen.add(g); size=0
 while q:
  h=q.popleft();size+=1
  for s in generators:
   t=mul(mul(s,h),s)
   if t not in seen: seen.add(t);q.append(t)
 lc=cycle_type(g); dc=cycle_type(dsperm(g))
 trace,prank=picard_data(g)
 rows.append(dict(picard_trace=trace,picard_rank=prank,class_id=len(rows)+1,class_size=size,lines=encoded(lc),double_sixes=encoded(dc),rational_lines=fixed(lc),rational_double_sixes=fixed(dc),line_spectrum=lc,double_six_spectrum=dc))
assert len(rows)==25 and sum(int(r['class_size']) for r in rows)==51840
assert len({r['line_spectrum'] for r in rows})==20
assert len({r['double_six_spectrum'] for r in rows})==24
classes=defaultdict(list)
for r in rows:classes[r['double_six_spectrum']].append(r)
ambiguous=[pair for pair in classes.values() if len(pair)>1]
assert len(ambiguous)==1 and len(ambiguous[0])==2
p0,p1=ambiguous[0]
assert p0['double_six_spectrum']==((1,2),(2,3),(4,7))
assert {p0['line_spectrum'],p1['line_spectrum']}=={((1,5),(2,1),(4,5)),((1,1),(2,3),(4,5))}
assert {p0['rational_lines'],p1['rational_lines']}=={5,1}
assert {(p0['picard_trace'],p0['picard_rank']),(p1['picard_trace'],p1['picard_rank'])}=={(3,4),(1,3)}
assert len({(r['double_six_spectrum'],r['rational_lines']) for r in rows})==25
assert len({(r['line_spectrum'],r['double_six_spectrum']) for r in rows})==25
# Double-six counts for extension degrees <= 6 have 24 signatures;
# adding the base-field rational-line count separates the sole collision.
assert len({tuple(fixed(r['double_six_spectrum'],n) for n in range(1,7)) for r in rows})==24
assert len({tuple(fixed(r['double_six_spectrum'],n) for n in range(1,7))+(r['rational_lines'],) for r in rows})==25
fields=['class_id','class_size','lines','double_sixes','rational_lines','rational_double_sixes','picard_trace','picard_rank']
rows_out=[{k:r[k] for k in fields} for r in rows]
def csv_text():
 import io
 buf=io.StringIO(newline=''); w=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n')
 w.writeheader();w.writerows(rows_out);return buf.getvalue()
cert=csv_text()
if len(sys.argv)>1:
 path=sys.argv[1]
 with open(path,'rb') as f: assert f.read()==cert.encode('utf-8'), 'certificate mismatch'
else:
 with open('certificate.csv','wb') as f:f.write(cert.encode('utf-8'))
print('VERIFIED_E6_51840_CLASSES_25_DOUBLE_SIX_SPECTRA_24_UNIQUE_COLLISION_1_BASE_LINE_SPLITS')
