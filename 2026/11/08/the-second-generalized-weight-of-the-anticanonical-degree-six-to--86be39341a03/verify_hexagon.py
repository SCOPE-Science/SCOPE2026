"""Exact independent checks for the second generalized weight of the degree-six toric del Pezzo hexagon.
Uses only Python standard library; no external data or network.
"""
from itertools import combinations, product
from collections import Counter
from math import gcd, comb

E = ((-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0))

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set(points))
    if len(pts)<2: return tuple(pts)
    lower=[]; upper=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return tuple(lower[:-1]+upper[:-1])

def canonical(V):
    return tuple(sorted((x-min(a for a,b in V),y-min(b for a,b in V)) for x,y in V))

def doubled_area(V):
    if len(V)<3:return 0
    return abs(sum(V[i][0]*V[(i+1)%len(V)][1]-V[i][1]*V[(i+1)%len(V)][0] for i in range(len(V))))

def in_P(x,y):
    return max(abs(x),abs(y),abs(x+y))<=1

def translations(H):
    return tuple((u,v) for u in range(-3,4) for v in range(-3,4)
                 if all(in_P(x+u,y+v) for x,y in H))

shape_info={}
for mask in range(1,1<<len(E)):
    V=hull(E[i] for i in range(len(E)) if mask>>i&1)
    key=canonical(V)
    if key not in shape_info:
        shape_info[key]=(V,translations(V))
relevant={k:(V,S) for k,(V,S) in shape_info.items() if len(S)>=2}
ct=Counter(('point' if len(V)==1 else 'segment' if len(V)==2 else 'polygon', doubled_area(V)) for V,S in relevant.values())
print('newton_shape_counts',dict(sorted(ct.items())))
assert ct==Counter({('point',0):1,('segment',0):6,('polygon',1):8,('polygon',2):3})
for k,(V,S) in relevant.items():
    if len(V)==2:
        assert gcd(abs(V[1][0]-V[0][0]),abs(V[1][1]-V[0][1]))==1
        assert doubled_area(hull(S))<=2
    if len(V)>2 and doubled_area(V)==1:
        assert doubled_area(hull(S))<=1
    if len(V)>2 and doubled_area(V)==2:
        assert len(S)==2 and doubled_area(hull(S))==0
print('newton_residual_checks PASSED')

# The two independent sections f=(x-1)(y-1)/x and g=(x-1)(y-1)/y have support E.
F={(-1,0):1,(-1,1):-1,(0,0):-1,(0,1):1}
G={(0,-1):1,(1,-1):-1,(0,0):-1,(1,0):1}
assert set(F).issubset(E) and set(G).issubset(E)

def eval_poly(coeff,x,y,p):
    return sum(c*pow(x,a,p)*pow(y,b,p) if a>=0 and b>=0 else c*pow(x,a%(p-1),p)*pow(y,b%(p-1),p)
               for (a,b),c in coeff.items())%p

def mat_rank_mod(A,p):
    if not A:return 0
    a=[list(row) for row in A]; m=len(a);n=len(a[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        a[r][j:]=[(x*inv)%p for x in a[r][j:]]
        for i in range(r+1,m):
            if a[i][j]:
                f=a[i][j]
                a[i][j:]=[(x-f*y)%p for x,y in zip(a[i][j:],a[r][j:])]
        r+=1
        if r==min(m,n):break
    return r

for p in (5,7,11,13):
    torus=list(product(range(1,p),repeat=2))
    zero=[z for z in torus if eval_poly(F,*z,p)==0 and eval_poly(G,*z,p)==0]
    assert len(zero)==2*(p-1)-1
    print('witness',p,'common_zeros',len(zero),'d2_upper',(p-2)**2)

p=5
T=list(product(range(1,p),repeat=2))
M=[[pow(x,a%(p-1),p)*pow(y,b%(p-1),p)%p for a,b in E] for x,y in T]
assert mat_rank_mod(M,p)==7
# A 2-dimensional subcode vanishing at >=8 points exists iff some 8-row
# evaluation submatrix has rank at most five.
for J in combinations(range(len(T)),8):
    if mat_rank_mod([M[i] for i in J],p)<=5:
        raise AssertionError('counterexample: eight zeros found at '+str(J))
print('q5_exhaustive',comb(16,8),'eight_point_sets_checked: rank>=6')
print('ALL_CHECKS_PASSED')
