"""Exact first-principles verification of stationary zero-digit correlations.

Requires SymPy. No floating-point assumptions or external data.
"""
import sympy as sp

sq5 = sp.sqrt(5)
beta = (1 + sq5)/2
alpha = 1 + beta**(-2)
points = [sp.simplify(t) for t in
          (-1, -1/beta, -1/beta**2, -1/beta**3,
           1/beta**3, 1/beta**2, 1/beta, 1)]
S = sp.zeros(7)
for i in range(7):
    slope = beta**2 if i in (0, 6) else beta
    intercept = beta*alpha if i == 0 else (-beta*alpha if i == 6 else 0)
    left = sp.simplify(slope*points[i] + intercept)
    right = sp.simplify(slope*points[i+1] + intercept)
    assert right > left
    total = sp.Integer(0)
    for j in range(7):
        if bool(sp.simplify(left <= points[j])) and bool(sp.simplify(points[j+1] <= right)):
            S[i,j] = sp.simplify((points[j+1]-points[j])/(right-left))
            total += S[i,j]
    assert sp.simplify(total-1) == 0, (i,total)

# Each row groups its targets by reflected cell labels.
groups = [[0,6],[1,5],[2,4],[3]]
Q = sp.zeros(4)
for a, g in enumerate(groups):
    for b, h in enumerate(groups):
        Q[a,b] = sp.simplify(sum(S[g[0],j] for j in h))
        for i in g[1:]:
            assert sp.simplify(Q[a,b]-sum(S[i,j] for j in h)) == 0

expected_Q = sp.Matrix([
    [0, sq5-2, 7-3*sq5, 2*sq5-4],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, (3-sq5)/2, (sq5-1)/2],
])
assert all(sp.simplify(z)==0 for z in Q-expected_Q)
pi = sp.Matrix([(sp.Rational(1,4)),sp.Rational(1,4),
                (3-sq5)/4,(sq5-1)/4])
assert all(sp.simplify(z)==0 for z in (pi.T*Q-pi.T))
assert sp.simplify(sum(pi)-1)==0
r = sp.Matrix([0,1,1,1]); ones = sp.ones(4,1)
mean=sp.simplify((pi.T*r)[0]); assert mean==sp.Rational(3,4)
f=r-mean*ones
cov=lambda n:sp.simplify((pi.T*sp.diag(*f)*(Q**n)*f)[0])
known=[sp.Rational(3,16),-sp.Rational(1,16),
       (4*sq5-9)/16,(27-12*sq5)/16]
assert [sp.simplify(cov(n)-known[n]) for n in range(4)]==[0]*4
z=sp.symbols('z')
char=sp.factor(Q.charpoly(z).as_expr())
assert sp.simplify(char-z*(z-1)*(z*z+beta**(-2)*z+beta**(-4)))==0
ratio=sp.simplify(beta**(-6))
for n in range(1,13):
    assert sp.simplify(cov(n+3)-ratio*cov(n))==0
sumC=sp.simplify(cov(0)+2*(cov(1)+cov(2)+cov(3))/(1-ratio))
assert sp.simplify(sumC-sq5/32)==0
# Green-Kubo independently via resolvent on the centered subspace.
poisson=(sp.eye(4)-Q+ones*pi.T).inv()*f
v=sp.simplify((pi.T*sp.diag(*f)*(2*poisson-f))[0])
assert sp.simplify(v-sq5/32)==0
print('GOLDEN_ENDPOINT_MARKOV_COVARIANCE_EXACT_OK full_cells=7 lumped=4 lags=16')
print('mean=',mean,'asymptotic_variance=',v,'three_step_ratio=',ratio)
