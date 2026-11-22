from itertools import permutations,combinations
from collections import Counter
N=6

def matchings(av):
 if not av:yield ();return
 a=av[0]
 for b in av[1:]:
  for tail in matchings([i for i in av if i not in (a,b)]):yield tuple(sorted(((a,b),)+tail))
M=sorted(set(matchings(list(range(N)))));idx={m:i for i,m in enumerate(M)}
E=list(combinations(range(N),2))
L=[sum(1<<i for i,m in enumerate(M) if e in m) for e in E]
C=sorted({L[i]|L[j] for i,j in combinations(range(15),2)})
G=[]
for g in permutations(range(N)):
 G.append(tuple(idx[tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in m))] for m in M))
G=list(set(G));assert len(G)==720

def tr(x,g):
 y=0
 while x:
  a=x&-x;x-=a;y |=1<<g[a.bit_length()-1]
 return y
for k in (3,4,5):
 left={sum(1<<i for i in a) for a in combinations(range(15),k)}
 records=[]
 while left:
  x=min(left);orbit={tr(x,g) for g in G}
  assert orbit<=left or len(orbit&left)==0
  left-=orbit
  traces={y&x for y in C}
  sh=len(traces)==1<<k
  records.append((x,len(orbit),int(sh),len(traces)))
 expected={3:([15,180,180,60,20],[8,8,8,7,7],375),4:([180,90,360,45,360,60,180,60,30],[15,16,16,16,14,13,13,13,11],495),5:([360,45,360,360,90,360,72,180,360,360,60,180,120,90,6],[28,23,26,28,25,26,31,21,24,24,25,21,20,23,15],0)}
 expected_sizes,expected_traces,expected_sh=expected[k]
 assert [x[1] for x in records]==expected_sizes
 assert [x[3] for x in records]==expected_traces
 assert sum(z[1] for z in records if z[2])==expected_sh
 print('k',k,'orbit count',len(records),'shattered orbit count',sum(x[2] for x in records),'poly coef',sum(z[1] for z in records if z[2]))
 for x,ln,sh,t in records:
  print(tuple(i for i in range(15) if x>>i&1),ln,sh,t)
print('PASS: full S6 orbit partition regenerated for all 3-, 4-, 5-point supports')
