"""Exact symbolic checks for the one-step-per-delay randomized Runge--Kutta stability result.
Run: python verify.py (requires SymPy >=1.12)."""
import sympy as S
s, gamma, z, w = S.symbols('s gamma z w', real=True)
assertions = 0

def verify(condition, description):
    global assertions
    if not condition:
        raise AssertionError(description)
    assertions += 1

# For the scalar pure-delay vector field f(t,x,y)=-b*y and lag equal to one step:
# the intermediate delayed value is Y_(j-1)-s*gamma*Y_(j-2).
# Hence Y_(j+1)=Y_j-s*Y_(j-1)+s**2*gamma*Y_(j-2).
B = S.Matrix([[1, -s, s*s*gamma], [1, 0, 0], [0, 1, 0]])
A = S.integrate(B, (gamma,0,1))
verify(A == S.Matrix([[1,-s,s*s/2],[1,0,0],[0,1,0]]), 'mean companion')

pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
M = S.zeros(6)
for k,(i,j) in enumerate(pairs):
    X=S.zeros(3)
    X[i,j]=1
    X[j,i]=1
    Y = (B*X*B.T).applyfunc(lambda v:S.integrate(S.expand(v),(gamma,0,1)))
    for row,(a,b) in enumerate(pairs):
        M[row,k]=S.factor(Y[a,b])
expected_M=S.Matrix([
 [1,-2*s,s*s,s*s,-s**3,s**4/S.Integer(3)],
 [1,-s,s*s/2,0,0,0],
 [0,1,0,-s,s*s/2,0],
 [1,0,0,0,0,0],
 [0,1,0,0,0,0],
 [0,0,0,1,0,0]
])
verify(M==expected_M,'six-dimensional covariance operator')
Q=s**7-s**5-4*s**4-4*s**3+12*s**2-24*s+24
verify(S.factor((S.eye(6)-M).det()-s*Q/12)==0,'determinant identity')

sturm=S.sturm(Q,s)
verify([S.degree(u,s) for u in sturm]==list(range(7,-1,-1)),'Sturm degrees')
def signs_at(x):
    return [int(S.sign(v.subs(s,x))) for v in sturm]
def changes(vals):
    vals=[v for v in vals if v]
    return sum(u!=v for u,v in zip(vals,vals[1:]))
verify(changes(signs_at(S.Integer(0)))==4,'Sturm at zero')
verify(changes(signs_at(S.Rational(3,2)))==3,'Sturm at three-halves')
verify(Q.subs(s,S.Rational(9,8))>0 and Q.subs(s,S.Rational(7,6))<0,'unique-root bracket')
verify(S.factor(Q.subs(s,S.Rational(7,6))) == -S.Rational(181541,279936),'exact rational sign')
verify(S.factor((S.eye(6)-M).det().subs(s,S.Rational(7,6))) == -S.Rational(1270787,20155392),'negative det at comparison point')

# Routh--Hurwitz test for expectation/deterministic central stage at s=7/6.
p=z**3-z**2+s*z-s*s/2
H=S.expand((1+w)**3-(1+w)**2*(1-w)+s*(1+w)*(1-w)**2-s*s/2*(1-w)**3)
verify(S.factor(H.subs(s,S.Rational(7,6))-(277*w**3+57*w**2+207*w+35)/72)==0,'bilinear transform')
verify(57*207>277*35,'strict cubic Routh inequality')

# Verify the mean-stage plus variance decomposition of the covariance operator.
v=S.symbols('v',nonnegative=True)
E=S.zeros(3); E[0,2]=s*s
Bmean=A
X=S.Matrix(3,3,lambda i,j: S.symbols('x'+str(i)+str(j)))
X=(X+X.T)/2
for i in range(3):
 for j in range(3):
  lhs=(B*X*B.T).applyfunc(lambda u:S.integrate(S.expand(u),(gamma,0,1)))[i,j]
  rhs=(A*X*A.T+(s**4/S.Integer(12))*X[2,2]*(S.eye(3)[:,0]*S.eye(3)[:,0].T))[i,j]
  verify(S.simplify(lhs-rhs)==0,'positive variance correction')

# Exact first-order perturbation at s=0: left eigenvector e1, right all ones.
verify(M.subs(s,0)*S.ones(6,1)==S.ones(6,1),'right eigenvector at zero')
verify((S.eye(6)[0,:]*M.subs(s,0)) == S.eye(6)[0,:],'left eigenvector at zero')
verify((S.eye(6)[0,:]*M.diff(s).subs(s,0)*S.ones(6,1))[0]==-2,'Perron eigenvalue derivative')

# Numerical evaluations below merely corroborate the exact proof.
import mpmath as mp
mp.mp.dps=45
root=mp.findroot(lambda x: x**7-x**5-4*x**4-4*x**3+12*x**2-24*x+24,(mp.mpf('1.14'),mp.mpf('1.15')))
verify(mp.mpf(9)/8 < root < mp.mpf(7)/6, 'numerical root in proved rational bracket')
print('Exact symbolic assertions:',assertions)
print('Unique positive stability root below 3/2:',mp.nstr(root,35))
print('Q(7/6):',Q.subs(s,S.Rational(7,6)))
print('det(I-M(7/6)):',S.factor((S.eye(6)-M).det().subs(s,S.Rational(7,6))))
print('Deterministic central-stage mean is Schur stable at 7/6: Routh checked.')
print('The exact moment operator and Sturm crossing checks passed.')
