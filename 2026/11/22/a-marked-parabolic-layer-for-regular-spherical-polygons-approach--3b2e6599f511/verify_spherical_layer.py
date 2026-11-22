"""Numerical cross-checks for the near-hemispherical geodesic-polygon layer theorem.
Install numpy and scipy; run: python3 verify_spherical_layer.py.
Finite samples and quadratures corroborate, but do not prove, the asymptotic result.
"""
import math
import numpy as np
from scipy.integrate import quad


def geom(n, eps):
    a = math.pi / n
    R = math.pi / 2 - eps
    rho = math.atan(math.tan(R) * math.cos(a))
    return a, R, rho


def edge_radius(a, R, phi):
    return np.arctan(math.tan(R) * math.cos(a) / np.cos(phi))


def layer_area_independent(n, eps):
    a, R, rho = geom(n, eps)
    return n * quad(lambda t: math.cos(rho)-math.cos(edge_radius(a, R, t)),
                    -a, a, epsabs=1e-12, epsrel=1e-12)[0]


def layer_area_exact(n, eps):
    a, R, rho = geom(n, eps)
    A = 2*n*(a-math.asin(math.sin(a)*math.cos(rho)))
    return A-2*math.pi*(1-math.cos(rho)), A


def fixed_limit_mark(n):
    a = math.pi/n
    C = (a-math.sin(a))/math.cos(a)
    return a, C


def sample_layer(n, eps, count=100000, seed=137):
    # Generate exact area-uniform points in the outer layer by a one-dimensional
    # angular rejection and an independent area quantile in the radial direction.
    a, R, rho = geom(n,eps)
    rg = np.random.default_rng(seed+n)
    cmath = math.cos(rho)
    lmax=cmath-math.cos(R)
    collected=[]
    while sum(len(z) for z in collected)<count:
        phi=rg.uniform(-a,a,size=300000)
        rmax=edge_radius(a,R,phi)
        w=cmath-np.cos(rmax)
        accepted=phi[rg.random(len(phi))*lmax<=w]
        collected.append(accepted)
    phi=np.concatenate(collected)[:count]
    rmax=edge_radius(a,R,phi)
    # area element sin(r)dr; cosine is uniform between the two radial boundaries
    cosr=cmath-rg.random(count)*(cmath-np.cos(rmax))
    r=np.arccos(cosr)
    x=(math.pi/2-r)/eps
    u=phi/a
    y=(x-1)/(1/math.cos(a)-1)
    assert np.all((x>=1-1e-9)&(x<=1/math.cos(a)+1e-8))
    assert np.all((y>=-1e-8)&(y<=1+1e-8))
    return phi,x,u,y


def finite_cdf(n,eps,x):
    a,R,rho=geom(n,eps)
    r=math.pi/2-eps*x
    if r<=rho:return 1.
    if r>=R:return 0.
    theta=math.acos(math.tan(rho)/math.tan(r))
    A=2*n*(a-math.asin(math.sin(a)*math.cos(rho)))
    Ar=2*n*(a*(1-math.cos(r))+theta*math.cos(r)-math.asin(math.sin(theta)*math.cos(rho)))
    L=A-2*math.pi*(1-math.cos(rho))
    return (A-Ar)/L


def limiting_cdf(n,x):
    a,C=fixed_limit_mark(n)
    if x<=1:return 0.
    if x>=1/math.cos(a):return 1.
    # Integrate density (a-arccos(x cos(a)))/C, independent of the finite sphere
    return quad(lambda t:(a-math.acos(t*math.cos(a)))/C,
                1,x,epsabs=1e-10,epsrel=1e-10)[0]


def run():
    exact_checks=0;limit_checks=0; sample_checks=0
    for n in (3,4,5,8,15):
        a,C=fixed_limit_mark(n)
        assert C>0
        for eps in (.0009,.003,.01,.03):
            L,A=layer_area_exact(n,eps)
            Li=layer_area_independent(n,eps)
            assert abs(L-Li)<2e-11,(n,eps,L,Li)
            coeff=n*C/math.pi
            assert abs((L/A)/eps/coeff-1)<.08,(n,eps,L/A,coeff)
            exact_checks+=2
            for t in (.17,.42,.68,.89):
                x=1+t*(1/math.cos(a)-1)
                obs=finite_cdf(n,eps,x)
                target=limiting_cdf(n,x)
                assert abs(obs-target)<.018, (n,eps,x,obs,target)
                limit_checks+=1
        phi,x,u,y=sample_layer(n,.0018,count=100000)
        # Compare histogram bins in angular and radial marginals to integrated densities
        cuts=np.linspace(-a,a,11)
        hist=np.histogram(phi,bins=cuts)[0]/len(phi)
        true=np.array([quad(lambda t:(1-math.cos(t))/(2*(a-math.sin(a))),cuts[j],cuts[j+1])[0]
                       for j in range(10)])
        assert np.max(np.abs(hist-true))<.008,(n,'angular',hist,true)
        xc=np.linspace(1,1/math.cos(a),11)
        histx=np.histogram(x,bins=xc)[0]/len(x)
        prob=np.diff([limiting_cdf(n,t) for t in xc])
        assert np.max(np.abs(histx-prob))<.009,(n,'radial',histx,prob)
        sample_checks+=2
    # Independent second limit, verified for large n with normalized variables.
    for n in (30,60,120):
        a,C=fixed_limit_mark(n)
        u_edges=np.linspace(-1,1,21)
        exact=np.array([quad(lambda u:a*(1-math.cos(a*u))/(2*(a-math.sin(a))),
                             u_edges[i],u_edges[i+1])[0] for i in range(20)])
        limit=np.array([.5*(u_edges[i+1]**3-u_edges[i]**3) for i in range(20)])
        assert np.max(np.abs(exact-limit))<.001
        # Direct band threshold uniform convergence and limiting area normalization.
        for u in np.linspace(-1,1,101):
            lower=(math.cos(a*u)-math.cos(a))/(1-math.cos(a))
            assert abs(lower-(1-u*u))<.004
        assert abs(a*(1/math.cos(a)-1)/(2*C)-1.5)<.004
        sample_checks+=122
    print('PASS:',exact_checks,'area/coefficient checks;',limit_checks,
          'finite conditional CDF tests;',sample_checks,
          'marked-law Monte Carlo and second-limit checks')

if __name__=='__main__':
    run()
