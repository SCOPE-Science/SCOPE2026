# Scientific review

## Correctness — PASS

The theorem compares a genuinely two-input vertex-\(\ell^2\)-to-edge-\(\ell^2\) norm. The three graph-ball scales are explicitly normalized as \(1\), \(2^{\alpha-1}\), \(3^{\alpha-1}\). Every hub/leaf branch tuple falls into one of eight remaining types or is analytically ruled out by strict concavity, subadditivity, and singleton constraints. The top two-row Gram eigenvalue is computed exactly on the exceptional feasible cell; all other feasible cells have squared norm at most \(2-4h+6h^2\). Explicit open positive cells attain both norms. Crossing tie surfaces does not invalidate the global upper bound because the maximal map is continuous and piecewise linear. Complex inputs reduce to their coordinatewise moduli. The checker ran on the actual standalone source and passed 110,000 randomized comparisons plus 11 strict positive witnesses; tests are auxiliary to the analytic argument.

## Originality — PASS relative to inspected evidence

The motivating 2026-11-11 paper by Liu–Lian–Wang proves sharp *one-input* fractional variation laws. The 2026-03-12 González-Riquelme–Kovač–Madrid paper also treats one-input ordinary maximal variation, including small graphs. The two Lu–Zhao manuscripts first public on 2026-11-18 and inspected in their available PDF form likewise state one-input estimates. Published two-input ordinary maximal star work covers the zero-exponent situation but not the fractional exponent family; general fractional star asymptotic bounds do not identify this three-vertex threshold. A complete-graph fractional perturbation law has a different ball geometry and does not cover the three-vertex path. The claim is not obtained by replacing an input with a difference inside a nonlinear maximal operator. No matching exact two-input fractional path theorem was identified in the actual indexed searches. Residual risk: an unindexed or differently formulated general theorem could imply the formula; bibliographic search alone is not proof of uniqueness.

## Value — PASS

The result solves the natural smallest noncomplete-path test case for sensitivity of a fractional maximal map under Euclidean measurement perturbations. Its primary contribution is not a numerical constant: the optimal global modulus **jumps at an interior fractional exponent** as one strictly feasible selection cell collapses, despite continuous dependence of each fixed-input maximal output. The threshold, its sharp one-sided constants, and exact positive attainability give a substantive boundary phenomenon for nonlinear averaging and clarify why one-input variation estimates do not control nonlinear perturbation stability.

## Limitations and closest literature

The theorem covers the unweighted three-vertex path, every \(0<\alpha<1\), and complex two-input vertex-\(\ell^2\) to edge-\(\ell^2\) differences only. It neither classifies all extremizer pairs nor resolves larger paths or arbitrary weighted graphs. Closest full-text works inspected are Liu–Lian–Wang (arXiv:2611.15377v1), González-Riquelme–Kovač–Madrid (arXiv:2603.12462v1), and Lu–Zhao (arXiv:2611.24189v1 and arXiv:2611.24180v1). Historical-priority assessment remains provisional pending independent bibliographic review.

Self-review: passed. Independent audit: not yet performed.
