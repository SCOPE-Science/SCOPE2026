# Scientific review

## Correctness — PASS

The claim is confined to fixed, finite, positive rank-one kernels and fixed graph surplus. The symmetric kernel \(u\otimes u/\alpha\) has Perron root one under \(\mathbb E u=1\). The scalar reduction to the analytic critical pair is obtained directly from the rooted-tree equation and its Perron derivative condition; the inverse is legitimate because the derivative is \(-\beta/\alpha\ne0\). Exact formal-series algebra, including the fifth-moment cancellation, yields the cubic coefficient, and the two-type quartic and its two roots have exact polynomial proofs. The moderate-tilt limit depends on the uniform shrinking-neighborhood version of Hu--Sun's Theorem 3.6, not on simulation. A standalone symbolic and finite graph checker passes all its checks. Risk: any change in the source's edge-tilt gauge, surplus normalization, or uniformity domain would change the conclusion; the matching conventions are given explicitly in RESULT.md.

## Originality — PASS (provisional historical priority)

Hu--Sun (arXiv:2610.23003v1), read in its theorem, critical-pair proof, and field-tilt argument, proves the quadratic radius coefficient and leaves the cubic coefficient in its \(O(|t-1|^3)\) remainder. Its general shrinking-tilt enumeration already makes a moderate-scale consequence possible, so **that theorem is credited as a necessary input**, not claimed anew. The distinct calculation is the explicit rank-one cubic coefficient, its fourth-moment dependence, and the two sign reversals in a concrete positive two-type family. Bhamidi--Sen--Wang's rank-one scaling-limit treatment and Bollobás--Janson--Riordan's phase-transition theory address broader graphs but do not visibly state this coefficient. Published-record and semantic research-index comparisons found no dominating match. Searches cannot prove priority, and additional uninspected saddlepoint literature could contain equivalent formulas.

## Mathematical value — PASS

For large connected components, the established quadratic response alone does not determine finite, nonsymmetric corrections when the edge-intensity tilt is of order \(k^{-1/3}\). The new cubic coefficient supplies that finite factor and reveals a change of sign **twice** within a single natural two-type family. This demonstrates that neither a universal skew sign nor the leading Perron moments alone capture the first asymmetric correction. The result is a motivated structural refinement of the Perron--Wright enumerator, not a relabelling of a finite table or a claim about an ambient random-graph fluctuation law.

## Closest literature and limits

The precise comparison is with Hu and Sun (2026), Theorem 3.6 and its proof, especially the analytic critical pair and the uniform error bound. Classical rank-one random-graph work provides background rather than the asserted moment-explicit moderate-tilt coefficient. The result assumes strictly positive finite types and fixed surplus, imports the source's asymptotic theorem, and does not establish historical uniqueness, general finite-rank extension, or independent validation.

Self-review: passed. Independent audit: not yet performed.
