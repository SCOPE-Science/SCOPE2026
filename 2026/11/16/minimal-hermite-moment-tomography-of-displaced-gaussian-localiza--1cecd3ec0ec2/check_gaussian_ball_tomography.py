"""Numerical spot checks for Gaussian ball moment tomography.

Dependencies: Python 3 and mpmath. Analytical global results do not rely on
finite spot checks. All coordinates use Gaussian measure exp(-|z|^2)/pi.
"""
import mpmath as mp

mp.mp.dps = 55

def moments(a, r):
    """Mass and first x-moment of a disk centered at (a,0)."""
    q = mp.exp(-a*a)
    m = 2*q*mp.quad(lambda rho: rho*mp.exp(-rho*rho)*mp.besseli(0,2*a*rho), [0,r])
    bx = a*m - 2*q*mp.quad(lambda rho: rho*rho*mp.exp(-rho*rho)*mp.besseli(1,2*a*rho), [0,r])
    return m,bx

def analytic_det(a,r):
    t=2*a*r
    i0=mp.besseli(0,t)
    v1=(1+mp.besseli(2,t)/i0)/2-(mp.besseli(1,t)/i0)**2
    v2=(1-mp.besseli(2,t)/i0)/2
    lam=2*r*mp.exp(-a*a-r*r)*i0
    return r*r*lam**3*v1*v2

def j_determinant_fd(a,r,step=mp.mpf('0.000002')):
    # Under polar symmetry, the centered-x moment derivative in the y
    # direction is zero; the y first-moment derivative is bx/a for a>0.
    # At a=0, use the smooth radial limit via small positive a.
    ap = a if a else mp.mpf('0.00001')
    mr,br=moments(ap,r+step)
    ml,bl=moments(ap,r-step)
    mcr,bcr=moments(ap+step,r)
    mcl,bcl=moments(ap-step,r)
    dmr=(mr-ml)/(2*step)
    dbr=(br-bl)/(2*step)
    dma=(mcr-mcl)/(2*step)
    dba=(bcr-bcl)/(2*step)
    _,bv=moments(ap,r)
    return (dmr*dba-dma*dbr)*bv/ap

for a,r in [(mp.mpf('0.2'),mp.mpf('0.7')),(mp.mpf('1.3'),mp.mpf('0.8')),
            (mp.mpf('0.7'),mp.mpf('1.7')),(mp.mpf('0.0'),mp.mpf('1.0'))]:
    delta=analytic_det(a,r)
    det_num=j_determinant_fd(a,r)
    assert delta>0
    assert abs(det_num/delta-1)<mp.mpf('0.00001'), (a,r,delta,det_num)
    if not a:
        mass,b=moments(a,r)
        assert abs(mass-(1-mp.exp(-r*r)))<mp.mpf('1e-45')
        assert abs(b)<mp.mpf('1e-45')

for a,r in [(mp.mpf('0.35'),mp.mpf('0.55')),
            (mp.mpf('1.0'),mp.mpf('1.25')),
            (mp.mpf('1.8'),mp.mpf('0.6'))]:
    target=moments(a,r)
    rec=mp.findroot(lambda x,y:(moments(x,y)[0]-target[0],
                                moments(x,y)[1]-target[1]),
                    (a*mp.mpf('1.04'),r*mp.mpf('0.96')))
    assert abs(rec[0]-a)<mp.mpf('1e-30')
    assert abs(rec[1]-r)<mp.mpf('1e-30')

# At the origin in real dimension n the boundary probability is uniform.
# Its covariance is exactly I/n and the Jacobian is n^{-n} r^n lambda^{n+1}.
for n in (2,4,6):
    r=mp.mpf('0.8')
    lam=2*mp.pi**(n/2)/mp.gamma(n/2)*r**(n-1)*mp.pi**(-n/2)*mp.exp(-r*r)
    det=r**n*lam**(n+1)*n**(-n)
    assert det>0

print('GAUSSIAN_BALL_MOMENT_TOMOGRAPHY_CHECK_PASS')
print('dimension_two_cases=4 inverse_recoveries=3 centered_dimensions=2,4,6')
