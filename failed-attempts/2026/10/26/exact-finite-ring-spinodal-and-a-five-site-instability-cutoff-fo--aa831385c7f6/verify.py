"""Direct finite-ring linearization checks for an active lattice-gas mean field.

Requires numpy. Executes deterministic identities and direct spatial Jacobian
comparisons; the symbolic proof in RESULT.md is the infinite-parameter argument.
"""
import math
import numpy as np
import sympy as sp


def flow(x, L, rho, a, t, r):
    p = x.reshape(L, 2)
    occupancy = p.sum(axis=1)
    q = 1.0 - occupancy
    ans = np.zeros_like(p)
    for i in range(L):
        left, right = (i-1) % L, (i+1) % L
        for z, source in enumerate((left, right)):
            target = right if z == 0 else left
            active = a*(p[source, z]*q[i] - p[i, z]*q[target])
            thermal = t*(p[left, z]*q[i]+p[right, z]*q[i]
                         -p[i, z]*(q[left]+q[right]))
            ans[i, z] = active + thermal + r*(p[i, 1-z]-p[i, z])
    return ans.ravel()


def finite_jacobian(L, rho, a, t, r):
    base = np.full(2*L, rho/2.0)
    delta = 1e-6
    jac = np.zeros((2*L,2*L))
    for j in range(2*L):
        xp, xm = base.copy(), base.copy()
        xp[j] += delta
        xm[j] -= delta
        jac[:,j] = (flow(xp,L,rho,a,t,r)-flow(xm,L,rho,a,t,r))/(2*delta)
    return jac


def bloch_eigenvalues(L, rho, a, t, r):
    out=[]
    for n in range(L):
        k=2*math.pi*n/L
        h=1-math.cos(k)
        A=a+2*t
        B=(1-rho)*(a+2*t)
        J=np.array([[-A*h, -1j*a*(1-rho)*math.sin(k)],
                    [-1j*a*(1-2*rho)*math.sin(k), -2*r-B*h]],dtype=complex)
        out.extend(np.linalg.eigvals(J))
    return np.array(out)


def threshold(L,rho,t,r):
    h=1-math.cos(2*math.pi/L)
    G=2*(1-rho)*((2*rho-1)-rho*h)
    if G<=0: return math.inf
    b=2*r+4*t*(1-rho)*h
    c=4*t*(r+t*(1-rho)*h)
    return (b+math.sqrt(b*b+4*G*c))/(2*G)


def nonconserved_growth(L,rho,a,t,r):
    lam=bloch_eigenvalues(L,rho,a,t,r)
    z=np.argmin(abs(lam))
    lam=np.delete(lam,z)
    return float(max(lam.real))


def run():
    checks=0
    rho,a,t,r,h=sp.symbols('rho a t r h',real=True)
    A=a+2*t
    B=(1-rho)*A
    C=a**2*(1-rho)*(2*rho-1)
    G=2*(1-rho)*((2*rho-1)-rho*h)
    b=2*r+4*t*(1-rho)*h
    d=4*t*(r+t*(1-rho)*h)
    determinant=A*h*(2*r+B*h)+a**2*(1-rho)*(1-2*rho)*h*(2-h)
    assert sp.simplify(determinant-h*(2*r*A+A*B*h-C*(2-h)))==0
    checks+=1
    assert sp.simplify(C*(2-h)-A*(2*r+B*h)-(G*a*a-b*a-d))==0
    checks+=1
    c=sp.symbols('c',real=True)
    f=(1-rho)*((1+c)*rho-1)
    rhom=(2+c)/(2*(1+c))
    assert sp.simplify(f.subs(rho,rhom)-c*c/(4*(1+c)))==0
    checks+=1
    for L in range(3,12):
        for rho in (0.25,0.55,0.8,0.94):
            for a,t,r in ((2,0,1),(12,.2,1),(90,.05,.7)):
                J=finite_jacobian(L,rho,a,t,r)
                eig=np.sort_complex(np.linalg.eigvals(J))
                ref=np.sort_complex(bloch_eigenvalues(L,rho,a,t,r))
                # complex conjugacy sorting may reorder near multiple eigenvalues.
                remain=list(ref)
                for v in eig:
                    j=int(np.argmin(abs(np.array(remain)-v)))
                    assert abs(v-remain.pop(j))<1e-6, (L,rho,a,t,r,v)
                checks+=1
                h=1-math.cos(2*math.pi/L)
                A=a+2*t
                B=(1-rho)*(a+2*t)
                C=a*a*(1-rho)*(2*rho-1)
                rhs=2*r*A + A*B*h-C*(2-h)
                pred=rhs<0
                actual=nonconserved_growth(L,rho,a,t,r)>1e-7
                assert actual==pred, (L,rho,a,t,r,rhs,actual)
                checks+=1
    for L in (5,6,8,12,24):
        rho=.92
        for t in (0,.25,3):
            a0=threshold(L,rho,t,1.)
            assert math.isfinite(a0)
            assert nonconserved_growth(L,rho,a0*.99,t,1)<-1e-9
            assert nonconserved_growth(L,rho,a0*1.01,t,1)>1e-9
            checks+=2
    for L in (3,4):
        for rho in (.1,.4,.6,.9,.99):
            for t in (0,.01,2):
                assert threshold(L,rho,t,1)==math.inf
                assert nonconserved_growth(L,rho,1e5,t,1)<0
                checks+=2
    for L in (5,6,10,20,100):
        c=math.cos(2*math.pi/L)
        optim=(2+c)/(2*(1+c))
        a_min=4*(1+c)/(c*c)
        assert abs(a_min-threshold(L,optim,0,1))<1e-8
        for drho in (-.02,.02):
            rho=optim+drho
            if 0<rho<1:
                assert threshold(L,rho,0,1)>a_min
        checks+=1
    for L in (80,120,200,400):
        rho=.8; r=1.2;t=.7
        R=(1-rho)*(2*rho-1)
        ai=(r+math.sqrt(r*r+8*r*t*R))/(2*R)
        A=ai+2*t;B=(1-rho)*(ai+2*t);C=ai*ai*R
        coeff=math.pi**2*(C+A*B)/(2*ai*R-r)
        e=threshold(L,rho,t,r)-ai
        assert abs(e*L*L/coeff-1)<.012,(L,e*L*L/coeff)
        checks+=1
    print(f'PASS {checks} deterministic check groups')

if __name__=='__main__':run()
