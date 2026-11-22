"""Reproduce exact determinant, optimizer, and independent matrix checks.

Requires Python 3, sympy, numpy. All formulas use ħ=1 and single-qubit time units.
"""
import numpy as np
import sympy as sp

r,g,w=sp.symbols('r g w', positive=True, real=True)
A=g*g+w*w
h=(r+g)**2+w*w
v=sp.Matrix([r*(r+g)/h,r*w/h])
M=1-v.dot(v)
H=sp.zeros(2)
for i,p in enumerate((g,w)):
    for j,q in enumerate((g,w)):
        vi=v.diff(p);vj=v.diff(q)
        H[i,j]=sp.factor(vi.dot(vj)+v.dot(vi)*v.dot(vj)/M)
Qdet=r**4/((g*g+2*g*r+w*w)*h**3)
assert sp.factor(H.det()-Qdet)==0
P=2*A**2+4*g*A*r-A*r*r-3*g*r**3
assert sp.factor(sp.diff(Qdet,r)-2*r**3*P/((g*g+2*g*r+w*w)**2*h**4))==0
assert sp.simplify(P.subs(r,sp.sqrt(A))- (A**2+g*A**sp.Rational(3,2)))==0
assert sp.simplify(P.subs(r,sp.sqrt(2*A))+2*sp.sqrt(2)*g*A**sp.Rational(3,2))==0

# Independent two-level SLD computation in the eigenbasis of rho.
def state(g,w,r):
    b=r/(r+g+1j*w)
    return np.array([[1,b],[np.conj(b),1]],dtype=complex)/2

def independent_quantum_fisher(g,w,r):
    rho=state(g,w,r)
    eig,vec=np.linalg.eigh(rho)
    deriv=[]
    for i,value in enumerate((g,w)):
        step=2e-6*max(1.,abs(value))
        if i==0: d=(state(g+step,w,r)-state(g-step,w,r))/(2*step)
        else: d=(state(g,w+step,r)-state(g,w-step,r))/(2*step)
        deriv.append(vec.conj().T@d@vec)
    ans=np.zeros((2,2))
    for i in range(2):
        for j in range(2):
            for a in range(2):
                for b in range(2):
                    ans[i,j]+=np.real(2*deriv[i][a,b]*deriv[j][b,a]/(eig[a]+eig[b]))
    return ans

qnum=sp.lambdify((g,w,r),H,'numpy')
n=0
for gg in (.25,1.,2.,5.):
    for ww in (-7.,-1.3,0.,.5,4.):
        for rr in (.3,1.,3.):
            actual=independent_quantum_fisher(gg,ww,rr)
            expected=np.array(qnum(gg,ww,rr),dtype=float)
            assert np.allclose(actual,expected,rtol=2e-7,atol=2e-9),(gg,ww,rr,actual,expected)
            assert np.allclose(np.linalg.det(actual),float(Qdet.subs({g:gg,w:ww,r:rr})),rtol=2e-7,atol=2e-9)
            n+=1
for gg in (.25,1.,3.):
    for ww in (0.,.25,2.,15.):
        aa=gg*gg+ww*ww
        lo,hi=np.sqrt(aa),np.sqrt(2*aa)
        for _ in range(80):
            mid=(lo+hi)/2
            val=2*aa*aa+4*gg*aa*mid-aa*mid*mid-3*gg*mid**3
            if val>0: lo=mid
            else: hi=mid
        root=(lo+hi)/2
        assert np.sqrt(aa)<root<np.sqrt(2*aa)
        assert abs(2*aa*aa+4*gg*aa*root-aa*root*root-3*gg*root**3)<1e-7*aa*aa
        n+=1
print('PASS: exact symbolic identity, sharp bounds and',n,'independent numerical parameter cases')
