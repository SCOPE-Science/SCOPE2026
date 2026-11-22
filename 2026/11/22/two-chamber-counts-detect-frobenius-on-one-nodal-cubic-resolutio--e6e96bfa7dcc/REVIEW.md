# Review of two chamber counts detecting Frobenius on one-nodal cubic resolutions

## Correctness — PASS

All negative curves are exhausted by Bézout and adjunction: six exceptional curves, fifteen secant transforms, and the unique conic root. Exact integer Picard pairings establish that a support is negative definite precisely when its selected \((-1)\)-curves are mutually disjoint and at most one exceptional curve accompanies the root. The general Zariski-chamber correspondence from Bauer–Funke–Neumann gives existence of every support. Three independently structured enumerations reconstruct the eleven Frobenius-stable-support and root-containing-support counts, including a star/triangle proof-of-exhaustion check for all 720 permutations; `verify_picard.py` checks the geometric intersections. A Galois-stable support is the negative support of a ground-field big divisor by an ample-divisor construction, and six closed conic points of each required partition exist with the stated small-field boundary. The finite programs prove only a genuinely finite classification; the geometric and descent steps are separately argued.

## Originality — PASS, qualified

Blache–Hallouin (arXiv:2301.13582v1) classify the eleven arithmetic types and conic construction. Bauer–Funke–Neumann (arXiv:0912.0958v1) prove the chamber/negative-definite-support correspondence. The published one-nodal cubic geometric chamber spectrum already establishes the total \(1898\), root subtotal \(648\), and support criterion; these are expressly credited, not claimed here. The assessed new material is the full eleven-type arithmetic pair table and minimality of the two scalar counts. Scientific searches for the exact table, broader arithmetic cover and equivalent permutation-character computations did not identify an existing result. Historic priority remains at risk if an inaccessible specialist enumeration already contains this table; this is a self-review, not independent novelty certification.

## Mathematical value — PASS

A ground-field Zariski-chamber support is a natural pattern of fixed components in the Zariski decomposition of an actual rational big divisor, not an arbitrary statistic. The two numerical invariants determine all possible Frobenius splittings of the six conic blow-up centers. The single count demonstrably fails for the \((4,2)\) and \((5,1)\) partitions; the uniquely distinguished \((-2)\) conic supplies exactly the second piece of information needed. This yields a complete natural arithmetic classification with a meaningful minimal-data obstruction, without asserting any downstream theorem or universal volume formula.

## Closest literature and limitations

- R. Blache and E. Hallouin (2023), §5.2 and Appendix A Table 8, classification of weak del Pezzo arithmetic types: https://arxiv.org/pdf/2301.13582
- T. Bauer, M. Funke and S. Neumann (2009), Proposition 1.1, chamber support correspondence: https://arxiv.org/pdf/0912.0958
- Published one-nodal cubic geometric chamber spectrum (2026), full support polynomial and root subtotal: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-zariski-chamber-spectrum-of-the-one-nodal-cubic-s-minimal-resolu--4b531d234d53/RESULT.md

This classifies a finite set of ground-field-realizable negative supports, not surfaces up to isomorphism or volumes of their Zariski chambers. The geometric total and eleven abstract Weyl classes are prior results. No independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
