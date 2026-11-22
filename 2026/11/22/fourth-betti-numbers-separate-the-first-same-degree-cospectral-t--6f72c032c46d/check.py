#!/usr/bin/env python3
"""Exact rational de Rham cohomology computation for four nine-vertex tree Lie algebras.
All algorithms are standalone; Python 3 standard library only.
Graph edges are zero-based. The cochain basis is the 9 vertex forms followed by 8 edge forms.
Differential: d x_i=0 and d z_uv=x_u wedge x_v for u<v.
"""
from collections import defaultdict,deque

def canonical_tree(n,edges):
 adj=[[] for _ in range(n)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 if n==1:return '()'
 deg=[len(a) for a in adj]
 leaves=[i for i in range(n) if deg[i]<=1]
 remain=n
 while remain>2:
  remain-=len(leaves)
  nxt=[]
  for v in leaves:
   deg[v]=0
   for u in adj[v]:
    if deg[u]>0:
     deg[u]-=1
     if deg[u]==1:nxt.append(u)
  leaves=nxt
 centers=leaves
 def rooted(x,parent):
  return '('+''.join(sorted(rooted(y,x) for y in adj[x] if y!=parent))+')'
 return min(rooted(c,-1) for c in centers)

def unlabeled_trees(n):
 data=[(1,tuple())]
 counts=[1]
 for size in range(2,n+1):
  oldn=size-1
  opts={}
  for _,ed in data:
   for v in range(oldn):
    edges=tuple(sorted(ed+((v,oldn),)))
    opts[canonical_tree(size,edges)]=(size,edges)
  data=sorted(opts.values(),key=lambda v:canonical_tree(v[0],v[1]))
  counts.append(len(data))
 return data,counts

def match_poly(n,edges):
 cnt=[0]*(n//2+1)
 for s in range(1<<len(edges)):
  used=0;valid=True
  for j,(u,v) in enumerate(edges):
   if s>>j&1:
    flag=(1<<u)|(1<<v)
    if flag&used:valid=False;break
    used|=flag
  if valid:cnt[s.bit_count()]+=1
 return tuple(cnt)


from itertools import combinations
from fractions import Fraction
from collections import defaultdict

def rank_q(rows):
 piv={}
 for row in rows:
  d={k:Fraction(v) for k,v in row.items() if v}
  while d:
   col=min(d); val=d[col]
   if col not in piv:
    piv[col]={k:v/val for k,v in d.items()};break
   for k,pv in piv[col].items():
    vv=d.get(k,0)-val*pv
    if vv:d[k]=vv
    else:d.pop(k,None)
 return len(piv)

def cohom_betti(n,edges,K=4):
 edges=sorted(tuple(sorted(e)) for e in edges)
 m=n+len(edges);sup_gen=[1<<v for v in range(n)]+[(1<<u)|(1<<v) for u,v in edges]
 groups=[defaultdict(list) for _ in range(K+2)]
 for k in range(K+2):
  for cs in combinations(range(m),k):
   mask=0;support=0
   for g in cs:mask|=1<<g;support|=sup_gen[g]
   groups[k][support].append(mask)
 ranks=[];stats=[]
 for k in range(K+1):
  rank=0;blocks=[]
  for support in set(groups[k])|set(groups[k+1]):
   out=groups[k+1][support];ind={m:i for i,m in enumerate(out)}
   rows=[{} for _ in out]
   for col,mask in enumerate(groups[k][support]):
    for zidx,(u,v) in enumerate(edges):
     z=n+zidx
     if not mask>>z&1:continue
     rest=mask^(1<<z)
     if rest>>u&1 or rest>>v&1:continue
     new=rest|(1<<u)|(1<<v)
     before=rest&((1<<z)-1)
     sign=-1 if (before.bit_count()+(before>>(u+1)).bit_count()+(before>>(v+1)).bit_count())%2 else 1
     rr=ind[new];rows[rr][col]=rows[rr].get(col,0)+sign
   rr=rank_q(rows)
   rank+=rr
   if rr:blocks.append((support,len(groups[k][support]),len(out),rr))
  ranks.append(rank);stats.append(blocks)
 dim=[sum(map(len,gg.values())) for gg in groups]
 return [dim[k]-(ranks[k] if k<=K else 0)-(ranks[k-1] if k else 0) for k in range(K+1)],ranks,dim,stats

from itertools import combinations

def rank_mod(rows, prime=1000003):
 p={};r=0
 for d in rows:
  d={k:v%prime for k,v in d.items() if v%prime}
  while d:
   c=min(d);v=d[c]
   if c not in p:
    vi=pow(v,-1,prime);p[c]={k:(a*vi)%prime for k,a in d.items()};r+=1;break
   for k,a in p[c].items():
    new=(d.get(k,0)-v*a)%prime
    if new:d[k]=new
    else:d.pop(k,None)
 return r

def betti_low(n,edges,K=4):
 edges=[tuple(sorted(e)) for e in edges];m=n+len(edges)
 masks=[];idx=[]
 for k in range(K+2):
  arr=[sum(1<<i for i in co) for co in combinations(range(m),k)]
  masks.append(arr);idx.append({mask:j for j,mask in enumerate(arr)})
 ranks=[]
 for k in range(K+1):
  rows=[{} for _ in masks[k+1]]
  for j,mask in enumerate(masks[k]):
   for eid,(u,v) in enumerate(edges):
    z=n+eid
    if not mask>>z&1:continue
    rr=mask^(1<<z)
    if rr>>u&1 or rr>>v&1:continue
    new=rr|(1<<u)|(1<<v)
    # exterior differentiation: permutation from z position to adjacent x_u,x_v; sign from crossings
    before=rr&((1<<z)-1)
    inv=(before>>(u+1)).bit_count()+(before>>(v+1)).bit_count()
    s=(-1)**(before.bit_count()+inv)
    row=rows[idx[k+1][new]];row[j]=row.get(j,0)+s
  ranks.append(rank_mod(rows))
 return [len(masks[k])-(ranks[k] if k<=K else 0)-(ranks[k-1] if k>0 else 0) for k in range(K+1)],ranks

EXPECTED = {
 "A1": {"edges":((0,1),(1,2),(2,3),(3,4),(4,5),(4,7),(5,6),(5,8)),"betti":(1,9,53,201,593),"ranks":(0,8,75,404,1383)},
 "A2": {"edges":((0,1),(1,2),(2,3),(2,5),(3,4),(5,6),(6,7),(6,8)),"betti":(1,9,53,201,594),"ranks":(0,8,75,404,1382)},
 "B1": {"edges":((0,1),(0,8),(1,2),(2,3),(2,5),(2,6),(3,4),(3,7)),"betti":(1,9,55,210,632),"ranks":(0,8,73,397,1351)},
 "B2": {"edges":((0,1),(1,2),(2,3),(2,5),(3,4),(5,6),(5,7),(5,8)),"betti":(1,9,55,210,633),"ranks":(0,8,73,397,1350)},
}
EXPECTED_CHAR = {"A":(1,8,19,14,2),"B":(1,8,17,10,0)}

def differential(n,edges,mask):
    """Return sparse signed d of a wedge monomial encoded by a bit mask."""
    answer={}
    for zidx,(u,v) in enumerate(sorted(tuple(sorted(e)) for e in edges)):
        z=n+zidx
        if not (mask>>z)&1:continue
        rest=mask^(1<<z)
        if (rest>>u)&1 or (rest>>v)&1:continue
        new=rest|(1<<u)|(1<<v)
        before=rest&((1<<z)-1)
        parity=(before.bit_count()+(before>>(u+1)).bit_count()+(before>>(v+1)).bit_count())&1
        answer[new]=answer.get(new,0)+(-1 if parity else 1)
    return {i:v for i,v in answer.items() if v}

def d_squared_check(n,edges):
    m=n+len(edges)
    for k in range(4):
        for co in combinations(range(m),k):
            mon=sum(1<<i for i in co)
            dd={}
            for term,a in differential(n,edges,mon).items():
                for target,b in differential(n,edges,term).items():
                    dd[target]=dd.get(target,0)+a*b
            assert all(v==0 for v in dd.values()),(k,co,dd)

def main():
    result={};counts=None
    for n in range(1,10):
        trees,counts=unlabeled_trees(n)
        groups=defaultdict(list)
        for _,edges in trees:
            degrees=[0]*n
            for u,v in edges:degrees[u]+=1;degrees[v]+=1
            groups[(match_poly(n,edges),tuple(sorted(degrees)))].append(edges)
        multi=[(key,grp) for key,grp in groups.items() if len(grp)>1]
        assert len(trees)==(1,1,1,2,3,6,11,23,47)[n-1]
        if n<9:assert not multi,(n,multi)
        else:
            assert len(multi)==2 and sorted(len(grp) for _,grp in multi)==[2,2]
            for key,grp in multi:
                fset={frozenset(tuple(sorted(e)) for e in egraph) for egraph in grp}
                for family in ('A','B'):
                    want={frozenset(EXPECTED[family+suffix]['edges']) for suffix in ('1','2')}
                    if fset==want:
                        assert key[0]==EXPECTED_CHAR[family]
                        result[family]=grp
            assert set(result)=={'A','B'}
        print('tree_count n=%d count=%d collision_groups=%d'%(n,len(trees),len(multi)))
    for name,case in EXPECTED.items():
        edges=case['edges']
        d_squared_check(9,edges)
        betti,ranks,dims,_=cohom_betti(9,edges,K=4)
        assert tuple(betti)==case['betti'],(name,betti)
        assert tuple(ranks)==case['ranks'],(name,ranks)
        assert dims[:6]==[1,17,136,680,2380,6188]
        bmod,rmod=betti_low(9,edges,K=4)
        assert bmod==betti and rmod==ranks,(name,bmod,rmod)
        print('%s char_matchings=%s betti_0_4=%s rational_ranks_0_4=%s mod1000003_same=YES d_squared=ZERO'%(name,match_poly(9,edges),betti,ranks))
    print('ALL CHECKS PASSED: exhaustive tree census, exact rational support blocks, independent prime-field ranks, d^2=0')

if __name__ == '__main__':main()
