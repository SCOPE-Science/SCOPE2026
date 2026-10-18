#!/usr/bin/env python3
"""Independent exact checks for even-agreement families in S6; stdlib only."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import factorial

N = 6

@lru_cache(None)
def partitions(n, maximum=None):
    if maximum is None:
        maximum=n
    if n==0: return ((),)
    return tuple((x,)+p for x in range(min(maximum,n),1-1,-1)
                 for p in partitions(n-x,x))

def cells(shape):
    return {(i,j) for i,length in enumerate(shape) for j in range(length)}

def ribbon(big, small):
    B=cells(big); S=cells(small)
    if not S.issubset(B):return None
    R=B-S
    if not R:return None
    # A connected skew strip, without a 2 x 2 square.
    stack=[next(iter(R))]; found=set(stack)
    while stack:
        i,j=stack.pop()
        for q in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if q in R and q not in found:
                found.add(q);stack.append(q)
    if len(found)!=len(R):return None
    if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}.issubset(R) for i,j in R):return None
    return 1-2*((len({i for i,j in R})-1)%2) # (-1)^(height-1)

@lru_cache(None)
def char_mn(shape, cycles):
    if not cycles:return int(not shape)
    t=cycles[0]; a=sum(shape)-t
    return sum(ribbon(shape,sub)*char_mn(sub,cycles[1:])
               for sub in partitions(a) if ribbon(shape,sub) is not None)

def z_value(part):
    z=1
    for k,m in Counter(part).items():z*=k**m*factorial(m)
    return z

def mul_poly(A,B):
    C={}
    for a,ac in A.items():
        for b,bc in B.items():
            key=tuple(sorted(a+b,reverse=True));C[key]=C.get(key,Fraction(0))+ac*bc
    return C

@lru_cache(None)
def h(k):
    if k<0:return {}
    if k==0:return {():Fraction(1)}
    return {a:Fraction(1,z_value(a)) for a in partitions(k)}

def char_jt(shape,cycles):
    # Jacobi--Trudi determinant in power sums: χ_lambda(mu)=z_mu [p_mu]det(h_{λ_i-i+j})
    m=len(shape);total=Fraction(0)
    for assignment in permutations(range(m)):
        inversions=sum(assignment[i]>assignment[j] for i in range(m) for j in range(i+1,m))
        pol={():Fraction(1)}
        for i,j in enumerate(assignment):pol=mul_poly(pol,h(shape[i]-i+j))
        total+=(-1)**inversions * pol.get(cycles,Fraction(0))
    res=total*z_value(cycles)
    assert res.denominator==1
    return int(res)

def cycle_type(perm):
    visited=set();lens=[]
    for i in range(len(perm)):
        if i not in visited:
            j=i; length=0
            while j not in visited:
                visited.add(j);length+=1;j=perm[j]
            lens.append(length)
    return tuple(sorted(lens,reverse=True))

T1=(5,1);T2=(3,2,1)
ct1,ct2=0,0
for p in permutations(range(N)):
    if cycle_type(p)==T1:ct1+=1
    if cycle_type(p)==T2:ct2+=1
assert (ct1,ct2)==(144,120)

rows=[];mins=[]
for shape in partitions(N):
    d=char_mn(shape,(1,)*N)
    assert d==char_jt(shape,(1,)*N)
    c1=char_mn(shape,T1);c2=char_mn(shape,T2)
    assert c1==char_jt(shape,T1)
    assert c2==char_jt(shape,T2)
    eigen=Fraction(3*ct1*c1+2*ct2*c2,d)
    assert eigen.denominator==1
    rows.append((shape,d,c1,c2,int(eigen)))
assert sum(d*d for _,d,_,_,_ in rows)==720
assert min(v for _,_,_,_,v in rows)==-48
assert max(v for _,_,_,_,v in rows)==672

# The wreath-product construction: preserve the unordered partition 01|23|45.
blocks=((0,1),(2,3),(4,5))
H=set()
for order in permutations(range(3)):
    for swaps in product((0,1),repeat=3):
        p=[None]*N
        for source in range(3):
            target=order[source]
            for j in range(2):p[blocks[source][j]]=blocks[target][j^swaps[source]]
        H.add(tuple(p))
assert len(H)==48
for a in H:
    for b in H:
        if a!=b:
            assert sum(u==v for u,v in zip(a,b))%2==0

print('character table shape dim chi(5,1) chi(3,2,1) eigenvalue')
for row in rows:print(*row)
print('class_sizes',ct1,ct2)
print('weighted_row_sum',3*ct1+2*ct2)
print('minimum_eigenvalue',min(v for _,_,_,_,v in rows))
print('weighted_Hoffman_bound', 720*48//(672+48))
print('wreath_group_size',len(H))
print('all_pairwise_even_agreement',True)
print('VERIFY_OK')
