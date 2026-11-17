"""Reproduce the algebraic identities and finite trajectory comparisons for a four-species cyclic replicator."""
import math
import sympy as sp
from scipy.integrate import solve_ivp

p, q, s, a = sp.symbols('p q s a', real=True)
u = [(1 + s + 2*p)/4, (1 - s + 2*q)/4,
     (1 + s - 2*p)/4, (1 - s - 2*q)/4]
C = sp.expand(sum(u[j]*u[(j+1) % 4] for j in range(4)))
f = [sp.expand(u[j]*((1+a)*u[(j-1) % 4]-u[(j+1) % 4]-a*C)) for j in range(4)]
k = a + 2
fs, fp, fq = (sp.expand(f[0]+f[2]-f[1]-f[3]),
              sp.expand(f[0]-f[2]), sp.expand(f[1]-f[3]))
assert sp.simplify(C-(1-s*s)/4) == 0
assert sp.simplify(fs-(-a*s/4+a*s**3/4-k*p*q)) == 0
assert sp.simplify(fp-(-k*(1+s)*q/4-a*s*p/4+a*s*s*p/4)) == 0
assert sp.simplify(fq-(k*(1-s)*p/4+a*s*q/4+a*s*s*q/4)) == 0
P=sp.prod(u)
Pdot=sp.expand(sp.diff(P,s)*fs+sp.diff(P,p)*fp+sp.diff(P,q)*fq)
assert sp.simplify(Pdot-a*s*s*P) == 0
# Verify the quadratic center manifold invariance for every parameter a>0.
D=a*a+4*k*k
h=4*k*k*(p*p-q*q)/D-4*a*k*p*q/D
inv=sp.diff(h,p)*(-k*q/4)+sp.diff(h,q)*(k*p/4)+a*h/4+k*p*q
assert sp.simplify(inv)==0
# Time/angular average of the quartic radial energy drift.
theta=sp.symbols('theta',real=True)
quartic=sp.expand(h*(-k*p*q+a*(q*q-p*p)/2))
periodic=sp.trigsimp(sp.expand_trig(quartic.subs({p:sp.cos(theta),q:sp.sin(theta)})))
mean=sp.simplify(sp.integrate(periodic,(theta,0,2*sp.pi))/(2*sp.pi))
beta=a*k*k/(2*D)
assert sp.simplify(mean+beta)==0
# Finite trajectory checks illustrate the nonlinear inverse-time limit.
def rhs(t,z,aa):
    pp,qq,ss=z; kk=aa+2
    return [-kk*(1+ss)*qq/4-aa*ss*pp/4+aa*ss**2*pp/4,
            kk*(1-ss)*pp/4+aa*ss*qq/4+aa*ss**2*qq/4,
            -aa*ss/4+aa*ss**3/4-kk*pp*qq]
for aa in (0.5,2.0):
    T=12000.0
    sol=solve_ivp(rhs,(0,T),[0.18,0.09,0.04],args=(aa,),
                  method='DOP853',rtol=2e-10,atol=2e-12,max_step=3.0)
    assert sol.success
    pp,qq,ss=sol.y[:,-1]
    observed=T*(pp*pp+qq*qq)
    target=2*(aa*aa+4*(aa+2)**2)/(aa*(aa+2)**2)
    assert abs(observed/target-1)<0.09,(aa,observed,target)
print('VERIFY_OK exact_four_cycle=3 exact_product_law=1 center_manifold=1 quartic_average=1 finite_decay_examples=2')
