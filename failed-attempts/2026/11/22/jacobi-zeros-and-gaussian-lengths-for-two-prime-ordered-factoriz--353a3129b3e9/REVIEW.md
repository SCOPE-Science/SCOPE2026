# Independent mathematical audit

## correctness

PASS

A length-k factorization corresponds to a word in a copies of p and b copies of q, cut into k weakly increasing nonempty blocks by sorting the prime labels within each factor. Every descent forces a cut, and other gaps may be cut independently. A word with j descents contributes t^(j+1)(1+t)^(a+b−1−j); its descending corners in the lattice-word path select j distinct abscissas and j distinct ordinates, giving binom(a,j)binom(b,j) words. The resulting finite sum is exactly the standard shifted Jacobi binomial formula times t(1+t)^(M−1). At t=0 the Jacobi factor is 1; at t=−1 it is (−1)^m binom(M,m), so no extra endpoint multiplicities occur. Orthogonality gives m simple roots x_j in (−1,1), then t_j=(x_j−1)/2. Newton's inequalities apply to P/t of degree a+b−1, giving the stated normalization. The normalized generating function has independent Bernoulli factors with success probabilities 1/2 and 1/(1−t_j)=2/(3−x_j); the shift is one. The variance is at least (M−1)/4 and M tends to infinity whenever a+b does, so bounded centered summands meet the triangular-array Lindeberg condition. For a=b=1 this gives t(1+2t) and no −1 root. Frozen code was inspected, not run; exact proof covers its test range and all larger exponents.

## originality

FAIL

The full coefficient identity is an explicit evaluation of Wagner's pre-existing binomial-basis product rule, not merely analogous to a different real-rooted polynomial. The classical Jacobi binomial expansion gives its closed form without any new identity for special functions. The exact endpoint zeros are the known degree gap in the same transform, interior zeros follow from Jacobi orthogonality, and the stated distributional conclusions then follow from normalized real linear factors and their divergent variance. This is mathematical coverage by prior implication, not a claim that an earlier source used identical wording or announced the same CLT.

## value

FAIL

The natural length statistic is mathematically coherent, but this record's contributions reduce to a standard binomial-basis product, a textbook Jacobi evaluation, and standard real-rooted PGF and bounded-summand consequences. It adds no new asymptotic estimates for the mean and variance, new scope, or independently motivated surviving invariant beyond those deductions. This fails as a research contribution, not as an expository formula or proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
