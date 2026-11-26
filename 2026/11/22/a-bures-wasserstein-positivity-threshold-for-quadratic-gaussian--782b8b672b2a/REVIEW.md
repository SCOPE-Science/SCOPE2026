# Independent mathematical audit

## correctness

PASS

The undamped kernel is the real coherent matrix element of I+(H−tr(A+D)I)/b with H=QᵀAQ+PᵀDP and [Q_j,P_k]=2iδ_jk. Normal ordering gives the trace terms with positive signs and the relative-coordinate quadratic with a negative sign. Point-mass approximation and graph-norm finite differences at x=0 transfer positivity in both directions between the continuous kernel and the finite-particle form; the latter is continuous in the (N+I)^{1/2} norm. More explicitly, the damped coherent integral map B and (N+I)B are Hilbert–Schmidt by the Poisson second moment times exp(−(2s−b)|x|²); S is bounded relative to N+I, so T=B*SB is trace class. Position and momentum translations of a fixed Gaussian isolate negative directions of A or D, with number-basis cutoffs converging in the weighted norm. Positive definite A is removed from the position term by a canonical change of variables with inverse transpose on momentum; orthogonal diagonalization gives 2Σ√λ for the exact lower energy. Squeezed Gaussian trial states attain that bound in the form domain. For singular matrices the variational infima of the ε-regularizations decrease to the limiting infimum by testing each fixed finite vector, and the square-root trace is continuous. This proves the boundary including equality, noncommutation and singularity. Scalar expansion gives b=D=1 and (√γ−1)²≤1 after γ≥0. For the matrix example the middle matrix has trace 25/2 and determinant 16, giving the stated threshold. Independent bounded replay: `python /workspace/review_replay.py 1` (36 symbolic coefficients and exact 2×2 example); these are diagnostics, not the proof. The supplied NumPy checker was inspected, not executed.

## originality

PASS

The matching scalar problem and metric are prior; the distinct contribution supported by the comparisons is the sharp finite coefficient criterion for this entire kernel family, including the exact scalar endpoint. No examined statement covers the result by substitution or specialization. This is not a priority certificate.

## value

PASS

Positivity for the identical scalar benchmark was an explicit problem in the prior operator literature. Replacing infinite moment tests with a sharp matrix criterion, valid for noncommuting and singular matrices, resolves that benchmark and provides a practical exact test for a naturally occurring operator family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
