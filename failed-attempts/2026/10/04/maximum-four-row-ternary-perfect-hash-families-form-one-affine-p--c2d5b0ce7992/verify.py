from itertools import product, permutations, combinations
from math import factorial
Q=range(3)
words=list(product(Q, repeat=4))

def sep3(a,b,c):
    return any({a[r],b[r],c[r]}=={0,1,2} for r in range(4))

def is_phf(C):
    return all(sep3(*t) for t in combinations(C,3))

def normalized_pair(d):
    return (0,0,0,0), tuple([1]*d+[0]*(4-d))

def find_target(d,target=9):
    x,y=normalized_pair(d)
    cand=[z for z in words if z!=x and z!=y and sep3(x,y,z)]
    # Precompute triple goodness indexed candidates.
    n=len(cand)
    xy_pair=[[False]*n for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):
        xy_pair[i][j]=xy_pair[j][i]=sep3(x,cand[i],cand[j]) and sep3(y,cand[i],cand[j])
    nodes=0
    witness=None
    def rec(chosen, avail):
      nonlocal nodes,witness
      nodes+=1
      if 2+len(chosen)>=target:
        witness=[x,y]+[cand[i] for i in chosen]
        return True
      need=target-2-len(chosen)
      if len(avail)<need:return False
      while avail:
        if len(avail)<need:return False
        i=avail[0]; rest=avail[1:]
        ok=True
        for j in chosen:
          if not xy_pair[i][j]:ok=False;break
        if ok:
          for j,k in combinations(chosen,2):
            if not sep3(cand[i],cand[j],cand[k]):ok=False;break
        if ok:
          new=[]
          for h in rest:
            if not xy_pair[i][h]:continue
            if all(sep3(cand[i],cand[j],cand[h]) for j in chosen):
              new.append(h)
          if rec(chosen+[i],new):return True
        avail=rest
      return False
    yes=rec([],list(range(n)))
    return yes,witness,n,nodes

results={d:find_target(d) for d in range(1,5)}
print('PAIR_CASES', {d:(v[0],v[2],v[3]) for d,v in results.items()})
assert results[1][0] is False and results[2][0] is False and results[4][0] is False
assert results[3][0] is True and is_phf(results[3][1])
std=sorted((i,j,(i+j)%3,(i+2*j)%3) for i in Q for j in Q)
assert len(std)==9 and is_phf(std)
# all pair distances 3
assert {sum(a[k]!=b[k] for k in range(4)) for a,b in combinations(std,2)}=={3}
# Enumerate Latin squares order 3 and ordered orthogonal pairs.
cells=list(product(Q,Q))
latins=[]
for vals in product(Q, repeat=9):
    L={cells[t]:vals[t] for t in range(9)}
    if all(len({L[i,j] for j in Q})==3 for i in Q) and all(len({L[i,j] for i in Q})==3 for j in Q):
        latins.append(L)
print('LATIN_COUNT',len(latins)); assert len(latins)==12
pairs=[]; codes=set()
for A in latins:
  for B in latins:
    if len({(A[c],B[c]) for c in cells})==9:
      pairs.append((A,B))
      code=tuple(sorted((i,j,A[i,j],B[i,j]) for i,j in cells))
      codes.add(code)
print('ORDERED_ORTHOGONAL_PAIRS',len(pairs),'NORMALIZED_CODES',len(codes))
# Full equivalence orbit of std under row permutations and independent symbols.
perms=list(permutations(Q)); rperms=list(permutations(range(4)))
orbit=set()
for rp in rperms:
  for ps in product(perms, repeat=4):
    C=[]
    for w in std:
      # transform original coordinate r symbol then reorder coordinates by rp
      v=tuple(ps[r][w[r]] for r in range(4))
      C.append(tuple(v[r] for r in rp))
    orbit.add(tuple(sorted(C)))
print('ORBIT_SIZE',len(orbit),'GROUP_ORDER',len(rperms)*(len(perms)**4),'STABILIZER',(len(rperms)*(len(perms)**4))//len(orbit))
assert len(orbit)==72
assert (len(rperms)*(len(perms)**4))//len(orbit)==432
# Every normalized orthogonal pair code belongs to orbit.
assert codes <= orbit
# Conversely every orbit image, after fixing any two coordinates as first rows and normalizing their ordered pair grid, is structurally OA; direct pair-distance verification suffices.
assert all({sum(a[k]!=b[k] for k in range(4)) for a,b in combinations(C,2)}=={3} for C in orbit)
# Count all labeled maximum sets using implication: any max has all distances 3, so projection to rows 0,1 is bijective and gives an ordered orthogonal Latin pair.
# Codes with first two coordinates fixed are exactly `codes`; in fact all 72 orbit codes project bijectively on rows 0,1.
assert len(codes)==72
print('ALL_MAX_LABELED_SETS',len(codes))
print('VERIFY_OK maximum=9 labeled_maxima=72 orbits=1 stabilizer=432 pair_distance=3')
