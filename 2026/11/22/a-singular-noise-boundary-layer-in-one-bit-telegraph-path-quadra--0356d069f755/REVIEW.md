# Scientific review

## Correctness — PASS

For a known-start symmetric telegraph chain and one independent symmetric bit flip, the Poisson parity covariance is exact. The conditional mean based on a binary observation is affine, so the covariance risk identity is an equality over **all** measurable estimators. The derivative numerator is strictly convex in the exponentiated observation time and has one interior root; the perfect-detector boundary is separately factored. Noise monotonicity and the rare-/fast-switching asymptotics follow by sign-preserving implicit differentiation and uniform expansions. The bundled checker reproduces the critical identities and supplementary numerical cases; finite grids are not used as an infinite proof.

## Originality — PASS, subject to literature-priority risk

The most relevant primary materials were inspected for mathematical coverage, not title similarity. Bäuerle–Gilitschenski–Hanebeck (2014) explicitly study the integrated telegraph process, but invert the measurement/estimation directions: noisy integrals are observed to filter hidden states, rather than one noisy state bit being observed to infer the integral. Pozdnyakov and colleagues develop occupation-time laws and hidden-state likelihoods, rather than one corrupted-state-bit Bayes quadrature timing. Michel optimizes a long-run interval for *unknown switching-rate inference*, whereas the claim here optimizes one known-rate trajectory's occupation integral. Related published discussions of noisy/Markov sampling likewise address different objectives. Semantic literature searches and comparison with accessible related claims did not produce a theorem that implies the cubic optimizer plus the singular rare-switching boundary layer. This does not certify worldwide novelty; an inaccessible earlier specialization is an acknowledged residual risk.

## Value — PASS

One-bit sensing of accumulated on/off duration is a natural constrained-path integration problem. The result gives a complete global design and its exact Bayes risk, and shows a nonuniform rare-event limit: arbitrarily small *fixed* bit error moves the limiting optimal normalized sampling time from two-thirds to one. The explicit crossover curve makes the precise sensing-noise scale actionable. These are structural facts, not just a finite table or an unsupported numerical improvement.

## Scope and remaining limitations

Exactly one nonadaptive reading; known initial state, symmetric switching, and independent symmetric bit errors are necessary for the stated theorem. No claim is made for asymmetric rates, unknown parameters, repeated observations, or other losses. Reproduction confirms algebra and representative cases but does not provide an independent audit.

Self-review: passed. Independent audit: not yet performed.
