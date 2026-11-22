# Scientific review — heterogeneous convex slope-box regression

## Correctness — PASS

The claim specifies finite open paths, arbitrary finite lower/upper edge bounds, strictly convex translation-invariant separable site losses, and adjacent total variation of **two-input differences**. Every solution equals a member of finitely many unconstrained block-minimizer branches; stationarity on maximal active-edge blocks is legitimate because interblock constraints are slack. The derivative of each smooth branch is a positive normalized averaging map on consecutive blocks. A signed step decomposition proves variation contraction for every such derivative, and continuous finite selection transfers this bound to the regression. Feasible input-pair witnesses attain coefficient one when a free edge exists; complete fixation forces coefficient zero. Uniform-on-compacts approximation with strictly convex power objectives covers independent \(p_i>1\). Exact rational branch tests and finite nonlinear optimization checks corroborate but do not replace these proofs.

## Originality — PASS (qualified)

Yeganova–Wilbur (2009) and Agarwal–Phillips–Sadri (2009) focus on **quadratic** bounded-slope fitting and algorithms. Luss–Rosset (2011) permit arbitrary convex losses under isotonic inequalities, but their inspected original proofs address the regression solution algorithm and do not establish any two-input path-variation estimate for nonlinear residual objectives with two-sided slope boxes. Yang–Barber (2017) treat the Euclidean isotonic projector, with a general seminorm-contraction criterion; the unweighted quadratic isotonic special case is known and is excluded from claims of originality. Closest published sharp weighted-isotonic variation work covers quadratic loss, not heterogeneous nonlinear Hessians. Distinctness follows from the extra nonlinear and slope-constrained quantifiers, not merely unfamiliar wording. Possible equivalent older results under nonlinear pool-adjacent-violators or monotone-operator terminology remain a priority risk.

## Mathematical value — PASS

The theorem answers whether replacing squared loss by heterogeneous robust nonquadratic losses can destroy the sharp two-input bounded-variation guarantee of path regression, even with spatially varying lower/upper slope limits and fixed edges. The answer is universally negative, with a sharp dichotomy and a reusable consecutive-block positivity mechanism. The result is structurally relevant to robustness of constrained local shape fitting, and not merely another numerical small-instance constant. No extension to branching graphs or nonsmooth non-strict losses is asserted.

Self-review: passed. Independent audit: not yet performed.
