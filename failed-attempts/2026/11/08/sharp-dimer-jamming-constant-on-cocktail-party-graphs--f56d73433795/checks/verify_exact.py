"""Independent exact state-space verification for uniform-edge dimer adsorption on K_{2n} minus a fixed matching.
Run: python verify_exact.py
"""
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def lumped(k,l):
    m=2*k+l
    if m==2:
        return Fraction(int(k==1))
    assert m>=4 and k>=0 and l>=0 and m%2==0
    e=m*(m-1)//2-k
    assert e>0
    a=Fraction(l*(l-1)//2,e)*lumped(k,l-2) if l>=2 else 0
    b=Fraction(2*k*l,e)*lumped(k-1,l) if k>=1 and l>=1 else 0
    c=Fraction(2*k*(k-1),e)*lumped(k-2,l+2) if k>=2 else 0
    return a+b+c

def labeled(n):
    all_vertices=(1<<(2*n))-1
    @lru_cache(None)
    def solve(mask):
        vs=[v for v in range(2*n) if mask & (1<<v)]
        edges=[(a,b) for i,a in enumerate(vs) for b in vs[i+1:] if a//2 != b//2]
        if not edges:
            return Fraction(int(len(vs)==2))
        return sum((solve(mask & ~(1<<a) & ~(1<<b)) for a,b in edges),Fraction())/len(edges)
    return solve(all_vertices),solve.cache_info().currsize

expected={2:Fraction(0),3:Fraction(1,5),4:Fraction(8,65),5:Fraction(1231,11375),6:Fraction(562248,6062875),7:Fraction(634107503,7766542875)}
for n in range(2,8):
    a=lumped(n,0)
    b,states=labeled(n)
    assert a==b==expected[n],(n,a,b,expected[n])
    print(f'n={n} p={a} decimal={float(a):.10f} independently_visited_masks={states}')
print('PASS: two structurally independent exact rational recurrences agree for n=2..7')
