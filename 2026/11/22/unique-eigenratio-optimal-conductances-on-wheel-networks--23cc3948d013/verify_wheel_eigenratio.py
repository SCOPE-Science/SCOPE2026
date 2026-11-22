import math
import numpy as np
import sympy as s

def lap(m,a,b):
    W=np.zeros((m+1,m+1))
    for i in range(m):
        for u,v,w in ((0,i+1,a[i]),(i+1,1+(i+1)%m,b[i])):
            W[u,u]+=w; W[v,v]+=w; W[u,v]-=w; W[v,u]-=w
    return W

def ratio(m,L):
    v=np.linalg.eigvalsh(L)
    return float(v[-1]/v[1]) if v[1]>1e-10 else float('inf')

rng=np.random.default_rng(143612)
count=0
for m in range(3,45):
    S=4*math.sin(math.pi*(m//2)/m)**2
    mu=4*math.sin(math.pi/m)**2
    a=S/(m*(S+m));b=1/(S+m)
    L=lap(m,[a]*m,[b]*m)
    R=(m+1)/(1+m*mu/S)
    assert abs(ratio(m,L)-R)<2e-9,(m,R,ratio(m,L))
    assert abs(np.linalg.eigvalsh(L)[-1]-(m+1)*a)<1e-10
    assert abs(np.linalg.eigvalsh(L)[1]-(a+mu*b))<1e-10
    assert R < m+1
    count+=3
    for i in range(80):
        weights=rng.dirichlet(np.ones(2*m)*rng.uniform(.3,4))
        alt=ratio(m,lap(m,weights[:m],weights[m:]))
        assert alt+1e-8>=R,(m,i,R,alt)
        count+=1
    # vary ratio around winner for strict shape check
    for scale in (.0001,.01,.1,.5,.9999,1.0001,2,10,100,10000):
        r=scale*m/S
        x=1/(m*(1+r)); y=r*x
        alt=ratio(m,lap(m,[x]*m,[y]*m))
        assert alt>R-1e-8,(m,scale,alt,R)
        count+=1
# exact characteristic polynomial roots for m=4,6,8 with rational m=6 special S=4,mu=1
for m,ar,br in ((3,s.Rational(1,6),s.Rational(1,6)),(4,s.Rational(1,8),s.Rational(1,8)),(6,s.Rational(1,15),s.Rational(1,10)),(8,s.Rational(1,16),s.Rational(1,16))):
    M=s.zeros(m+1)
    for i in range(m):
        for u,v,w in ((0,i+1,ar),(i+1,1+(i+1)%m,br)):
            M[u,u]+=w; M[v,v]+=w; M[u,v]-=w; M[v,u]-=w
    z=s.symbols('z')
    char=s.factor(M.charpoly(z).as_expr())
    # exactly check characteristic expression by cos formulas
    expected=z*(z-(m+1)*ar)
    for k in range(1,m):expected*=z-ar-2*br*(1-s.cos(2*s.pi*k/m))
    assert s.simplify(s.expand(char-expected))==0,(m,char)
    count+=1
print('VERIFY_OK',count,'spectral, minimax, nonsymmetric, exact polynomial comparisons')
for m in (6,7,12,100,1000):
 S=4*math.sin(math.pi*(m//2)/m)**2
 mu=4*math.sin(math.pi/m)**2
 print('m',m,'r',m/S,'R*',(m+1)/(1+m*mu/S),'rim_budget',m/(m+S),'gap_fraction',(S+m*mu)/(S+m))
