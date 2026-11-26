# Independent mathematical audit

## correctness

PASS

The formulas are correct for every stated k,r,s. Operator/trace duality and rank-one trace-norm tests give the maximization of the weighted nuclear norm. For a general complex symbol the Hilbert–Schmidt adjoint has the conjugate symbol (equivalent by complex conjugation, and identical for this real mask). The SVD factorization for positive weights gives joint concavity by taking the infimum of affine costs; continuity allows zero weights. Rotating identical weighted rows or columns combines their squared weights, proving the exact reduction to one additional row or column of each type. Averaging the core permutations and, when both shores are present, transposition gives the stated symmetric weight profiles. With no added vertices the two crown eigenspaces give 2-2/k. For one shore with total core mass x, the k-1 orthogonal core directions contribute (k-1)sqrt(x)/k and the constant direction contributes sqrt(1-(2k-1)x/k²). The derivative at x=1 has the sign of k²-4k+2, negative at k=2,3 only; strict concavity gives the stated stationary value or the endpoint. For both shores the two-dimensional block has determinant -x(1-x)/k and trace 1-x/k; these give the square-root discriminant in the proof. Its trace norm plus the other k-1 singular values is strictly concave, has positive derivative at zero and derivative (k²-5k+2)/(k(k-1)) at one. This is negative exactly at k=2,3,4. Completing the square in the radicand and maximizing the linear term plus its square root gives (k-1+2k sqrt(k+2))/(4k-1) on the interior branch. At x=1 both objectives give the bare crown norm. The weighted polar isometry supplies a contraction attaining the norm, with aggregate universal weights freely splittable. Read RESULT.md lines 36–92, VERIFICATION.md and checks/verify_partial_crown.py. The stored finite checks were inspected, not executed, and are not needed for the analytic proof.

## originality

FAIL

The distinct catalogue record 9f78317148b0 explicitly gives the identical canonical masks, the entire one- and two-shore piecewise formulas including the breakpoints, and norm invariance under arbitrary finite row/column duplication. Setting its core size m=k and flags u=1_{r>0}, v=1_{s>0}, then duplicating its universal rows and columns, recovers every frozen case. This is demonstrated coverage of the full claimed advance, not just of the credited small norms or a method resemblance. The older catalogue path is provenance evidence, not a claim about authorship or absolute scientific priority.

## value

FAIL

The two thresholds are natural and useful invariants, but the frozen record does not advance them beyond the existing component-by-component norm formulas. Reading the branch boundaries and renaming the optional borders are mechanical deductions, and the self-contained proof uses the same scalar optimization. There is no independently useful unknown exact fact, different proof mechanism, or surviving new classification in the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
