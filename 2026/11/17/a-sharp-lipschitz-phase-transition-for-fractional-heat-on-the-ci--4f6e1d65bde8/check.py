"""Independent numerical checks of sharp fractional-circle Lipschitz formula.
No finite test is offered as proof of an infinite theorem.
"""
import math
import mpmath as mp
mp.mp.dps=55
pi=mp.pi

def Fourier(alpha,t,n=900):
    return 4/pi*sum(((-1)**j)*mp.exp(-mp.mpf(t)*((2*j+1)**(2*mp.mpf(alpha))))/(2*j+1) for j in range(n))

def heat_periodized(theta,t,k=8):
    return sum(mp.exp(-(theta+2*pi*m)**2/(4*t))/mp.sqrt(4*pi*t) for m in range(-k,k+1))

def c_alpha(a):
    return (4**a)*mp.gamma(a+mp.mpf('0.5'))/(mp.sqrt(pi)*abs(mp.gamma(-a)))

def jump_slope(a):
    return 2*c_alpha(a)/a*(2/pi)**(2*a)*mp.dirichlet(2*a,[0,1,0,-1])

for t in ['0.03','0.10','0.6','1.4']:
    t=mp.mpf(t)
    geometric=2*mp.quad(lambda x:heat_periodized(x,t),[-pi/2,0,pi/2])-1
    spectral=Fourier(1,t,90)
    assert abs(geometric-spectral)<mp.mpf('1e-30'),(t,geometric,spectral)
print('GAUSSIAN_PERIODIZATION_VERSUS_FOURIER_PASS')
for t in ['0.10','0.3','1','3']:
    t=mp.mpf(t)
    exact=4/pi*mp.atan(mp.exp(-t))
    assert abs(exact-Fourier(mp.mpf('.5'),t,1200))<mp.mpf('1e-32')
print('POISSON_CLOSED_FORM_VERSUS_FOURIER_PASS')
for a in ['0.22','0.50','0.78']:
    a=mp.mpf(a)
    for t in ['0.12','0.3','1.0']:
        t=mp.mpf(t)
        L=Fourier(a,t,1300)
        assert mp.mpf('0')<L<1
    slope=jump_slope(a)
    assert slope>0
print('FRACTIONAL_MONOTONICITY_RANGES_AND_POSITIVE_JUMP_SLOPES_PASS')
assert abs(jump_slope(mp.mpf('.5'))-2/pi)<mp.mpf('1e-40')
print('POISSON_SHARP_INITIAL_SLOPE_PASS')
for t in ['0.006','0.009','0.012']:
    t=mp.mpf(t)
    deficit=1-Fourier(1,t,150)
    gaussian=(8*mp.sqrt(t)/(pi*mp.sqrt(pi)))*mp.exp(-pi*pi/(16*t))
    assert abs(deficit/gaussian-1)<mp.mpf('.055'),(str(t),str(deficit/gaussian))
print('GAUSSIAN_SUPERALGEBRAIC_BOUNDARY_PROFILE_PASS')
print('ALL_FRACTIONAL_CIRCLE_CHECKS_PASS')
