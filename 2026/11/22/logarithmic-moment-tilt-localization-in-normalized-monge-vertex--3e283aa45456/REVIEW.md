# Scientific assessment

## Correctness — PASS

The object is the uniform distribution on distinct vertices of the nonnegative, entry-sum-one, nonsymmetric Monge polytope in the Frobenius metric. Erickson and Kretschmann's published Proposition 5.1 provides a complete vertex parametrization. Each normalized rectangle has squared norm \(1/(ab)\) and each complete strip has squared norm \(1/n\); summation gives an exact finite moment identity. A normalized power tilt factorizes into two independent truncated power laws, except for explicitly quantified strip mass. Integral comparison proves the three regimes and the logarithmic critical window. The untilted radial limit and all moment divergences follow with exact constants. The standard-library exact checker verifies the generator list and moments in small dimensions; the asymptotic proof is analytic, not inferred from enumeration.

## Originality — PASS (provisional priority)

The full original vertex-structure paper, *The structure and normalized volume of Monge polytopes* (arXiv:2311.07522, Proposition 5.1), was inspected and is fully credited for the vertex parametrization. Related full published results on two-row Monge uniform-volume sampling, directional mean width, and smallest enclosing sphere, as well as rectangular inball geometry, address different sampling measures or metric questions. Direct literature and mathematical-record searches did not identify a statement establishing the uniform-vertex collision moments, power-biased rectangle localization, or sharp logarithmic crossover. This is not a claim of uniqueness by database partition, and general harmonic-series identities are not new. The older Rudolf–Woeginger extreme-ray article and the newer Erickson–Jones Monge-volume paper were not both available in full, leaving a residual equivalence risk.

## Mathematical value — PASS

The statistic \(\sum c_{ij}^2\) is a canonical Euclidean norm and the exact collision probability for two independent draws from the vertex's categorical cost array. Tilting by its powers is therefore the natural conditional law after independent collision observations, rather than an arbitrary artificial weighting. The theorem finds a complete infinite-family moment spectrum, an infinite-mean limiting radial law, and a previously unrecorded change between macroscopic and localized extreme cost patterns at the collision tilt \(s=1\), including the finite-size logarithmic crossover distribution. It explains why a typical vertex and an average collision probability have parametrically different scales.

## Scope, antecedents, and limitations

The work covers square nonsymmetric polytopes with entry-sum normalization and Frobenius metric. The complete vertex list is old and explicitly attributed. The 1995 extreme-ray text was not inspected in full; the September 2026 lattice-path paper was compared at abstract level. Exact finite checks support but cannot prove asymptotic limits. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
