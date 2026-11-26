"""Reproducibility checks for optimal two-coordinate batch sampling on a three-node Gram path.

Requires numpy and sympy. Finite checks supplement, but do not replace, the symbolic proof.
"""
import numpy as np
import sympy as sp


def formula(u, v):
    assert 0 < u and 0 < v and u*u + v*v < 1
    a = np.sqrt(1 - v*v)
    b = np.sqrt(1 - u*u)
    delta = 1 - u*u - v*v
    z = 3 - u*u - v*v - 2*u*a - 2*v*b
    p = np.array([a*(a-u), 1-u*a-v*b, b*(b-v)]) / z
    return p, delta/z


def setup(u, v):
    g = np.array([[1.,u,0.],[u,1.,v],[0.,v,1.]])
    a = np.linalg.cholesky(g).T
    raw = np.linalg.inv(a).T
    normals = raw / np.linalg.norm(raw, axis=0)
    h = normals.T @ normals
    return a, normals, h


def rate(normals, p):
    return np.linalg.eigvalsh((normals*p[None,:]) @ normals.T)[-1]


# An exact-arithmetic, nontrivial benchmark: u=v=3/5.
r=sp.Rational(3,5)
g=sp.Matrix([[1,r,0],[r,1,r],[0,r,1]])
gi=g.inv()
d=sp.diag(*[sp.sqrt(gi[i,i]) for i in range(3)])
h=sp.simplify(d.inv()*gi*d.inv())
assert h==sp.Matrix([[1,-sp.Rational(3,4),sp.Rational(9,16)],[-sp.Rational(3,4),1,-sp.Rational(3,4)],[sp.Rational(9,16),-sp.Rational(3,4),1]])
p=sp.diag(sp.Rational(2,3),sp.Rational(1,3),sp.Rational(2,3))
mat=p*h*p
assert sorted(mat.eigenvals(),key=float)==[sp.Rational(1,36),sp.Rational(7,36),sp.Rational(7,9)]

rng = np.random.default_rng(20261013)
checked=0
for k in range(350):
    rad=np.sqrt(rng.uniform(.00005,.9995))
    angle=rng.uniform(.015,np.pi/2-.015)
    u=rad*np.cos(angle)
    v=rad*np.sin(angle)
    opt, predicted=formula(u,v)
    A,V,H=setup(u,v)
    assert np.all(opt>0) and abs(opt.sum()-1)<2e-12
    assert abs(rate(V,opt)-predicted)<2e-10
    s=np.array([1.,-1.,1.])
    K=np.linalg.inv(H)
    assert np.allclose(opt, (s*(K@s))/(s@K@s),rtol=1e-9,atol=1e-10)
    # The balanced witness has identical signed inner products with each unit normal.
    y=np.linalg.solve(V.T,s)
    y/=np.linalg.norm(y)
    assert np.allclose((V.T@y)**2,predicted,atol=2e-10)
    # The sharp result optimizes over all, not only symmetric, probability laws.
    for j in range(95):
        p2=rng.dirichlet(np.array([.35,.35,.35]))
        assert rate(V,p2)>=predicted-3e-10
        checked+=1
    # Check the actual two-coordinate least-squares projection identity.
    for i in range(3):
        B=[j for j in range(3) if j !=i]
        PB=A[:,B]@np.linalg.inv(A[:,B].T@A[:,B])@A[:,B].T
        assert np.linalg.norm((np.eye(3)-PB)-np.outer(V[:,i],V[:,i]))<2e-10
    checked+=1

# A 2-D quadrature of the limiting probability simplex at the rational example.
pred=formula(.6,.6)[1]
A,V,H=setup(.6,.6)
for x in np.linspace(0,1,101):
    for y in np.linspace(0,1-x,101):
        assert rate(V,np.array([x,y,1-x-y]))>=pred-1e-10
        checked+=1
print('PASS exact rational symbolic eigenvalues; 350 Gram families, 33250 random laws,')
print('10552 probability-grid laws, 1050 direct projection identities; total numeric checks:',checked)
