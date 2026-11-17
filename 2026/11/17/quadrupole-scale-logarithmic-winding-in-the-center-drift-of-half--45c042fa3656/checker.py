"""Finite algebraic and asymptotic checks for a half-plane three-vortex center expansion."""
import cmath
import math

GAMMA = (2.0, 2.0, -1.0)
a2 = math.sqrt(3.0)/(14.0*math.pi)
a = math.sqrt(a2)
W0 = (1.0+0j, -2.0-1j*math.sqrt(3.0), -2.0-2j*math.sqrt(3.0))
W = tuple(a*z for z in W0)
OMEGA = -5.0*math.sqrt(3.0)/6.0
G = sum(GAMMA)
Q = sum(g*z*z for g,z in zip(GAMMA,W))
assert abs(sum(g*z for g,z in zip(GAMMA,W))) < 2e-14
assert abs(sum(g*abs(z)**2 for g,z in zip(GAMMA,W))) < 2e-14
assert abs(Q-6*math.sqrt(3.0)/(7.0*math.pi)) < 2e-14
assert abs(sum(GAMMA[i]*GAMMA[j] for i in range(3) for j in range(i+1,3)))<1e-14
for k in range(3):
    f = sum(GAMMA[j]/(W[k]-W[j]) for j in range(3) if j!=k)/(2j*math.pi)
    assert abs(f-(-.5+1j*OMEGA)*W[k].conjugate()) < 2e-13

def drift(x):
    # Exact center derivative, including every mirrored pair, in complex form.
    s=sum(GAMMA[i]*GAMMA[j]/(x[i]-x[j].conjugate())
          for i in range(3) for j in range(3))
    return (-s/(2j*math.pi*G)).conjugate()

Y = 1.75
for tau in (1e-2, 2e-3, 1e-4, 1e-5):
    phase=cmath.exp(1j*OMEGA*math.log(tau))
    z=tuple(1j*Y+math.sqrt(tau)*phase*w for w in W)
    actual=drift(z)
    asym=G/(4*math.pi*Y)-tau/(8*math.pi*Y**3)*(phase*phase*Q).real
    err=abs(actual-asym)
    assert abs(actual.imag)<5e-14
    assert err < 1.0*tau**1.5
    print('tau',tau,'dReC/dt',format(actual.real,'.12g'),
          'quadrupole_residual',format(err,'.4g'),
          'residual_over_tau_3_2',format(err/tau**1.5,'.5g'))

amplitude=abs(Q)/(16*math.pi*Y**3*math.sqrt(1+OMEGA**2))
assert amplitude>0
print('VERIFY_OK profile_equations=3 conserved_moments=3 image_drifts=4')
print('EXAMPLE Ω=',OMEGA,'Q=',Q,'oscillation_amplitude_at_height_1_75=',amplitude)
print('FINITE_CHECK_ONLY: all-time expansion and limsup/liminf follow from the analytical proof')
