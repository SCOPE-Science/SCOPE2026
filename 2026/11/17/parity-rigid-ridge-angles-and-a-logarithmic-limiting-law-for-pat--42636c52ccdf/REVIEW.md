# Review of the path-edge simplex angle law

## Correctness — PASS

The claim uses the original unit-weight unsigned incidence vectors and intrinsic metric in their affine hull. Its all-dimensional proof reduces the ambient facet gradients to \(H=G^{-1}-bb^{\mathsf T}/t\), derives the exact inverse of a tridiagonal Dirichlet operator, checks each sign class including the sole odd-order endpoint zero, and proves the limit by parity-split Riemann sums and a two-dimensional integral. The included standalone checker independently reconstructs exact affine facet-gradient Grams and verifies 559 ridge pairs in dimensions indexed by \(3\le m\le15\); finite checks are corroboration and are not used to establish the limit theorem.

## Originality — PASS (provisional historical priority)

The 2013/2014 Tran–Ziegler edge-polytope study establishes the graph-incidence realization and notes tree-edge simplices, but its theorems on face structure do not calculate the Euclidean facet-angle Gram matrix. Nagaoka–Tsuchiya's 2017 preprint likewise concerns reflexive embeddings and normality of edge polytopes. Classical inverse-tridiagonal identities are known; the complete indexed angle spectrum and nonuniform signed logarithmic asymptotic law are the compared new claims, not their algebraic ingredients. The closest published odd-cycle edge-simplex result yields a *uniform* cosine law; removing the cyclic edge changes the affine geometry and yields a different limit, so its statement does not imply this theorem. Additional published searches for ordinary path incidence simplices, root/Laplacian ambiguities, angle distributions and broader simplex theory showed no covering implication. Unindexed or differently named earlier work remains a residual risk.

## Mathematical value — PASS

The result gives the entire Euclidean ridge-angle array for a canonical infinite family of graph-edge polytopes, a sharp parity-dependent right-angle classification, and a nontrivial closed probability law for uniformly sampled angles. This distinguishes the path from the neighboring odd-cycle simplex despite each being combinatorially a simplex and explains the geometric dependence on the graph's Dirichlet Green kernel. The limit is a motivated natural geometric statistic, not an arbitrary finite parameter slice.

## Scientific limitations

The result is specific to ordinary unsigned unit-weight path incidence vectors in the inherited metric. No area-weighted ridge distribution, other trees, weighted graph family, or convergence rate is established. The literature comparisons support best-knowledge priority, not a proof of absence in all published sources.

Self-review: passed. Independent audit: not yet performed.
