import json, itertools
from fractions import Fraction

# Directions: 0..4 = a1..a5, 5..9 = A1..A5 (inverses, Ai = inv(ai))
def inv(d): return d+5 if d<5 else d-5
def neg(w): return tuple(inv(d) for d in reversed(w))
def red(w):
    st=[]
    for d in w:
        if st and st[-1]==inv(d): st.pop()
        else: st.append(d)
    return tuple(st)

A=[0,1,2,3,4]
def show(d): return ('a' if d<5 else 'A')+str((d%5)+1)
def showw(w): return ''.join(show(d) for d in w)

# Candidate pair: cyclic shift + twist at a5, differing by order within f(a5)
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2)}       # a5 -> a1 a2 a3
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1)}       # a5 -> a1 a3 a2
# analytic inverses: phi^{-1}: a1->a5 A1 A2, a2->a1, a3->a2, a4->a3, a5->a4
g_phi={0:(4,5,6),1:(0,),2:(1,),3:(2,),4:(3,)}
g_psi={0:(4,5,7),1:(0,),2:(1,),3:(2,),4:(3,)}  # psi^{-1}: a1->a5 A1 A3? verify below

def apply(f,w):
    out=[]
    for d in w:
        if d<5: out.extend(f[d])
        else: out.extend(neg(f[d-5]))
    return red(tuple(out))

def check_inverse(f,g,name):
    for i in range(5):
        if apply(g,(i,))!=(i,): return False,('g(f) fail',i,showw(apply(g,(i,))))
        if apply(f,apply(g,(i,)))!=(i,): return False,('f(g) fail',i)
    # also check g inverts f on generators: apply(f, g(a_i)) == a_i and apply(g,f(a_i))==a_i
    for i in range(5):
        if apply(f,apply(g,(i,)))!=(i,) or apply(g,apply(f,(i,)))!=(i,):
            return False,('comp fail',i)
    return True,(None,)

for f,g,nm in [(f_phi,g_phi,'phi'),(f_psi,g_psi,'psi')]:
    print(nm, check_inverse(f,g,nm))

def mat(f):
    # M[i][j] = count of ai+1 in f(aj+1) (i row, j col)
    M=[[0]*5 for _ in range(5)]
    for j in range(5):
        for d in f[j]:
            M[d%5][j]+=1
    return M

Mphi=mat(f_phi); Mpsi=mat(f_psi)
print('Mphi==Mpsi:', Mphi==Mpsi)
for r in Mphi: print(r)

import numpy as np
M=np.array(Mphi)
print('M^6>0?', bool(((np.linalg.matrix_power(M,6))>0).all()))
print('eig max abs:', max(abs(e) for e in np.linalg.eigvals(M)))
# char poly via sympy rational
import sympy as sp
x=sp.symbols('x')
print('charpoly:', sp.Matrix(Mphi).charpoly(x).as_expr())
print('det:', sp.Matrix(Mphi).det())
