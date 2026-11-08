#!/usr/bin/env python3
"""Exact-rational verification for the implicit Taylor Markov benchmark.
Requires sympy; run: python checker.py
This checks finite algebraic identities; universal dimension claims use the proof.
"""
import sympy as sp

h, z = sp.symbols('h z')
D = h*h + 2*h + 2
R = 1/(1-z+z*z/2)
checks = 0

def cert(eq):
    global checks
    assert sp.cancel(eq) == 0, sp.factor(eq)
    checks += 1

def cycle(n):
    P=sp.zeros(n)
    for i in range(n):
        P[i,(i+1)%n]=1
    return P-sp.eye(n)

def birth(n):
    Q=sp.zeros(n)
    for i in range(n-1):
        Q[i,i]=-1
        Q[i,i+1]=1
    return Q

def transition(Q):
    return (sp.eye(Q.rows)-h*Q+sp.Rational(1,2)*h*h*Q*Q).inv()

cert(sp.series(R, z, 0, 5).removeO() - (1+z+z*z/2-z**4/4))
for n in range(1, 6):
    Q=cycle(n)
    T=transition(Q)
    for i in range(n):
        cert(sum(T[i,j] for j in range(n))-1)
        for j in range(n):
            cert(T[i,j]-T[0,(j-i)%n])

# Canonical first row for the directed cycles.
cyc = {
2: (2*h*h+2*h+1, [h*h+h+1,h*(h+1)]),
3: (9*h**4+18*h**3+18*h**2+12*h+4,
    [3*h**4+6*h**3+8*h*h+8*h+4, h*(3*h**3+6*h*h+8*h+4),h*h*(3*h*h+6*h+2)]),
4: (2*(h+1)*(h*h+1)*(2*h*h+2*h+1),
    [h**5+2*h**4+3*h**3+5*h*h+4*h+2,
     h*(h**4+2*h**3+4*h*h+4*h+2),
     h*h*(h**3+2*h*h+3*h+1), h**4*(h+2)]),
5: (25*h**8+100*h**7+200*h**6+300*h**5+360*h**4+320*h**3+200*h*h+80*h+16,
    [5*h**8+20*h**7+40*h**6+80*h**5+136*h**4+160*h**3+128*h*h+64*h+16,
     h*(5*h**7+20*h**6+50*h**5+100*h**4+136*h**3+120*h*h+64*h+16),
     h*h*(5*h**6+20*h**5+50*h**4+80*h**3+76*h*h+40*h+8),
     h**4*(5*h**4+20*h**3+40*h*h+40*h+16),
     h**4*(5*h**4+20*h**3+20*h*h-4)])}
for n,(den,nums) in cyc.items():
    T=transition(cycle(n))
    for j,num in enumerate(nums):
        cert(T[0,j]-num/den)
        # Except for the single critical entry, the polynomials have positive coefficients.
        if (n,j)!=(5,4):
            p=sp.Poly(sp.expand(num),h)
            assert all(c>=0 for c in p.all_coeffs())
            checks += 1
    p=sp.Poly(sp.expand(den),h)
    assert all(c>=0 for c in p.all_coeffs()) and den.subs(h,0)>0
    checks += 1

# Acyclic pure-birth chain, with final state absorbing. Its last-column
# coefficients depend only on the number of remaining transitions.
a={1:h*(h+2)/D,
   2:h*h*(h*h+4*h+2)/D**2,
   3:h**4*(h*h+6*h+6)/D**3,
   4:h**4*(h**4+8*h**3+12*h*h-4)/D**4}
b={0:2/D,
   1:4*h*(h+1)/D**2,
   2:2*h*h*(3*h*h+6*h+2)/D**3,
   3:8*h**4*(h+1)*(h+2)/D**4,
   4:2*h**4*(5*h**4+20*h**3+20*h*h-4)/D**5}
for n in range(2,7):
    T=transition(birth(n))
    for i in range(n):
        cert(sum(T[i,j] for j in range(n))-1)
        for j in range(i,n):
            expected=a[j-i] if j==n-1 and 1<=j-i<=4 else (b[j-i] if j!=n-1 and j-i<=4 else (sp.Integer(1) if i==j==n-1 else None))
            if expected is not None:
                cert(T[i,j]-expected)
        for j in range(i):
            cert(T[i,j])

qc=5*h*h*(h+2)**2-4
qa=h*h*(h+2)*(h+6)-4
cert(cyc[5][1][4]-h**4*qc)
cert(a[4]-h**4*qa/D**4)
cert(qc-qa-4*h*h*(h+1)*(h+2))

# Integer/rational points straddling two different exact thresholds.
for value in [sp.Rational(1,4), sp.Rational(2,5), sp.Rational(1,2), 1, 2, 10]:
    C=transition(cycle(5)).subs(h,value)
    B=transition(birth(5)).subs(h,value)
    assert (C[0,4]<0) == (value<sp.sqrt(1+2/sp.sqrt(5))-1)
    assert (B[0,4]<0) == (qa.subs(h,value)<0)
    checks+=2
    assert C*sp.ones(5,1)==sp.ones(5,1)
    assert B*sp.ones(5,1)==sp.ones(5,1)
    checks+=2

# General arbitrarily small-step obstruction: coefficient of P^4 in
# R(h(P-I)) equals -h^4/4, provided the cycle has at least five states.
cert(sp.expand(sp.series(R,z,0,5).removeO().subs(z,h*(sp.Symbol('p')-1))).coeff(sp.Symbol('p'),4)+h**4/4)

print('PASS:',checks,'exact symbolic/rational assertions')
print('cyclic five-state threshold:',sp.N(sp.sqrt(1+2/sp.sqrt(5))-1,18))
print('absorbing five-state threshold:',sp.nroots(qa)[-1])
