"""Finite exact checks for three-element chains in random product orders."""
from itertools import permutations,product,combinations
from math import comb, factorial, log
from fractions import Fraction

def p_overlap_one(d):
    counts = [[comb(i+j-2, i-1)*comb(6-i-j,3-i) for j in range(1,4)] for i in range(1,4)]
    return sum((Fraction(c,120)**d) for row in counts for c in row)*4

def p_overlap_two(d):
    return 12*Fraction(1,24)**d+6*Fraction(1,12)**d

def pred_moments(n,d):
    total=comb(n,3)
    p=Fraction(6,6**d)
    neighbors1=total*3*comb(n-3,2) if n>=5 else 0
    neighbors2=total*3*(n-3)
    return total*p,(total*(total-1)-neighbors1-neighbors2)*p*p+neighbors1*p_overlap_one(d)+neighbors2*p_overlap_two(d)

def empirical_moments(n,d):
    orderings=list(permutations(range(n)))
    triples=list(combinations(range(n),3))
    count=0
    sm=sm2=0
    for orders in product(orderings, repeat=d):
        rank=[[None]*n for _ in range(d)]
        for k,order in enumerate(orders):
            for r,v in enumerate(order):rank[k][v]=r
        W=0
        for T in triples:
            ref=tuple(sorted(T,key=lambda x:rank[0][x]))
            if all(tuple(sorted(T,key=lambda x:rank[k][x]))==ref for k in range(1,d)):
                W+=1
        sm+=W;sm2+=W*(W-1);count+=1
    return Fraction(sm,count),Fraction(sm2,count)

assert p_overlap_one(1)==1
assert p_overlap_two(1)==1
assert p_overlap_one(2)==Fraction(8,20**2)+Fraction(4,30**2)+Fraction(16,40**2)+Fraction(8,120**2)
for n,d in [(3,1),(4,1),(5,1),(3,2),(4,2),(5,2),(4,3)]:
    ex=pred_moments(n,d);got=empirical_moments(n,d)
    assert ex==got,(n,d,ex,got)
    print('CHECK',n,d,tuple(map(str,got)))

delta=3*log(20)/log(6)-5
assert 0<delta<.02
assert 3*log(12)/log(6)-4>delta
for n in [100,1000,10000,100000,1000000]:
    d=round(3*log(n)/log(6))
    m, f2=pred_moments(n,d)
    K = f2-m*m
    ratio=float(K)/(n**5*20**(-d))
    print('ASYMP',n,d,'ratio',ratio,'target',2)
assert ratio>0
print('PASS')
