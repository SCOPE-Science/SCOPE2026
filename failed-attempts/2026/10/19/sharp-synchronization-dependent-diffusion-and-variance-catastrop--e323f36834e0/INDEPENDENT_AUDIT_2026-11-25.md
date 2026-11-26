# Independent mathematical audit

## correctness

PASS

For chi<1, the stationary stiffness average is K>0; the two-sided convolution converges conditionally on the chain. Coupling two candidate stationary starts with the same chain state and the same future noises contracts their Y difference, proving uniqueness without a moment assumption. Reversibility and the Gaussian conditional variance give the integral of exp(-sH), H=2diag(K+phi)-Q. Its smallest eigenmode is strictly positive by irreducibility, so no stationary-state coordinate can avoid divergence when the smallest eigenvalue is nonpositive, including zero. The opposite-state difference mode for psi has eigenvalue 2(K+2lambda) in H. The remaining block of H/2 has pivots K+lambda and K+alpha with Schur complement K+alpha-A/(K+lambda)-alpha^2/(K+alpha), whose sign is B. Directly solving Hw=D1 yields w=DN/(2B) for each nonreciprocal state. Qpsi=-2lambda psi and phi psi=0 give covariance A w exp(-(K+2lambda)|t|)/2 for the propulsion drift, not for the white-noise part. Twice the triangular covariance integral plus Dt gives the stated variance. B at alpha=0 and lambda gives the two strength boundaries; the quotient derivative has numerator D A[K(K+lambda)-A]/2 and at the interior pole KN=A alpha_c, giving exactly the residue stated. For B<=0 the no-jump event in a nonreciprocal state leaves a nonzero multiple of the heavy-tailed Y_0 plus independent finite-variance noise at each t>0, so the raw second moment is infinite (a finite mean is not asserted). At chi=1 with a<K, bounded positive damping suffices in both closed classes; the nonreciprocal class has E[Y^2]=2D/K, the reciprocal drift vanishes, and w tends to D/(2K) from chi<1, giving the specified class average. The packaged script was inspected, not executed; the proof provides the parameter-uniform checks.

## originality

FAIL

The partial-synchronization core is already represented by a distinct published Resultary record: the same finite-moment region, full finite-time variance, relaxation eigenmode, effective diffusivity, flatness and derivative sign, and all-positive-time divergence. This is equivalent coverage, not a finding that the later-dated catalogue entry has historical priority. The explicit pole coefficient follows by expanding its exact rational law; the a<K endpoint average follows by taking that law's one-sided limit and comparing it with the two known closed-class values. No independently substantial uncovered remainder was identified.

## value

PASS

As mathematics the full phase diagram addresses a natural transport problem: stationary separation can coexist with infinite increment square expectation at every positive time, and the sign reversal, exact flat surface, and critical synchronization separate distinct physical regimes. This substantive content does not rescue the failed originality axis; the remaining explicit coefficient and endpoint comparison do not by themselves support a separate repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
