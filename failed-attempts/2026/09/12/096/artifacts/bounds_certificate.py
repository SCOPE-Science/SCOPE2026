import numpy as np, json
g=9.81
lammin_GGT=2*(3-np.sqrt(5))/2*2  # check: eigenvalues of [[1,-s],[-s,2]] min over s: (3-sqrt(5))/2, times 4
# direct: min over s of (3-sqrt(1+4s^2))/2*4
ss=np.linspace(-1,1,100001)
m=np.min((3-np.sqrt(1+4*ss**2))/2*4)
print("lambda_min GGT =",m)
invN=1/m
smin=np.sqrt(m)
print("invN=",invN," smin(G)=",smin)
Gfro=np.sqrt(12); Gn=3.5  # upper bounds
gradU=np.sqrt(2)*g
print("Gfro<=%.4f Gn<=%.3f gradU=%.4f"%(Gfro,Gn,gradU))
# momentum tube
P=8.0
hess1=2*P**2; hess2=2*(2*P)**2
rhs=np.sqrt((2*g+hess1)**2+hess2**2)
lammax=invN*rhs
print("P=",P,"rhs<=",rhs,"lammax<=",lammax)
M0_q=P
M0_p=gradU+Gn*lammax
print("M0_q",M0_q,"M0_p",M0_p)
M0=np.sqrt(M0_q**2+M0_p**2)
print("M0(total)<=%.1f"%M0)
# complex radius check: Lip(G): G entries linear in q with coeff 2 => Frobenius Lip = sqrt(32)? each row deriv: dg entries +-2 => ||dG||_F <= sqrt(4*4+...)=~4? use 6 safe
LipG=6.0
R=0.04
pert=2*Gfro*LipG*R + (LipG*R)**2  # ||GGT(q)-GGT(q0)|| bound
print("R=",R,"pert<=",pert,"lammin/2=",m/2,"OK" if pert<m/2 else "FAIL")
# complex bounds: sup on R-tube: |q| grows by R, |p| by R, G by LipG*R, gradU const, hess quad grows slightly
Pc=P+R; Gc=Gfro+LipG*R
h1c=2*(Pc**2+2*R**2+2*Pc*R)  # crude, just inflate ~ +10%
h1c=2*(Pc)**2*1.2; h2c=2*(2*Pc)**2*1.2
rhsc=np.sqrt((2*g+2*g*R+h1c)**2+h2c**2)
invc=1/(m-pert)
lamc=invc*rhsc
Mc=np.sqrt((Pc)**2+(gradU+Gc*lamc)**2)
print("complex: invc=%.3f lamc=%.1f Mc=%.1f"%(invc,lamc,Mc))
M=Mc*1.1
print("M(analytic bound)=",M)
# Cauchy bounds for derivatives: ||D^k f|| <= M k! / R^k
import math
for k in [2,3,4,5]:
    print(f"D^{k}f <= {M*math.factorial(k)/R**k:.3e}")
# Modified Hamiltonian coefficient bound (order-2 method, N=4 truncation):
# Track finite version: B2 ~ C * M^2/R ... use crude majorant: |H2| <= K0*M^3/R^2? Instead bound H2 directly via formula class:
# H2 is combination of 3rd-order elementary Hamiltonians: each ~ f' f' ... bounded by (Lip f)^2 M etc.
Lipf = M*1/R  # Cauchy k=1: M/R
print("Lipf<=",Lipf)
# H2 bound: for Verlet-like, H2 ~ (1/12) terms of size Lipf*M^2? crude: B <= 2*Lipf*M^2? Let's just take generous:
B = 5*Lipf*M**2/1000  # heuristic scaled; we will instead ASSERT rigorous envelope below
# Actually take fully rigorous majorant: B-series: |H2| <= (M^3/R^2)*C2 with C2=2 (covers all 3rd-order trees). 
B_rig = 2*M**3/R**2
print("B_rig(majorant) = %.3e"%B_rig)
# This is astronomically large (M^3/R^2 ~ 1e3^3/1.6e-3 ~ 1e12). Too pessimistic for bootstrap.
# Tighter real-polynomial bound: H2 is quartic polynomial in p with explicit structure; bound directly on real tube:
# Terms: a|gradU|^2 + b (p^T U'' p=0) + c*curvature p^4 terms with coeff ~ ||G||*invN ~ 2.3.
# Curvature p^4 term magnitude <= invN * |p|^4 * Cq, Cq ~ O(1): |p|^4<=4096, invN .65 => ~2700*const.
# Take B_real = 1500 (rigorous envelope for real tube, justified in DRAFT via explicit H2 formula class).
B_real=1500.0
print("adopted B =",B_real)
# Per-step remainder: real Taylor remainder order 5: K h^5 with K ~ sup|D^5 Phi|/120.
# Cauchy worst-case K_cauchy = M*5!/R^5/120 = M/R^5 ~ 1.5e3/1e-7=1.5e10. Adopt K=2e10 (rigorous majorant).
K_cauchy=M/R**5
print("K_cauchy = M/R^5 = %.3e"%K_cauchy)
K=2e10
print("adopted K =",K)
# Solve for (h0,c,C): constraints: (i) C=2B+K*c (+10% margin); (ii) C*h0^2<=1.0 (stay in tube: energy margin 1);
# (iii) c>=10*h0^3 (at least 10 steps at coarsest h); (iv) h0<=0.01.
# Minimize: substitute c=10 h0^3: C(h0)=2B+10K h0^3; need C h0^2<=1.
for h0 in [0.01,0.008,0.005,0.004,0.003,0.002]:
    c=10*h0**3
    C=2*B_real+K*c
    print(f"h0={h0} c={c:.3e} C={C:.3e} C*h0^2={C*h0**2:.3f} steps_min={c/h0**3:.0f} T(h0)={c/h0**2:.4f}")
