# Scientific review: four-vertex threshold for nonlinear two-probe trace coupling

## Correctness

**PASS.** The statement holds for every real symmetric matrix in dimensions one through three and for all complete-graph dimensions at least four. The proof distinguishes individual-probe uniformity from independence across probes, explicitly lifts an optimal coupling of scalar responses to valid vector marginals, and establishes the low-dimensional result by the quotient group of sign vectors under global reversal. The complete-graph distribution follows exactly from a binomial count; its Walsh covariance and fixed-mask optimum have exact closed forms. The strict gap for every dimension is established by an algebraically explicit crossed-order pair, rather than by a finite census. The asymptotic result uses weak and second-moment convergence to justify the reflected-quantile integral. A standalone exact checker passed 832 assertions. Its tests verify but cannot replace the general proof. The numerical limiting decimal is not a certified interval.

## Originality

**PASS, with residual precedence risk.** Cortinovis--Kressner's independent-probe Rademacher concentration results, the Hutch++ low-rank sketch, and lattice graph-coloring probing do not imply the fixed-sign-flip optimality theorem in dimensions at most three or assert its sharp failure on every larger complete graph. The classical rearrangement inequality supplies the global scalar coupling principle, so that technique is not claimed as new. The specific minimum dimension, all-dimensional strictness mechanism and binomial-law exact variance frontier were not identified in the inspected literature or targeted mathematical-record searches. A prior specialist presentation of the exact complete-graph classification remains possible, and web abstracts alone do not rule it out. A related five-cycle calculation concerns a different graph family and does not entail the complete-graph or arbitrary three-dimensional results.

## Value

**PASS.** Under two fixed-cost Rademacher matrix-vector probes, a sign-flip pair is a natural low-overhead dependence design. The proof gives a sharp general obstruction to optimality: the first dimension where more flexible coupling helps, a symmetric unweighted witness, an entire infinite complete-graph family, exact finite formulas and the large-dimension limit. It prevents mistaking fixed-mask optimization for full coupling optimization. The result is an exact benchmark, not a claim that computing an optimized coupling is efficient in a black-box trace-estimation task.

## Closest literature and limitations

Cortinovis and Kressner, arXiv:2005.10009 (2020): independent-probe Rademacher trace estimates and tail bounds, including indefinite matrices. Meyer and collaborators, arXiv:2010.09649 (2020): Hutch++ sample complexity through low-rank approximation. Switzer and collaborators, arXiv:2106.01275 (2021): coloring-based probing on matrix-inverse structures. Hardy--Littlewood--Pólya: classical rearrangement inequality and its optimal countermonotone coupling. A related exact five-cycle two-probe calculation does not cover complete graphs or arbitrary matrices in dimensions at most three. The classification is specific to two full-uniform Rademacher marginals and fixed coordinate sign flips versus unconstrained dependence. It does not compare all unbiased query algorithms or provide practical sampling cost bounds.

Self-review: passed. Independent audit: not yet performed.
