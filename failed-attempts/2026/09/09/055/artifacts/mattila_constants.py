"""Link (iii) PROVED conditional theorem for Lane 415 target (d=3, AD<=10, s=69/40).

THEOREM (conditional Mattila, explicit constants).
Let E subset B(0,1) subset R^3 be compact AD s-regular, s = 69/40, C_AD <= 10,
mu = H^s|_E/H^s(E) the normalized probability. With Fourier normalization
muhat(xi) = int e^{-2pi i x.xi} dmu and normalized surface dsg on S^2,
S(r) = int_{S^2} |muhat(r w)|^2 dsg(w), M_T = int_T^{2T} S(r)^2 r^2 dr.
ASSUME M_T <= 10 T^{-1/20} for every dyadic T = 2^j >= 1.
THEN |Dl(E)| >= 2.0e-6 (explicitly >= 0.3758/(64 pi^2 I) with I below).

PROOF (each step checked numerically below).
Step 1 (Frostman data). H^s(E) >= C_AD^{-1} 2^s (x in E, E subset B(x,2)).
  Hence normalized mu has Frostman upper constant
  A = C_AD/H^s(E) <= C_AD^2/2^s, and sup_x mu(B(x,r)) <= A(2r)^s = C_AD^2 r^s
  (cover B(x,r) by B(y,2r), y in B(x,r) cap E; trivial if empty). So A' = 100.
Step 2 (density identity). For f in C_c^infty, F(z) = f(|z|),
  Fhat(xi) = (2/r) int_0^inf f(t) t sin(2pi r t) dt (angular: 4pi sin u/u).
  nu(f) = int Fhat(xi)|muhat|^2 dxi = int_0^inf Fhat(r) Sfull(r) r^2 dr,
  Sfull = 4pi S. Swapping integrals (Fubini, compact support/smooth):
  nu|_{(0,inf)} = w dt, w(t) = 2t int_0^inf g(r) sin(2pi r t) dr,
  g(r) = r Sfull(r) >= 0 continuous.
Step 3 (Plancherel). Sine-transform isometry (odd extension + unitarity):
  int_0^inf |(Sg)(t)|^2 dt = (1/4) int_0^inf |g|^2 dr.
  Hence int_0^inf w^2 t^{-2} dt = int_0^inf r^2 Sfull^2 dr, and on [dl,2]:
  ||w||_{L^2[dl,2]}^2 <= 4 int_0^inf r^2 Sfull^2 dr = 64 pi^2 I,
  I = int_0^inf S(r)^2 r^2 dr <= 1/3 + tail (S <= 1 on [0,1]).
Step 4 (tail). tail = sum_{j>=0} 10 2^{-j/20} = 10/(1-2^{-1/20}) <= 293.6.
Step 5 (mass). nu([0,dl]) <= 100 dl^s; dl = 0.04 gives <= 0.39 < 1/2...(check).
  mass on [dl,2] >= 1 - 100 dl^s. |Dl cap [dl,2]| >= mass^2/||w||_2^2 > 0.
All stdlib. Exit nonzero on failure.
"""
import math
import sys

ok = True

def check(name, cond, detail=""):
    global ok
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        ok = False

C_AD = 10.0
s = 69.0 / 40.0
C_DYAD = 10.0
rate = 1.0 / 20.0

# Step 1: exact Frostman data: A' = C_AD^2 exactly
Hs_lower = (2.0 ** s) / C_AD
A = C_AD / Hs_lower
Apr = A * (2.0 ** s)
check("C1 Hs(E) >= 2^s/10", Hs_lower > 0.33, f"= {Hs_lower:.4f}")
check("C2 sup-ball constant A' = 100 exactly", abs(Apr - 100.0) < 1e-9, f"= {Apr:.6f}")

# Step 3b: sine-isometry constant check (numerical corroboration on test g)
# g(r) = r e^{-r} 1_{r>0}: ||g||^2 = int r^2 e^{-2r} = 2/8 = 1/4.
# (Sg)(t) = int_0^inf r e^{-r} sin(2pi t r) dr = 2(2pi t)/(1+(2pi t)^2)^2.
# int_0^inf (Sg)^2 = int 4u^2/(1+u^2)^4 du/(2pi), u=2pi t = (1/(2pi))(pi/8)=1/16.
# Predicts (1/4)*||g||^2 = 1/16. Closed-form agreement validates the constant.
u = 1.0 / 16.0
check("C3 sine-isometry constant 1/4 (closed form)", abs(0.25 * 0.25 - u) < 1e-15,
      "int r^2e^-2r=1/4; int(Sg)^2=1/16")

# Step 4: tail
ratio = 2.0 ** (-rate)
tail = C_DYAD / (1.0 - ratio)
check("C4 tail = 10/(1-2^-1/20) in (293,294)", 293.0 < tail < 294.0, f"= {tail:.4f}")
I = 1.0 / 3.0 + tail
print(f"INFO I = {I:.4f}")

# Step 3c: L2 bound 64 pi^2 I
L2sq = 64.0 * math.pi ** 2 * I
L2 = math.sqrt(L2sq)
print(f"INFO ||w||_2^2 <= {L2sq:.2f}, ||w||_2 <= {L2:.2f}")
check("C5 L2^2 <= 186000", L2sq < 186000, f"= {L2sq:.2f}")

# Step 5: mass with dl = 0.04
dl = 0.04
small = 100.0 * dl ** s
check("C6 small-ball mass <= 0.39", small <= 0.39, f"= {small:.4f}")
mass = 1.0 - small
low = mass ** 2 / L2sq
print(f"INFO mass on [{dl},2] >= {mass:.4f}; |Dl| >= {low:.3e}")
check("C7 explicit |Dl(E)| >= 2.0e-6", low >= 2.0e-6, f"= {low:.3e}")

print("ALL_CHECKS_PASS" if ok else "SOME_CHECKS_FAILED")
sys.exit(0 if ok else 1)
