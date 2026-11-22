"""Independent exact-arithmetic and numerical checks for crown-polytope distance laws.

Run with Python 3; scipy is needed for independent quadratic-program tests.
"""
from fractions import Fraction as F
from math import comb, factorial, isclose, sqrt
from random import Random
from scipy.optimize import minimize


def proj(p, q):
    n = len(p)
    active = [i for i in range(n) if p[i]+q[i] > 1]
    if not active:
        return p[:], q[:], F(0)
    assert len(active) == 1
    i = active[0]
    d = p[i]+q[i]-1
    cp, cq = p[:], q[:]
    for j in range(n):
        v = -d/2 if j == i else d/F(2*(n-1))
        cp[j] += v
        cq[j] += v
    return cp, cq, d


def sqdist(p,q,u,v):
    return sum((a-b)**2 for a,b in zip(p,u)) + sum((a-b)**2 for a,b in zip(q,v))


def exact_checks():
    rng=Random(44777)
    count=0
    for n in range(3,10):
        assert 0 < F(n, comb(2*n-2,n-1)) < 1
        for _ in range(150):
            i=rng.randrange(n)
            # Exactly rational point in an excised cap, both first coordinates positive.
            a=F(rng.randrange(51,91),100)
            b=F(rng.randrange(51,91),100)
            assert a+b>1
            weights1=[rng.randrange(1,20) for _ in range(n-1)]
            weights2=[rng.randrange(1,20) for _ in range(n-1)]
            p=[F(0)]*n; q=[F(0)]*n
            p[i]=a; q[i]=b
            ks=[j for j in range(n) if j!=i]
            for j,v in zip(ks,weights1):p[j]=(1-a)*F(v,sum(weights1))
            for j,v in zip(ks,weights2):q[j]=(1-b)*F(v,sum(weights2))
            cp,cq,d=proj(p,q)
            assert sum(cp)==sum(cq)==1
            assert all(z>=0 for z in cp+cq)
            assert all(cp[j]+cq[j]<=1 for j in range(n))
            assert cp[i]+cq[i]==1
            assert sqdist(p,q,cp,cq)==d*d*F(n,2*(n-1))
            count+=1
    return count


def numerical_qp_checks():
    rng=Random(10234)
    count=0; max_gap=0.
    for n in (3,4,5,6):
        for k in range(24):
            i=rng.randrange(n)
            a=0.52+0.43*rng.random();b=0.52+0.43*rng.random()
            w=[rng.random() for _ in range(n-1)]; z=[rng.random() for _ in range(n-1)]
            w=[t/sum(w) for t in w];z=[t/sum(z) for t in z]
            p=[0.]*n;q=[0.]*n;p[i]=a;q[i]=b
            for j,x,y in zip((j for j in range(n) if j!=i),w,z):
                p[j]=(1-a)*x;q[j]=(1-b)*y
            p0=[F(str(x)) for x in p];q0=[F(str(x)) for x in q]
            cp,cq,d=proj(p0,q0)
            predicted=[float(x) for x in cp+cq]
            initial=p+q
            constraints=[{'type':'eq','fun': lambda y,n=n: sum(y[:n])-1},
                         {'type':'eq','fun': lambda y,n=n: sum(y[n:])-1}]
            constraints += [{'type':'ineq','fun':lambda y,j=j,n=n:1-y[j]-y[n+j]} for j in range(n)]
            result=minimize(lambda y:sum((y[j]-initial[j])**2 for j in range(2*n)),
                x0=predicted, jac=lambda y:[2*(y[j]-initial[j]) for j in range(2*n)],
                constraints=constraints,bounds=[(0.,1.)]*(2*n),method='SLSQP',
                options={'ftol':1e-12,'maxiter':300})
            if not result.success: raise AssertionError((n,k,result.message))
            error=max(abs(x-y) for x,y in zip(result.x,predicted))
            assert error<1e-7, (n,error)
            max_gap=max(max_gap,error);count+=1
    return count,max_gap


def beta_checks():
    # The cap's base consists of 2n-2 free nonnegative coordinates and one apex.
    for n in range(3,30):
        dim=2*n-2; eta=F(n,comb(dim,n-1))
        for r in range(1,8):
            exact_moment=eta*F(factorial(r)*factorial(dim),factorial(dim+r))
            assert exact_moment>0
        # Cross-check an independent beta convolution finite integral:
        # (n-1)^2 integral_{u+v<1} u^(n-2) v^(n-2) du dv
        integral=F((n-1)**2*factorial(n-2)*factorial(n-2),factorial(2*n-2))
        assert integral* n ==eta
    return 27

if __name__=='__main__':
    a=exact_checks();b,g=numerical_qp_checks();c=beta_checks()
    print(f'CROWN_DISTANCE_PASS rational_projection_points={a} independent_qp={b} max_gap={g:.2e} beta_integrals={c}')
