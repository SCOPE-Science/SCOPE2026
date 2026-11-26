# Independent mathematical audit

## correctness

PASS

Reconstructed the real quartic quotient in the antisymmetric and kernel coordinates. The two polynomial identities bound the nonnegative-sign branch strictly below 1/2; on the opposite branch removing the kernel coordinate strictly increases the quotient unless it was already zero. The value 2/3 at u=1/2 excludes the first branch. The derivative on the remaining interval has sign given by the strictly decreasing cubic in u^2, which changes sign once; restoring the one-sided numerator sign gives exactly the claimed maximizing line. The norm derivative yields the bound for both signs of beta (and beta=0); a norming initial vector proves optimality with prefactor one. Skew symmetry and the characteristic polynomial give the contrast with Euclidean contractivity and spectral stability. Independently expanded the polynomial identities and derivative and isolated the cubic root by rational signs at 0.23310321709649116 and 0.23310321709649117 (python3 /workspace/branches/review_replay.py 4). The bundled diagnostics were inspected, not run, and are not an all-vector proof.

## originality

PASS

The supported distinct result is the path-specific global maximization including exclusion of the kernel coordinate, the cubic value and the full set of normers. The logarithmic-norm-to-semigroup implication and two-coordinate benchmarks are existing results; no inspected comparison provides the path extremum or its normers.

## value

PASS

The minimal equal-edge path with a nontrivial continuous kernel direction is a useful test case for whether an invariant subspace controls a non-Hilbert contraction threshold. The complete normer classification resolves that issue rather than only producing a lower bound from the plane. The exact scalar threshold gives a usable benchmark distinguishing initial norm growth from spectral and Euclidean stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
