"""Exact checks for the two-site open exclusion rectification theorem.

Requires SymPy 1.13 or later.  Run with: python verify.py
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

u, v, d, delta = s.symbols('u v d delta', positive=True)
l = (1 + delta) / 2
r = (1 - delta) / 2
Q = s.Matrix([
    [-l-r, l, r, 0],
    [u*(1-l), -u*(1-l)-r-d*u, d*u, r],
    [v*(1-r), d*v, -v*(1-r)-l-d*v, l],
    [0, v*(1-r), u*(1-l), -v*(1-r)-u*(1-l)],
])
assert [s.expand(sum(Q.row(i))) for i in range(4)] == [0]*4
T = [s.factor((-Q).minor_submatrix(i, i).det()) for i in range(4)]
Ttot = s.factor(sum(T))
h, p, q = u-v, u+v, u*v
D = ((u+1)*(v+1)*(4*d*p+p+2)
     - delta*h*(4*d*(q+p-1)+q+3*p+5)
     + delta**2*(3*p**2-p*q-10*q+p-2)
     + delta**3*h*(q-p+1))
N = d*(u*T[1]-v*T[2])
assert s.expand(8*Ttot-D) == 0
assert s.expand(2*N-d*u*v*delta*(p+2-delta*h)) == 0
J = 4*d*u*v*delta*(p+2-delta*h)/D
assert s.factor(J-N/Ttot) == 0
H = (p+2)**2 + 4*d*(q-1)
R = 16*d*u*v*delta**2*h*(H-delta**2*h**2)/(D*D.subs(delta,-delta))
assert s.factor(J+J.subs(delta,-delta)-R) == 0
assert s.factor(s.diff(J,delta,2).subs(delta,0)/2
                -8*d*u*v*h*H/((u+1)**2*(v+1)**2*(4*d*p+p+2)**2)) == 0

# Independent stationary solution: exact Fraction Gaussian elimination.
def frac_current(U,V,B,E):
    L = (F(1)+E)/2
    Rr = (F(1)-E)/2
    G = [
        [-L-Rr, L, Rr, F(0)],
        [U*(1-L), -U*(1-L)-Rr-B*U, B*U, Rr],
        [V*(1-Rr), B*V, -V*(1-Rr)-L-B*V, L],
        [F(0), V*(1-Rr), U*(1-L), -V*(1-Rr)-U*(1-L)],
    ]
    A = [[G[j][i] for j in range(4)] + [F(0)] for i in range(4)]
    A[-1] = [F(1)]*4 + [F(1)]
    for k in range(4):
        row = next(i for i in range(k,4) if A[i][k])
        A[k],A[row] = A[row],A[k]
        z=A[k][k]
        A[k]=[w/z for w in A[k]]
        for i in range(4):
            if i != k:
                z=A[i][k]
                A[i]=[a-z*b for a,b in zip(A[i],A[k])]
    pi = [A[i][-1] for i in range(4)]
    assert all(x>0 for x in pi)
    assert all(sum(pi[i]*G[i][j] for i in range(4))==0 for j in range(4))
    return B*(U*pi[1]-V*pi[2])

def closed(U,V,B,E):
    pp=U+V; qq=U*V; hh=U-V
    dd=((U+1)*(V+1)*(4*B*pp+pp+2)
       - E*hh*(4*B*(qq+pp-1)+qq+3*pp+5)
       + E**2*(3*pp**2-pp*qq-10*qq+pp-2)
       + E**3*hh*(qq-pp+1))
    assert dd>0
    return 4*B*U*V*E*(pp+2-E*hh)/dd

count=0
for U,V,B,E in product([F(1,5),F(1,2),F(3,2),F(4)],
                        [F(1,3),F(2),F(5)],
                        [F(1,2),F(1),F(5),F(16)],
                        [F(1,5),F(1,2),F(4,5)]):
    assert frac_current(U,V,B,E) == closed(U,V,B,E)
    assert frac_current(U,V,B,-E) == closed(U,V,B,-E)
    assert (closed(U,V,B,E)+closed(U,V,B,-E) > 0) == ((U-V)*((U+V+2)**2+4*B*(U*V-1)-E**2*(U-V)**2)>0) if U != V and ((U+V+2)**2+4*B*(U*V-1)-E**2*(U-V)**2) != 0 else True
    count += 2

# Rational witness: two asymmetric dwell rates and a half-bias inversion.
U,V,B=F(1,2),F(3,2),F(63,4)
assert U*V < 1
D1=(U+1)*(V+1)/(1-U*V)
D0=(U+V+2)**2/(4*(1-U*V))
assert D1==15 and D0==16 and D1<B<D0
assert ((U+V+2)**2+4*B*(U*V-1)) == F(1,4)
assert (closed(U,V,B,F(1,4))+closed(U,V,B,-F(1,4)))<0
assert (closed(U,V,B,F(1,2))+closed(U,V,B,-F(1,2)))==0
assert (closed(U,V,B,F(3,4))+closed(U,V,B,-F(3,4)))>0
print('PASS symbolic tree identities, full even-current factorization, local curvature')
print(f'PASS {count} independent exact-rational full-generator comparisons')
print('PASS two critical rates 15 and 16 and unique bias inversion 1/2')
