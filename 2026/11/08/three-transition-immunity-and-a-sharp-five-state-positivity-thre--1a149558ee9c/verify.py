"""Exact rational identities for a Padé (0,2) Markov positivity theorem.

Run: python verify.py (requires SymPy).
"""
from random import Random
import sympy as sp

h, z, x = sp.symbols('h z x', real=True)
f = 1 / (1-z+z*z/2)
D = h*h+2*h+2
P = h**4+8*h**3+12*h**2-4

assert sp.series(f,z,0,5).removeO().expand() == 1+z+z*z/2-z**4/4
expected = [2/D, 4*(h+1)/D**2,
            4*(3*h**2+6*h+2)/D**3,
            48*h*(h+1)*(h+2)/D**4]
for k in range(4):
    actual = sp.diff(f,z,k).subs(z,-h)
    assert sp.cancel(actual-expected[k]) == 0

Q = sp.zeros(5)
for i in range(4):
    Q[i,i],Q[i,i+1] = -1,1
R = (sp.eye(5)-h*Q+h*h*Q*Q/2).inv()
assert sp.cancel(R[0,4]-h**4*P/D**4) == 0
assert all(sp.cancel(v-1)==0 for v in R*sp.ones(5,1))
for m,numer in [(1,h*(h+2)),
                (2,h**2*(h**2+4*h+2)),
                (3,h**4*(h**2+6*h+6)),
                (4,h**4*P)]:
    rem = 1-sum(h**k*sp.diff(f,z,k).subs(z,-h)/sp.factorial(k)
                for k in range(m))
    assert sp.cancel(rem-numer/D**m) == 0
    assert sp.cancel(R[4-m,4]-numer/D**m) == 0
assert sp.factor(sp.diff(P,h)) == 4*h*(h*h+6*h+6)
assert sp.sign(P.subs(h,sp.Rational(49660,100000))) == -1
assert sp.sign(P.subs(h,sp.Rational(49661,100000))) == 1
assert sp.factor(sp.diff(f,z,4).subs(z,0)) == -6
# Complete symbolic entrywise classification on the concrete witness.
for i in range(5):
    for j in range(5):
        assert R[i,j] == 0 if j<i else True
        if j<4 and j>=i:
            assert sp.cancel(R[i,j]-h**(j-i)*sp.diff(f,z,j-i).subs(z,-h)/sp.factorial(j-i)) == 0

# Extra exact-arithmetic tests on graphs with depth <=3, no mathematical proof inferred.
rng = Random(1602)
trials=0
for n in (3,4,5,7):
    # Three transient layers, absorbing layer; all transitions forward.
    layers = [i%4 for i in range(n)]
    layers.sort()
    for _ in range(16):
        G=sp.zeros(n)
        for i in range(n):
            for j in range(i+1,n):
                if layers[j]>layers[i] and rng.random()<0.3:
                    G[i,j] = rng.randrange(1,4)
            G[i,i]=-sum(G[i,j] for j in range(n) if j!=i)
        for step in (sp.Rational(1,3),sp.Integer(1),sp.Integer(7)):
            T=(sp.eye(n)-step*G+step*step*G*G/2).inv()
            assert all(sp.cancel(v-1)==0 for v in T*sp.ones(n,1))
            assert all(v>=0 for v in T)
            trials+=1
print('VERIFY_OK', 'exact_formula+derivative+root+small_graph_trials',trials)
