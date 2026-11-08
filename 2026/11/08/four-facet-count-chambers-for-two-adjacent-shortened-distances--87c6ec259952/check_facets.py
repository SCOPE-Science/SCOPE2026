"""Exact independent checks of facet counts for adjacent shortened distances.
Only Python standard library is used. Every comparison is rational.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict


def candidates(r,s):
    # Complete candidate list for r>s, obtained by connecting the special
    # 3-point tight-edge path to a binary anchor. Reflections cover r<s.
    if r<s:
        return {tuple(reversed(u)) for u in candidates(s,r)}
    return {
      (F(0),F(0),F(0)), (F(0),F(0),s), (F(0),1-s,F(1)),
      (F(0),s,F(0)), (F(0),r,r-s), (F(0),r,F(1)),
      (1-r,F(1),1-s), (1-r,F(1),F(1)),
      (r,F(0),F(0)), (r,F(0),s),
      (F(1),1-r,F(0)), (F(1),1-r,1-r+s),
      (F(1),1-s,F(1)),(F(1),s,F(0)),
      (F(1),F(1),1-s), (F(1),F(1),F(1))
    }


def connected_tight(p,r,s):
    n=len(p); graph=[set() for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):
        d=r if (i,j)==(0,1) else (s if (i,j)==(1,2) else F(1))
        if abs(p[i]-p[j])>d:return False
        if abs(p[i]-p[j])==d: graph[i].add(j);graph[j].add(i)
    seen={0};stack=[0]
    while stack:
      for j in graph[stack.pop()]:
        if j not in seen:seen.add(j);stack.append(j)
    return len(seen)==n


def count_formulas(r,s,m):
    templates=candidates(r,s)
    if len(templates)!= (16 if r!=s and r+s>1 else 14 if (r!=s or r+s>1) else 12):
        raise AssertionError(('template degeneracy',r,s,len(templates)))
    a=sum(connected_tight(t+(F(0),),r,s) for t in templates)
    b=sum(connected_tight(t+(F(1),),r,s) for t in templates)
    c=sum(connected_tight(t+(F(0),F(1)),r,s) for t in templates)
    if (a,b,c) != ((10,10,16) if r!=s and r+s>1 else (9,9,14) if r==s and r+s>1 else (8,8,14) if r!=s else (7,7,12)):
        raise AssertionError((r,s,a,b,c))
    total=a+b+c*(2**m-2)
    expected=(16*2**m-12 if r!=s and r+s>1 else
              14*2**m-10 if r==s and r+s>1 else
              14*2**m-12 if r!=s else
              12*2**m-10)
    assert total==expected,(total,expected)
    # Reconstruct, from exact candidate data, all binary assignments of m outsiders.
    brute=0
    for bits in product((F(0),F(1)),repeat=m):
      brute+=sum(connected_tight(t+bits,r,s) for t in templates)
    assert brute==expected,(r,s,m,brute,expected)
    return expected

# Independent enumeration of ALL vertices from active halfspace intersections
# for four-point metrics (3 free coordinates). Explicit integer determinants
# and Cramer's rule, no template list and no floating arithmetic.
def det3(mat):
    a,b,c=mat
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def direct4(r,s):
    pairs=[]
    for i,j in combinations(range(4),2):
       d=r if (i,j)==(0,1) else (s if (i,j)==(1,2) else F(1))
       for sign in (1,-1):
         v=[0,0,0]
         if i<3:v[i]+=sign
         if j<3:v[j]-=sign
         pairs.append((tuple(v),d))
    vs=set()
    for (v1,d1),(v2,d2),(v3,d3) in combinations(pairs,3):
       mat=(v1,v2,v3); det=det3(mat)
       if not det: continue
       d=(d1,d2,d3)
       x=tuple(det3(tuple(tuple(d[row] if col==k else mat[row][col] for col in range(3)) for row in range(3)))/det for k in range(3))
       if all(sum(v[k]*x[k] for k in range(3))<=di for v,di in pairs): vs.add(x)
    return len(vs)

if __name__=='__main__':
    scenarios=[(F(3,4),F(3,5)),(F(3,5),F(3,4)),
      (F(2,3),F(2,3)),(F(3,4),F(1,4)),
      (F(1,4),F(3,4)),(F(1,2),F(1,2)),
      (F(3,5),F(4,5)),(F(9,10),F(1,5)),
      (F(7,10),F(7,10))]
    ncases=0
    for r,s in scenarios:
      for m in range(1,7): count_formulas(r,s,m);ncases+=1
      assert count_formulas(r,s,1)==direct4(r,s),(r,s)
    print('EXACT_ACTIVE_HALFSPACE_ENUMERATION_N4_OK',len(scenarios),'SCENARIOS')
    print('EXACT_TIGHT_GRAPH_ENUMERATION_AND_UNIVERSAL_COUNT_IDENTITIES_OK',ncases,'CASES')
    print('ALL_ADJACENT_SHORTENING_FACET_CHECKS_PASSED')
