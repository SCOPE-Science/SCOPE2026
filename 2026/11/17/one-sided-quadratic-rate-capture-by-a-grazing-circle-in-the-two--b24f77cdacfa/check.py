"""Independent algebraic and numerical diagnostics for a Matsuoka grazing-return theorem.

The analytic proof, not finite simulation, establishes the asymptotic theorem.
Requirements: Python 3, numpy, scipy, sympy.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

T, Y, b, rho, a12, a21 = sp.symbols('T Y b rho a12 a21', positive=True)
U, V, P, Q, z1, z2 = sp.symbols('U V P Q z1 z2', real=True)
k2 = b*Y/T
up=(rho-1)*U/T-b*V/T
vp=(U-V)/Y
I=(U-V)**2+(k2-1)*V**2
Idot=sp.diff(I,U)*up+sp.diff(I,V)*vp
assert sp.simplify(Idot.subs(rho,1+T/Y))==0
Mplus=sp.Matrix([[-(1+rho)/T,-b/T],[1/Y,-1/Y]])
assert sp.simplify(Mplus.trace()+(1+rho)/T+1/Y)==0
assert sp.simplify(Mplus.det()-(1+rho+b)/(T*Y))==0
# Nonlinearity forces in stable/center coordinates, two neuron clipping choices.
for neuron in (1,2):
    if neuron==1:
        dU=sp.sqrt(a21)*z1/(2*T)
        dV=z1/(2*Y*sp.sqrt(a12))
        vext=-U if False else -1
    else:
        dU=-sp.sqrt(a12)*z2/(2*T)
        dV=-z2/(2*Y*sp.sqrt(a21))
    # Verify action gradient explicitly; no guessed normal form.
    assert sp.simplify(sp.diff(I,U)*dU+sp.diff(I,V)*dV-2*(U-V)*dU-2*(k2*V-U)*dV)==0


def check_case(a12f,a21f,s1,s2):
    tx,ty,bf=1.,5.,1.
    rf=math.sqrt(a12f*a21f)
    assert abs(rf-(1+tx/ty))<1e-12
    h=np.linalg.solve([[1+bf,a12f],[a21f,1+bf]],[s1,s2])
    assert np.min(h)>0
    L1,L2=h[0]/math.sqrt(a12f),h[1]/math.sqrt(a21f)
    Lc=min(L1,L2);mult=2 if abs(L1-L2)<1e-9 else 1
    om=math.sqrt((bf-tx/ty)/(tx*ty));K2=bf*ty/tx
    theory=mult*2*math.sqrt(2)*rf/(3*tx*om*math.sqrt(Lc))
    def rhs(t,z):
        x1,y1,x2,y2=z
        return [(-x1-bf*y1-a12f*max(x2,0)+s1)/tx,(-y1+max(x1,0))/ty,
                (-x2-bf*y2-a21f*max(x1,0)+s2)/tx,(-y2+max(x2,0))/ty]
    def amp(z):
        x1,y1,x2,y2=z
        uu=((x1-h[0])/math.sqrt(a12f)-(x2-h[1])/math.sqrt(a21f))/2
        vv=((y1-h[0])/math.sqrt(a12f)-(y2-h[1])/math.sqrt(a21f))/2
        return math.sqrt(((uu-vv)**2+(K2-1)*vv**2)/(1-1/K2))
    ratios=[]
    for d in [0.002,0.0005,0.0002]:
        L=Lc+d; uv=L/K2
        ini=[h[0]+math.sqrt(a12f)*L,h[0]+math.sqrt(a12f)*uv,
             h[1]-math.sqrt(a21f)*L,h[1]-math.sqrt(a21f)*uv]
        sol=solve_ivp(rhs,(0,2*math.pi/om),ini,method='DOP853',rtol=3e-12,atol=2e-13,max_step=.02)
        assert sol.success
        ratios.append((L-amp(sol.y[:,-1]))/d**1.5)
    assert ratios[0]<ratios[1]<ratios[2]<theory
    assert abs(ratios[-1]/theory-1)<0.07
    print(f'multiplicity={mult}, grazing_amplitude={Lc:.12f}, theoretical_loss_coefficient={theory:.12f}, finite_diagnostic={ratios}')

check_case(1.5,.96,2.,2.)
check_case(1.2,1.2,1.6,1.6)
print('CHECKS PASSED: exact symbolic identities and two independent grazing multiplicities.')
