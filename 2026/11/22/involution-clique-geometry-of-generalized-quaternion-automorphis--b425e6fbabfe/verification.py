from math import gcd, comb
from collections import Counter

def test(k):
 N=2**k; h=N//2
 units=[u for u in range(N) if gcd(u,N)==1]
 mul=lambda x,y: ((x[0]+x[1]*y[0])%N,(x[1]*y[1])%N)
 invol=[(v,u) for u in units for v in range(N) if mul((v,u),(v,u))==(0,1) and (v,u)!=(0,1)]
 neigh={a:set() for a in invol}
 for i,a in enumerate(invol):
  for b in invol[i+1:]:
   if mul(a,b)==mul(b,a):
    neigh[a].add(b);neigh[b].add(a)
 c=(h,1)
 C={(0,1+h),(h,1+h)}
 Aev={(v,N-1) for v in range(0,N,2)}
 Aodd={(v,N-1) for v in range(1,N,2)}
 B={(v,h-1) for v in range(0,N,2)}
 assert set(invol)=={c}|C|Aev|Aodd|B
 pred={c:set(invol)-{c}}
 for a in C:pred[a]={c}|(C-{a})|Aev|B
 for a in Aev:
  v=a[0]; grp={((v%h)+j*h,N-1) for j in range(2)} | {((v%h)+j*h,h-1) for j in range(2)}
  pred[a]={c}|C|(grp-{a})
 for a in B:
  v=a[0]; grp={((v%h)+j*h,N-1) for j in range(2)} | {((v%h)+j*h,h-1) for j in range(2)}
  pred[a]={c}|C|(grp-{a})
 for a in Aodd: pred[a]={c}|{((a[0]+h)%N,N-1)}
 assert all(pred[a]==neigh[a] for a in invol)
 degrees=Counter(len(neigh[a]) for a in invol)
 edges=sum(map(len,neigh.values()))//2
 tris=sum(len(neigh[a]&neigh[b]) for a in invol for b in neigh[a])//6
 maximal=[]
 # exact K7 cliques and K3 cliques indexed by residues
 for r in range(0,h,2):
  maximal.append({c}|C|{(r,N-1),(r+h,N-1),(r,h-1),(r+h,h-1)})
 for r in range(1,h,2):
  maximal.append({c,(r,N-1),(r+h,N-1)})
 assert len(maximal)==N//2
 assert all(all(b in neigh[a] for a in s for b in s if a!=b) for s in maximal)
 assert len(invol)==3*N//2+3
 assert degrees==Counter({3*N//2+2:1,N+2:2,6:N,2:N//2})
 assert edges==21*N//4+3
 assert tris==35*N//4+1
 print(f'Q_{2*N}: aut={N*len(units)} inv={len(invol)} degs={dict(degrees)} edges={edges} triangles={tris} maximal_cliques={len(maximal)}')
for k in range(3,9):test(k)
print('QUATERNION_AUTOMORPHISM_INVOLUTION_GRAPH_VERIFIED')
