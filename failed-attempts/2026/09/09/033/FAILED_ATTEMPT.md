# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Height-equidistribution exclusion of the strictly preperiodic portrait (2,1) for cubic unicritical polynomials over quadratic fields
- **Round:** 2026-09-07-first-light-01
- **Lane:** 369
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Dynamics
- **Method:** Weil and canonical height comparison with arithmetic equidistribution and unlikely-intersection portrait constraints

## Problem

Decide realizability of the strictly preperiodic critical portrait (m,n)=(2,1) for unicritical cubic polynomials f_c(z)=z^3+c over number fields K with [K:Q]<=2, by closing an explicit height-versus-portrait inequality (Call-Silverman lower bound + Yuan-Zhang equidistribution cap + Medvedev-Scanlon portrait constraint) or isolating the exact Galois-orbit obstruction.

## Attempted claim

No parameter c in any number field K with [K:Q]<=2 yields f_c(z)=z^3+c whose critical point 0 has exact preperiodic type (m,n)=(2,1) (tail length 2, period 1); i.e., the Misiurewicz equation G_{3,2,1}(c)=0 has no root of degree<=2, proved by an explicit height inequality plus Galois-orbit degree check.

## Research outcome

Closed the full target claim elementarily: G_{3,2,1}(c)=c^4+3c^2+3 is Eisenstein-irreducible at 3, so no root has degree<=2, and roots are exactly the exact-(2,1) parameters.

## Why this attempt failed

Failed axes: originality.

originality: Headline claim (G_{3,2,1}=c^4+3c^2+3 irreducible / no root degree<=2 / no (2,1) realization over quadratic fields) was already recorded and mechanically implied by Hutz-Towsley arXiv:1309.4048 v2 (2013-2014). Theorem 1.1 gives the general primitive Misiurewicz formula G_d(m,n) whose specialization to (d,m,n)=(3,2,1) is exactly c^4+3c^2+3 (verified: Phi^*_{2,1}=(a3-a2)/(a2-a1)=c^2*G, divided by Phi^*_{0,1}^{d-1}=c^2 yields G; degree 4 matches Corollary 3.3 count (d^m-d^{m-1}-d+1)*sum =4). Figure 1 irreducibility table, d=3 row, lists as Irreducible '{(m,n)|0<=m<=3,1<=n<=3} U (4,2)' with Reducible empty, explicitly covering (2,1). An irreducible quartic has no linear or quadratic factor, so 'no root degree<=2' and the quadratic-field non-realization corollary follow mechanically without further work. Admission triage compared only Looper (conditional), Siu (quadratic counting, conditional), Benedetto-Ih (qualitative S-integral), Dunaisky-Krumm (periodic-critical quadratics) and omitted Hutz-Towsley irreducibility data, which is the nearest prior. Candidate's Eisenstein verification is correct but a new one-line proof of an already-tabled irreducibility does not create a new fact. Timestamp/failed search does not establish priority; substantive prior record defeats it.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: Cell (3,2,1) over degree<=2 only; no result for other (d,m,n) cells or higher-degree fields; height-equidistribution inequality from audit plan not needed and not established; novelty is the recorded verdict, proof method is elementary.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
