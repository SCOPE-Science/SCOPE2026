# Independent mathematical audit

## correctness

PASS

With first coordinates decreasing, area is the sum of independent first-coordinate spacings times prefix maxima of the second coordinates. For k >= i, the record indicator at i uses relative ranks independent of the maximum of the first k values. For k < i, conditioning on a record at i leaves the first i−1 values iid uniforms below that record value, whose conditional mean is i/(i+1). This gives Cov(I_i,Z_k)=−k/[i(i+1)(k+1)]. The spacing mean 1/(n+1) gives the asserted local formula. Reversing the sum telescopes 1/[i(i+1)] to 1/(k+1)−1/(n+1), proving the harmonic identity, strict negativity for n >= 2, and the n=1 boundary via the empty sum. The area mean and both limits follow from the mean prefix maxima and harmonic asymptotics. The marginal-CDF transform is valid for population content, not arbitrary Euclidean area. Bounded independent rational rank enumeration through n=7 confirmed local and total covariances and the mean, e.g. Cov(M_3,A_3)=−13/288; replay with Python 3 at /workspace/branches/249e8ce1-e08b-4598-be97-0bc58a87155c/reproduce_record_area.py. Supplied verifier and verification notes were inspected but not run; enumeration is corroboration, not an all-n proof.

## originality

FAIL

A distinct indexed result demonstrably covers both exact covariances, and gives a stronger area variance and correlation limit. This is a scientific overlap decision, not a claim about historical priority: the matching catalogue path is dated later than the assigned path, and the failed access attempts do not establish earlier coverage or its absence.

## value

FAIL

The relationship between skyline cardinality and covered area is natural and the positionwise sign is informative. As a distinct contribution this package supplies no remaining precise gap: the same indexed record already has the covariance kernel, the aggregate formula and the mean, with stronger variance and standardized-dependence results. Neither the deterministic boundary nor the standard product-content transformation supplies a new scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
