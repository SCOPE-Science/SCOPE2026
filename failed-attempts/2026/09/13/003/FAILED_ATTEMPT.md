# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Dimension-free joint Poincare bound for heavy-tail entropic couplings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1447
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Schrodinger bridges and functional inequalities
- **Method:** Gamma-calculus variance decomposition into Gaussian conditionals plus marginal Poincare

## Problem

Let mu, nu be symmetric non-log-concave probability measures on R^n in the class with density proportional to exp(-V) where V(x) = ((n+nu_dof)/2) log(1+|x|^2/nu_dof) + W(x) with degrees of freedom nu_dof > 2 and W kappa_0-uniformly convex (kappa_0 >= 0, possibly zero), so each marginal satisfies a Poincare inequality but no logarithmic Sobolev inequality, is not log-concave, and is not a bounded oscillation of a uniformly convex potential; let pi_eps(mu,nu) be the quadratic-cost entropic coupling with regularization eps > 0 (relative entropy against the product marginals). Via Gamma-calculus variance decomposition into Gaussian bridge conditionals plus marginal Poincare terms, does there exist an explicit threshold nu_0(eps,kappa_0), independent of n, such that the joint law pi_eps satisfies a dimension-free Poincare inequality C_P(pi_eps) <= P(eps,kappa_0,nu_dof) for all nu_dof >= nu_0, with P independent of n, while for nu_dof approaching 2 an explicit heavy-tail witness defeats any such n-free bound? A complete answer proves the uniform joint spectral-gap bound above the threshold for all n, or disproves it with an explicit tail witness violating the claimed n-free constant.

## Attempted claim

Let mu, nu be symmetric non-log-concave probability measures on R^n in the class with density proportional to exp(-V) where V(x) = ((n+nu_dof)/2) log(1+|x|^2/nu_dof) + W(x) with degrees of freedom nu_dof > 2 and W kappa_0-uniformly convex (kappa_0 >= 0, possibly zero), so each marginal satisfies a Poincare inequality but no logarithmic Sobolev inequality, is not log-concave, and is not a bounded oscillation of a uniformly convex potential; let pi_eps(mu,nu) be the quadratic-cost entropic coupling with regularization eps > 0 (relative entropy against the product marginals). Via Gamma-calculus variance decomposition into Gaussian bridge conditionals plus marginal Poincare terms, does there exist an explicit threshold nu_0(eps,kappa_0), independent of n, such that the joint law pi_eps satisfies a dimension-free Poincare inequality C_P(pi_eps) <= P(eps,kappa_0,nu_dof) for all nu_dof >= nu_0, with P independent of n, while for nu_dof approaching 2 an explicit heavy-tail witness defeats any such n-free bound? A complete answer proves the uniform joint spectral-gap bound above the threshold for all n, or disproves it with an explicit tail witness violating the claimed n-free constant.

## Research outcome

Disproved the target: for Student-t marginals (admissible W=0) every exact coupling, including pi_eps at all eps>0, has infinite Poincare constant for all n and all nu>2, via explicit witnesses G_R with Var/Dir growing linearly in R.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the headline joint infiniteness C_P(pi_eps)=infinity for Student-t couplings is substantively implied by long-standard prior facts and is a mechanical corollary, not a new boundary. It is textbook that a Poincare (spectral-gap) inequality implies exponential tails/concentration and that on the line Muckenhoupt/Bobkov-Gotze criteria decide the inequality; polynomial-tailed laws such as Student-t / generalized Cauchy / Pearson / kappa-concave laws fail standard Poincare and satisfy only weighted Poincare. Saumard arXiv:1804.03926 explicitly treats Student t_alpha / generalized Cauchy via Stein kernels and weighted Poincare, Muckenhoupt criteria, and sub-gamma (not exponential) concentration, and the Bobkov-Ledoux kappa-concave program proves weighted, not standard, Poincare for Cauchy-type tails. The only joint step, C_P(pi)>=C_P(mu) for exact-marginal couplings tested on G_R(x,y)=f_R(x_1), is an immediate one-coordinate reduction. Hence prior results on equivalent formulations (Cauchy/Pearson/kappa-concave), broader exponential-tail necessity theorems, and the exhaustive 1D Muckenhoupt criterion jointly imply the claim; no new threshold, census, or boundary is changed. A literal-title search miss does not establish priority. value: FAIL: even taken as a rigorous disproof, the result is a textbook restatement/mechanical corollary plus exposure of a cheap admission defect, with no independently retrievable new boundary. ADMISSION_DEFECT: the target presupposed marginal Poincare for the whole class including W=0, so the negative resolution merely falsifies that false presupposition by picking W=0 and invoking the standard polynomial-tails-vs-exponential-tails obstruction at every nu>2. It does not classify which kappa0>0 pairs might still admit bounds, does not address weak/super-Poincare alternatives beyond a disclaimer, and the explicit linear-ratio witness is the standard Muckenhoupt two-point-mass witness, not a new extremal boundary. Under the shared STANDARD a TARGET whose likely negative resolution merely exposes a type/normalization error, vacuity, or false premise fails admission, and certification/numerics alone do not create value. A future researcher needs only the textbook fact that Student-t lacks Poincare, not this repackaged joint threshold record.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof uses the W=0 member of the admitted class (0-uniformly convex, hence allowed) with equal marginals mu=nu; it does not classify which (mu,nu,W) pairs with kappa_0>0 might still admit finite joint constants, nor does it address non-Poincare functional inequalities (weak Poincare, super-Poincare) which may hold with dimension-free rates. Numerical checks are confirmatory only; the theorem is fully analytic.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
