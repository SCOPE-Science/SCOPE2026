# Independent mathematical audit

## correctness

PASS

For Q=BBᵀ=(r−λ)I+λJ, Q is positive definite and the factors Q^(1/4) and Q^(−1/4)B have constant squared row and column norms N/v and N/b, where N=tr√Q. Their Schur bound equals the weighted nuclear norm at the uniform pair. Write Y=√(Q/b) and X=√H(z). The difference in the trace-square-root tangent inequality is exactly (1/2)tr[Y^(-1)(X−Y)^2], nonnegative with equality iff X=Y, even for singular H(z). The linear tangent term vanishes on the simplex because c_sᵀY^(-1)c_s is constant across k-sets. Pair constraints imply the point moments by summing over the k−1 pairs through a point in each block, and imply normalization by summing over all pairs. The strictly positive uniform vector gives the full affine dimension b−rank A. For complete systems with k≤v−2, subtracting two k-set equations that differ in one point forces all pair coefficients equal and then zero; for k=v−1 the equations on complements force all column-relation coefficients equal and then zero. This review is analytical; the supplied exact finite verifier was inspected but not executed, and the frozen independent-verification statuses are not_performed.

## originality

FAIL

The frozen main claim is already covered by a distinct earlier Resultary record that classifies all joint normers, not merely those with uniform point weights, and gives the identical affine dimension. The complete-system dimension specialization adds the standard rank calculation for the pair-versus-k-set inclusion matrix, not a distinct optimizer theorem.

## value

FAIL

Exact norming weight geometry is a worthwhile question, but this record repeats only a restricted part of an existing joint optimizer classification. Beyond that established result it supplies a routine complete-design inclusion-rank specialization, not a new optimizer phenomenon or independently useful unresolved invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
