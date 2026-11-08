# Scientific review: Complete directed flow inballs

## Correctness — PASS

For every \(n\geq3\) and real zero-sum netflow with strictly positive proper prefix sums, the claim uses precisely the affine edge-coordinate Euclidean metric. The full incidence rank, all-positive feasibility construction, and complete-graph Laplacian yield a common coordinate-normal projection length \(\sqrt{(n-2)/n}\). Every feasible flow satisfies the cut bound \(\min_e x_e\leq\min_k\beta_k/[k(n-k)]\); an explicit constant-plus-adjacent-edge flow attains it. Vanishing residual cut sums force exactly the edges across all minimizing cuts to zero. Strict residual prefix positivity gives full-dimensional product factors and the stated center-locus dimension. The unit-source/unit-sink parity formulas follow by maximizing the quadratic cut capacity. The standalone rational/LP/SVD checker passed 63 general instances and additional parity checks. The computation is only corroboration, not the proof.

## Originality — PASS, with priority risk

The strongest inspected same-object sources are Corteel–Kim–Mészáros, *Flow polytopes with Catalan volumes* (arXiv:1612.00102), Dugan, *On the f-vectors of flow polytopes for the complete graph* (arXiv:2409.15519), and Lee–Liu, *Deformation cones of Tesler polytopes* (arXiv:2212.11423). Their results concern normalized volume, face enumeration, and deformation/normal-fan structure, respectively; none states a sharp intrinsic Euclidean inradius with a complete product classification of incenters. Mészáros–Morales–Rhoades (arXiv:1409.8566) supplies the earlier flow/Tesler correspondence and face theory, not this metric theorem. The broad general inradius theorem for transportation polytopes does not imply this result for a lower-dimensional flow face, and an inradius theorem for graphical zonotopes involves a different Minkowski-sum body. Exact or equivalent formulations may exist in classical lower-bounded network-flow, max-min fairness, or Chebyshev-center literature; searchable evidence does not rule this out. No independent literature-priority audit has occurred.

## Mathematical value — PASS

The Chan–Robbins–Yuen family is a standard high-dimensional polytope with established enumerative and volume theory. The present result computes its previously unverified edge-metric radius exactly, including the sharp \(4/n^2\) scaling; more importantly, it characterizes every maximizing center and shows that optimal balls have a center set of asymptotically half the polytope's dimension. The general theorem gives an exact geometry/flow bridge and a stratification by bottleneck cuts for arbitrary positive-prefix real netflows, not an arbitrary parameter specialization. These invariants offer a useful metric contrast to the established volume/face/deformation results. It does not claim a general theorem for other graphs or alternative embeddings.

## Limitations and related literature

The edge-coordinate metric is essential: the Birkhoff-face incarnation of Chan–Robbins–Yuen is not asserted to be Euclidean isometric. The vanishing-prefix case is excluded, and the existing generic feasibility principle for network lower bounds is not claimed new. A possible older equivalent presentation under fair-flow optimization terminology is the principal residual risk. Independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
