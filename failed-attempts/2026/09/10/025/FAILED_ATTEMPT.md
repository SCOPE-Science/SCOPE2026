# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Partial-data anisotropic Calderon quotient stability on the finite cylinder: recovery modulo boundary-fixing diffeomorphisms via linear-weight Carleman and CGO
- **Round:** 2026-09-07-first-light-01
- **Lane:** 553
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Inverse Problems
- **Method:** Carleman estimates with complex geometrical optics construction and partial-data integral identities

## Problem

Prove partial-data uniqueness and logarithmic stability for near-constant anisotropic conductivities on a named finite 3D cylinder UP TO the Lee-Uhlmann diffeomorphism gauge, from front-face Dirichlet-to-Neumann data via linear-weight Carleman plus CGO integral identities with gauge fixing; fallback is linearized partial-data injectivity modulo Lie-derivative gauge at the identity.

## Attempted claim

Let Omega={x in R^3: x1^2+x2^2<1, 0<x3<1} and let Gamma_acc be a fixed explicit open neighborhood in partial Omega of F_+={x in partial Omega: nu(x).e1>0}. Let gamma_1,gamma_2 be C^2 anisotropic conductivities on closure(Omega) with ||gamma_j-I||_{C^2}<=epsilon_0 for fixed explicit epsilon_0>0. Let Lambda^{part}_{gamma_j} denote the partial DN map with Dirichlet data supported in Gamma_acc and Neumann measured on Gamma_acc. Define the quotient distance d_Q(gamma_1,gamma_2)=inf_F ||F_*gamma_1-gamma_2||_{L^infty(K)} over C^2 diffeomorphisms F:closure(Omega)->closure(Omega) with F|_{partial Omega}=Id, where K is a fixed interior compact containing (0,0,1/2) and F_* is conductivity pushforward. Then Lambda^{part}_{gamma_1}=Lambda^{part}_{gamma_2} implies d_Q(gamma_1,gamma_2)=0; moreover d_Q(gamma_1,gamma_2)<=C|log||Lambda^{part}_{gamma_1}-Lambda^{part}_{gamma_2}||_*|^{-alpha} for explicit alpha>0, proved via one linear-weight Carleman estimate with phi(x)=x1, CGO solutions vanishing on partial Omega\Gamma_acc, and a divergence-free (Bianchi-type) gauge fixing near I.

## Research outcome

Target nonlinear quotient log-stability and preset fallback ker=G proof both NOT achieved (explicit gaps recorded). Emergent finding claimed instead: amplitude-completion ellipticity package for single-weight CGOs on the named front-face cylinder -- plane-wave deficiency certified, full rank-6 restoration via transport amplitudes certified (opposite-sign needs quadratic escape term, same-sign linear suffices), gauge inclusion proved, all 8 artifact replays OK.

## Why this attempt failed

Failed axes: value.

value: EMERGENT_FINDING assessed under ordinary value standard with no presumption; judged on strongest headline separately from honestly-disclosed open survey. The package consists of: (a) finite-matrix rank counts for a chosen CGO parametrization on one cell (plane<=4/=3, opposite linear 5/full 6, same-sign linear 6 over tested frequencies/seeds, 30-degree shadow arithmetic), plus (b) the easy-direction gauge inclusion G subset ker via standard div-W integration-by-parts. It does not close TARGET or FALLBACK (both admitted unmet) and supplies no PDE injectivity: without the missing boundary Carleman (C) and two-term-WKB remainder with K_- vanishing (R) plus quantitative axis leg, symbol ranks do not imply ker subset G, quotient estimate, or stability, as DRAFT Sec 2c concedes. (a) is an unexplained enumeration, not a rigorously established exact invariant of a natural object: ranks depend on arbitrary parametrization choices (test magnitudes, random seeds, 8 amplitude rows, tolerance 1e-9) rather than an intrinsic property; same-sign linear-6 has no analytic explanation (pure numerics); plane<=4 is immediate dimension counting (3 div-free rows + 1 plane row); 30-degree cap is elementary dot-product geometry; escape pairing ik(2tau^2-k^2)/8tau^3, while exact, is a 3x3 algebraic identity any worker on this route recomputes instantly with no demonstrated downstream citation need. It is not the protected kind of narrow datum (exact order/constant/witness/presentation of a canonical object motivated before computation that a future researcher must retrieve): a future quotient attempt cannot cite these sample ranks to impose gauge, benchmark invisibility, or attempt stability without redoing the analysis with (C)+(R). (b) is a textbook restatement: L_V formula and diffeomorphism-gauge invariance (hence linearized invariance) are standard in the anisotropic program; the div-W proof is a routine exercise, and only the trivial inclusion is shown. No new general theorem, no intrinsic invariant, no reusable lemma with standalone citation use; honest disclosure of incompleteness does not create value. Intrinsic low value / arbitrary-scope enumeration: must be REJECT, not repairable by bounded addition, since converting ranks into a PDE lemma requires constructing (C)+(R) and closing ker=G - a new research direction, not a bounded identity/motivation addition. Certification alone (8 OK replays) does not rescue an arbitrary parametrization-dependent number.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Symbol-level + computational certificate, not a PDE theorem closing ker=G or quotient log-stability.', 'Full boundary Carleman estimate (C) and two-term-WKB remainder with K_- vanishing (R) not constructed.', 'Axis (xi||e1) leg is qualitative Muntz uniqueness; no quantitative rate.', 'alpha=1/24 is conditional modulus arithmetic, not an established estimate.', 'Monte Carlo gauge-kernel replay is evidence only; proof is the div-W identity.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
