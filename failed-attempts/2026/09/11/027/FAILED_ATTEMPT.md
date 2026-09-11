# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** An explicit F2-cosystolic bound for one fixed-degree PGL3 Ramanujan triangle family
- **Round:** 2026-09-07-first-light-01
- **Lane:** 740
- **Disposition:** NO_RESULT
- **Domain:** High-Dimensional Expansion
- **Method:** Garland local-spectral gap analysis with Evra-Kaufman local-to-global coboundary expansion

## Problem

Transfer Garland/Evra–Kaufman machinery to one concrete family: certify the vertex-link spectral gaps for a fixed-q PGL3 Ramanujan triangle-quotient family and apply one local-to-global coboundary step to obtain an explicit F2 cosystolic-expansion constant; if linearity stalls, deliver the certified link table plus a proved weak-cosystole inequality and name the blocking eigenvalue.

## Attempted claim

For the infinite family X_n of 2-dimensional Ramanujan triangle complexes given by fixed-q (q=4) Cartwright–Steger PGL3(F_q((t))) congruence quotients with vertex degree D=D(q) fixed, prove h^1(X_n; F2) >= c with c=0.01: every F2 1-cochain alpha with ||alpha|| <= 1/2 satisfies |delta alpha| >= 0.01 * dist(alpha, Z^1(X_n;F2)), where norms count 2-faces and 1-faces normalized by |X_n(2)| and |X_n(1)| respectively.

## Research outcome

Target h^1>=0.01 blocked at certified link eigenvalue lambda=0.4 (DD step structurally negative, beta>5.13 needed vs cap). Revealed fallback pursued: part (1) lambda2<=0.45 certified exactly (0.4), but part (2) weak systole m/log(m) underivable from any available template (best-case DD RHS -15683/15000; tolerable-lambda ceiling 0.0153, 26x below actual; trickling gives no F2 constant). Binary criterion fails. No emergent finding (outputs are textbook corollary + anticipated plug-in). CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Vertex-link certificate covers the building link type (PG(2,4) incidence graph); transfer to every finite CS congruence quotient vertex link is by local isomorphism, stated but the quotient tower itself was not constructed.', 'Fallback part (1) (lambda2=0.4<=0.45) is certified; fallback part (2) (weak systole) was not proved — no available template yields any positive F2 input at lambda=0.4.', 'No new method for F2 local-to-global expansion at lambda=0.4 was developed; the 26x lambda gap is documented, not closed.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Vertex-link certificate covers the building link type (PG(2,4) incidence graph); transfer to every finite CS congruence quotient vertex link is by local isomorphism, stated but the quotient tower itself was not constructed.', 'Fallback part (1) (lambda2=0.4<=0.45) is certified; fallback part (2) (weak systole) was not proved — no available template yields any positive F2 input at lambda=0.4.', 'No new method for F2 local-to-global expansion at lambda=0.4 was developed; the 26x lambda gap is d…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
