# Scientific review

## Correctness

PASS. The claim is an all-\(n\), all-\(c\) exact variance identity and its third-order phase consequences. The proof uses the exact permutation covariance formula, independent Bernoulli cell jitters, explicit diagonal probabilities, exact row-sum and square-sum formulas, and polynomial collection. The uniform asymptotic follows from the bounded remainder and irrational rotation density; rational cases follow from exact phase cycling. The accompanying standalone verifier passed 733 rational assertions, including independent permutation enumeration. Finite checks do not substitute for the algebraic proof.

## Originality

PASS with specialist historical-priority risk. The 2023 Krumscheid–Pettersson source contains the general variance/covariance structure and its asymptotic LHS projection theory, not the present exact all-offset polynomial, first phase at the third order, or rational-versus-irrational complete limit sets. The 2022 Liu–Owen work addresses conditional pre-integration and randomized QMC, not this exact LHS calculation. Prior work on independent jittered square grids concerns a different sampling design with distinct variance rate and leading-order phase behavior. Neither the basic LHS variance identity nor the leading-order constant alone is asserted as new. Search limitations and older-specialist coverage remain as recorded in the structured audit.

## Value

PASS. Discontinuous halfspaces are a natural benchmark for non-axis-aligned Latin-hypercube sampling. The result separates a stable leading \(n^{-1}\) error budget from a grid-alignment effect that survives at the first nontrivial subleading order, gives exact finite-\(n\) variance rather than an asymptotic approximation, and specifies all possible arithmetic limit values. This permits exact calibration and resolution-comparison tests for a canonical boundary-discontinuous integrand. A paper-sized extension or a downstream general theorem is not required for this complete natural finite-sample invariant.

## Closest literature and limitations

General sampling variance theory and asymptotic LHS projection laws are acknowledged prior art. Finite-offset phase formulas for this sampling method were not found in the inspected material; that is not an assertion of global uniqueness. The proved range is restricted to uniformly randomized two-dimensional Latin hypercubes and a unit-slope straight threshold. No human or independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
