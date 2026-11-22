"""Reproduce exact covariance identity and independently discretized Markov checks.
Python >=3.10; requires sympy, mpmath, numpy, scipy.
"""
import math
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import splu

# Formal Laurent-polynomial/exponential verification: x=e^A,y=e^B, with
# differentiation in the Laplace parameter represented by (A*x*d_x+B*y*d_y)/2.
x, y, A, B = sp.symbols('x y A B', positive=True)
f_plus=(x-1/x)/(x*y-1/(x*y))
f_minus=(y-1/y)/(x*y-1/(x*y))
u=sp.factor(f_plus+f_minus)
deriv=lambda f: (A*x*sp.diff(f,x)+B*y*sp.diff(f,y))/2
v=deriv(u); g_plus=deriv(f_plus); g_minus=deriv(f_minus)
T2=2*(1-u+v)/u**2
Tplus=(f_plus*(v+1)-u*(f_plus+g_plus))/u**2
Tminus=(f_minus*(v+1)-u*(f_minus+g_minus))/u**2
cross=T2+Tplus*(x-1/y)+Tminus*(y-1/x)
meanprod=(x-1)*(y-1)
target=-(A+B)*(x*x-1)*(y*y-1)/(2*(x+y)*(x*y-1))
assert sp.cancel(cross-meanprod-target)==0
assert sp.cancel(target+(A+B)*(x-1/x)*(y-1/y)/(2*(x-1/x+y-1/y)))==0
print('PASS symbolic mixed moment / negative covariance identity')
a0,b0,t=sp.symbols('a0 b0 t',positive=True)
A0=a0*t; B0=b0*t
F=(sp.exp(A0)-1)*(sp.exp(B0)-1)-(A0+B0)*sp.sinh(A0)*sp.sinh(B0)/(sp.sinh(A0)+sp.sinh(B0))
assert sp.simplify(sp.limit(F/t**3,t,0)-a0*b0*(a0+b0)/2)==0
print('PASS exact weak-reset cancellation and mixed-moment exponent')

mp.mp.dps=60

def transform(a,b,r,D,s,t):
    q=s+t; lam=lambda z:mp.sqrt((r+z)/D)
    l=lam(q)
    fp=mp.sinh(a*l)/mp.sinh((a+b)*l)
    fm=mp.sinh(b*l)/mp.sinh((a+b)*l)
    gplus=(r+q)*fp/(q+r*(fp+fm))
    gminus=(r+q)*fm/(q+r*(fp+fm))
    def later(dist0,distreset,z):
        l=lam(z)
        return (z*mp.exp(-dist0*l)+r*mp.exp(-distreset*l))/(z+r*mp.exp(-distreset*l))
    return gplus*later(a+b,a,t) + gminus*later(a+b,b,s)

for a,b,r,D in [(1,1,1,1),(.7,2.3,.9,1.2),(3,.5,4,2),(.2,.4,.03,1),(.8,1.9,12,2),(2.5,3.5,.2,.7)]:
    a,b,r,D=map(lambda v: mp.mpf(str(v)), (a,b,r,D))
    h=lambda s,t:transform(a,b,r,D,s,t)
    deriv_cross=mp.diff(h,(0,0),(1,1))
    means=(mp.exp(a*mp.sqrt(r/D))-1)*(mp.exp(b*mp.sqrt(r/D))-1)/r**2
    actual=deriv_cross-means
    X=mp.mpf(a)*mp.sqrt(r/D);Y=mp.mpf(b)*mp.sqrt(r/D)
    expected=-(X+Y)*mp.sinh(X)*mp.sinh(Y)/(mp.sinh(X)+mp.sinh(Y))/r**2
    assert mp.almosteq(actual,expected,rel_eps=mp.mpf('1e-45'),abs_eps=mp.mpf('1e-40')), (actual,expected)
