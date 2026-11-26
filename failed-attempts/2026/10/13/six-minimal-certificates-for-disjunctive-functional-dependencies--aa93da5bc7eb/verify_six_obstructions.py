"""Finite verification of the six colored minimal obstructions.
Run: python3 verify_six_obstructions.py
No nonstandard dependencies.
"""
from itertools import permutations
from math import comb

SIDE=4
PATTERNS={
    "matching_3":((0,0),(1,1),(2,2)),
    "square":((0,0),(0,1),(1,0),(1,1)),
    "path_Y_2_Z_3":((0,0),(0,1),(1,0),(1,2)),
    "path_Y_3_Z_2":((0,0),(1,0),(0,1),(2,1)),
    "two_row_stars":((0,0),(0,1),(1,2),(1,3)),
    "two_column_stars":((0,0),(1,0),(2,1),(3,1)),
}

def embeddings(pattern):
    ys=sorted(set(a for a,b in pattern))
    zs=sorted(set(b for a,b in pattern))
    result=set()
    for imgy in permutations(range(SIDE),len(ys)):
        ymap=dict(zip(ys,imgy))
        for imgz in permutations(range(SIDE),len(zs)):
            zmap=dict(zip(zs,imgz))
            mask=sum(1<<(SIDE*ymap[a]+zmap[b]) for a,b in pattern)
            result.add(mask)
    return result

orbits={name:embeddings(pat) for name,pat in PATTERNS.items()}
expected={"matching_3":96,"square":36,"path_Y_2_Z_3":144,
          "path_Y_3_Z_2":144,"two_row_stars":36,"two_column_stars":36}
assert {name:len(v) for name,v in orbits.items()}==expected
all_bad=set().union(*orbits.values())
assert len(all_bad)==492
for group in orbits.values():
    assert all(mask.bit_count() in (3,4) for mask in group)
    assert all(not (mask&(mask-1)==0) for mask in group)

star_masks=[]
for y in range(SIDE):
 for z in range(SIDE):
  star_masks.append(sum(1<<(SIDE*a+b) for a in range(SIDE) for b in range(SIDE)
                        if a==y or b==z))

def covers(m):return any(m&~star==0 for star in star_masks)

def forbidden(m):return any((m&pat)==pat for pat in all_bad)

minfail={3:0,4:0}
for m in range(1<<(SIDE*SIDE)):
    c=covers(m)
    f=forbidden(m)
    assert c!=f,(m,c,f)
    if not c and all(covers(m^(1<<k)) for k in range(SIDE*SIDE) if (m>>k)&1):
        assert m in all_bad,hex(m)
        minfail[m.bit_count()]+=1
assert minfail=={3:96,4:396},minfail
for p in range(1,SIDE+1):
 for q in range(1,SIDE+1):
  vals={}
  for name, pat in PATTERNS.items():
   ys=sorted({a for a,b in pat}); zs=sorted({b for a,b in pat})
   masks=set()
   for ay in permutations(range(p),len(ys)):
    for az in permutations(range(q),len(zs)):
     my=dict(zip(ys,ay)); mz=dict(zip(zs,az))
     masks.add(sum(1<<(q*my[a]+mz[b]) for a,b in pat))
   vals[name]=len(masks)
  F3=6*comb(p,3)*comb(q,3) if p>=3 and q>=3 else 0
  def choose(a,b):return comb(a,b) if a>=b else 0
  F4=(choose(p,2)*choose(q,2)+6*choose(p,2)*choose(q,3)
      +6*choose(p,3)*choose(q,2)+6*choose(p,2)*choose(q,4)
      +6*choose(p,4)*choose(q,2))
  assert vals["matching_3"]==F3,(p,q,vals,F3)
  assert sum(v for k,v in vals.items() if k!="matching_3")==F4,(p,q,vals,F4)
print("VERIFY_OK: all 65,536 bipartite 4x4 edge sets; six pattern orbits;")
print("96 minimal three-edge and 396 minimal four-edge obstructions.")
