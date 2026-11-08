#!/usr/bin/env python3
"""Exact checks for the canonical real Pentarnion algebra in a rationally scaled basis."""
import sympy as S

A,B,C,D,E=S.symbols('a b c d e')
X=[A,B,C,D,E]
# Basis: 1,I=sqrt(2)i,J=sqrt(2)j,K=sqrt(2)k,L=sqrt(2)ell.
# All table entries are integers; T[i][j][k] is coefficient of basis k in e_i e_j.
T=[[[0 for k in range(5)] for j in range(5)] for i in range(5)]
for j in range(5):
    T[0][j][j]=1
    T[j][0][j]=1
for i in range(1,5): T[i][i][0]=-2
for i,j in ((1,2),(2,3),(3,1),(4,1),(4,2),(4,3)):
    for k in set(range(1,5))-{i,j}:
        T[i][j][k]=1
        T[j][i][k]=-1

def matrix(side):
    return S.Matrix(5,5,lambda row,col: sum(X[i]*(T[i][col][row] if side=='left' else T[col][i][row]) for i in range(5)))
L=matrix('left')
R=matrix('right')
Ssum=B+C+D
Q=B*B+C*C+D*D
r2=Q-Ssum*Ssum/S.Integer(3)
N=A*A+2*(Q+E*E)
F=S.expand((A+2*E)*((A-E)**2+Ssum**2/S.Integer(3))+(A+3*Ssum-E)*r2)
assert S.expand(L.det(method='domain-ge')-N*F)==0
assert S.expand(R.det(method='domain-ge')-N*F.subs({B:-B,C:-C,D:-D,E:-E}, simultaneous=True))==0
assert S.expand(F-(A**3+A*(Q-3*E**2)+Ssum*(3*Q-Ssum**2)+E*(Ssum**2-Q)+2*E**3))==0
# Cofactor logic: rank<=3 forces singularity of determinant, and N>0 for nonzero real p.
# The written proof classifies real singularities using sum of derivatives in adapted coordinates.
assert S.expand(S.diff(F,A)+S.diff(F,E)-3*((A-E)**2+Ssum**2/S.Integer(3)))==0
special_left={A:1,B:0,C:0,D:0,E:1}
special_right={A:1,B:0,C:0,D:0,E:-1}
assert L.subs(special_left).rank()==3
assert R.subs(special_right).rank()==3
assert L.subs(special_right).rank()==5
assert R.subs(special_left).rank()==5
assert L.subs({A:-2,B:0,C:0,D:0,E:1}).rank()==4
# Independent exact matrix-level checks over a nontrivial integer grid.
checks=0
for a in range(-2,3):
 for b in range(-1,2):
  for c in range(-1,2):
   for d in range(-1,2):
    for e in range(-1,2):
     v={A:a,B:b,C:c,D:d,E:e}
     lhs=L.subs(v);rhs=R.subs(v)
     detL=N.subs(v)*F.subs(v)
     detR=N.subs(v)*F.subs({A:a,B:-b,C:-c,D:-d,E:-e})
     assert lhs.det()==detL and rhs.det()==detR
     if (a,b,c,d,e)!=(0,0,0,0,0):
        if detL!=0:assert lhs.rank()==5
        elif a==e and b==c==d==0:assert lhs.rank()==3
        else:assert lhs.rank()==4
        if detR!=0:assert rhs.rank()==5
        elif a==-e and b==c==d==0:assert rhs.rank()==3
        else:assert rhs.rank()==4
     checks+=1
print(f'VERIFY_OK polynomial_factorizations=2 gradient_identity=1 exact_integer_vectors={checks} exceptional_left_rank=3 exceptional_right_rank=3')
