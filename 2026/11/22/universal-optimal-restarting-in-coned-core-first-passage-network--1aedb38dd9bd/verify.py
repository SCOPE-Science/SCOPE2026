"""Exact graph-generator checks for resetting and absorption on coned-core paths.

Dependencies: Python 3.10+, SymPy.
"""
import sympy as sp

m,r,z=sp.symbols('m r z', positive=True)
mean=(m*r**2+4*m*r+2*m+r**3+5*r**2+6*r+3)/(m*r+r**2+r+1)
H=r**4+(2*m+2)*r**3+(m**2+2*m+2)*r**2+(4-2*m)*r+(3-m-2*m**2)
assert sp.factor(sp.diff(mean,r)-H/(m*r+r**2+r+1)**2)==0
assert sp.factor(mean.subs(r,0)-(2*m+3))==0
assert sp.simplify(sp.limit(mean,m,sp.oo)-(r+4+2/r))==0
assert sp.simplify(H.subs(r,sp.sqrt(2))-(m*(3+2*sp.sqrt(2))+11+8*sp.sqrt(2)))==0
# Exact first finite-size correction to the asymptotic optimum and optimized mean.
a=-1-sp.Rational(3,2)/sp.sqrt(2)
K=-2-sp.Rational(3,2)*sp.sqrt(2)
eps=sp.symbols('eps',positive=True)
Hr=sp.simplify((eps**2*H.subs({m:1/eps,r:sp.sqrt(2)+a*eps})).expand())
assert sp.simplify(Hr.subs(eps,0))==0
assert sp.simplify(sp.diff(Hr,eps).subs(eps,0))==0
Eeps=sp.cancel(mean.subs({m:1/eps,r:sp.sqrt(2)+a*eps}))
assert sp.simplify(Eeps.subs(eps,0)-(4+2*sp.sqrt(2)))==0
assert sp.simplify(sp.diff(Eeps,eps).subs(eps,0)-K)==0

# Each internal core is an arbitrary simple graph on m-1 vertices. The universal
# gateway connects all core vertices; a three-edge tail ends at the target.
def core_edges(k,typ):
    if typ=='empty': return set()
    if typ=='path': return {(i,i+1) for i in range(k-1)}
    if typ=='complete': return {(i,j) for i in range(k) for j in range(i+1,k)}
    if typ=='parity': return {(i,j) for i in range(k) for j in range(i+1,k) if (i*7+j*11)%3==1}
    raise ValueError(typ)

def graph_matrix(k,typ,rate,laplace):
    # core 0..k-1, gateway k, reset vertex k+1, other tail k+2,
    # absorbing target k+3. Only transient states enter the matrix.
    G,S,U=k,k+1,k+2
    size=k+3
    edges=set(core_edges(k,typ))|{(i,G) for i in range(k)}|{(G,S),(S,U)}
    Q=sp.zeros(size,size)
    for i,j in edges:
        Q[i,j]+=1;Q[j,i]+=1
    # target is connected only to U; its rate is part of the killed diagonal.
    Q[U,U]-=1
    # Internal graph movements and gateway/tail jumps all have rate 1.
    for i in range(size):
        Q[i,i]-=sum(Q[i,j] for j in range(size) if j!=i)
    # Add actual reset transitions to S at rate r. At S, self-resets are null.
    for i in range(size):
        if i!=S:
            Q[i,S]+=rate
            Q[i,i]-=rate
    L=laplace*sp.eye(size)-Q
    # For the mean, solve (-Q) t = 1. For Laplace transform use
    # (zI-Q) f = e_U: absorption from U at rate 1.
    b=sp.ones(size,1) if laplace==0 else sp.Matrix([1 if i==U else 0 for i in range(size)])
    t=L.inv()*b
    return sp.factor(t[S])

count=0
for n in range(3,9):
    for typ in ('empty','path','complete','parity'):
        for rate in (sp.Rational(0), sp.Rational(1,3), sp.Rational(3,2)):
            expected=sp.factor(mean.subs({m:n,r:rate}))
            got=graph_matrix(n-1,typ,rate,sp.Rational(0))
            assert got==expected,(n,typ,rate,got,expected)
            count+=1
# Verify an independent nonzero Laplace transform from full labelled generators
# agrees across all core topologies and with the four-class expression.
F=(m*r+m*z+r**2+2*r*z+r+z**2+z+1)/(m*r**2*z+2*m*r*z**2+4*m*r*z+m*r+m*z**3+4*m*z**2+3*m*z+r**3*z+3*r**2*z**2+5*r**2*z+r**2+3*r*z**3+10*r*z**2+8*r*z+r+z**4+5*z**3+7*z**2+4*z+1)
for n in (3,4,6):
    for typ in ('empty','path','complete','parity'):
        for rate in (sp.Rational(0),sp.Rational(2,5)):
            zval=sp.Rational(3,7)
            got=graph_matrix(n-1,typ,rate,zval)
            expected=sp.factor(F.subs({m:n,r:rate,z:zval}))
            assert got==expected,(n,typ,rate,got,expected)
            count+=1
print('GRAPH_GENERATOR_CERTIFICATE_PASSED',count,'exact rational checks; all symbolic identities passed')
