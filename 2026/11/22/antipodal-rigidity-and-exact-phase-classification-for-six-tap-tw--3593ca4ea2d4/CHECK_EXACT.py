"""Exact Gaussian-integer census for the unit-magnitude six-tap theorem."""
from itertools import product
U=((1,0),(0,1),(-1,0),(0,-1))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def corr(g,s):
    v=(0,0)
    for j in range(6-s): v=add(v,mul(g[j+s],conj(g[j])))
    return v
# Independently enumerate ALL 4^6 labelled quaternary windows.
count_antipodal=0; count_order10=0
for g in product(U, repeat=6):
    if corr(g,2)==(0,0) and corr(g,4)==(0,0): count_antipodal+=1
    if all(corr(g,s)==(0,0) for s in (1,2,3,4)): count_order10+=1
assert count_antipodal==128,(count_antipodal,'expected 128')
assert count_order10==0,count_order10
print(f'EXACT_GAUSSIAN_OK q=4 N=20 antipodal={count_antipodal} order10={count_order10}')
# q=2, roots ±1: no even-lag complementary pairs.
count_binary=0
for g in product((U[0],U[2]), repeat=6):
    count_binary+=corr(g,2)==(0,0) and corr(g,4)==(0,0)
assert count_binary==0
print(f'EXACT_GAUSSIAN_OK q=2 antipodal={count_binary}')
print('ALL_EXACT_CHECKS_OK')
