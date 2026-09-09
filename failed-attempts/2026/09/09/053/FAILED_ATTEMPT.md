# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Dimension-free KLS bound for 1-unconditional bodies with bounded cotype-2 constant via stochastic localization, or a thin-shell obstruction in the cross-polytope-to-cube interpolation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 412
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** Eldan stochastic localization with Kannan-Lovasz-Simonovits bisection and thin-shell covariance control

## Problem

Can Eldan stochastic localization, combined with KLS bisection and thin-shell comparison, prove a dimension-free spectral-gap (KLS) bound for 1-unconditional isotropic bodies with bounded cotype-2 constant, or else isolate an explicit thin-shell variance obstruction in the cross-polytope-to-cube (l_p^n) interpolation family?

## Attempted claim

Every 1-unconditional isotropic convex body K subset R^n with cotype-2 constant C_2(K) <= A satisfies the KLS spectral-gap bound psi_K >= c(A) > 0 with c depending only on A (in particular independent of n), proved via Eldan stochastic localization with KLS bisection and thin-shell covariance control; a proved uniform bound or a certified explicit variance-blow-up obstruction in the l_p^n cross-polytope-to-cube interpolation counts as decisive progress.

## Research outcome

Proved the exact preset fallback: uniform-in-time expected operator-norm bound 8 L_K^2 (in fact 2 L_K^2) for every 2D coordinate section covariance along Eldan localization of the isotropic cross-polytope. Full target assessed as not viable in-window; target-phase lemmas and computations preserved in WORKLOG.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: substantively mechanically implied by pre-existing general facts with no body-specific content. Nearest priors jointly imply the claim: (i) classical law of total covariance, (ii) Eldan 2013 Sec.2 posterior identity mu_t=Law(X|F_t) with C_t=I, (iii) isotropic Cov=L^2 I definition, (iv) textbook PSD op<=Tr. Together they yield the strictly more general lemma: for ANY probability mu on R^n with finite second moment and Cov=L^2 I, and ANY fixed k-dimensional coordinate projection, sup_t E[||P_E A_t P_E^T||_op] <= k L^2 by the identical 4-line proof. The fallback is the k=2 instance with mu=uniform on isotropic dilate of B_1^n — a mere parameter substitution. DRAFT step 4 invokes unconditional symmetry but uses only isotropy (Cov=L_K^2 I), which holds for every isotropic body; no cross-polytope volume, moment, cotype, or localization-trajectory computation is used. Literal zero-hits for the exact sentence do not establish priority per audit standard; substantive comparison shows zero new mathematics beyond instantiating the general variance decomposition. Admission fallback_originality claim that 'general localization theory yields no uniform section constant without the unconditional-structure argument' is refuted by the submitted proof itself, which supplies no such argument. value: FAIL with ADMISSION_DEFECT. Exact fallback proof is complete so Admission conditional value approval would normally apply, but it is reopened because the qualification was materially false on objective pre-Admission evidence. Admission claimed the bound is 'not mechanically implied,' 'requires the unconditional-structure argument,' gives 'the first localization covariance data point' requiring 'cross-polytope computation,' and 'transfers/feeds the KLS attack or certifies where the route breaks.' The proof demonstrates the opposite: the bound is the universal dimension-count 2L_K^2 valid for all isotropic measures, performs no B_1^n computation (sigma^2/vol/L_K tables in artifacts are unused by the proof), and has no discriminative power for KLS/thin-shell (it bounds expected section operator norm by initial trace for any body). A future researcher needs the one-line general lemma, not the B_1^n k=2 instance; the constant 2 is dim(E), not a computed invariant motivated before computation. This is a textbook restatement (total covariance + op<=Tr) and parameter substitution, which must be rejected even if correct and new. Intrinsic low value: no bounded topic-preserving addition can supply the missing substantive KLS-relevant content without beginning a new direction. Hence REJECT, labelled ADMISSION_DEFECT.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Proves only the section covariance-diameter lemma (constant 2, hence 8), not the full dimension-free KLS bound psi_K>=c(A); no bisection-to-full-KLS implication is claimed. Numerical replay corroborates the t=0 anchor only and does not substitute for the analytic uniform-in-t argument.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
