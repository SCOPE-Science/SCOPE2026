"""Independent finite check of ternary two-deck gap intervals and lattice-hole formula."""
from math import gcd

def binary_pair_values(a,b):
    # Generate all binary words by insertion, independently of interval proof.
    seen=set()
    for mask in range(1<<(a+b)):
        if mask.bit_count()!=a:continue
        ones=0;count=0
        for j in range(a+b):
            if (mask>>j)&1:ones+=1
            else: count+=ones
        seen.add(count)
    return seen

slices=0
for b in range(1,9):
 for c in range(1,9):
  if b+c>12:continue
  possible=set()
  for x in range(b+1):
   for y in range(c+1):
    m=(b-x)*y
    left=binary_pair_values(b-x,c-y)
    right=binary_pair_values(x,y)
    got={m+l+r for l in left for r in right}
    expected=set(range(m, m+(b-x)*(c-y)+x*y+1))
    assert got==expected, (b,c,x,y,got,expected)
    possible.update((x,y,z) for z in got)
    slices+=1
  L={(x,y,z) for x in range(b+1) for y in range(c+1) for z in range(b*c+1) if 0<=c*x+z-b*y<=b*c}
  h=((b*b-1)*(c*c-1)+(gcd(b,c)**2-1))//6
  assert len(L-possible)==h and possible<=L
print('PASS independently generated',slices,'singleton gap slices and verified exact attainable intervals and hole counts.')
