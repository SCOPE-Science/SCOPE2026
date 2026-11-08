"""Reproduce the graph-splitting spectral formula and strict local stability frontier.

Requires NumPy and SymPy. The analytic proof is in RESULT.md; checks here are finite
and are not offered as an infinite-case certification.
"""
import math
import numpy as np
import sympy as sp


def graph_laplacian(n):
    # Connected path; no randomness is needed for this reproducible check.
    G = np.zeros((n,n),dtype=float)
    for i in range(n-1):
        t = (i+1)/4 + 0.5
        G[i,i] += t; G[i+1,i+1] += t
        G[i,i+1] -= t; G[i+1,i] -= t
    return G


def map_f(z, gamma, G, a, beta):
    n=len(z); K=G+a*np.eye(n)
    u=z/np.linalg.norm(z)
    x=np.linalg.solve(np.eye(n)+gamma*K,2*u-z-gamma*beta*u**3)
    return z+x-u


def expected_jacobian(gamma,G,a,beta):
    n=len(G); b=beta/n; c=a+b
    s=1-gamma*c
    assert s>0
    P=np.eye(n)-np.ones((n,n))/n
    M=np.eye(n)+gamma*(G+a*np.eye(n))
    inv=np.linalg.inv(M)
    return np.eye(n)-inv+((2-3*gamma*b)*inv-np.eye(n))@P/s


def main():
    g, l, a, b = sp.symbols('g l a b', positive=True)
    c=a+b
    s=1-g*c
    eig=sp.factor(1 - 1/(1+g*(a+l)) + ((2-3*g*b)/(1+g*(a+l))-1)/s)
    theory=1-g*(l+2*b)/(s*(1+g*(a+l)))
    assert sp.simplify(eig-theory)==0
    assert sp.simplify((1+theory)*s*(1+g*(a+l)) - (2+g*(l-4*b)-2*g*g*(a+l)*c))==0
    assert sp.simplify((2+g*(l-4*b)-2*g*g*l*b).subs(a,0)-(1-2*g*b)*(2+g*l))==0
    assertions=3

    G=sp.Matrix([[1,-1,0],[-1,2,-1], [0,-1,1]])
    assert sorted(G.eigenvals()) == [0,1,3]
    a0=sp.Integer(1); b0=sp.Integer(1); g0=sp.Rational(1,3)
    vals=[sp.factor(theory.subs({g:g0,l:x,a:a0,b:b0})) for x in (1,3)]
    radial=g0*a0/(1+g0*a0)
    assert vals == [sp.Rational(-4,5),sp.Rational(-8,7)], vals
    assert radial == sp.Rational(1,4)
    critical=(sp.sqrt(129)-1)/32
    assert sp.simplify((2+g*(l-4*b)-2*g*g*(a+l)*c).subs({g:critical,l:3,a:1,b:1}))==0
    assert float(critical)<float(g0)<sp.Rational(1,2)
    assertions+=5

    for n in [2,3,4,5,7]:
        G=graph_laplacian(n); lam=np.linalg.eigvalsh(G); L=lam[-1]
        for a in [0.0,0.125,1.0,3.0]:
            for beta in [0.2,1.0,6.0]:
                b=beta/n; c=a+b
                star=(L-4*b+math.sqrt((L-4*b)**2+16*(a+L)*c))/(4*(a+L)*c)
                assert (a==0 and abs(star-1/(2*c))<1e-11) or (a>0 and 1/(2*c)<star<1/c)
                for frac in [0.27,0.72,0.997,1.004]:
                    gamma=star*frac
                    assert gamma<1/c
                    s=1-gamma*c
                    e=np.ones(n)/math.sqrt(n)
                    zstar=s*e
                    F=map_f(zstar,gamma,G,a,beta)
                    assert np.max(abs(F-zstar))<2e-13
                    J=expected_jacobian(gamma,G,a,beta)
                    E=np.empty_like(J)
                    for j in range(n):
                        v=np.zeros(n); v[j]=1
                        eps=1e-6*s
                        E[:,j]=(map_f(zstar+eps*v,gamma,G,a,beta)-map_f(zstar-eps*v,gamma,G,a,beta))/(2*eps)
                    assert np.max(abs(E-J))<1e-7, (n,a,beta,gamma, np.max(abs(E-J)))
                    diag=sorted([gamma*a/(1+gamma*a)]+[1-gamma*(x+2*b)/(s*(1+gamma*(a+x))) for x in lam[1:]])
                    computed=sorted(np.linalg.eigvalsh(J))
                    assert np.max(abs(np.array(diag)-np.array(computed)))<3e-12
                    if frac<1:
                        assert max(abs(x) for x in computed)<1
                    else:
                        assert min(computed)<-1
                    assertions+=5
    print('PASS: %d symbolic, exact-rational, spectral and finite-difference assertions' % assertions)
    print('Exact three-vertex example: transverse eigs',vals,'radial',radial,'critical',critical)

if __name__=='__main__':
    main()
