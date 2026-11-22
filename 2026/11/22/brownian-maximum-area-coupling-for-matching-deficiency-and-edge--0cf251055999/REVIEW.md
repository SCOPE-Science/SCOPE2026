# Self-review

## Correctness — PASS

The independent fair creation sequence is the same random graph distribution as the original uniform-weight threshold model. Ross's exact matching characterization is used with its correct parity rounding; the creation-rule edge statistic is exact. Reversing the bits identifies a common symmetric random walk, where the unmatched count differs from its running maximum by at most one and the centered edge count equals minus one-half the sum of partial sums. Donsker's functional invariance principle gives the joint limit. Fourth-moment maximal and weighted-sum bounds ensure convergence of covariance and correlation. Gaussian integration by parts along the Brownian-area Cameron–Martin shift and the arcsine argmax law give the exact constant \(-5/32\). Monotonicity of maximum matching under edge addition gives the strict finite-order sign. All named assumptions and parity conventions are explicit. Exhaustive exact finite tests agree. Risk: numerical tests cannot certify infinite-size statements; those rest on the analytic proof.

## Originality — PASS (qualified)

The closest primary work is Ross (2011), which already determines the *marginal* matching-number distribution by the creation-sequence suffix maximum; Reilly–Scheinerman (2009) give the independent-bit representation and edge statistic; Diaconis–Holmes–Janson give threshold-graph limit theory. These results are credited. The joint maximum–area law under one graph sample and the explicitly calculated \(n^2\)-scale covariance are not among the claims found in those primary texts. Searches also compared related reinforced threshold-graph matching probabilities, edge fluctuation results and greedy split-graph matching results; they do not establish the same joint law. The corresponding earlier conditioned-Hamiltonian random threshold graph result concerns a different probability measure and different invariants. Risk: an unlocated general joint-functional or covariance result might supply the conclusion by a stronger theorem; no exhaustive priority guarantee is made. Merely finding no search hit is not treated as proof of novelty.

## Value — PASS

The question is motivated by a natural pair of competing global resources in the same network: dense edges and feasibility of disjoint pairings. The separate marginals obscure the strong negative dependence, whereas the common-path representation and the exact limiting correlation of roughly \(-0.898\) quantify how edge-rich samples systematically suppress matching deficiency. The result also supplies a non-Gaussian/Gaussian joint benchmark for dense random threshold networks; this is more than a naming exercise, isolated special parameter, or a tiny numerical improvement. Limitation: no generalization beyond the specified uniform model is asserted.

## Closest literature and limits

- E. Perez Reilly and E. R. Scheinerman (2009), DOI 10.37236/219: independent creation model, perfect matching and edge marginal.
- C. Ross (2011), arXiv:1111.7157, Section 4: deterministic maximum-matching tail-excess formula and matching marginal; expressly credited.
- P. Diaconis, S. Holmes and S. Janson (2009 public preprint), arXiv:0908.2448: model and graph-limit setting, not the joint Brownian maximum–area fluctuation.

Self-review: passed. Independent audit: not yet performed.
