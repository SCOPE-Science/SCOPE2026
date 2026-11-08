# Scientific assessment

## Correctness — PASS

The parity check is onto and equivariant under the constacyclic shift. For each proper divisor of the full action order, fixed ambient vectors must have zero syndrome, allowing the complete fixed-weight enumerator to be obtained from disjoint coordinate cycles. At the full divisor, the dual simplex code has constant nonzero weight, so the standard MacWilliams transform applies. Weight-preserving Möbius inversion gives the exact orbit count of every period and weight. A standalone separately constructed finite-field checker exhaustively verifies the complete claim on seven instances, including a nonprime repunit case; this is supporting evidence rather than a substitute for the general proof.

## Originality — PASS against inspected literature

Etzion's 2026 manuscript [1] develops the same constacyclic Hamming-code model and explicitly raises enumeration and composite-repunit period questions. Zhang–Cao [2] already prove **total** constacyclic orbit formulas for arbitrary simple-root constacyclic codes. Those unrefined totals are not a novelty claim. Neither the inspected full texts of [1], [2], [3] nor the examined covering-sequence construction [4] states the simultaneous exact period–Hamming-weight orbit multiplicities or the fixed-weight polynomial family of the theorem. The general orbit Burnside and MacWilliams tools are standard; the specific weight-refined classification is the claimed contribution. Risks include equivalent unindexed joint-spectrum results or a specialization of a broader formula not identified in the inspected literature; historical priority has not been independently confirmed.

## Value — PASS

A length/period-only count leaves unresolved how many orbits of each period have each Hamming weight; that matters when selecting constant-composition or low-weight codewords for the covering-sequences construction. The result answers the specific composite-repunit period feasibility question and refines every feasible period to an explicit weight distribution, for infinitely many parameter choices. The exact formulas and a full nonprime example make the claimed invariant both natural and reproducible, rather than an arbitrary parameter slice.

## Scope and limits

No assertion is made about optimal covering sequence length, higher covering radius, or orbit equivalence under larger automorphism groups. The formulas are proved for the constacyclic Hamming-code action only. See RESULT.md for the proof and verify_orbits.py for limited-case checks.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] https://arxiv.org/abs/2607.14840 (first released 2026-07-16; Sections IV and VI)
[2] https://arxiv.org/abs/2305.06505 (Sections 2–3 and orbit formula)
[3] https://arxiv.org/abs/2405.00309 (abstract and group-action results)
[4] https://doi.org/10.1007/s10623-025-01726-5
