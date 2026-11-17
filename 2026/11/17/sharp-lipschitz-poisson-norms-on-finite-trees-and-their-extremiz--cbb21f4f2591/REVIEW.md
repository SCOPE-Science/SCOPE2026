# Self-review

## Correctness — PASS

For every cut edge, summing the mean-zero Poisson equation over one shore yields the exact edge-flux identity. Applying the tree Lipschitz inequality gives the cross-cut bound, realized by an explicit signed distance ramp; equality in every positive cross pair proves the complete extremizer classification. Root-distance sums bound each cross-cut sum by half the order times the cut balance and identify paths as the unique maximum. A leaf-edge estimate identifies stars as the unique minimum. A bottom-up/rerooted distance recurrence proves the claimed linear-time computation. Exact rational experiments independently reproduce the formula for all labelled trees through six vertices; the universal statements rest on the proof, not enumeration.

## Originality — PASS (qualified)

Compared to the tree-distance matrix inverse and perturbation results of Bapat--Kirkland--Neumann (2005), Green representations of Chung--Yau (2000), and distance-index extremality of Dankelmann--Entringer (2000) and Székely--Wang (2013), the precise claimed output concerns the Lipschitz norm of the graph-Laplacian pseudoinverse, the maximum **edge-separated** pair-distance sum, all equality fields and an exact linear-time algorithm. Those inspected statements neither assert nor directly imply this operator norm and its classification without the extra cut-flow and sharpness argument. Older equivalent reformulations remain a genuine bibliographic risk.

## Mathematical value — PASS

The result gives a complete sharp stability invariant for discrete Poisson recovery on every finite tree, not a single small instance. Exact operator conditioning can vary between order-one amplification on stars and quadratic-in-order amplification on paths. The extremizer classification identifies precisely which Lipschitz inputs are maximally amplified, while the linear-time formula makes the sharp constant feasible to compute on large trees. The graph-topology-dependent boundary is mathematically motivated by Poisson stability, not by an arbitrary parameter slice.

## Unresolved limits

The evidence does not establish precedence over all historical manuscripts. Weighted networks, cyclic graphs and alternative norms remain outside the theorem. Finite checker tests are diagnostic and cannot establish the universal proof.

Self-review: passed. Independent audit: not yet performed.
