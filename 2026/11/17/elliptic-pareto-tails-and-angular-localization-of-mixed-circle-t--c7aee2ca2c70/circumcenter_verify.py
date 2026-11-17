"""Independent numerical checks for the fixed-vertex circumcenter theorem.
Uses only NumPy and SciPy; sample circumcenters are solved from Cartesian equations.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk

PI = math.pi

def coefficient(r):
    return 2*(1-r*r)*float(ellipk(r*r))/(PI*PI)

def probability_quadrature(r, threshold):
    w = (1-r*r)/(2*threshold)
    def integrand(u):
        z = r*math.cos(u)
        low = max(-1, min(1,z-w))
        high = max(-1,min(1,z+w))
        return math.acos(low)-math.acos(high)
    return quad(integrand,0,2*PI,epsabs=3e-12,limit=500,points=[0,PI/2,PI,3*PI/2,2*PI])[0]/(2*PI*PI)

def cartesian_circumcenter(a,b,c):
    # Orthogonal-bisector equations: 2(a-c).O=|a|^2-|c|^2, 2(b-c).O=|b|^2-|c|^2.
    ax=a[:,0]-c[0]; ay=a[:,1]-c[1]
    bx=b[:,0]-c[0]; by=b[:,1]-c[1]
    den=ax*by-ay*bx
    s=(1.0-c@c)/2.0
    ox=s*(by-ay)/den
    oy=s*(ax-bx)/den
    return np.hypot(ox,oy),np.arctan2(oy,ox)

def run():
    rng=np.random.default_rng(20261111)
    N=1_200_000
    alpha=rng.uniform(0,2*PI,N)
    beta=rng.uniform(0,2*PI,N)
    a=np.column_stack((np.cos(alpha),np.sin(alpha)))
    b=np.column_stack((np.cos(beta),np.sin(beta)))
    for r in [0.0,0.35,0.70,0.92]:
        rad,angles=cartesian_circumcenter(a,b,np.array([r,0.]))
        C=coefficient(r)
        print(f'r={r:.2f}, C={C:.12f}, 8*P(R>8)={8*np.mean(rad>8):.12f}, exact 8*P={8*probability_quadrature(r,8):.12f}')
        for T in (2.,4.,8.):
            obs=float(np.mean(rad>T)); pred=probability_quadrature(r,T)
            se=math.sqrt(pred*(1-pred)/N)
            if abs(obs-pred)>6*se+0.0002:
                raise AssertionError((r,T,obs,pred,se))
        if r==0:
            for T in (1,2,8):
                assert abs(probability_quadrature(r,T)-2/PI*math.asin(1/(2*T)))<1e-11
        # Joint conditional mark: angular moment E[cos(2Theta)] is the first anisotropic Fourier mode.
        # Direct quadrature of analytic limiting angular density.
        gnorm=quad(lambda u:1/math.sqrt(1-r*r*math.cos(u)**2),0,2*PI,epsabs=2e-11)[0]
        assert abs(gnorm-4*float(ellipk(r*r)))<2e-9
        obs_cos=float(np.mean(np.cos(2*angles[rad>8])))
        exact_cos=(quad(lambda u:math.cos(2*u)/math.sqrt(1-r*r*math.cos(u)**2),0,2*PI)[0]/gnorm)
        # At T=8 conditional finite-T orientation differs from the limit by O(1/T^2); loose diagnostic only.
        assert abs(obs_cos-exact_cos)<0.025,(r,obs_cos,exact_cos)
        print(f'angular moment: sample {obs_cos:.6f}; asymptotic {exact_cos:.6f}')
    assert all(coefficient(q)>coefficient(v) for q,v in zip(np.linspace(0,.99,101)[:-1],np.linspace(0,.99,101)[1:]))
    for eta in (1e-4,1e-6,1e-8):
        rr=math.sqrt(1-eta)
        ratio=coefficient(rr)/(eta*math.log(1/eta)/(PI*PI))
        print('eta',eta,'boundary-log ratio',ratio)
        assert 1<ratio<2.0
    print('MIXED_CIRCLE_CIRCUMCENTER_NUMERIC_CHECKS_OK')

if __name__=='__main__':run()
