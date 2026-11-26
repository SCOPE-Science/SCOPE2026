# Independent mathematical audit

## correctness

PASS

Conjugating the orthonormal-frame coordinates under the specified inner-product convention gives the complex conjugate of tr(W^T C W); skew perturbations contribute zero. Takagi congruence gives the sum of the weighted squares of the frame entries, bounded by sum_i s_i p_i with p_i the projection diagonal (0<=p_i<=1, sum p_i=k). The leading k coordinate frame attains the leading partial sum. For k=1 an isotropic vector on the first two coordinates gives zero, including when the second weight vanishes; if both vanish then C=0. For even k the 2x2 unitary blocks give zero diagonal in UU^T. For odd k>=3 the residual triple cancels using cos(2 theta)=-c/(a+b) in [-1,0], with an all-zero exception harmless. For example at n=k=3 and weights (4,2,1), the last construction gives trace 6*(-1/6)+1=0 while the identity gives 7. The path-connected complex Stiefel manifold and common-phase action then supply exactly the closed disk, including k=n and zero radii. Successive differences and Takagi uniqueness give the classification. VERIFICATION.md and verify_trace_disks.py were inspected; the package's 1,056 cases / 10,560 checked frames are recorded toleranced evidence, not an independent rerun. The exact hand check above is replayable by evaluating tr(DUU^T) for U=(cos(theta) I_2+i sin(theta) [[0,1],[1,0]]) direct-sum 1.

## originality

FAIL

The primary papers inspected cover the rank-one disk or the infinite-dimensional shape, not the full stated finite profile. However, a distinct indexed result bde8f36b6108 explicitly contains the all-rank finite-dimensional theorem including top rank, inverse profile and skew invisibility within its general Hilbert-space statement. Unitary congruence is an immediate Takagi consequence. No distinct finite claim survives this statement-level comparison. Its visible November 2 date is later than the frozen October 27 date: this is a finding of present duplicate coverage, not evidence of earlier publication, order of discovery, or dependence.

## value

FAIL

The finite normalized trace profile would be a useful invariant, particularly at top rank, if it were not already available in the indexed general result. The finite specialization and the congruence reformulation add no independent mathematical information to that coverage. The elementary proof validates the finding but does not supply a substantively different result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
