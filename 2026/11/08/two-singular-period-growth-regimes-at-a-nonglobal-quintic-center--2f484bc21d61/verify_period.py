"""Independent algebraic and illustrative numerical checks for the local quintic center."""
import math
import warnings
import sympy as s
from scipy.integrate import quad, IntegrationWarning
warnings.simplefilter('ignore', IntegrationWarning)
x,v,k,b=s.symbols('x v k b',real=True)
p=s.exp(-k*x**4/4)
Vprime=s.exp(-k*x**4/2)*x*(1+b*x**4)
Hprime=s.expand(s.diff(p*p*v*v/2,x)*v + p*p*v*(-x+k*x**3*v*v-b*x**5)+Vprime*v)
assert s.simplify(Hprime)==0
assert s.simplify(s.diff(p,x)/p+k*x**3)==0
z=s.symbols('z',real=True)
# Time-preserving coordinate z = x-k*x**5/20 + O(x**9).
gamma=s.simplify((b-k/s.Integer(4))+k/s.Integer(20))
assert gamma==b-k/s.Integer(5)
assert s.simplify(-5*gamma/16-(k-5*b)/16)==0
# Inverse of w=k*(u**4-x**4)/2: 2*u*(1+b*u**4)du=(u**(-2)+b*u**2)dw/k.
u,w=s.symbols('u w',positive=True)
assert s.simplify(2*u*(1+b*u**4)/(2*k*u**3)-(u**-2+b*u**2)/k)==0

def period(A,kap,beta):
    def outer(t):
        X=A*(1-t*t)
        h=kap*(A**4-X**4)/2
        if h<=0: return 0.0
        def term(w):
            root=math.sqrt(X**4+2*w/kap)
            return math.exp(-w)*(1/root+beta*root)/kap
        S=quad(term,0,min(h,55),epsabs=1e-10,epsrel=1e-9,limit=180)[0]
        return 2*A*t/math.sqrt(S)
    return 4*quad(outer,0,1,epsrel=2e-8,limit=180)[0]
checks=[]
for kap,beta,A,expected in [(1,0,1,6.67317303189),(1,0,8,130.794981249),(1,2,1,4.59700937028),(1,2,8,7.65421080035)]:
    got=period(A,kap,beta)
    assert abs(got-expected)<0.0005,(A,beta,got)
    checks.append((kap,beta,A,round(got,8)))
assert checks[1][3] > 100 and checks[2][3] < 2*math.pi < checks[3][3]
print('CHECK_OK',len(checks)+5,'checks',checks)
