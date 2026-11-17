# Scientific review: three-site Shepard bounded-variation stability

## Correctness — PASS

The exact domain is the real triple of sampled values, three arbitrary strictly ordered real sites, and any real positive inverse-distance exponent. The interpolant is the continuous nodal extension of normalized inverse-power weights, restricted to the outer-node interval. The proof reduces the seminorm to its two extremal unit jumps, derives the unique off-cell maximum of each distant-node weight, and computes its variation exactly. Strict monotonicity in the shorter-to-longer gap ratio yields the unique equispaced minimizer. The high-power/short-gap logistic limit is derived from controlled asymptotics, including the zero and infinite scaling endpoints. Equality for every positive parameter pair is realized by a specified step triple. A derivative-free standard-library checker corroborated the closed form on 220 sampled parameter triples and tested the limiting regimes; the proof, not the tests, covers all parameters.

## Originality — PASS, qualified

Shepard's original inverse-distance construction specifies the normalized positive interpolant and describes how the exponent shapes interpolation, but does not present a sharp output-total-variation norm in the inspected original-method sections. The closest published shape-preservation literature on Shepard operators discusses local monotonicity, convexity, and global smoothness rather than the identical three-node mesh-dependent BV seminorm and the coupled singular mesh–power limit. The later Shepard–Gupta work concerns a modified operator and convergence estimates. A public mathematical-results search for inverse-distance three-node sharp variation, parameter aliases, coalescing knots, step responses and mesh-power limits found related spline and compact multinode variants but no matching theorem by implication. This does not establish exhaustive historical uniqueness. The 2005 monograph's directly relevant univariate chapters could only be inspected at publisher-preview level; they present a material unresolved priority risk, not a contradiction or established stronger coverage.

## Mathematical value — PASS

Inverse-distance weighting is a standard positive, range-preserving scattered-data interpolant, so its variation amplification is a natural signal-stability quantity independent of its uniform error estimates. The theorem exactly solves the smallest multi-cell case across **all** positive exponents and mesh ratios and characterizes both the unique optimal spacing and loss of uniform stability under knot collision. Its logistic boundary layer identifies the critical joint scale of power and mesh contrast, showing why high-power tuning and mesh refinement cannot be interchanged. The exact coefficient and optimizing data can serve as a benchmark for modifying weight locality or preventing close-site instability. No assertion is made for more than three sites or multivariate schemes.

## Closest prior literature and limits

- D. Shepard, 1968, https://doi.org/10.1145/800186.810616 — inspected original inverse-distance weighted-average construction and parameter discussion; does not include this BV calculation in inspected sections.
- G. A. Anastassiou and S. G. Gal, 2001, https://doi.org/10.1016/S0898-1221(01)00129-8 — inspected title and abstract only; bivariate local shape preservation is different from the exact full-interval three-site BV norm.
- S. G. Gal, 2005, https://doi.org/10.1007/b137115 and chapter https://doi.org/10.1007/0-8176-4401-6_2 — inspected publisher overview, contents and chapter preview only; a plausible directly relevant historical comparison remains incomplete.
- U. Amato and B. Della Vecchia, 2018, https://doi.org/10.1186/s13660-018-1823-7 — inspected public abstract/introduction summary; a different Shepard–Gupta approximation and convergence result.

All correctness, originality, and value assessments are for the one theorem stated in `RESULT.md`. This is a mathematical self-review, not an independent priority or proof certification.

Self-review: passed. Independent audit: not yet performed.
