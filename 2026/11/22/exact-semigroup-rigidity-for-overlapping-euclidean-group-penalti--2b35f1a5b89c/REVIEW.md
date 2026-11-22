# Scientific review — Exact semigroup rigidity for overlapping Euclidean group penalties

## Correctness — PASS

The positive side is the explicit radial-threshold formula for disjoint blocks, including zero and killed blocks. The negative side is proved for all finite hypergraphs and all positive weights: local implicit-function expansion forces \(H\nabla F=0\) if time-additivity holds; the Hessian is a sum of positive-semidefinite tangent projections; a common-group pair with asymmetric memberships and a single large coordinate forces unequal gradient-to-input ratios and \(\nabla F^{\mathsf T}H\nabla F>0\). The exact three-coordinate witness gives \(Hg=(-1/4,1/2,-1/4)\), and the packaged checker passed 1,044 supplementary assertions. It is an all-finite-family proof; sampling is corroborative only.

## Originality — PASS (qualified)

Liu–Ye (2010), arXiv:1009.0306, Sections 2–3, defines and computes proximal maps of this precise direct group-sum penalty, but the inspected material concerns dual methods and component properties rather than the exact parameter-additivity iff condition. Qi–Li (2022), arXiv:2211.09221, Sections 1–3, motivates separability through non-overlapping approximations, without a semigroup classification. Mairal et al. (2011), Section 2 and proximal algorithms, cover the same underlying structured penalty but different algorithmic claims. Bungert et al. (2019), Theorem 4.5, treats general equivalences between gradient flows and variational minimizers; it offers a conceptual sufficient condition, not the concrete finite-hypergraph iff characterization or forced local defect. Semantic searches of published mathematical records on direct/grouped/overlapping prox semigroups returned no matching assertion; the closest records concern other proximal maps, ordinary \(\ell_p\) norm semigroups, lasso ADMM or unrelated semigroups. Neither lexical search nor indexing proves uniqueness. Unindexed priority and possible implicit consequences of general one-homogeneous flow results remain the main risks.

## Mathematical value — PASS

Iterating a proximal regularizer with step parameters is a natural numerical and variational operation. The classification gives a complete, simple combinatorial condition for exact replacement by a single regularization step, with a constructive strict obstruction for *every* proper overlap and every choice of positive weights. It distinguishes direct overlapping group penalties from non-overlap approximations and from infinite-step gradient-flow convergence, without claiming broader general convexity results.

## Limits and independent status

No claim extends to latent group norms, arbitrary block norms, or nonquadratic fidelity. The small-step coefficient is local and the numerical tests are not proofs. Equivalence may exist in literature not retrieved; independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
