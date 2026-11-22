"""Reproduce critical cubic and numerical checks for a three-player Gaussian resource-allocation game.

Requires Python 3, sympy, numpy, scipy. Analytical proof is provided separately.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp


def symbolic_cubic():
    a, b, t = sp.symbols('a b t', real=True)
    z = 2 * sp.cosh(t*a*b) + sp.exp(t*a*a/2)
    g = sp.exp(t*a*b) / z
    f = t*(b-a)*g*(1-g)
    series = sp.series(f,a,0,4).removeO().expand()
    assert sp.simplify(series.coeff(a,0)-2*b*t/9)==0
    assert sp.simplify(series.coeff(a,1)-t*(b*b*t-2)/9)==0
    assert sp.simplify(series.coeff(a,2)+b*t*t*(5*b*b*t+7)/54)==0
    assert sp.simplify(series.coeff(a,3)+t*t*(3*b**4*t*t-6*b*b*t-1)/54)==0
    v, mu4 = sp.symbols('v mu4', positive=True)
    c = -t*t*(3*mu4*t*t-6*v*t-1)/54
    ccrit = sp.factor(c.subs(t,2/v))
    assert sp.simplify(ccrit - sp.Rational(2,27)*(13*v*v-12*mu4)/v**4)==0
    print('EXACT symbolic third-order coefficient:',ccrit)


def field(x, nodes, probs, v=1):
    x=np.asarray(x,float)
    sigma2=v/2
    y=np.zeros(3)
    for b,p in zip(nodes,probs):
        z=np.exp(-(x-b)**2/(2*sigma2))
        G=z/z.sum()
        y+=p*G*(1-G)*(b-x)/sigma2
    return y


def test_example(name,nodes,probs,kappa):
    assert abs(sum(probs)-1)<1e-14
    assert abs(sum(w*b for w,b in zip(probs,nodes)))<1e-14
    assert abs(sum(w*b*b for w,b in zip(probs,nodes))-1)<1e-14
    assert abs(sum(w*b**4 for w,b in zip(probs,nodes))-kappa)<1e-14
    alpha=(13-12*kappa)/27
    for z in [(1,-1,0),(1,2,-3),(4,-1,-3)]:
        z=np.array(z,dtype=float)
        x=z*1e-3
        f=field(x,nodes,probs)
        proj=f-f.mean()
        target=alpha*np.dot(x,x)*x
        assert np.linalg.norm(proj-target) < 8e-5*np.linalg.norm(target), (name,z,proj,target)
        assert np.max(np.abs(field(-x,nodes,probs)+f))<1e-13
    sol=solve_ivp(lambda t,x:field(x,nodes,probs),(0,10000),[0.1,-0.1,0],
                  atol=1e-12,rtol=2e-10,dense_output=True,max_step=20)
    assert sol.success
    q0=sol.sol(0)[0];q100=sol.sol(100)[0];q10000=sol.sol(10000)[0]
    if kappa==1:
        assert q100>q0 and q10000>q100
    else:
        assert 0<q10000<q100<q0
        target=math.sqrt(27/(4*(12*kappa-13)))
        # On the invariant line, a(t) ~ sqrt(27/[4(12*kappa-13)t]).
        assert abs(math.sqrt(10000)*q10000/target-1)<0.02
    print(name,'cubic radial coefficient',alpha,'r(100)',q100,'r(10000)',q10000)

if __name__=='__main__':
    symbolic_cubic()
    test_example('two-point',[-1,1],[0.5,0.5],1)
    test_example('three-point',[-math.sqrt(3),0,math.sqrt(3)],[1/6,2/3,1/6],3)
    print('ALL CHECKS PASSED')
