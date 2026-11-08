"""Independent exact finite checks for the parabolic polynomial-intensity theorem.

Usage: python3 verify.py; requires sympy.  Finite tests support but never
replace the general interpolation and rational-periodicity proof.
"""
import sympy as S
T=S.symbols('T', real=True)
I=S.I

def polynomial_intensity(a):
    z=T+I*T**2
    p=sum(c*z**k for k,c in enumerate(a))
    return S.Poly(S.expand(p*S.conjugate(p)),T)

checks=0
for d in range(1,5):
    N=4*d
    a=[S.Integer((3*k+d)%7-3)+I*S.Integer((2*k+1)%5-2) for k in range(d+1)]
    f=polynomial_intensity(a)
    assert f.degree() <= N
    assert f.coeff_monomial(T**(N-1)) == 0
    checks+=2
    nodes=list(range(1,N+1))
    degrees=list(range(N-1))+[N]
    V=S.Matrix([[S.Integer(t)**k for k in degrees] for t in nodes])
    assert V.det(method='domain-ge') == sum(nodes)*S.prod(nodes[j]-nodes[i] for i in range(N) for j in range(i+1,N))
    checks+=1
    y=S.Matrix([f.eval(t) for t in nodes])
    co=V.inv()*y
    assert all(S.simplify(co[k]-f.coeff_monomial(T**deg))==0 for k,deg in enumerate(degrees))
    checks+=1

# The nonzero-sum condition cannot simply be dropped at d=1.
nodes=[-3,-1,1,3]
Q=S.Matrix([[9,11*I/S.Integer(2)],[-11*I/S.Integer(2),1]])
assert Q.det()<0
z=T+I*T**2
v=S.Matrix([1,z])
f=S.simplify((v.conjugate().T*Q*v)[0])
assert S.expand(f-(T**2-1)*(T**2-9))==0
assert all(f.subs(T,t)==0 for t in nodes)
checks+=6
print('PARABOLIC_PHASE_RETRIEVAL_EXACT_CHECKS_PASS',checks)
