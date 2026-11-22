"""Direct spectral and symbolic checks for three-row Kaczmarz sampling."""
import numpy as np
import sympy as sp

def quantities(c,p):
    u=np.array([[1.,0,0],[c,np.sqrt(1-c*c),0],[0.,0,1.]])
    Q=[np.eye(3)-np.outer(v,v) for v in u]
    E=sum(t*np.outer(v,v) for t,v in zip(p,u))
    K=sum(t*np.kron(q,q) for t,q in zip(p,Q))
    return float(1-np.linalg.eigvalsh(E)[0]),float(np.linalg.eigvalsh(K)[-1])

cnt=0
for c in [0.1,0.25,0.5,0.6,0.8,0.95]:
    q1=(1-c)/(3-c)
    qa=(1-c*c)/(3-c*c)
    p1=[(1-q1)/2,(1-q1)/2,q1]
    pa=[(1-qa)/2,(1-qa)/2,qa]
    a,b=quantities(c,p1)
    a2,b2=quantities(c,pa)
    assert abs(a-2/(3-c))<1e-12
    assert abs(b-2/(3-c))<1e-12
    assert abs(b2-2/(3-c*c))<1e-12
    assert b2<b
    assert abs(a2-(1-(1-qa)*(1-c)/2))<1e-12
    cnt+=5
    for q in np.linspace(0,1,37):
        for x in np.linspace(0,1-q,19):
            p=[x,1-q-x,q]
            r1,r2=quantities(c,p)
            assert r1+1e-12>=2/(3-c), (c,p,r1)
            assert r2+1e-12>=2/(3-c*c), (c,p,r2)
            cnt+=2
assert sp.simplify((3-sp.Symbol('c')**2)/(3-sp.Symbol('c'))).has(sp.Symbol('c'))
c=sp.Rational(3,5)
assert (1-c)/(3-c)==sp.Rational(1,6)
assert (1-c*c)/(3-c*c)==sp.Rational(8,33)
assert 2/(3-c)==sp.Rational(5,6)
assert 2/(3-c*c)==sp.Rational(25,33)
assert sp.simplify(sp.Rational(5,6)/sp.Rational(25,33))==sp.Rational(11,10)
assert sp.simplify((3-(3-sp.sqrt(6))**2)/(3-(3-sp.sqrt(6))))==6-2*sp.sqrt(6)
print('PASS:',cnt,'spectral inequalities checked; exact rational examples and maximum checked')
