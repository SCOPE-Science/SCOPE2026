# Independent mathematical audit

## correctness

PASS

There are m spacings, including boundaries, with Dirichlet(1,…,1) law. The shifted-simplex integration is valid below the zero-probability endpoint t=1/k and yields the two harmonic sums in RESULT.md. Independently, for unnormalized iid unit exponentials let R be their maximum and Z their sum of squares. Independent ordered increments of rates r=1,…,m give Cov(R,Z)=2 sum_j(A_j B_j + C_j), with A_j, B_j, C_j the tails of sum 1/r, 1/r², 1/r³ from r=j. Summing C_j gives H_m^(2); splitting the double sum in A_j B_j at r=s gives H_m+(H_m²−H_m^(2))/2. Since the total T is independent of the normalized spacings, E[RZ]=m(m+1)(m+2)E[MQ]; E R=H_m and E Z=2m give the claimed moment. Subtraction, the positive harmonic increment, the two checked variances, and H_m^(2)→π²/6 give the stated sign, Pearson expression and asymptotic. m=2 gives Cov=1/48. Inspected the frozen verification notes, script and output without executing them; independent exact ordered-gap arithmetic for m=2,…,30 is replayable with python3 /workspace/branches/independent_bounded_checks.py. The bounded checks corroborate rather than prove the all-m theorem.

## originality

FAIL

Exact prior coverage: the distinct October 26 Resultary record a4f2c9f76454 states the same mixed moment, covariance, Pearson formula and sharp asymptotic for the identical boundary-inclusive model, with n in place of m. Two October 18 matches independently cover the mixed moment/covariance, one via a stronger weighted-tail identity. The October 4 exponential-range covariance also implies the headline mixed moment by the shifted sample and gamma factorization. This is demonstrated overlap, not an inference from titles or access failure.

## value

FAIL

The covariance is scientifically useful for comparing two established diagnostics, but the submitted finding adds no mathematical invariant, range, or asymptotic beyond exact pre-existing coverage. The examples and probability-integral-transform scope do not constitute a distinct valuable remainder; no repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