print('PASS independent 60-digit joint-transform derivatives (6 parameter sets)')
for a,b,r,D in [(1,1,1,1),(.7,2.3,.9,1.2),(3,.5,4,2),(.2,.4,.03,1)]:
    a,b,r,D=map(lambda v:mp.mpf(str(v)), (a,b,r,D))
    def marginal(dist,s):
        f=mp.exp(-dist*mp.sqrt((r+s)/D))
        return (r+s)*f/(s+r*f)
    var_mpmath=mp.diff(lambda s:marginal(b,s),0,2)-mp.diff(lambda s:marginal(b,s),0)**2
    Bv=b*mp.sqrt(r/D)
    var_formula=(mp.exp(2*Bv)-Bv*mp.exp(Bv)-1)/r**2
    assert mp.almosteq(var_mpmath,var_formula, rel_eps=mp.mpf('1e-46'))
print('PASS independent 60-digit marginal-variance derivatives (4 parameter sets)')

# Independent lattice CTMC converging to the continuum expression. Solve
# only finite sparse generator systems; truncation is reflecting at +/-K.
def mean_reach_target(a,b,r,D,N,K,target_side):
    # targets left -a or right b, represented as integers on grid 1/N
    lo=-K*N;hi=K*N
    goal = -a*N if target_side=='left' else b*N
    states=[i for i in range(lo,hi+1) if i!=goal]
    idx={p:j for j,p in enumerate(states)}
    Q=lil_matrix((len(states),len(states)),dtype=float)
    hop=D*N*N
    for i in states:
        z=idx[i]
        for j in (i-1,i+1):
            if j<lo or j>hi:continue
            Q[z,z]-=hop
            if j!=goal:Q[z,idx[j]]+=hop
        if i!=0:
            Q[z,z]-=r
            if 0!=goal:Q[z,idx[0]]+=r
    lu=splu((-Q).tocsc())
    sol=lu.solve(np.ones(len(states)))
    return sol[idx[(b if target_side=='left' else -a)*N]]

def lattice_cov(a,b,r,D,N,K):
    states=list(range(-a*N+1,b*N))
    idx={p:j for j,p in enumerate(states)}
    Q=lil_matrix((len(states),len(states)),dtype=float)
    gp=np.zeros(len(states));gm=np.zeros(len(states))
    hop=D*N*N
    for i in states:
        z=idx[i]
        for j in (i-1,i+1):
            Q[z,z]-=hop
            if j==b*N:gp[z]+=hop
            elif j==-a*N:gm[z]+=hop
            else:Q[z,idx[j]]+=hop
        if i!=0:
            Q[z,z]-=r
            Q[z,idx[0]]+=r
    lu=splu((-Q).tocsc())
    ones=np.ones(len(states)); t1=lu.solve(ones)
    t2=2*lu.solve(t1)
    pplus=lu.solve(gp); pminus=lu.solve(gm)
    tplus=lu.solve(pplus); tminus=lu.solve(pminus)
    remain_left=mean_reach_target(a,b,r,D,N,K,'left')
    remain_right=mean_reach_target(a,b,r,D,N,K,'right')
    i=idx[0]
    mixed=t2[i]+tplus[i]*remain_left+tminus[i]*remain_right
    # independently compute both marginal means by the full generator
    # at the reset site (the return value is from the other boundary for above)
    def marginal_mean(target_side):
        goal=(-a if target_side=='left' else b)*N
        lo=-K*N;hi=K*N
        st=[j for j in range(lo,hi+1) if j!=goal]
        di={p:j for j,p in enumerate(st)}
        M=lil_matrix((len(st),len(st)),dtype=float)
        for k in st:
            z=di[k]
            for j in (k-1,k+1):
                if lo<=j<=hi:
                    M[z,z]-=hop
                    if j!=goal:M[z,di[j]]+=hop
            if k!=0:
                M[z,z]-=r;M[z,di[0]]+=r
        return splu((-M).tocsc()).solve(np.ones(len(st)))[di[0]]
    mm=marginal_mean('left')*marginal_mean('right')
    return mixed-mm

z=math.sqrt(.7)
expected=-(1+2)*z*math.sinh(z)*math.sinh(2*z)/(math.sinh(z)+math.sinh(2*z))/.7**2
for N in (8,16,32):
    val=lattice_cov(1,2,.7,1.,N,10)
    err=abs(val-expected)
    print('Lattice N=',N,'Cov=',round(val,10),'continuum=',round(expected,10),'error=',round(err,10))
    assert err < 0.06, (N,val,expected)
print('PASS 3 independent lattice-generator comparisons; all checks passed')
