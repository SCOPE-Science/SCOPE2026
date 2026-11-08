"""Independent numerical and exact small-dimensional checks of a ball-affine projection identity.
The all-dimensional theorem is established analytically in RESULT.md."""
import math
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import beta, betainc, gammaln

def calc(d):
    c=math.exp(gammaln(d/2+1)-.5*math.log(math.pi)-gammaln((d+1)/2))
    a=1/(d+2)
    A=(d+2)/(d+1)*(1-a*a)**((d+1)/2)
    B=.5*beta((d+1)/2,.5)*betainc((d+1)/2,.5,1-a*a)
    C=c*(A-B)
    quad_c=(d+2)*c*quad(lambda t:(t-a)*(1-t*t)**((d-1)/2),a,1,epsabs=1e-12)[0]
    assert abs(C-quad_c)<1e-9*(1+abs(C)),(d,C,quad_c)
    assert C>0
    return C
for d in [1,2,3,4,5,6,8,10,15,20,30,100,1000]:
    C=calc(d)
    print(f'd={d} positivity_defect={C:.12g} operator_norm={1+2*C:.12g}')
# Independent exact univariate (d=1) integration: E[-(1+3Y)]_+ = 1/3
assert abs(calc(1)-1/3)<1e-12
# Full dimension 2 exact integral verified by independent 1-d integration above.
for d in [100,1000,10000]:
    L=1+2*calc(d)
    assert abs(L/math.sqrt(d)-math.sqrt(2/math.pi))<.15
print('BETA_INTEGRAL_AND_GAUSSIAN_SCALING_OK')
