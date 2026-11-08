# Self-review

## Correctness — PASS

The two-layer model reduces exactly to choosing an \(r\)-subset of rows uniformly, and the collision count becomes a quadratic codegree sum. The zero-row-sum identity for centered codegrees yields the exact ordered-edge overlap sums \(H,-2H,H\), hence the finite-population coefficient \((r)_2/(d)_2-2(r)_3/(d)_3+(r)_4/(d)_4\). Algebra factors this as a strictly positive coefficient for all \(d\ge4\), \(2\le r\le d-2\). Constant codegree is exactly the block-intersection condition for a symmetric design. The 7-vertex examples have the same mean and variances \(0\) and \(6/5\). Exact rational enumeration over 1,548 finite matrix/subset cases checks implementation of these identities, but does not substitute for the all-order algebra.

## Originality — PASS (provisional)

Full-text inspection of Chiclana, arXiv:2610.14724, including the model setup, Section 3.2, covariance identities and discussion of path occupancy, found generating-function variance inequalities and second-order expectations but not the stated exact collision-variance formula, its four-cycle specialization, or design rigidity. The model-specific statement is not implied by a numerical or first-order expectation bound alone. Classical symmetric-design texts define the equality condition, and Hoeffding-type finite-population quadratic-statistic theory supplies a possible general identity; novelty therefore rests in the exact graph-model specialization and structural characterization, not an assertion that the underlying sampling-variance algebra is unprecedented. Targeted public and mathematical-record searches found no direct matching assertion. Historical priority is not fully established.

## Value — PASS

This identifies the first geometry-sensitive *sample-to-sample* dispersion of a natural occupancy statistic in a permutation-mixed regular path model whose first collision moment is geometry-independent. The exact correspondence with bipartite four-cycles, a symmetric-design rigidity criterion, and an explicit same-order same-degree separation provide intrinsic structural content beyond a generic small finite calculation. The result makes no claim about arbitrary-length paths.

## Closest literature and residual limits

Rafael Chiclana, *Poisson occupancy of paths on permuted regular graphs* (2026), arXiv:2610.14724, Section 3.2; Eric S. Lander, *Symmetric Designs* (1983), Chapter 1; W. Hoeffding (1948), general U-statistics. A prior algebraic specialization under another name, particularly in finite-population sampling theory, cannot be ruled out by the searches performed. The code tests finitely many matrices only. Independent scrutiny remains outstanding.

Self-review: passed. Independent audit: not yet performed.
