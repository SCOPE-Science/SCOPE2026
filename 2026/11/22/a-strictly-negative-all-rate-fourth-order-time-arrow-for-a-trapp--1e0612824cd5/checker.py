"""Independent algebraic and finite-dimensional semigroup checks for the stationary
telegraph-driven harmonic position time arrow. Public scientific verification.
Run: python checker.py (requires sympy, numpy, scipy).
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

k, g, v, d, z = sp.symbols('k g v d z', positive=True)
c1 = v/(k+2*g)
m2 = (v*c1+d)/k
c3 = (3*v*m2+6*d*c1)/(3*k+2*g)
m4 = (v*c3+3*d*m2)/k
M = sp.zeros(4)
M[0, 0] = -2*g
M[1, 0] = v; M[1, 1] = -k
M[2, 0] = 2*d; M[2, 1] = 2*v; M[2, 2] = -(2*k+2*g)
M[3, 1] = 6*d; M[3, 2] = 3*v; M[3, 3] = -3*k
init = sp.Matrix([c1,m2,c3,m4])
first = (m4 + v*c3/(z+2*g))/(z+k)
second = ((z*sp.eye(4)-M).inv()*init)[3]
assert sp.cancel(first-second + 24*g*v**4/((2*g+k)*(2*g+3*k)*(z+2*g)*(z+k)*(z+3*k)*(z+2*g+2*k))) == 0
for n in (0,1,2):
    a_n = (-k)**n*m4 + v*c3*sum((-k)**(n-1-j)*(-2*g)**j for j in range(n))
    assert sp.factor(a_n-(M**n*init)[3]) == 0
n=3
a_n = (-k)**n*m4 + v*c3*sum((-k)**(n-1-j)*(-2*g)**j for j in range(n))
assert sp.factor(a_n-(M**n*init)[3]+24*g*v**4/((2*g+k)*(2*g+3*k))) == 0

checks=4
for K,G,V,D in [(1.,0.2,1.3,0.),(1.,1.,2.,0.5),(1.,0.5,0.7,4.),(1.,1.5,1.4,2.),(0.8,1.2,2.,0.),(3.,0.5,1.,1.1)]:
    c1v=V/(K+2*G);m2v=(V*c1v+D)/K
    c3v=(3*V*m2v+6*D*c1v)/(3*K+2*G);m4v=(V*c3v+3*D*m2v)/K
    mat=np.zeros((6,6))
    mat[0,0]=-2*G
    mat[1,0]=V;mat[1,1]=-K
    mat[2,0]=2*D;mat[2,1]=2*V;mat[2,2]=-(2*K+2*G)
    mat[3,1]=6*D;mat[3,2]=3*V;mat[3,3]=-3*K
    mat[4,5]=V;mat[4,4]=-K;mat[5,5]=-2*G
    initial=np.array([c1v,m2v,c3v,m4v,m4v,c3v])
    # Independent four-stage positive impulse-response cascade.
    cas=np.zeros((4,4));rates=[2*G,K,3*K,2*G+2*K]
    for i,rate in enumerate(rates):
        cas[i,i]=-rate
        if i:cas[i,i-1]=1.
    cas_input=np.array([1.,0.,0.,0.]); rate_const=24*G*V**4/((2*G+K)*(2*G+3*K))
    for t in (0.01,0.1,0.5,1.,2.,4.,8.,12.):
        full=expm(mat*t).dot(initial)
        arrow=full[4]-full[3]
        # Fourth stage of the positive impulse-response cascade.
        cascade=expm(cas*t).dot(cas_input)[3]
        predicted=-rate_const*cascade
        assert abs(arrow-predicted)<2e-9*(1+abs(predicted)),(K,G,V,D,t,arrow,predicted)
        assert arrow<0 and cascade>0
        checks+=2
print(f'PASS {checks} independent symbolic/semigroup checks')
