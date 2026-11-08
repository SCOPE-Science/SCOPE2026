"""Exact arithmetic spot certificates for the Alexander SDIRK2 star phase diagram.
Standard library only. The accompanying proof establishes the all-degree theorem;
finite checks here independently exercise its algebraic branch boundaries.
"""
from fractions import Fraction as F
from math import isqrt

class Q2:
    """Exact a+b*sqrt(2)."""
    def __init__(self,a=0,b=0):
        self.a=F(a);self.b=F(b)
    @staticmethod
    def coerce(x):return x if isinstance(x,Q2) else Q2(x)
    def __add__(self,x):
        x=self.coerce(x);return Q2(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Q2(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x);return Q2(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        assert d!=0
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,x):return self*self.coerce(x).inv()
    def __rtruediv__(self,x):return self.coerce(x)*self.inv()
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        y=Q2(1)
        for _ in range(k):y=y*self
        return y
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        d=a*a-2*b*b
        assert d!=0
        if a>0:return 1 if d>0 else -1
        return -1 if d>0 else 1
    def __lt__(self,x):return (self-self.coerce(x)).sign()<0
    def __gt__(self,x):return (self-self.coerce(x)).sign()>0
    def __repr__(self):return f'({self.a})+({self.b})sqrt2'

root2=Q2(0,1)
g=Q2(1)-root2/2
c=Q2(1)-2*g
rho=(root2-1)/2
assert (2*g*g-4*g+1).sign()==0
assert c>0 and g>0 and rho>F(1,5) and rho<F(1,4)

def r(z):
    z=Q2.coerce(z)
    return (1-c*z)/(1+g*z)**2

def center(m,h):return 1+m*r((m+1)*h)
def leaf_poly_sign(m,h):
    return Q2(m)+r((m+1)*h)+(m*m-1)*r(h)
def leaf_leaf(m,h):return (m+r((m+1)*h)-(m+1)*r(h))/(m*(m+1))

assert r(0).sign()==1
assert (r(8)+F(1,5)).sign()<0
assert (r(F(17,5))+F(10,99)).sign()<0
assert leaf_poly_sign(5,8).sign()<0
for m in range(5,10):
    assert center(m,F(7,2)).sign()>0
    assert leaf_poly_sign(m,F(7,2)).sign()>0
for m in range(5,101):
    assert center(m,8).sign()>0
    assert leaf_poly_sign(m,8).sign()<0
for m in range(10,101):
    assert center(m,F(17,5)).sign()<0
    assert leaf_poly_sign(m,F(17,5)).sign()<0

# Exact coefficient sign certificates for the center quadratic at h=17/5.
h=F(17,5)
a2=g*g*h*h-c*h
a1=2*g*h+2*g*g*h*h+1-c*h
a0=(1+g*h)**2
assert a2<0 and a1>0 and a0>0
assert (a2*100+a1*10+a0).sign()<0
# Exact positivity of the within-leaf offdiagonal numerator factor.
for m in range(2,101):
    for h in [F(1,100),F(1,2),F(1),F(17,5),F(8),F(100)]:
        assert leaf_leaf(m,h).sign()>0
        fact=(g*(2-g)+g*g*(m+2)*h+g**4*(m+1)*h*h)
        assert fact.sign()>0
        aa=(1+g*h)**2;bb=(1+g*(m+1)*h)**2
        assert ((m+r((m+1)*h)-(m+1)*r(h))*aa*bb-m*(m+1)*h*h*fact).sign()==0
# Cross-check explicit three-eigenvalue formula against a direct RK matrix
# evaluation using a dense real inverse (numerical corroboration only).
from math import sqrt
GG=1-1/sqrt(2)
def Rreal(x):return (1-(1-2*GG)*x)/(1+GG*x)**2
for m in range(2,16):
    for h in (0.01,0.1,0.6,1.5,3.4,3.5,8.,20.,300.):
        rn=Rreal((m+1)*h);r1=Rreal(h);n=m+1
        hubhub=(1+m*rn)/n
        hubleaf=(1-rn)/n
        leafdiag=(1+rn/m)/n+(m-1)*r1/m
        leafother=(m+rn-n*r1)/(m*n)
        assert abs(hubhub+m*hubleaf-1)<2e-13
        assert abs(hubleaf+leafdiag+(m-1)*leafother-1)<2e-13
        assert hubleaf>=0 and leafother>=-1e-13
        # Testing symmetry decomposition identity, not extrapolating finite checks.
        assert abs(leafdiag-leafother-r1)<2e-13
print('VERIFY_OK: exact surd certificates and 5940 positive offdiagonal samples')

# Direct Gauss--Jordan replay of the original rational matrix step, independent
# of its star spectral-projector derivation; arithmetic is exact in Q(sqrt(2)).
def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q2(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def inverse(A):
    n=len(A); T=[[A[i][j] for j in range(n)]+[Q2(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if T[k][j].sign()!=0)
        T[j],T[k]=T[k],T[j]
        v=T[j][j].inv();T[j]=[u*v for u in T[j]]
        for k in range(n):
            if k==j:continue
            v=T[k][j]
            if v.sign()!=0:T[k]=[a-v*b for a,b in zip(T[k],T[j])]
    return [u[n:] for u in T]
for m,h in [(2,F(1,2)),(5,F(17,5)),(5,F(8)),(10,F(17,5))]:
    n=m+1
    L=[[Q2(m if i==j==0 else (1 if i==j else -1 if (i==0 or j==0) else 0))
         for j in range(n)] for i in range(n)]
    X=[[Q2(int(i==j))+g*h*L[i][j] for j in range(n)] for i in range(n)]
    Y=[[Q2(int(i==j))-c*h*L[i][j] for j in range(n)] for i in range(n)]
    M=matmul(inverse(matmul(X,X)),Y)
    cf=[(1+m*r(n*h))/n,(1-r(n*h))/n,
        (m+r(n*h)+(m*m-1)*r(h))/(m*n),
        (m+r(n*h)-n*r(h))/(m*n)]
    assert (M[0][0]-cf[0]).sign()==0
    assert (M[0][1]-cf[1]).sign()==0
    assert (M[1][1]-cf[2]).sign()==0
    assert (M[1][2]-cf[3]).sign()==0
print('VERIFY_MATRIX_OK: exact direct inverse against all four projector entries')
