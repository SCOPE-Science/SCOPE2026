"""Independent numerical checks for boundary-distance formulas on boxes.
No empirical check serves as a proof of a limiting assertion.
"""
import math
import numpy as np
from scipy.stats import qmc
from scipy.integrate import quad

def surface_sample(u, sides):
    a,b,c=map(float,sides)
    areas=np.array([b*c,b*c,a*c,a*c,a*b,a*b],dtype=float)
    z=u[:,0]*sum(areas)
    kk=np.searchsorted(np.cumsum(areas),z,side='right')
    xyz=np.zeros((len(u),3))
    # sample coordinates in [0,length] and fix one at 0 or length
    xyz[:,0]=a*u[:,1]; xyz[:,1]=b*u[:,2]; xyz[:,2]=c*u[:,3]
    for j,(axis,edge) in enumerate(((0,0),(0,a),(1,0),(1,b),(2,0),(2,c))):
        mask=kk==j
        xyz[mask,axis]=edge
    return xyz

def exact(sides,r):
    a,b,c=sides
    e1=a+b+c;e2=a*b+a*c+b*c;e3=a*b*c
    S=2*e2
    cdf=(math.pi*S*r*r+(8/3)*(math.pi-2)*e1*r**3+3*(1-math.pi)*r**4)/S**2
    moment=(e1*e1*e2-2*e2*e2+2*e1*e3)/(6*e2)
    return cdf,moment

# For each pair, use two separate scrambled 4D Sobol designs, averaging both.
def check():
    cases=[(1.,1.,1.),(1.,1.7,2.4),(0.8,1.2,2.7),(1.,2.,3.)]
    for ix,dims in enumerate(cases):
        r=0.64*min(dims)
        theor,m2=exact(dims,r)
        estimates=[]; moments=[]
        for j in range(2):
            s=qmc.Sobol(8,scramble=True,seed=1700+10*ix+j).random_base2(18)
            x=surface_sample(s[:,:4],dims);y=surface_sample(s[:,4:],dims)
            ds=np.einsum('ij,ij->i',x-y,x-y)
            estimates.append(np.mean(ds<=r*r));moments.append(np.mean(ds))
        mc=float(np.mean(estimates));mm=float(np.mean(moments))
        print('BOX',dims,'r',r,'cdf_exact',round(theor,9),'cdf_qmc',round(mc,9),'difference',round(mc-theor,9),'m2_exact',round(m2,9),'m2_qmc',round(mm,9),'m2_difference',round(mm-m2,9))
        assert abs(mc-theor)<.0035,(dims,mc,theor)
        assert abs(mm-m2)<.03,(dims,mm,m2)
        e2=sum(dims[i]*dims[j] for i,j in ((0,1),(1,2),(0,2)))
        e1=sum(dims); S=2*e2
        c2=math.pi/S;c3=(8/3)*(math.pi-2)*e1/S**2
        e1inv=3*S*S*c3/(8*(math.pi-2))
        e3inv=(6*e2*m2-e1inv*e1inv*e2+2*e2*e2)/(2*e1inv)
        assert abs(e1inv-e1)<1e-12 and abs(e3inv-np.prod(dims))<1e-11
        roots=np.sort(np.roots([1,-e1inv,e2,-e3inv]).real)
        assert np.max(np.abs(roots-np.sort(dims)))<1e-5
    angles=[math.pi/3, math.acos(1/3), math.pi/2, 2.25]
    for theta in angles:
        integrand=lambda z: 1/(1+z*z-2*z*math.cos(theta))
        numeric,err=quad(integrand,0,math.inf,epsabs=1e-11,epsrel=1e-11)
        analytic=(math.pi-theta)/math.sin(theta)
        assert abs(numeric-analytic)<1e-10,(theta,numeric,analytic)
    # Independent exact integral checks for the two planar covariogram moments.
    v1=quad(lambda t:4*t*math.sqrt(1-t*t),0,1,epsabs=1e-12)[0]
    v2=quad(lambda t:2*t*t*math.sqrt(1-t*t),0,1,epsabs=1e-12)[0]
    assert abs(v1-4/3)<1e-10 and abs(v2-math.pi/8)<1e-10
    print('VERIFY_OK boxes=4 samples_per_box=524288 exact_inverse=4 wedge_angles=4')
if __name__=='__main__':check()
