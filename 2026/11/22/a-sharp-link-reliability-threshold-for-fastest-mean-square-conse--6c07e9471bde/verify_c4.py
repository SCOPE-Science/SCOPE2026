"""Independent exact checks for C4 random-edge consensus rate theorem.
Requires SymPy. Finite checks corroborate, but do not replace, the proof.
"""
from itertools import product
import sympy as s
p,h=s.symbols('p h', positive=True)
n=4
edges=[(0,1),(1,2),(2,3),(3,0)]
L=s.zeros(n);Bs=[]
for u,v in edges:
    z=s.zeros(n,1);z[u]=1;z[v]=-1
    B=z*z.T;Bs.append(B);L+=B
P2=L*(4*s.eye(4)-L)/4
P4=L*(L-2*s.eye(4))/8
assert P2**2==P2 and P4**2==P4 and P2*P4==s.zeros(n)
Ps=[P2,P4]
K=s.zeros(2)
for j,X in enumerate(Ps):
    T=s.zeros(4)
    for bits in product((0,1),repeat=4):
        W=s.eye(4);weight=s.Integer(1)
        for bit,B in zip(bits,Bs):
            if bit:W-=h*B;weight*=p
            else:weight*=1-p
        T+=weight*W*X*W
    for i,Y in enumerate(Ps):
        K[i,j]=s.factor(s.trace(Y*T)/s.trace(Y))
expected=s.Matrix([
 [1-4*p*h+(2*p*p+2*p)*h*h, 2*p*(1-p)*h*h],
 [4*p*(1-p)*h*h,1-8*p*h+(12*p*p+4*p)*h*h]])
assert s.simplify(K-expected)==s.zeros(2)
S=s.Matrix([[K[0,0],s.sqrt(2)*K[0,1]],
            [K[1,0]/s.sqrt(2),K[1,1]]])
assert S==S.T
C=s.diff(S,h,2)/2
assert s.factor(C[0,0])==2*p*(p+1)
assert s.factor(C.det())==16*p**3*(p+3)
Tpoly=(33*p*p-6*p+9)*h*h-(20*p+4)*h+4
assert s.factor((s.trace(K)**2-4*K.det())/(4*p*p*h*h)-Tpoly)==0
R=1-6*p*h+(7*p*p+3*p)*h*h+p*h*s.sqrt(Tpoly)
assert s.simplify((s.trace(K)+s.sqrt(s.trace(K)**2-4*K.det()))/2-R)==0
D=s.factor((s.diff(R,h).subs(h,s.Rational(1,2)))/p)
N=33*p*p-36*p+11;Q=33*p*p-46*p+17
assert s.simplify(D-(7*p-3+N/s.sqrt(Q)))==0
assert s.simplify(N*N-(3-7*p)**2*Q+16*(p-1)*(3*p-2)*(11*p*p-8*p+1))==0
pstar=(4-s.sqrt(5))/11
assert s.simplify(11*pstar*pstar-8*pstar+1)==0
assert s.simplify(D.subs(p,pstar))==0
assert s.simplify(R.subs({p:s.Rational(3,4),h:s.Rational(2,5)}))==s.Rational(7,25)
assert s.simplify(R.subs({p:1,h:s.Rational(1,3)}))==s.Rational(1,9)
print('PASS: 16 exact Bernoulli masks per projector, symbolic covariance matrix and spectral discriminant; positive-definite quadratic coefficient; exact crossover factorization and root; two endpoint rate identities.')
