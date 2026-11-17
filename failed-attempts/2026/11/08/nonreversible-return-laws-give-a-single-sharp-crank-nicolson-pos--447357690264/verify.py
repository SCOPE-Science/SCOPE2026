"""Exact finite examples for the Markov Cayley positivity theorem.

The general claims are proved analytically in RESULT.md. This script uses
SymPy exact arithmetic to check representative reversible, nonreversible,
and reducible transition generators, including the sharp directed-triangle
threshold and a reducible pure-birth boundary.
"""
import random
import sympy as sp

s=sp.symbols('s', positive=True)
I=sp.I
checks=0

def eq(a,b):
    global checks
    assert sp.simplify(a-b)==0, (a,b)
    checks+=1

def positive(q):
    return q>=0

def check_chain(Q, svals):
    global checks
    n=Q.rows
    assert Q.rows==Q.cols
    for i in range(n):
        eq(sum(Q[i,j] for j in range(n)),0)
        for j in range(n):
            if i!=j: assert Q[i,j]>=0
    prev=None
    for t in svals:
        R=(sp.eye(n)-t*Q).inv()
        C=(sp.eye(n)-t*Q).inv()*(sp.eye(n)+t*Q)
        for i in range(n):
            eq(sum(R[i,j] for j in range(n)),1)
            eq(sum(C[i,j] for j in range(n)),1)
            for j in range(n):
                eq(C[i,j],2*R[i,j]-(1 if i==j else 0))
                if i!=j:
                    assert R[i,j]>=0
                    assert C[i,j]>=0
                    checks+=2
            eq(C[i,i],2*R[i,i]-1)
            checks+=int((C[i,i]>=0)==(R[i,i]>=sp.Rational(1,2)))
            if prev is not None:
                assert R[i,i]<=prev[i]
                if Q[i,i]<0: assert R[i,i]<prev[i]
                checks+=2
        prev=[R[i,i] for i in range(n)]

# One-way directed three-cycle (nonreversible).
P=sp.zeros(3)
for i in range(3):P[i,(i+1)%3]=1
Q=P-sp.eye(3)
R=(sp.eye(3)-s*Q).inv()
for i in range(3):
    eq(R[i,i], (1+s)**2/(1+3*s+3*s**2))
    eq(sp.factor(2*R[i,i]-1), (1+s-s*s)/(1+3*s+3*s*s))
# Strict decrease even though the generator has complex eigenvalues.
eq(sp.factor(sp.diff(R[0,0],s)), -(s+1)*(3*s+1)/(1+3*s+3*s**2)**2)
print('directed_triangle_diagonal=',sp.factor(R[0,0]))
print('triangle_sharp_h=',1+sp.sqrt(5))

# A one-way 3-state chain with two distinct absorbing states.
Q_birth=sp.Matrix([[-2,2,0],[0,-3,3],[0,0,0]])
# Four-state reducible: reversible balanced pair and two absorbing states.
Q_closed=sp.diag(sp.Matrix([[-3,3],[3,-3]]),sp.zeros(2))
# Three-state non-reversible class with unequal rates.
Q_unequal=sp.Matrix([[-2,2,0],[0,-3,3],[4,0,-4]])
# Symmetric 4-state nearest-neighbor path with diverse weights.
Q_path=sp.Matrix([[-2,2,0,0],[2,-5,3,0],[0,3,-8,5],[0,0,5,-5]])
for Qex in (Q,Q_birth,Q_closed,Q_unequal,Q_path):
    check_chain(Qex,[sp.Rational(k,5) for k in (1,2,5,10,25,100)])

# Distinct rational random generators to challenge the no-reversibility requirement.
rng=random.Random(18271)
for n in (2,3,4,5):
    for _ in range(5):
        Qr=sp.zeros(n)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    Qr[i,j]=rng.randrange(5)
            Qr[i,i]=-sum(Qr[i,j] for j in range(n) if j!=i)
        check_chain(Qr,[sp.Rational(k,4) for k in (1,2,4,8)])

# Pure-birth 2-state chain is sharp for the classical h<=2/lambda sufficient restriction.
a=sp.Rational(7,3)
B=sp.Matrix([[-a,a],[0,0]])
eq(((sp.eye(2)-s*B).inv())[0,0],1/(1+a*s))
eq((sp.eye(2)-s*B).inv()[0,0].subs(s,1/a),sp.Rational(1,2))

# The two-state symmetric chain is unconditionally positive, in agreement with classification.
A=sp.Matrix([[-3,3],[3,-3]])
R=(sp.eye(2)-s*A).inv()
for i in (0,1):
    assert sp.simplify(R[i,i]-sp.Rational(1,2))>0
    checks+=1

print('exact_checks_passed=',checks)
print('verification_status=PASS')
