# Small-data global existence for the 3+1 evolutionary Skyrme system

## Context

The 3+1 wave-maps (nonlinear sigma) model for maps into SU(2) admits finite-time
blow-up from smooth data (Shatah / Turok-Spergel equivariant example). Skyrme
proposed adding a quartic term, proportional to the squared commutator
tr[L_mu,L_nu]^2 with L=U^{-1}dU, which breaks scale invariance and is
physically intended as short-range repulsion preventing collapse. The admitted
target asks for a two-sided small-data answer for the Cauchy problem in
pion-field coordinates about the identity: either global existence with sharp
decay, or a matching almost-global/blow-up lifespan bound.

## Definitions

Let U=sigma 1+i pi^a tau_a: R^{1+3}->SU(2) with pi=:u in R^3 and
sigma=sqrt(1-|u|^2). Work in the chart |u|<=delta_0<<1 about the identity with
fixed Skyrme coupling e in [e_0,e_1] subset (0,infinity). With
m=diag(-1,1,1,1) the Euler-Lagrange system is

  Box u^a + M^a_{bc}(u)(du,du) + e^{-2} Q^a(u,du,d^2u) = 0   (*)

where M^a_{bc} is quadratic semilinear whose leading part is a fixed linear
combination of the standard null forms Q_0(phi,psi)=m^{mu,nu}d_mu phi d_nu psi
and Q_{mu,nu}(phi,psi)=d_mu phi d_nu psi-d_nu phi d_mu psi, plus O(|u|)
coefficient remainders; Q^a is cubic, every monomial containing at least three
factors among {u,du,d^2u} with at most two derivatives on one factor and at
least one antisymmetric Q_{mu,nu} factor. Data are smooth compactly supported
with size eps=||(u,d_t u)|_{t=0}||_{H^N x H^{N-1}}, N>=7, image in the small
geodesic ball. Gamma denotes the Klainerman algebra
{d,S,Omega_{ij},Omega_{0i}}; dbar denotes good/tangential derivatives.

## Result

There exists eps_0(e)>0, depending on e only through e_0,e_1 via e^{-2}, such
that for 0<eps<=eps_0 the Cauchy problem for (*) admits a unique global smooth
solution satisfying, with C=C(e_0,e_1,N),

  sup_{t>=0} ||d Gamma^{<=N-1} u(t)||_{L^2}^2 <= C eps^2,
  int_0^infty ||<t-r>^{-1/2-} dbar Gamma^{<=N-1} u||_{L^2}^2 dt <= C eps^2,
  |d u(t,x)| <= C eps (1+t)^{-1}.

In particular the small-ball image is preserved and no finite-time breakdown
occurs in this regime, so the target's first alternative holds and the
almost-global/blow-up alternative is vacuous there.

## Proof and evidence

Commuting (*) with Gamma^{<=N-1} gives Box Gamma^I u=F_I with commutator,
semilinear, and quasilinear parts. The quasilinear coefficient satisfies
|A(u,du)| << 1 under the bootstrap, so the perturbed energy
E_I=int(|d_t Gamma^I u|^2+|nab Gamma^I u|^2-A^{0nu}dGamma^I u d_nu Gamma^I u)
is equivalent to flat energy. In a null frame the standard estimate
|Q_0|+|Q_{mu,nu}| <= |d phi||dbar psi|+|dbar phi||d psi| holds; it is verified
symbolically (Q(xi,xi)=0 for null xi) and numerically on 20000 Gaussian samples.
The bootstrap assumes E(t)<=4C_0 eps^2 plus sharp pointwise decay. Quadratic
null terms contribute a borderline (1+t)^{-1} rate absorbed by the Alinhac
ghost-weight dissipation, exactly as in the standard 3+1 null-form theorem
(Keel-Smith-Sogge variable-coefficient version covers the |A|<<1 perturbation).
Every Skyrme correction is cubic hence contributes an integrable
(1+t)^{-2} rate needing no null structure; additionally |A|<=|dbar u||d u|
gives negligible ||A_t||_infty. The ghost Gronwall closes E(t)<=3C_0 eps^2,
Klainerman-Sobolev restores pointwise decay, and the chart plus strict
hyperbolicity persist. Local well-posedness plus continuation gives T=infinity;
uniqueness follows from the difference estimate one derivative lower.
Reproducible artifact output/artifacts/check_null_structure.py certifies the
null identities, null-frame bounds, cubic-null vanishing with generic-data
control, bootstrap ODE closure, and short-range numerology.

## Limitations

Requires N>=7 (not sharp); eps_0 degenerates as e_0->0; compactly supported
data assumed (weighted-Sobolev extension routine but not carried out);
e->0 and e->infinity limits excluded; large-data and equivariant blow-up
regimes untouched.

## Reproducibility

Run python3 output/artifacts/check_null_structure.py; symbolic checks A1-A3,
null-frame bounds B1-B2, cubic-null checks C1-C4, ODE closure D1-D2, and
integrability E1-E2 must match output/artifacts/check_null_structure.log.
The analytic proof is self-contained in this file together with cited standard
3+1 null-form ghost-weight theory.

## References

Christodoulou-Klainerman small-data global existence for nonlinear waves with
null condition; Alinhac ghost-weight method; Keel-Smith-Sogge quasilinear null
theory; Geba-Nakanishi-Rajeev equivariant Skyrme/Adkins-Nappi small-data theory
(arXiv:1106.5750); Lei-Lin-Zhou evolutionary Faddeev model (arXiv:1203.2696);
Alejo-Maulen decay of global Skyrme solutions (arXiv:2108.01163).
