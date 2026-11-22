# Scientific review: primitive three-orbit uncertainty split

## Correctness — PASS

The claim is the restricted three-orbit minimization theorem, not the general Gaussian-conditioning formula. The conditional covariance equals the inverse principal precision compression. Its Dirichlet path blocks give exact A, D and E formulas; the arithmetic condition forces admissible steps immediately on either side of the excluded balanced step. Strict positive and decreasing second derivatives settle A and logarithmic D uniquely at the left step; the longest-gap formula settles E uniquely at the right step. The small-mass expansion is derived at fixed cycle size. Numerical tests of direct block inversion and high-precision primitive-step enumeration agree with the analytical theorem; their finite scope is explicit.

## Originality — PASS, qualified

The closest known pinned-cycle theorem already supplies unrestricted optimality and the trace-inverse path formula; the present statement would not pass if it merely repeated these. It instead establishes *opposite restricted optimal generators* for A/D versus E under full-orbit observability, requiring a strict third-derivative comparison absent from the unrestricted claim. Giribet–Feldberg establish general Gaussian residual conditioning and a nominal-visibility distinction without this arithmetic design result. Classical Ornstein–Uhlenbeck designs establish free equispacing, not constrained primitive generators. Published-record and relevant literature searches found no matching result under equivalent formulations. A wider undiscovered optimal-design theorem remains a bibliographic risk.

## Mathematical value — PASS

The orbit generator is a structural constraint: it is exactly what makes one spatial sensor fully observable through time. Unrestricted free-spaced optimizers cannot respect that requirement when the size is divisible by nine. Even more strongly, no single primitive generator simultaneously optimizes average, generalized-volume and worst-direction forcing uncertainty. The theorem determines all three restricted optimizer classes (each unique up to reflection) and sharp costs for an infinite family, with a singular massless limit that makes the strict left/right trace preference disappear. This is a motivated exact design obstruction, not an arbitrary small-size calculation.

## Limits and literature

Applicable only to equally weighted cycles, three noiseless orbit samples, cycles divisible by nine and positive precision mass. It makes no claim for arbitrary sensor budgets, nonprimitive shifts, nontrivial observational noise, heterogeneous precision or complete forced-state error. Free-placement results and standard Gaussian formulas are explicitly credited. Independent bibliographic and mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
