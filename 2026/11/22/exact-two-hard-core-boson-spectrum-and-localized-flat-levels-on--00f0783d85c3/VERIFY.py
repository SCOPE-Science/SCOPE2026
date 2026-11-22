import sympy as s
from itertools import combinations
z=s.symbols('z')
for m in range(3,8):
 vertices=list(range(2*m+1));edges=set()
 for i in range(m):
  a,b=2*i+1,2*i+2
  for p,q in ((0,a),(0,b),(a,b)):
   edges.add(tuple(sorted((p,q))))
 pairs=list(combinations(vertices,2));idx={p:i for i,p in enumerate(pairs)}
 H=s.zeros(len(pairs))
 for u,v in pairs:
  p=idx[(u,v)]
  for x in (u,v):
   y=v if x==u else u
   for a,b in edges:
    if x in (a,b):
     t=b if x==a else a
     if t!=y:
      q=idx[tuple(sorted((t,y)))];H[p,q]=1
 assert H==H.T
 poly=s.factor(H.charpoly(z).as_expr())
 predicted=s.factor((z+2)**(m*(m-1)//2)*z**(m*(m-2))*(z*z+z-2*m+2)**m*(z-2)**(m*(m-3)//2)*(z**3-3*z*z+(4-2*m)*z+4)**(m-1)*(z**3-3*z*z+(4-4*m)*z+4))
 print(m,len(pairs),poly==predicted, s.factor(poly / predicted) if m==3 else '')
