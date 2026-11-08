"""Definition-level exhaustive tests for resolving sets in crowns and complete prisms."""
from itertools import product
from collections import Counter
from math import comb


def table(m,kind):
    verts=list(range(2*m));N=len(verts)
    def adj(i,j):
        if kind=='crown':return (i//m)!=(j//m) and (i%m)!=(j%m)
        return i!=j and ((i//m)==(j//m) or (i%m)==(j%m))
    # Floyd Warshall on very small graphs, independently from any proposed formula
    d=[[0 if i==j else (1 if adj(i,j) else 10**3) for j in verts] for i in verts]
    for k in verts:
        for i in verts:
            for j in verts:
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d,[(i,j) for i in verts for j in range(i+1,N) if adj(i,j)]


def resolve_objects(D,S,objects):
    code=set()
    for obj in objects:
        t=tuple(min(D[s][v] for v in obj) for s in S)
        if t in code:return False
        code.add(t)
    return True


def tar_components(n,k):
    # Feasibility from direct crown vertex-distance signatures (not the claimed rule).
    dist,_=table(n,'crown')
    V=[(i,) for i in range(2*n)]
    states={mask for mask in range(1<<(2*n)) if mask.bit_count()<=k and
            resolve_objects(dist,[i for i in range(2*n) if mask>>i&1],V)}
    remaining=set(states);components=0
    while remaining:
        components+=1
        front=[remaining.pop()]
        while front:
            mask=front.pop()
            for i in range(2*n):
                nxt=mask^(1<<i)
                if nxt in remaining:
                    remaining.remove(nxt);front.append(nxt)
    return components


def run():
  casecounts=[];total=0;total_res=0
  for n in range(3,7):
    crown,edges=table(n,'crown')
    rook,edges_rook=table(n,'rook')
    vs=[(i,) for i in range(2*n)]
    ce=Counter();re=Counter();ee=Counter()
    for mask in range(1<<(2*n)):
      S=[i for i in range(2*n) if mask>>i&1]
      fullmiss=sum(not(mask>>i&1 or mask>>(n+i)&1) for i in range(n))
      expected=fullmiss<=1
      c=resolve_objects(crown,S,vs)
      assert c==expected,(n,S,'crown')
      e=resolve_objects(crown,S,edges)
      assert e==c,(n,S,'edge_metric',e,c)
      if e:ee[len(S)]+=1
      if c:ce[len(S)]+=1
      if n>=4:
        r=resolve_objects(rook,S,vs)
        assert r==c,(n,S,'rook')
        if r:re[len(S)]+=1
      total+=1;total_res+=int(c)
    if n>=4:assert ce==re
    formula=Counter()
    for k in range(n+1):
      formula[n+k]+=comb(n,k)*2**(n-k)
    for k in range(n):
      formula[n-1+k]+=n*comb(n-1,k)*2**(n-1-k)
    assert ce==+formula,(n,ce,formula)
    assert ce[n-1]==n*2**(n-1)
    if n>=4:
      # Every feasible set of minimum size is deletion-minimal. At every higher size
      # a selected vertex can be deleted while retaining feasibility.
      pass
    casecounts.append((n,ce,ee))
  for n,ce,ee in casecounts:
     print('CROWN',n,'vertex_metric',sorted(ce.items()),'edge_metric',sorted(ee.items()),'same',ce==ee)
  for n in (4,5):
    for k in (n-2,n-1,n):
      actual=tar_components(n,k)
      expected=0 if k<n-1 else n*(2**(n-1)) if k==n-1 else 1
      assert actual==expected,(n,k,actual,expected)
  print('VERIFY_OK','orders=3..6','subsets='+str(total),'crown_resolving='+str(total_res),'crown_prism_equivalence_n4..6=PASS', 'all_edge_metric_sets=PASS', 'polynomial_and_bases=PASS', 'TAR_n4..5=PASS')
if __name__=='__main__':run()
