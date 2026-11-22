"""Finite diagnostics of the power-sum formulas in the accompanying theorem.

The all-degree minimization and uniqueness are analytic arguments, not consequences
of these finite tests. Requires sympy, numpy and scipy for the numerical section.
"""
from math import factorial, pi
import numpy as np
import sympy as sp
from scipy.optimize import minimize

checks = 0

def assert_ok(condition, message):
    global checks
    assert condition, message
    checks += 1

def newton_coefficients(S, n):
    e = [sp.Integer(1)]
    for j in range(1, n+1):
        e.append(sp.expand(sum((-1)**(k-1)*e[j-k]*S[k] for k in range(1,j+1))/j))
    return e

def next_power(e, S, n):
    return sp.expand(sum((-1)**(k-1)*e[k]*S[n+1-k] for k in range(1,n+1)))

s=sp.symbols('s', real=True)
for n in range(2, 10):
    S = [None,s]+[sp.symbols(f'v_{n}_{k}') for k in range(2,n+1)]
    e = newton_coefficients(S,n)
    p = next_power(e,S,n)
    subs = {S[k]:0 for k in range(2,n+1)}
    for k in range(1,n+1):
        assert_ok(sp.simplify(e[k].subs(subs)-s**k/sp.factorial(k))==0, f'Newton coefficient n={n}, k={k}')
    assert_ok(sp.simplify(p.subs(subs)-(-1)**(n-1)*s**(n+1)/sp.factorial(n))==0,f'first tail n={n}')
    for k in range(2,n+1):
        D=sp.diff(p,S[k]).subs(subs)
        formula=-(n+1)*(-s)**(n+1-k)/(k*sp.factorial(n+1-k))
        assert_ok(sp.simplify(D-formula)==0,f'tail derivative n={n},k={k}')

# Geometric Poisson/Parseval checks at independent nonregular configurations.
for zeros in [[0.14+0.13j,-0.07+0.03j],
              [0.11+0.02j,-0.06+0.07j,0.05-0.04j],
              [0.3+0.1j,0.1-0.2j,-0.2-0.05j,0.03+0.08j]]:
    z=np.array(zeros,dtype=complex)
    e_direct=np.sum((z[:,None]*z[None,:].conj())/(1-z[:,None]*z[None,:].conj())).real
    k=np.arange(1,150)
    sk=np.sum(z[:,None]**k[None,:],axis=0)
    e_fourier=np.sum(abs(sk)**2)
    assert_ok(abs(e_direct-e_fourier)<1e-11,'Poisson/Parseval identity')
    angles=np.linspace(0,2*pi,16384,endpoint=False)
    P=np.sum((1-abs(z[:,None])**2)/abs(np.exp(1j*angles)[None,:]-z[:,None])**2,axis=0)
    variance=np.mean((P-len(z))**2)
    assert_ok(abs(variance-2*e_fourier)<1e-10,'Poisson boundary variance')

# Leading small-centroid law checked via exact polynomial roots, without
# confusing finite computations with the asymptotic proof.
for n in range(2,7):
    for sval in [0.06,0.11]:
        es=[float(sval**j/factorial(j)) for j in range(n+1)]
        polynomial=[(-1)**j*es[j] for j in range(n+1)]
        roots=np.roots(polynomial)
        powers=np.array([np.sum(roots**k) for k in range(1,90)])
        expected=sval**2+sval**(2*n+2)/factorial(n)**2
        err=np.sum(abs(powers)**2)-expected
        assert_ok(abs(err)<100*sval**(2*n+4),'truncated-exponential test')

# Compare optimized and centered-at-origin sampling on a few nondegenerate cases.
def energy_for_power_sums(n,sval,vars):
    S=[None,complex(sval)]+[complex(vars[2*j],vars[2*j+1]) for j in range(n-1)]
    e=[1]
    for j in range(1,n+1):
        e.append(sum((-1)**(k-1)*e[j-k]*S[k] for k in range(1,j+1))/j)
    roots=np.roots([(-1)**j*e[j] for j in range(n+1)])
    if max(abs(roots))>=1: return 1e5+np.max(abs(roots))**2
    A=roots[:,None]*roots[None,:].conj()
    return float(np.real(np.sum(A/(1-A))))

for n,sval in [(2,.12),(2,.2),(3,.18),(3,.24),(4,.32)]:
    init=np.zeros(2*(n-1))
    initial=energy_for_power_sums(n,sval,init)
    opt=minimize(lambda u:energy_for_power_sums(n,sval,u),init,method='BFGS',options={'gtol':1e-11})
    assert_ok(opt.fun<=initial+1e-10,'optimized candidate improves or matches')
    assert_ok(opt.fun>=sval*sval-1e-11,'first Fourier energy lower bound')
    if n<=3:
        predicted=(-1)**n*(n+1)/(n*factorial(n))*sval**(n+2)
        got=complex(opt.x[2*(n-2)],opt.x[2*(n-2)+1]).real
        assert_ok(abs(got-predicted)<max(.08*abs(predicted),1e-5),'optimal last power-sum leading term')

print(f'PASS: {checks} finite symbolic and numerical checks')
