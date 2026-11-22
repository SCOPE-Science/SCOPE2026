# Scientific review

**Correctness — PASS.** The claim is fully quantified for integers \(n\ge4\) and real \(r,B>0\). The proof establishes existence and injective strict convexity among all individual edge weights, derives the exact three-class grounded-free Laplacian spectrum, solves the interior and one-sided KKT equations, checks positive weights and the boundary, and obtains the minimum by homogeneity. The packaged `verify.py` passed 908 parameter sets spanning matrix reconstruction, exact checks, KKT identities and price ordering. The finite checks support, but do not replace, the analytic all-size proof.

**Originality — PASS on inspected evidence.** The closest same-network published D-optimal and E-optimal results, examined in full, have distinct objectives and thresholds; their statements do not entail the present inverse-trace optimum. The earlier matching-priced resistance result concerns a different number of costly links. Ghosh–Boyd–Saberi (2006/2008) supplies the general optimization method and equal-price complete-graph case, not the claimed expensive-single-edge classification. The more recent power-law-cost work supplies general first-order conditions, not the closed form. Equivalent unindexed or inaccessible work remains a publication-priority risk.

**Value — PASS.** The exact threshold and full unique conductor allocation solve a natural, economically interpretable A-optimal network-design problem; more importantly, matching it to established D- and E-optimal thresholds gives two distinct disagreement scales, including an exact unit-width A/E interval that persists with network size. This is not an arbitrary finite numerical slice or a routine restatement of the generic KKT recipe.

**Limits.** No extension is proved for arbitrary price vectors, multiple marked edges or nonlinear cost. Historical literature discovery cannot guarantee absolute novelty. Formal independent validation is outside this record.

Self-review: passed. Independent audit: not yet performed.
