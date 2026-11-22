# Scientific review

## Correctness — PASS

The attachment probabilities \(D_{v,n}/[2(n-1)]\) and \(L_{v,n}/[2(n-1)]\) are disjoint, and the third probability is nonnegative on all attainable states. Their centered-increment drift is \(-A_{v,n}/[2(n-1)]\). Exact rational computation from the enclosed checker independently agrees with the full-tree histories through eight vertices. The second-moment recurrence gives \(\mathbb E A_{v,n}^2=O(\sqrt n)\), supporting both the deterministic approximation \(L_{v,n}\sim D_{v,n}/2\) and the negligible bracket corrections. Standard exponential Yule martingales prove \(D_{v,n}/\sqrt n\to W_v>0\). Gamma products determine the centering martingale weights. The diagonal bracket has the exact leading coefficient \(W_v/(4c_v^2)\); distinct nonleaf marked vertices have no simultaneous centered raw increments, so their cross-brackets vanish. The Lindeberg bound follows from jumps of order \(\sqrt n/n^{3/4}\). Stable multivariate martingale convergence and degree studentization yield the stated independent \(\mathcal N(0,1/4)\) laws. The proof's asymptotic component is analytical; finite checks alone do not establish it.

## Originality — PASS under examined evidence

Hartle and Krapivsky, arXiv:2602.01021v1, Sections II, III.5 and IV, identify limiting empirical degree–leafdegree counts, mean/variance of leafdegree of a *random degree-conditioned vertex*, and global class-count fluctuations. These statements neither condition on a fixed old birth label nor give a mixed-normal \(n^{1/4}\)-scale limit for several such labels. The published *Uniform half-degree law* gives an \(O_{\mathbb P}(n^{1/4}(\log n)^2)\) simultaneous deviation upper bound but not the sharp joint Gaussian limit. Other prior results on old-hub degree versus *global* leaf count and on affine attachment degree-count CLTs do not have these marked local variables. Search and implication checks did not locate coverage. Residual risk: full text of a closely relevant published uniform concentration result was inaccessible; an unpublished or unindexed general marked-martingale theorem could subsume the claim.

## Value — PASS

This determines the previously unquantified *second-order, joint, age-marked* boundary fluctuations of natural highly connected vertices. Empirical degree-conditioned distributions cannot replace such a theorem, because old hubs have nondegenerate, dependent random growth amplitudes; the result establishes a universal normal fluctuation law after observable-degree studentization and proves the disappearance of cross-hub Gaussian noise dependence. The result has a structurally motivated \(n^{1/4}\) fluctuation scale and explicit variance, not an arbitrarily chosen parameter slice.

## Checked literature and limits

The motivating paper was inspected in its lawful arXiv HTML text, including the formulas for degree-stratified leaf moments and the finite-degree aggregate fluctuations. Public published summaries of the uniform half-degree law and root-degree/global-leaf covariances were compared by exact statement and implication; raw complete content for the former could not be fetched. An additional search for marked-vertex and leaf-neighbor Gaussian theorems found no exact match; absence of a match is not a uniqueness proof. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
