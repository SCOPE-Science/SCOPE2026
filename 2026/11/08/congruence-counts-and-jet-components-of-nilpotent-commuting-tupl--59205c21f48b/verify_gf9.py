#!/usr/bin/env python3
"""Independent GF(9) base-field check; representation F_3[alpha]/(alpha^2+1)."""
from itertools import product
q=9
def plus(x,y):return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def neg(x):return (-(x%3))%3 + 3*((-(x//3))%3)
def minus(x,y):return plus(x,neg(y))
def times(x,y):
 a,b=x%3,x//3;c,d=y%3,y//3
 return (a*c-b*d)%3 + 3*((a*d+b*c)%3)
def sq0(x):
 a,b,c=x
 return plus(times(a,a),times(b,c))==0
def commute(x,y):
 a,b,c=x;d,e,f=y
 return minus(times(b,f),times(e,c))==0 and minus(times(a,e),times(d,b))==0 and minus(times(c,d),times(f,a))==0
squares=[x for x in product(range(q),repeat=3) if sq0(x)]
n2=sum(commute(x,y) for x in squares for y in squares)
E2=1+(q+1)*(q*q-1)
assert len(squares)==q*q, (len(squares),q*q)
assert n2==E2,(n2,E2)
print('GF9 m=1 r=2',n2,'expected',E2,'PASS')
sets=[]
for x in squares:sets.append(set(y for y in squares if commute(x,y)))
n3=sum(len(sets[i]&sets[j]) for i in range(len(squares)) for j in range(len(squares)) if squares[j] in sets[i])
E3=1+(q+1)*(q**3-1)
assert n3==E3,(n3,E3)
print('GF9 m=1 r=3',n3,'expected',E3,'PASS')
print('ALL_GF9_BASE_TESTS_PASS')
