"""Reproduce the two-token flip-cycle Jacobian and local-contraction checks."""
import math
import numpy as np
import sympy as sp

def transform(x, a, b, beta, eta):
    dot = x @ x.T
    weights=np.exp(beta*(dot-dot.max(axis=1,keepdims=True)))
    weights/=weights.sum(axis=1,keepdims=True)
    v=np.diag([a,-b])
    n=x+eta*(weights @ x) @ v
    return n/np.linalg.norm(n,axis=1)[:,None]

def state(horizontal,sgn):
    u=np.asarray(horizontal,dtype=float)
    return np.column_stack((u, np.asarray(sgn)*np.sqrt(1-u*u)))

def run():
    A,B,E,T=sp.symbols('a b eta t', positive=True, real=True)
    Cmat=(sp.eye(2)+E*A*sp.ones(2,2)/2)/(E*B-1)
    Bmat=(sp.eye(2)+E*A*sp.Matrix([[(1+T)/2,(1-T)/2],[(1-T)/2,(1+T)/2]]))/(E*B*T-1)
    c_expected=[(1+E*A)/(E*B-1),1/(E*B-1)]
    b_expected=[(1+E*A)/(E*B*T-1),(1+E*A*T)/(E*B*T-1)]
    for mat, vals in [(Cmat,c_expected),(Bmat,b_expected)]:
        z=sp.symbols('z')
        assert sp.factor(mat.charpoly(z).as_expr()-sp.prod(z-v for v in vals)) == 0
    a,b,beta,eta=1.,3.,1.,3.
    t=math.tanh(beta)
    assert b*t-a>2/eta
    A=np.array([[(1+t)/2,(1-t)/2],[(1-t)/2,(1+t)/2]])
    cases=[('consensus',[1,1], (np.eye(2)+eta*a*np.ones((2,2))/2)/(eta*b-1), [ (1+eta*a)/(eta*b-1), 1/(eta*b-1)]),
           ('split',[1,-1], (np.eye(2)+eta*a*A)/(eta*b*t-1),[(1+eta*a)/(eta*b*t-1),(1+eta*a*t)/(eta*b*t-1)])]
    for name,sgn,M,vals in cases:
        origin=state([0,0],sgn)
        y=transform(origin,a,b,beta,eta)
        assert np.max(np.abs(y+origin)) < 1e-14, (name,y)
        eps=1e-6
        J=np.zeros((2,2))
        for i in range(2):
            d=np.zeros(2);d[i]=eps
            J[:,i]=(transform(state(d,sgn),a,b,beta,eta)[:,0]-transform(state(-d,sgn),a,b,beta,eta)[:,0])/(2*eps)
        assert np.max(np.abs(J-M))<1e-8, (name,J,M)
        assert np.max(np.abs(np.sort(np.linalg.eigvals(M))-np.sort(vals)))<1e-12
        assert max(abs(v) for v in vals)<1
        d=np.array([1.e-3,-8.e-4]); xx=state(d,sgn)
        for _ in range(2*30): xx=transform(xx,a,b,beta,eta)
        assert np.max(np.abs(xx-origin))<1e-8, (name,xx-origin)
    # Near the exact boundary the split Floquet eigenvalue changes through 1.
    critical=2/(b*t-a)
    for h,expect_less in [(0.99*critical,False),(1.01*critical,True)]:
        c=h*b*t-1
        assert c>0
        leading=(1+h*a)/c
        assert (abs(leading)<1)==expect_less
    # Strictness of concentration requirement.
    beta0=math.atanh(a/b)
    assert b*math.tanh(beta0)-a<1e-14
    assert b*math.tanh(beta0+0.01)-a>0
    print('VERIFY_OK symbolic_characteristic_polynomials=2 finite_differences=4 stable_period_two_orbits=2 sharp_boundary=2')

if __name__=='__main__': run()
