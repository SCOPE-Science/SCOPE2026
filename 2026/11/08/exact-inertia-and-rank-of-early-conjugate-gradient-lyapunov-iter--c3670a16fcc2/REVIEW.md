# Review of exact early-iterate inertia

## Correctness

PASS. The result follows from an exact CG polynomial of degree \(k-1\), whose leading sign is \((-1)^{k-1}\), and an anti-triangular Vandermonde factorization of \(q(\lambda_i+\lambda_j)\). Nonbreakdown through the stated range is guaranteed by at least \(2r-1\) active eigenvalue sums. The sum-kernel determinant is nonzero regardless of lower coefficients, and Sylvester's law transfers the resulting signature through full-column-rank congruences. Exact rational tests of the real recurrence and polynomial kernel passed. The finite tests are not used as infinite proof.

## Originality

PASS, with residual historical-priority risk. The September 2026 source derives rank *upper bounds* but not exact positive/negative inertia. The 2020/2021 projection-method literature discusses semidefinite output and possible indefinite corrections, but different algorithms and no universal alternating inertia count. Relevant record searches and available prior claims did not show a stronger covering statement. Hochbruck–Starke (1995) could only be compared at the abstract level; an unindexed equivalent treatment remains a risk.

## Value

PASS. This is a rank-and-inertia classification over every symmetric positive-definite coefficient matrix and every nonzero rank-one right-hand-side factor, with no condition-number restriction. It provides a mathematical reason that unpreconditioned matrix CG, even on a positive-semidefinite Gramian problem, cannot preserve the Gramian cone in intermediate iterations. The exact rank growth also strengthens previously established upper bounds and informs low-rank storage and safeguards.

## Scope and limitations

The classification is restricted to exact, unconstrained, unpreconditioned matrix CG initialized at zero on \(AX+XA=bb^\mathsf T\), and to \(1\le k\le r\), where \(r\) is the active spectral support dimension. It does not give a magnitude of the negative eigenvalues, stability in floating point, or inertia after this range. Comparisons with preconditioned and projected solvers do not transfer directly.

Self-review: passed. Independent audit: not yet performed.
