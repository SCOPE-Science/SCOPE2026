"""Exact rational checks for constant-amplitude Riccati pulse chronology.

All calculations use projective matrices divided by their positive cosines,
so u=tan(a*time) is an exact rational input.
"""
from fractions import Fraction as Q
from itertools import product

I=((Q(1),Q(0)),(Q(0),Q(1)))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def pm(a,u):
    a=Q(a);u=Q(u)
    assert a>0 and u>0
    return ((Q(1),-a*u),(u/a,Q(1)))
def apply(M,x):
    num=M[0][0]*x+M[0][1]
    den=M[1][0]*x+M[1][1]
    assert den>0
    return num/den
def threshold(M):
    return sum(sum(row) for row in M)

n=0
for a,b,u,v in product((Q(1,2),Q(1),Q(2),Q(3)), (Q(1,2),Q(1),Q(2),Q(3)), (Q(1,7),Q(1,3),Q(1,2)), (Q(1,7),Q(1,3),Q(1,2))):
    A,B=pm(a,u),pm(b,v)
    assert threshold(mm(B,A))==threshold(mm(A,B))
    n+=1
A,B,C=pm(Q(2),Q(1,2)),pm(Q(1,2),Q(1,2)),pm(Q(1),Q(1,2))
assert [apply(M,Q(1)) for M in (A,B,C)]==[Q(0),Q(3,8),Q(1,3)]
assert apply(mm(C,mm(B,A)),Q(1))==Q(-6,7)
assert apply(mm(C,mm(A,B)),Q(1))==Q(-3,2)
assert [apply(mm(B,A),Q(1)),apply(mm(A,B),Q(1))]==[Q(-1,4),Q(-4,7)]
# Check universal three-pulse signed-numerator identity in the normalized model.
for a,b,c,u,v,w in product((Q(1,2),Q(1),Q(2)),repeat=6):
    A,B,C=pm(a,u),pm(b,v),pm(c,w)
    delta=threshold(mm(C,mm(B,A)))-threshold(mm(C,mm(A,B)))
    expected=u*v*w*(a*a-b*b)/(a*b)*(c+Q(1)/c)
    assert delta==expected
print(f'RICCATI_PULSE_EXACT_OK two_phase={n} triple_identity={3**6} three_phase_witness=1')
