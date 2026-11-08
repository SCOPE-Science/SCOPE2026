from itertools import combinations,permutations
from collections import Counter,defaultdict
from math import comb
V=list(combinations(range(4),2));matches=[set([V.index(tuple(sorted((0,1)))),V.index(tuple(sorted((2,3))))]),set([V.index(tuple(sorted((0,2)))),V.index(tuple(sorted((1,3))))]),set([V.index(tuple(sorted((0,3)))),V.index(tuple(sorted((1,2))))])]

def canon(es):
 def bits(s):return sum(1<<V.index(tuple(sorted(e))) for e in s)
 return min(bits({tuple(sorted((p[i],p[j]))) for i,j in es}) for p in permutations(range(4)))

def poly(G):
 deg=[0]*4
 for i,j in G: deg[i]+=1;deg[j]+=1
 isolated_edges=sum(deg[i]==deg[j]==1 for i,j in G)
 remaining=sum(d<=1 for d in deg)-2*isolated_edges
 coeff=Counter({0:1})
 for _ in range(remaining):
  coeff=Counter({i:coeff[i]+coeff[i-1] for i in range(max(coeff)+2)})
 for _ in range(isolated_edges):
  coeff=Counter({i:coeff[i]+2*coeff[i-1] for i in range(max(coeff)+2)})
 return coeff,deg,isolated_edges,remaining

classes=defaultdict(list)
for bm in range(1<<6):
 G=[e for idx,e in enumerate(V) if bm>>idx&1];classes[canon(G)].append((bm,G))
print('classes',len(classes))
counts=Counter()
for code,ls in sorted(classes.items(),key=lambda x:(len(x[1][0][1]),x[0])):
 bm,G=ls[0];e=len(G);r=sum(not any((1<<j)&bm for j in m) for m in matches)
 P,deg,isol,rem=poly(G)
 parts=[P[k] for k in range(max(P)+1)]
 row=Counter()
 for k,c in P.items():
  row[e+k]+=len(ls)*c
  row[e+k+1]+=len(ls)*r*c
 counts.update(row)
 print('edges',e,'G',G,'mult',len(ls),'Rchoices',r,'isolatededge',isol,'free',rem,'P',parts,'contribution',sum(row.values()))
print('poly=',[counts[k] for k in range(max(counts)+1)],'total=',sum(counts.values()))
