# Self-review

## Correctness — PASS

The finite fixed-budget simplex and positive loss update are explicitly specified. With dimensionless allocations \(x_i=\tau q u^i\), the entire objective difference from any one-pulse vector is exactly \(R-cQ\). The product inequality \(\prod_{j<i}(1+x_j)\ge1+\sum_{j<i}x_j\) proves the strict bound \(R>Q/(1+S)\) for every split. Exact two-point perturbations prove necessity of the threshold and exclude local minima of earlier pulses. A uniform lower bound near the last pulse establishes its local threshold. A two-value exchange proves sorting. Boundary cases \(c=(1+S)^{-1}\) and \(c=1\), arbitrary \(N\ge2\), nonnegativity and the effort cap are all handled. The packaged exact-rational script passed 14,155 tests; it is a sanity check, not an exhaustive proof.

## Originality — PASS, with residual historical risk

The most directly relevant accessible primary full text, Autran arXiv:2611.20131v1 Section 6, proves two-step concentration only under the stronger sufficient condition \(c<(1+S)^{-2}\), plus a particular spurious-local-minimum example. The new all-horizon sharp boundary \(c\le(1+S)^{-1}\), full two-boundary local pulse phase diagram, and sorting rule are not logical consequences of those stated results. The identified Cacace–Oliviero–Pezzella production–destruction dynamic-programming manuscript was only inspectable at abstract level and remains a source-access risk. Published-record, semantic and searches of accessible mathematical records did not identify a statement that covers the complete theorem; an unsuccessful search does not establish worldwide priority.

## Value — PASS

The natural fixed-effort scheduling question has a sharp, dimensionless, horizon-independent global boundary and a distinct exact metastability boundary. It quantifies where an old-state quadrature creates concentrated global optima or a strict but nonglobal late pulse, while the full removal-flux accounting has different curvature. This materially strengthens the earlier sufficient two-step bound, handles every finite number of steps, and provides a reproducible sorting reduction for nonconvex control allocation. The theorem is deliberately scoped to the numerical quadrature artifact, not to arbitrary ecological models.

## Closest literature and limitations

1. Autran, *Quadrature-Induced Local Minima in Structure-Preserving Lotka–Volterra Control*, https://arxiv.org/html/2611.20131 (Section 6, Propositions 6.2–6.3 and conclusion): same dynamics and costs, different theorem scope and insufficient earlier threshold.
2. Cacace, Oliviero and Pezzella, *Modified Patankar Semi-Lagrangian Scheme for the Optimal Control of Production-Destruction Systems*, https://arxiv.org/abs/2501.13085: framework-level comparator; full text not verified in this review.

No uniqueness assertion is made for mixed-support minimizers, and the non-pulse local-minimum structure remains unresolved. Literature comparison is not an independent priority certificate.

Self-review: passed. Independent audit: not yet performed.
