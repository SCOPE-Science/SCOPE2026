# Independent mathematical audit

## correctness

PASS

On the probability space (c0, μ), invariance gives P_n X_n = (B_w^n X)_0 with law X_0. Bounded products on an infinite subsequence and sample-wise coordinate decay make that common law a point mass at zero, by convergence in distribution. Nonvanishing products and a countable intersection then make the entire vector zero. The fixed-vector recursion forces x_n=x_0/P_n, giving exactly the claimed divergence condition. When products diverge, the product-disk coding is uniformly approximated by its coordinate truncations, hence continuous into the supremum norm and injective with compact image; the exact intertwining carries iid shift invariance and mixing to that image. Finite-coordinate event approximation in probability extends block independence to all Borel events. Nonatomicity follows from the zeroth marginal. The topological mixing criterion also follows by hitting finite-support targets from finite-support inputs with a tail correction y_j P_j/P_{n+j}; conversely hitting an open neighborhood with zeroth coordinate bounded away from zero from arbitrarily small norm balls forces |P_n|→∞. These arguments apply to real and complex scalars without a lower bound on individual weights. The nested frozen checks/verify_examples.py was inspected, not executed; it tests prefix algebra, not invariant-law necessity.

## originality

PASS

The genuinely distinct direction is necessity for arbitrary invariant Borel probabilities, answering the stated c0 equivalence question. Fixed-point sufficiency and the topological mixing criterion are not themselves new; the explicit compact Bernoulli model gives stronger sufficiency at the sharp threshold.

## value

PASS

The result resolves a precise stated c0 existence question. It separates hypercyclicity from stationary-law existence (e.g. the bounded weights with product spikes and returns to one), classifies when δ0 is the only invariant probability, and exhibits compact nonatomic mixing laws wherever the sharp condition holds. It makes no full-support claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
