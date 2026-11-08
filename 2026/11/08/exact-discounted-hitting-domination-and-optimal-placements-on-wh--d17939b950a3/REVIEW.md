# Scientific review

**Scope.** Exact discounted first-hitting support and optimal placement on \(W_{n+1}=K_1\vee C_n\), \(n\ge4\), all homogeneous \(0<\lambda<1\) and \(0<\tau\le1\). A single theorem supplies every source-set support floor, all fixed-size optimal source distributions and multiplicities, and the exact threshold minimum.

## Correctness — PASS

The unpinned first-step equations have a unique solution by \(\lambda\)-contraction. Solving their second-order recurrence on a gap with two rim sources gives \(cx+(1-cx)p_{m,j}\); the hub coupling equation gives \(X=\lambda(k+Q)/(n-\lambda c(n-k-Q))\) with a positive denominator. The minimum rim coordinate is at the midpoint of a longest gap. Strict concavity of \(q_m\) proves each unbalanced gap transfer increases worst support when the hub is not selected; with the hub selected the only variable is the largest gap. Rooted cyclic compositions prove the stated exact optimizer multiplicities. These steps prove the whole parameter range, including \(k=1\), \(k=n\), hub-only, and threshold endpoints. A separate direct linear-system implementation corroborated all nonempty source sets on \(n=4,\ldots,8\) for three rational discounts and tested the exact hub-exclusion example. The finite test is not an infinite proof.

## Originality — PASS (qualified)

Allagan, Pereyra and Massey (arXiv:2609.31535v1, 2026-09-25) establish the potential and general theory, a gap formula on degree-two paths, and exact results on spiders and stars; those are prior. Their inspected full manuscript does not classify wheel graphs or solve the hub-dependent cyclic coupled gap optimization. A wheel rim has degree three and, without a selected hub, the hub value is determined endogenously by every gap, so the published degree-two gap formula does not imply the new strict balancing/optimizer-count result. Guo et al. (DOI 10.1109/TKDE.2023.3349164) study group hitting-probability queries and target-set ranking, not the wheel-specific uniform minimum-support floor and complete optimal placements. The closest available mathematical database record treats discounted hitting domination of complete bipartite graphs, a different topology. Other prior work concerns directed cycles or friendship graphs, neither covering the wheel result. Priority against unindexed equivalent work remains a residual risk, not an assertion of absolute uniqueness.

## Value — PASS

Wheels combine the universal-hub temptation with a redundant cyclic network: unlike trees, every gap interacts globally through a potentially unpinned hub. The result replaces an exponential search over source sets by a complete exact \(O(n)\)-candidate formula for all real discount and floor parameters; it characterizes *every* fixed-cardinality optimizer and counts them. The sharp five-vertex example shows two and only two optimum placements, both excluding the unique high-degree hub, illustrating a nontrivial placement effect for a natural family. This is a motivated graph-class solution, not an arbitrary isolated parameter computation.

## Sources and risks

Primary manuscript inspected as full text: Allagan–Pereyra–Massey, arXiv:2609.31535v1, especially model definition, Section 5 gap recurrence, Sections 6–7 spider/star formulas and conclusion. Related group-hitting paper by Guo et al. inspected from its author-hosted full text, including the problem and algorithm sections. Other previous research records were searched by the actual mathematical claim and compared for implication. No exhaustive global literature priority certification is claimed. The exact optimizer-count statement depends on the labelled-vertex counting convention, and the model excludes nonuniform or directed transition kernels.

Self-review: passed. Independent audit: not yet performed.
