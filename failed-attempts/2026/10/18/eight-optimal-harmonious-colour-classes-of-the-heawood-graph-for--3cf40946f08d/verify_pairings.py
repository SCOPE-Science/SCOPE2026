"""Independent unordered-vertex-pair partition enumeration on a Fano incidence graph."""
V=tuple(range(14))
E={(p-1,7+l-1) for p in range(1,8) for l in range(1,8) if ((p&l).bit_count()%2)==0}
assert len(E)==21
allmatchings=0;proper=0;exact=0;first=None
# Exhaust all (14-1)!! pairings, with no assumed side types.
def rec(remaining,blocks):
 global allmatchings,proper,exact,first
 if not remaining:
  allmatchings+=1
  c={v:j for j,b in enumerate(blocks) for v in b}
  if any(c[u]==c[v] for u,v in E):return
  proper+=1
  types={tuple(sorted((c[u],c[v]))) for u,v in E}
  if len(types)==21:
   exact+=1
   if first is None:first=blocks
  return
 u=remaining[0]
 for i in range(1,len(remaining)):
  v=remaining[i]
  rec(remaining[1:i]+remaining[i+1:],blocks+((u,v),))
rec(V,())
assert allmatchings==135135
assert exact==8
print('unordered_seven_pair_partitions',allmatchings)
print('proper_partitions',proper)
print('exact_harmonious_partitions',exact)
print('witness_partition',first)
print('labeled_optimal_colorings',exact*5040)
print('VERIFY_OK')
