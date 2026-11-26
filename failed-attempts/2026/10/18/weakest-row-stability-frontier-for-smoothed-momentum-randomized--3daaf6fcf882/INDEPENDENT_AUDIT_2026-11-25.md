# Independent mathematical audit

## correctness

PASS

For each coordinate the two state matrices use the Bernoulli indicator of that coordinate only; independence across coordinates is unnecessary for the expected squared norm. On symmetric matrices the resulting covariance map has the displayed three-dimensional matrix Q and preserves the PSD cone, so its spectral radius is a nonnegative real eigenvalue. At M=0 it is strictly below one. Direct expansion of det(I-Q) gives p(1-beta)F, and the quadratic has one positive zero. Continuity plus the absence of eigenvalue 1 gives subcritical stability; at the root the radius is one by continuity and singularity of I-Q. Above the root det(I-Q)<0, so the real monic characteristic polynomial has a zero >1, completing the sign argument implicit in the frozen proof. For a nonzero initial coordinate and zero velocity the time-one second-moment matrix is positive definite and dominates a positive multiple of a PSD Perron eigenmatrix. This eigenmatrix has positive error diagonal for M>0, which proves a positive lower bound at equality and exponential growth above it in that coordinate. Differentiation in p yields the weakest-row criterion, and substituting p=0 and M=1 respectively verifies the limiting root and the strict smoothing threshold. The signed-mean 2x2 Jury test is independent of this classification. Nondecay refers to not tending to zero, not monotonicity or a pathwise assertion. The frozen symbolic/path checks were read, not run, and are not needed for the all-parameter proof.

## originality

FAIL

The earlier, distinct Resultary record e894b5e60aeb states the same arbitrary-diagonal mean-square frontier for the same update, initial velocity, and parameter ranges, including failure at equality and growth above the threshold. The present polynomial is exactly the negative of its defining quadratic. The least-probability wording and two limiting formulas follow from that previously stated arbitrary-probability frontier. The equal-probability special case cited in the frozen record is not the strongest available coverage.

## value

FAIL

The sharp arbitrary-diagonal stability classification is scientifically motivated, but is already available, including the boundary behavior. The submitted remainder is a monotone reformulation of the same condition and two direct one-parameter evaluations of the existing quadratic, not an independently useful new classification in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
