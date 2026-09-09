# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First certified regularity-six strength-one obstruction among three quadrics in six variables
- **Round:** 2026-09-07-first-light-01
- **Lane:** 394
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** constructive extremal-witness certification via generic-initial-ideal logging, minimal-Betti computation, and quadric-rank strength certificates inside Ananyan-Hochster strength decomposition

## Problem

Exhibit and certify the first minimal low-strength high-regularity obstruction among three-quadric ideals in 5-7 variables: an explicit triple of quadrics in six variables over Q with collective Ananyan-Hochster strength exactly 1 and Castelnuovo-Mumford regularity 6, logging its reverse-lex generic initial ideal, its minimal graded Betti table, and its strength certificate.

## Attempted claim

There exists an explicit homogeneous ideal I0=(q1,q2,q3) of three quadrics in S=Q[x1..x6], with exact recorded integer coefficients, such that with respect to reverse-lexicographic order x1>...>x6 its generic initial ideal Gin(I0) equals a single recorded Borel-fixed stable monomial ideal G0 of Castelnuovo-Mumford regularity 6 (maximal generator degree 7), the quotient S/I0 has Castelnuovo-Mumford regularity exactly 6 verified by its recorded minimal graded Betti table, and the collective Ananyan-Hochster strength of span_Q{q1,q2,q3} equals exactly 1 certified by one recorded 2-term decomposition q*=l1*m1+l2*m2 plus a recorded symmetric-matrix rank proof that no nonzero combination has strength >=2. This claim is framed as a standalone extremal boundary example in the strength-one locus, not as support for the already-proved s>=2 complete-intersection cap (A_2(3)=2, reg 3).

## Research outcome

No certified witness for target (reg-6 strength-one 3-quadric triple with Gin G0) or exact fallback (reg-5 strength-one triple) was obtained. Built an exact grevlex-GB + Koszul-strand Betti pipeline and established: (i) all 1330 monomial 3-quadric triples in 6 vars have vanishing strand-Euler totals at j=5,6; (ii) all 120 monomial triples in 4 vars have reg in {1:62, 2:48, 3:10}; (iii) ~300 random non-monomial 4-var-support triples, 11 structured pencil-wide rank<=4 triples, and 120 family-F2 (x1*a+x2*b) trials all have reg<=3 (generic behavior: complete intersection of reg 3). The 4-var-support lift path provably caps below the goal, and no credible reg>=5 candidate emerged, so neither the target nor the exact fallback criterion is met; the enumeration data are routine and do not qualify as an emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No Macaulay2/Singular/Sage in this environment; all Grobner/Koszul computations were done with a purpose-built exact pipeline (grevlex Buchberger over QQ/GF(32003), monomial-basis Koszul-strand homology via dense GF(p) linear algebra), cross-checked QQ-vs-mod-p on smoke cases but without an independent computer-algebra-system replay. Search coverage: complete for 4-variable monomial triples (120/120) and 6-variable monomial Euler screen (1330/1330), but only sparse sampling (~300 random + 11 structured + 120 F2 trials) of the non-monomial rank<=4 locus; no proof that reg-5/6 strength-one triples do not exist. Gin/G0 leg of the target was never reached for lack of a high-reg candidate.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No Macaulay2/Singular/Sage in this environment; all Grobner/Koszul computations were done with a purpose-built exact pipeline (grevlex Buchberger over QQ/GF(32003), monomial-basis Koszul-strand homology via dense GF(p) linear algebra), cross-checked QQ-vs-mod-p on smoke cases but without an independent computer-algebra-system replay. Search coverage: complete for 4-variable monomial triples (120/120) and 6-variable monomial Euler screen (1330/1330), but only sparse sampling (~300 random + 11 st…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
