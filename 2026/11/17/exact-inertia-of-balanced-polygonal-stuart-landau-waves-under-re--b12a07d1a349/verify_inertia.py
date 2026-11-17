"""Reproducible structural checks for real-coupled balanced Stuart--Landau states.

The theorem is proved using inertia and the rank-two mean-field Hessian;
these examples test the linearization, exact characteristic factors and index.
"""
import numpy as np
import sympy as sp

def exact_tests():
    z,c=sp.symbols('z c',real=True)
    s3=sp.sqrt(3)
    vec=[(sp.Integer(1),sp.Integer(0)),(-sp.Rational(1,2),s3/2),(-sp.Rational(1,2),-s3/2)]
    J=sp.zeros(6)
    for i,(x,y) in enumerate(vec):
        for j in range(3):
            J[2*i,2*j]+=c
            J[2*i+1,2*j+1]+=c
        for a,va in enumerate((x,y)):
            for b,vb in enumerate((x,y)):
                J[2*i+a,2*i+b]-=2*va*vb
    actual=sp.factor((z*sp.eye(6)-J).det())
    expected=z*(z+2)*(z*z+(2-3*c)*z-3*c)**2
    assert sp.simplify(actual-expected)==0
    for cr,pol in [(sp.Rational(1,3),z*(z+2)*(z*z+z-1)**2),(-sp.Rational(1,3),z*(z+2)*(z*z+3*z+1)**2)]:
        assert sp.simplify(actual.subs(c,cr)-pol)==0
    vec4=[(sp.Integer(1),sp.Integer(0))]*2 + [(-sp.Integer(1),sp.Integer(0))]*2
    H=sp.zeros(8)
    for i,(x,y) in enumerate(vec4):
        for j in range(4):
            H[2*i,2*j]+=c
            H[2*i+1,2*j+1]+=c
        for a,va in enumerate((x,y)):
            for b,vb in enumerate((x,y)):
                H[2*i+a,2*i+b]-=2*va*vb
    exact=sp.factor((z*sp.eye(8)-H).det())
    assert sp.simplify(exact-z**3*(z-4*c)*(z+2)**3*(z+2-4*c))==0
    return actual,exact

def analytic_j(w, alpha, c):
    m=len(w); J=np.zeros((2*m,2*m)); C=c*np.eye(2)
    for j in range(m):
        for i in range(m): J[2*j:2*j+2,2*i:2*i+2]+=C
        v=np.array([w[j].real,w[j].imag]); J[2*j:2*j+2,2*j:2*j+2]-=2*np.outer(v,v)
        # inactive has w=0 and alpha_j-M*c<0; active beta chosen to cancel local term
        J[2*j:2*j+2,2*j:2*j+2] += (alpha[j]-m*c-np.vdot(v,v).real)*np.eye(2)
    return J

def field(x, alpha,c):
    w=x[::2]+1j*x[1::2]
    f=(alpha-abs(w)**2)*w+c*(np.sum(w)-len(w)*w)
    return np.array([v for z in f for v in (z.real,z.imag)])

def counts(j,eps=1e-7):
    e=np.linalg.eigvalsh(j)
    return sum(e>eps),sum(abs(e)<=eps),sum(e< -eps)

def random_tests():
    rng=np.random.default_rng(4217)
    cases=0
    for M in range(3,10):
        for active in range(3,M+1):
            for c in (-.33,.19):
                q=rng.normal(size=(active,2));q-=q.mean(axis=0)
                w=np.array([complex(x,y) for x,y in q]+[0j]*(M-active))
                beta=np.array([M*c+abs(z)**2 for z in w[:active]]+[M*c-(.1+.1*j) for j in range(M-active)])
                J=analytic_j(w,beta,c)
                expected=(0,active-2,2*M-active+2) if c<0 else (2,active-2,2*M-active)
                assert counts(J)==expected,(M,active,c,counts(J),expected)
                x=np.array([v for z in w for v in (z.real,z.imag)])
                assert np.max(np.abs(field(x,beta,c)))<1e-11
                h=1e-6
                D=np.stack([(field(x+h*np.eye(2*M)[j],beta,c)-field(x-h*np.eye(2*M)[j],beta,c))/(2*h) for j in range(2*M)],axis=1)
                assert np.max(np.abs(D-J))<1e-7
                cases+=1
    return cases

def collinear_tests():
    w=np.array([1+0j,1+0j,-1+0j,-1+0j])
    checks=0
    for c,expected in [(sp.Rational(-1,3),(0,3,5)),(sp.Rational(1,10),(1,3,4)),(sp.Rational(1,2),(1,4,3)),(sp.Integer(1),(2,3,3))]:
        cf=float(c)
        alpha=np.full(4,4*cf+1)
        assert counts(analytic_j(w,alpha,cf),eps=1e-8)==expected
        checks+=1
    return checks

if __name__=='__main__':
    e,q=exact_tests()
    nr=random_tests()
    nc=collinear_tests()
    print(f'VERIFY_OK equilateral_exact=1 collinear_exact=1 noncollinear_inertia_and_jacobian_cases={nr} collinear_sign_cases={nc}')
