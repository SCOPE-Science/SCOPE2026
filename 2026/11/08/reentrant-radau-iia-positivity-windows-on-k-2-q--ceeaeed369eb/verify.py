#!/usr/bin/env python3
"""Exact symbolic and finite-matrix checks of a Radau IIA bipartite positivity theorem.
Requires Python 3.10+ and sympy>=1.12; no data files are used.
"""
import sympy as S
h, q, u = S.symbols('h q u', real=True)
R = lambda z: (6-2*z)/(z*z+4*z+6)
A = q*q*(q+2)**2*h**4 + (-2*q**4+12*q*q+8*q)*h**3 + (-2*q**3+22*q*q+76*q+48)*h*h + (12*q*q+72*q+96)*h+36*(q+2)
B = 2*q*(q+2)**2*h**4 + (-2*q**4-6*q**3+12*q*q+32*q)*h**3+(3*q**4+10*q**3+22*q*q+28*q)*h*h+(12*q**3+36*q*q+24*q)*h+18*q*(q+2)
D=lambda z:z*z+4*z+6
D_A=D(q*h)*D((q+2)*h)
D_B=D(2*h)*D((q+2)*h)
num_A=S.Rational(1,2)*R(q*h)+1/(q+2)+q*R((q+2)*h)/(2*(q+2))
num_B=(q-1)*R(2*h)/q+1/(q+2)+2*R((q+2)*h)/(q*(q+2))
c=0
assert S.factor(num_A-A/((q+2)*D_A))==0;c+=1
assert S.factor(num_B-2*B/(q*(q+2)*D_B))==0;c+=1
# Sturm exact count: the first loss of unconditional positivity is at q=10.
for k in range(2,10):
    for P in [A,B]:
        assert S.Poly(P.subs(q,k),h).count_roots(0,S.oo)==0
        c+=1
# These witnesses ensure two distinct positive roots (Descartes gives at most two).
for P,step in [(A,1),(B,4)]:
    poly=S.Poly(S.together(P.subs(h,step)).subs(q,u+10),u)
    assert all(v<0 for v in poly.all_coeffs());c+=1
# Resultant exact identity; factor q-2 reflects equal parts, irrelevant to q>=10.
F=3*q**6-64*q**5-708*q**4-2388*q**3-2375*q**2-1776*q-576
resultant=S.resultant(A,B,h)
assert S.factor(resultant+46656*q**4*(q-2)**4*(q+2)**10*F)==0;c+=1
assert F.subs(q,30)<0<F.subs(q,31);c+=1
assert S.Poly(F,q).count_roots(0,S.oo)==1;c+=1
for k,stepsigns in [(10,{1:(-1,1),2:(1,1),4:(1,-1)}),(31,{1:(-1,1),2:(1,-1),S.Rational(44,25):(-1,-1)})]:
    for step,expected in stepsigns.items():
        assert tuple(int(S.sign(P.subs({q:k,h:step}))) for P in [A,B])==expected
        c+=1
# Direct exact matrix identity, independent of symbolic rational numerator derivation.
for Q in range(2,14):
    n=Q+2
    L=S.zeros(n)
    for i in range(2):
        for j in range(2,n):
            L[i,i]+=1; L[j,j]+=1
            L[i,j]-=1; L[j,i]-=1
    E0=S.ones(n,n)/n
    v=S.Matrix([Q,Q]+[-2]*Q)
    EN=(v*v.T)/(2*Q*n)
    E_Q=S.zeros(n);E_Q[:2,:2]=S.eye(2)-S.ones(2,2)/2
    E_2=S.zeros(n);E_2[2:,2:]=S.eye(Q)-S.ones(Q,Q)/Q
    assert L==Q*E_Q+2*E_2+n*EN
    c+=1
    for H in [S.Rational(1,11),S.Rational(1,2),S.Rational(7,4),S.Integer(2),S.Integer(4)]:
        T=E0+R(Q*H)*E_Q+R(2*H)*E_2+R(n*H)*EN
        assert (H*H*L*L+4*H*L+6*S.eye(n))*T==(6*S.eye(n)-2*H*L)
        assert T[0,0]==num_A.subs({q:Q,h:H})
        assert T[2,2]==num_B.subs({q:Q,h:H})
        assert all(T[i,j]>0 for i in range(n) for j in range(n) if i!=j)
        c+=4
print('VERIFY_OK',c)
