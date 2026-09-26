# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/003`  
**Audited source tree:** `845dac2895f09a8b2d02f1eb7c162f7c148eae0e`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** FAILED

## Correctness

FAIL — The verifier labels 41 backbone pairs as contacts by |distance²−(2r)²|≤2×10⁻¹², but with its exact Fraction coordinates 39 have strictly positive gap; only (2,3) and (8,14) are exact pair contacts. Its 55-row R is therefore the rigidity matrix of a hypothetical contact graph, not the active-constraint matrix of the stated packing. More decisively, set ε=10⁻¹⁵ and r'=r+ε. For every listed wall contact move its center inward by ε in the normal direction; additionally set v₂x=−1,v₃x=+1,v₈y=−1,v₁₄y=+1 (velocities in units of ε); leave all other velocity components zero. Exact rational comparison of all 465 center pairs and 124 wall inequalities at these new coordinates gives no overlap or boundary violation (minimum pair squared gap and wall gap are zero). This strictly larger feasible radius directly refutes first-order maximality at the committed rational configuration. Positive stress for the artificial 55-row matrix does not repair the missing equalities.

## Originality

UNSUPPORTED — Packomania already provides the heuristic N=31 placement and reported contact/loose counts. The rank/stress arithmetic for a tolerance-selected graph may be a new calculation, but it is not a valid rigidity result about active constraints and the claimed novelty cannot support acceptance.

## Scientific value

FAIL as claimed — The explicit larger feasible packing defeats the headline jammed-backbone assertion. The approximate graph calculation can be retained as diagnostic data in the archive; a corrected exact-contact or interval-certified packing would require fresh work.

## Prior work and source access

- https://packomania.com/csq/csq.html
- https://packomania.com/csq/txt/csq31.txt

## Scope of the decision

The verdict concerns “Certified jammed backbone for the smallest open equal-circle-in-square case (N = 31)” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
