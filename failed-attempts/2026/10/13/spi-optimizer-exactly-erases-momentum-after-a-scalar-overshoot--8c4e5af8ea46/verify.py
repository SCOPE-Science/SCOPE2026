import math
import numpy as np

def spi(alpha,s,theta0,N=50):
    theta=theta0
    v=0.0
    out=[]
    for t in range(N):
        keep = (theta*v)>0.0
        vnext=alpha*v*(1.0 if keep else 0.0)+s*theta
        thetanext=theta-vnext
        out.append((thetanext,vnext,keep))
        theta,v=thetanext,vnext
    return out

# Exact overshoot branch and permanent momentum erasure.
for alpha in (0.0,0.2,0.9,0.99):
    for s in (1.01,1.2,1.7,1.999,2.0,2.3,4.0):
        for theta0 in (-3.0,-0.4,0.7,2.5):
            rows=spi(alpha,s,theta0,30)
            for t,(theta,v,keep_used) in enumerate(rows, start=1):
                closed_theta=(1-s)**t*theta0
                closed_v=s*(1-s)**(t-1)*theta0
                assert abs(theta-closed_theta)<2e-10*max(1.0,abs(closed_theta))
                assert abs(v-closed_v)<2e-10*max(1.0,abs(closed_v))
                if t>=2:
                    assert keep_used is False

# Stability phases.
for s in (1.1,1.5,1.9):
    rows=spi(0.95,s,1.0,300)
    assert abs(rows[-1][0])<1e-10
rows=spi(0.8,2.0,1.0,20)
for t,(theta,v,_) in enumerate(rows, start=1):
    assert abs(theta-((-1.0)**t))<1e-12
for s in (2.01,2.2,3.0):
    rows=spi(0.8,s,1.0,40)
    assert abs(rows[-1][0])>1.0

# Ordinary momentum exact Schur boundary.
def mom_radius(alpha,s):
    M=np.array([[1+alpha-s,-alpha],[1.0,0.0]])
    return max(abs(z) for z in np.linalg.eigvals(M))

for alpha in (0.1,0.5,0.9):
    upper=2*(1+alpha)
    assert mom_radius(alpha,0.5)<1
    assert mom_radius(alpha,upper*(1-1e-8))<1
    assert mom_radius(alpha,upper*(1+1e-8))>1
    midpoint=0.5*(2.0+upper)
    assert midpoint>2.0
    assert mom_radius(alpha,midpoint)<1.0
    # SPI diverges there because it is exact GD after the first crossing.
    rows=spi(alpha,midpoint,1.0,30)
    assert abs(rows[-1][0])>1.0

print("verification passed")
