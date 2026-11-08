"""Finite symbolic and numerical checks for an exact three-line Gabor zero-intensity law."""
import math
import sympy as sp

u, b = sp.symbols('u b', positive=True)
den = 1 + b*u + u**2
count = u*(b+2*u)/den
profile = sp.diff(count, u)*u
assert sp.simplify(profile - u*(b+4*u+b*u*u)/den**2) == 0
assert sp.simplify(sp.diff(profile,u) + (u-1)*(u+1)*(b*(u*u+1)+(8-b*b)*u)/den**3) == 0
assert sp.simplify(sp.limit(count,u,sp.oo) - sp.limit(count,u,0)) == 2
assert sp.simplify(sp.diff(profile,u).subs(u,1)) == 0
q=b*(u*u+1)+(8-b*b)*u
assert sp.simplify(profile-b*b/(4*(b*b-4)) + q*q/(4*(b*b-4)*den*den)) == 0
assert sp.simplify((u*sp.diff(u*sp.diff(profile,u),u)).subs(u,1)-2*(b-4)/(b+2)**2) == 0
checks=5
for beta in (sp.Rational(1,2), 1, 2, 4, 5, 8, 20):
    val=float(beta)
    if val <= 4:
        us=(1.,)
    else:
        disc=math.sqrt((val**2-16)*(val**2-4))
        us=((val**2-8-disc)/(2*val), 1., (val**2-8+disc)/(2*val))
        assert abs(us[0]*us[2]-1)<1e-10
        v=[float(profile.subs({u:z,b:beta})) for z in us]
        assert v[0]>v[1] and v[2]>v[1] and abs(v[0]-v[2])<1e-9
        checks+=3
    for t in (0.003, 0.01,0.1,0.2,0.5,1,2,5,10,100,500):
        assert float(profile.subs({u:t,b:beta}))>0
        checks+=1
# Independent direct Gaussian STFT sampled frequency identity for selected tone choices.
import cmath
for Delta,amps,nu,omega,x in ((0.7,(1.,1.3,2.),0.,1.2,0.3),(1.,(2.,0.8,1.5),-2.,0.4,-0.7)):
    Z=(0.4+0.6j, -0.7+0.1j,1.1-0.3j)
    direct=sum(amps[j]*Z[j]*math.exp(-math.pi*(omega-nu-j*Delta)**2)*cmath.exp(2j*math.pi*(nu+j*Delta-omega)*x) for j in range(3))
    z=cmath.exp(2*math.pi*Delta*(omega-nu)+2j*math.pi*Delta*x)
    poly=sum(amps[j]*Z[j]*math.exp(-math.pi*j*j*Delta*Delta)*z**j for j in range(3))
    factor=math.exp(-math.pi*(omega-nu)**2)*cmath.exp(2j*math.pi*(nu-omega)*x)
    assert abs(direct-factor*poly) < 1e-8*max(1,abs(direct))
    checks+=1
print('THREE_LINE_MODALITY_CHECKS_PASSED',checks)
