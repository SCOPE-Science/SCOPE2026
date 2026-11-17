# Independent mathematical audit

## correctness

PASS

C PASS. Uniform attachment gives exact update Z'=Z+z t, L'=L+1−b and U'=U+zt−bt for random parent P, hence closed first/mixed moments. Solving leads to C_n(z)=(n−2)z(1−z)/(2(n−1)!)∏_{r=2}^{n−2}(z+r). Writing this as (n−2)z(1−z)/4 times ∏_{r=3}^{n−1}(r−1+z)/r matches the earlier polynomial verbatim. The normalized product is the probability generating function of Bernoulli(1/r), r=3,..,n−1; its real negative zeros yield log-concavity, so first differences change sign once (perhaps a single zero). Empty products n=3 and deterministic n=2 handled. Independently enumerated all recursive trees n=3..7 with matching covariance coefficients; finite tests are corroboration.

## originality

FAIL

O FAIL for decisive prior coverage: the public 2026-10-12 theorem ‘A four-class boundary for leaf–depth covariance in uniform recursive trees’ has EXACT same C_n(z) displayed as Eq.(1). Reindexing its ∏_{j=3}^{n−1}(j−1+z)/j transforms directly to the current factorial product. Its original proof even derives the identical recurrence. From this known polynomial, coefficient first-difference/Poisson-binomial unimodality and one-switch sign are routine real-rootedness facts; not a new mathematical invariant. Earlier result also obtains stronger depth-residue Fourier asymptotic regimes. Independent sibling leaf-erasure theorem is related but not needed for coverage.

## value

FAIL

V FAIL for the submitted claim. The covariance between leaf number and each depth is naturally motivated, and the existing Oct12 theorem already gives the exact polynomial and a much broader residue-covariance analysis. Extracting the coefficient sequence and sign transition with standard log-concavity is a textbook consequence of its explicitly factored generating function; no separately substantive new classification remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
