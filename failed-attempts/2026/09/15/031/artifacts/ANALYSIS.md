# Analysis note — maximal Bochner–Riesz on H^n at critical index

## Setup
X = H^n(R), rho=(n-1)/2. Spherical multiplier m_R(la) = (1-(rho^2+la^2)/R)_+^z,
R>=rho^2. S_R^z f = f * ka_R^z, S_*^z f = sup_R |S_R^z f|.
Target T(p): Re z = (n-1)(1/p-1/2), 1<p<=2 (resp. p=1, Re z=(n-1)/2):
  S_*: L^p -> L^p + L^r for some finite r (resp. L^1 -> L^{1,w}+L^r).

Norm on sum: ||g||_{L^p+L^r} = inf_{g=g1+g2} ||g1||_p + ||g2||_r.

## Fact 1 (sum-space localization; why local strong bound is indispensable)
If supp g in fixed compact B, |B|<oo, and r>p, then for any decomposition,
||g2 1_B||_p <= |B|^{1/p-1/r} ||g2||_r, so ||g||_{L^p(B)} <= C(B) ||g||_{L^p+L^r}.
Hence TARGET implies a uniform LOCAL estimate: for f supported in a fixed
small ball, ||S_*^z f||_{L^p(B')} <= C ||f||_p. No choice of r rescues local failure.

## Fact 2 (transplantation necessity -> Euclidean maximal BR)
Small-scale asymptotics: H^n metric ~= Euclidean; spherical kernel
ka_R^z(x), |x|<=1, R large, is a perturbation of the Euclidean BR kernel
R^{n/2} K^z(sqrt(R) x). Standard Kenig-Stanton-Tomas scaling then gives:
TARGET ==> Euclidean maximal BR S_*^{z,Eucl} bounded on L^p(R^n) at the same
index de = (n-1)(1/p-1/2), first on compactly supported data, hence (by
translation/dilation invariance of the Euclidean maximal operator) globally.
Margin over Euclidean critical de_E = n(1/p-1/2)-1/2:
  de - de_E = 1/2-(1/p-1/2) = 1-1/p >= 0, strict for p>1.
So local side needs Euclidean maximal BR strictly above critical (p>1) or at
critical weak-type (p=1, de=(n-1)/2). [Needs exact known theorem: Stein classical
sufficiency de > n a - 1/2 would COVER p>1 local part. To verify by search.]

## Fact 3 (global obstruction to fixed-kernel domination)
For |x|=r>=1, Harish-Chandra: phi_la(r) = c(la)e^{(ila-rho)r}+c(-la)e^{(-ila-rho)r}+err.
ka_R^z(r) = e^{-rho r} I(R,r), I(R,r)=int_0^{sqrt(R-rho^2)} e^{+-ila r} a(la) m_R(la) dla,
a(la)=|c(la)|^{-2}c(la) ~ la^{(n-1)/2} growing. For fixed r, sup_R |I(R,r)| is a
maximal partial oscillatory integral of a NON-L^2 amplitude -> expected infinite
a.e. Hence NO fixed dominating kernel K* = sup_R |ka_R| in any L^q; Minkowski
domination route sup_R|f*ka_R| <= |f|*K* is DEAD. Maximal must exploit
cancellation in R jointly with f (maximal-multiplier / Carleson-type problem).

## Fact 4 (spectral picture: maximal partial spherical integrals)
S_R^z f = inverse-spherical-transform of m_R . fhat. sup_R over sharp-ish
cutoffs mu=sqrt(R-rho^2): maximal truncation problem with Plancherel density
|c(la)|^{-2} ~ la^2 d-la near la=0 (bottom of spectrum). Reduction to 1D weighted
Carleson hits Muckenhoupt: la^2 weight is NOT A_p for p<=3 (needs -1<2<p-1).
So the naive weighted-Carbleson route is structurally obstructed for 1<p<=2.

## Routes
R1 (local via Stein classical + transplantation): needs exact Stein maximal
    sufficiency statement. If confirmed covering de=(n-1)a, local CLOSES.
R2 (global via fixed dominating kernel + Kunze-Stein): expected DEAD by Fact 3;
    numerics on H^3 to confirm sup_R|ka_R(r)| = oo growth in Rmax.
R3 (global via spectral maximal / weighted Carleson): obstructed by Fact 4
    (weight not A_p); would need genuinely new maximal-multiplier input.
R4 (disproof via local scaling): IMPOSSIBLE in principle — transplantation gives
    only Euclidean maximal at de, which is above-critical/consistent; no contradiction.

## Recovery test (reproducible)
output/artifacts/br_h3_maximal.py: exact H^3 model (phi=sin/sinh, density la^2):
 round-trip self-test, kernel envelope vs Rmax, maximal action on bump + ring,
 L^p+L^r proxy norms. Decides R2 fate empirically and probes R3 at p=2,z=0.
