"""Independent symbolic and finite-domain checks of the reported logarithmic-trap hierarchy.
Only diagnostics: the proof in RESULT.md establishes the unbounded-domain theorem.
"""
from fractions import Fraction
import sympy as sp
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu

s,v,g=sp.symbols('s v g',positive=True)
sigma=sp.symbols('sigma',integer=True)
assertions=0

def check(expr):
    global assertions
    assert sp.simplify(expr)==0,expr
    assertions+=1

def generator(exprplus,exprminus):
    f=-1/s
    outplus=sp.expand((f+v)*sp.diff(exprplus,s)+g*(exprminus-exprplus))
    outminus=sp.expand((f-v)*sp.diff(exprminus,s)+g*(exprplus-exprminus))
    return outplus,outminus

for n in range(1,9):
    p=2*n
    c=sp.Rational(n)*v/g
    Vplus=s**p+c*s**(p-1)
    Vminus=s**p-c*s**(p-1)
    outp,outm=generator(Vplus,Vminus)
    leading=p*(sp.Rational(2*n-1)*v*v/(2*g)-1)*s**(p-2)
    extra=c*(p-1)*s**(p-3)
    check(outp-(leading-extra))
    check(outm-(leading+extra))

# Backward-equation linear algebra and integrating factor.
U,d,Up,dp,k,Uold,dold=sp.symbols('U d Up dp k Uold dold')
a=1/s
Eplus=(-a+v)*(Up+dp)-2*g*d+k*(Uold+dold)
Eminus=(-a-v)*(Up-dp)+2*g*d+k*(Uold-dold)
solution=sp.solve([Eplus,Eminus],[Up,dp],dict=True)[0]
expected_up=(2*g*v*d-k*v*dold-k*a*Uold)/(v*v-a*a)
expected_dp=2*g*s/(v*v*s*s-1)*d-k*(v*Uold+a*dold)/(v*v-a*a)
check(solution[Up]-expected_up)
check(solution[dp]-expected_dp)

beta=sp.symbols('beta',positive=True)
C=sp.Integer(1)
for n in range(1,8):
    prev=C
    C=sp.factor(prev*beta/(2*(beta-(2*n-1))))
    target=sp.factor(1/(2**n*sp.prod(1-sp.Integer(2*j-1)/beta for j in range(1,n+1))))
    check(C-target)
    diff=2*n*prev/(v*(beta-(2*n-1)))
    assert sp.simplify(diff-2*n*prev/(v*(beta-2*n+1)))==0
    assertions+=1

# Known n=1,2 coefficients recovered from the source MFPT and earlier second-moment bound.
D=sp.symbols('D')
check((1/(2*(1-1/beta))).subs(beta,1/D)-1/(2*(1-D)))
check((1/(4*(1-1/beta)*(1-3/beta))).subs(beta,1/D)-1/(4*(1-D)*(1-3*D)))
print('symbolic_assertions',assertions)

# Discretize the exact two-state velocity-jump generator by a monotone upwind scheme
# with absorption at both 0 and a remote artificial boundary R. This is not a proof.
vnum=.5; gnum=1.0; beta_num=2*gnum/(vnum*vnum)
R=1000.0; h=.025
N=round(R/h)
rows=[]; cols=[]; vals=[]
idx=lambda i,q: 2*(i-1)+q
for i in range(1,N):
    x=i*h
    for q,sg in enumerate((1,-1)):
        row=idx(i,q)
        drift=sg*vnum-1/(1+x)
        hop=abs(drift)/h
        dest=i+(1 if drift>0 else -1)
        rows.extend((row,row)); cols.extend((row,idx(i,1-q))); vals.extend((hop+gnum,-gnum))
        if 0<dest<N:
            rows.append(row); cols.append(idx(dest,q)); vals.append(-hop)
A=coo_matrix((vals,(rows,cols)),shape=(2*(N-1),2*(N-1))).tocsc()
lu=splu(A)
prev=np.ones(A.shape[0]); moments=[]
for n in range(1,4):
    prev=lu.solve(n*prev)
    moments.append(prev.copy())
C=Fraction(1,1)
for n in range(1,4):
    C=C/(2*(Fraction(1,1)-Fraction(2*n-1,8)))
    print(f'order_{n}_coefficient', str(C),'threshold_beta',2*n-1)
for x in (20,40,80):
    i=round(x/h)
    out=[]
    for n,m in enumerate(moments,1):
        p=m[idx(i,0)]; q=m[idx(i,1)]; mean=.5*(p+q)
        prod=1.
        for j in range(1,n+1):prod*=1-(2*j-1)/beta_num
        lead=1/(2**n*prod)
        prevlead=1. if n==1 else 1/(2**(n-1)*np.prod([1-(2*j-1)/beta_num for j in range(1,n)]))
        difflead=2*n*prevlead/(vnum*(beta_num-2*n+1))
        out.append({'n':n,'mean_over_leading':round(mean/(lead*x**(2*n)),5),
          'orientation_difference_over_leading':round((p-q)/(difflead*x**(2*n-1)),5)})
    print('finite_domain_diagnostic',x,out)
