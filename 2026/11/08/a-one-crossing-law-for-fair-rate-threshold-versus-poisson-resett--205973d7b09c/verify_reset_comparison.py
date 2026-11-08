import numpy as np
from scipy.integrate import solve_bvp, quad
from scipy.optimize import brentq

def check(name, w, a):
    r=1/quad(lambda x: (a-x)*w(x), 0, a, epsabs=1e-12)[0]
    L=max(12.0,8.0*a)
    xs=np.linspace(0,L,700)
    # solve h''=r w(x) h, h'(0)=-r/2, h(L)=0
    def ode(x,y):
        return np.vstack([y[1],r*np.array([w(z) for z in x])*y[0]])
    def bc(ya,yb): return np.array([ya[1]+r/2,yb[0]])
    initial=np.vstack([r*a/2*np.exp(-xs),-r*a/2*np.exp(-xs)])
    sol=solve_bvp(ode,bc,xs,initial,tol=2e-8,max_nodes=25000)
    assert sol.status==0,(name,sol.message)
    h=lambda x: sol.sol(np.asarray(x))[0]
    crossing=brentq(lambda x:h(x)-r/2*(a-x),0,a)
    normp=2*quad(lambda x:w(x)*float(h(x)),0,L)[0]
    assert abs(normp-1)<1e-6,(name,normp)
    assert h(0) < r*a/2 and float(h(a))>0
    tails=[]
    for t in np.linspace(.01*a, 2*a,90):
        tailt=2*quad(lambda x:w(x)*(r/2)*(a-x),min(t,a),a)[0] if t<a else 0.
        tailp=2*quad(lambda x:w(x)*float(h(x)),t,L,epsabs=1e-8)[0]
        assert tailp>tailt,(name,t,tailp,tailt)
        tails.append(tailp-tailt)
    print(name,'r',r,'cross',crossing,'mass',normp,'min tail diff',min(tails))
for name,fn in [('Brownian',lambda x:1.),('quadratic speed',lambda x:1+x*x),('affine-square speed',lambda x:.5+2*x*x),('sluggish alpha1',lambda x:x),('sluggish alpha3',lambda x:x**3)]:
    check(name,fn,1.)
