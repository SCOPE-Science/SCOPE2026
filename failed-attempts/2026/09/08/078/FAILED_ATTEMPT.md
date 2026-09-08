# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact deletion-contraction chromatic-polynomial census of planar triangulations on 8-12 vertices with a certified non-3-colorability witness and Beraha gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 237
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Graph Theory
- **Method:** deletion-contraction recursion with Birkhoff-Lewis reduction and root-isolation replay

## Problem

Compute, with replayable witnesses, the exact chromatic polynomials of all non-isomorphic planar triangulations and near-triangulations (triangulations of a disk) on n=8,...,12 vertices, and certify one minimal non-3-colorable witness plus a Beraha-interval zero-free gap.

## Attempted claim

For every non-isomorphic planar triangulation and near-triangulation G on 8<=n<=12 vertices (plantri census classes), the exact chromatic polynomial P_G(q) as listed in the committed table is correct as regenerated from its logged deletion-contraction recursion tree with canonical labelling and Birkhoff-Lewis reduction; at least one minimal non-3-colorable witness G* satisfies P_{G*}(3)=0 with a logged contraction UNSAT tree; and the committed chromatic-zero table contains no zero in the logged Beraha subinterval, certified by interval root isolation.

## Research outcome

Partial-theorem census: exact deletion-contraction chromatic polynomials for 17 plantri-natural triangulations/near-triangulations on 8-12 vertices, dual-verified by independent counting; certified deletion-minimal non-3-colorable witness W_8; exact-Sturm real-root gap (10/3,4) for all 17; exact Beraha-B_5 data points.

## Why this attempt failed

Failed axes: originality, value.

originality: The delivered 17-graph table is not new as a substantive claim. Nearest priors mechanically imply or already publish its entries: (1) Wheels W8-W12 fall under the textbook closed form pi(x)=x[(x-2)^(n-1)-(-1)^n(x-2)] published on MathWorld Chromatic-Polynomial and Wheel-Graph pages; the five entries were verified to be exact evaluations of that formula, i.e. mere parameter substitutions n=8..12. (2) Icosahedron I12 polynomial is published verbatim on the MathWorld Icosahedral-Graph page as z(z-1)(z-2)(z-3)(z^8-24z^7+...+20170); expansion matches the committed I12 coefficients byte-for-byte, so it is a textbook restatement. (3) Stacked S9 (K4 stellated 5x) equals q(q-1)(q-2)(q-3)^6 by the standard simplex-gluing lemma; verified equal, hence mechanically implied. (4) Fans F8-F12 (K1 plus path joins) and bipyramids D8-D12 (cycle plus 2K1 joins) are standard textbook join families whose polynomials follow by routine deletion-contraction or join formulas; tabulating n=8..12 adds no new method or identity. (5) The (10/3,4) real-root gap and Q(sqrt5) B5 evaluations are direct Sturm/Horner readings of those already-known polynomials, not a new zero-free theorem; Sokal cond-mat/9904146 already gives the general complex-disc program and Tutte golden-identity literature gives the Beraha relations. The admitted target (complete 297-class census with recursion witnesses) would have been new, but the delivered artifact abandons it for 17 highly symmetric members. A failed-search log or generator-layer distinction does not establish priority over closed-form prior art. value: The result is not independently worth retrieving later. It is a textbook restatement plus parameter substitution (wheels via known formula, icosahedron already published, stacked trivial) plus a tiny arbitrary slice (15 join-family members plus 2 extras) explicitly admitted NOT to be the complete 297-class or disk census, so it has neither census completeness nor extremal/witness novelty. The W8 minimal non-3-colorable witness is the elementary odd-rim-wheel parity fact chi(W_n)=4 iff n even (textbook), with minimality by deleting to C7/C6-even-wheel; no future reducibility checker needs this instance certified. The (10/3,4) real-only Sturm gap on this arbitrary 17-set is an unexplained number on an arbitrary object: interval choice is unmotivated relative to Beraha numbers (B7 about 3.247 lies below it, B5 about 2.618 far below), no complex-disc or infinite-family consequence is proved, and no downstream theorem uses it. The narrow-datum exception does not apply because the values were already known or mechanically implied by published closed forms, and certification/replay alone does not rescue an arbitrary scope. Hence intrinsic low value, not a bounded-addition fix.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial theorem only: 17 explicit graphs, NOT the admitted full 297-class sphere census nor the disk census. Gap is real-roots-only on (10/3,4), not a complex zero-free disc; no Birkhoff-Lewis reduction log; no Tutte golden identity proved (B_5 values are data). plantri unavailable in sandbox (no binary/pip), so classes are explicit constructions, not generator output.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
