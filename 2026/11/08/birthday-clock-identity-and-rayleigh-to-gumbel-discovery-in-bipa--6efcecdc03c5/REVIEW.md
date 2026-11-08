# Review of the birthday-clock discovery theorem

## Correctness — PASS

The construction identifies the actual non-lazy sequential-IDLA walk on a bipartite graph with independent uniform \(B\) draws, followed by independent uniform \(A\) draws exactly when a \(B\) draw repeats. Crucially, a visit to a new \(A\) vertex ends one particle but does not alter the uniformity of the next \(B\) draw from the rooted restart. Independent geometric failure blocks yield the product PGF, with the correct \(j+1\) offset for discovery during an occupied-\(B\) plateau. Inclusion-exclusion proves the finite CDF; Poisson marking with explicit coupling error proves the fixed-class vector limit; an exponential union bound proves convergence of the means. A geometric-clock variance calculation combined with ordinary coupon collection proves the growing-class Gumbel regime under the stated small-ratio hypothesis. The standalone exact-arithmetic recurrence check passed 1516 assertions over \(2\le a\le8\) and \(1\le b\le16\). These finite tests support but do not replace the infinite proofs.

## Originality — PASS, with residual uncertainty

The finite-graph sequential-IDLA model is defined in Rivera et al. (arXiv:1808.09219), whose accessible 39-page preprint discusses dispersion statistics and several graph classes but does not give the two-stream law, exact complete-bipartite class-completion distribution or Rayleigh/Gumbel regimes. Mittelstaedt (arXiv:1902.03195) treats one-dimensional IDLA on integers and Eulerian occupation counts. Falgas-Ravry, Larsson and Markström (arXiv:1601.04455) study general iid coupon collectors and contain the classical Erdős–Rényi coupon-cover limit, which covers the coupon portion *after* the new bipartite walk-clock reduction; it does not provide that clock or its exact graph law. Searches also compared the result against accessible research records on complete-bipartite random-walk cover time and bipartite broadcasting. No inspected statement directly implies the full graph-specific result. An unlocated equivalent historical derivation remains possible; literature searches do not certify priority.

## Value — PASS

The object is a canonical finite-graph IDLA growth process, and the invariant is the first time the source-side class becomes completely occupied, measured by the number of opposite-class vertices discovered. The exact law exposes a previously unquantified two-stage collision mechanism and yields a full joint discovery-time limit rather than a single expectation. The fixed-small-class maximum-Rayleigh and growing-class Gumbel distributions distinguish two physically different coverage regimes. The precise count-vector coupling bound and exact finite CDF support reproducibility and future refinements to wider growth windows. This is not a reparameterization of walk cover time, since different particles settle irreversibly and the observable concerns occupancy order.

## Risks and limits

The growing-class theorem is established only when \(a(\log a)^3=o(b)\), not throughout the full unbalanced regime. The asymptotic Poisson count approximation concerns a fixed scaled \(B\)-discovery horizon and does not assert continuous-limit total-variation convergence of discrete discovery times. The formula is specific to non-lazy sequential IDLA started from the \(A\) class, and does not describe parallel dispersion time. Historical priority and independent mathematical validation are unconfirmed.

Self-review: passed. Independent audit: not yet performed.
