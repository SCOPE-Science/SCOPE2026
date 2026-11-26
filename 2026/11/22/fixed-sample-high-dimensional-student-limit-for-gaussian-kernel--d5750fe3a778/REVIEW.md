# Independent mathematical audit

## correctness

PASS

The balanced split statistic and its s-denominator within-group variances agree with the published equations. For the finitely many cross-split pairs, distance-square fluctuations about 2d sigma^2 are jointly O_p(sqrt(d)). Taylor expansion about that center with the same random bandwidth in all pairs gives a uniform O_p(d^(-1)) remainder; neither conditioning on the bandwidth nor pretending it is independent is needed. The constant and evaluation squared norm cancel when taking the witness contrast. The remaining second-split squared-norm term is common across both first-split groups and cancels from their mean difference and each centered variance. Dividing by the positive common factor exp(-d sigma^2/ell_d^2)*sqrt(d)/ell_d^2 makes the remainders o_p(1) and leaves the scores X_i dot G_d/sqrt(d) and Y_i dot G_d/sqrt(d), with G_d the difference of second-split means. The vector contribution from one coordinate has covariance (2 sigma^4/s)I by split independence and zero means; the multivariate iid CLT yields independent Gaussian limit scores despite shared G_d. Their difference of means is independent of pooled within-group residual sum of squares, which after variance scaling is chi-square_(2s-2). The published denominator uses s twice in squared units, giving sqrt(2s) Z/sqrt(Q), not ordinary t_(2s-2). The limiting denominator is positive almost surely, hence zero denominators vanish in probability. The repaired bandwidth example explicitly applies the median to ell_d^2, and a positive fallback on a zero median preserves the stated limit and avoids undefined kernels under discrete laws. No main limit or calibration number changes.

## originality

PASS

The repair credits Zhu–Shao's explicit fixed-sample high-dimensional Gaussian-kernel regime and centered-pair expansion framework, a closer antecedent than the growing-sample work alone. The credible distinct contribution is the exact limiting calibration of the published split statistic with its biased studentizer, including shared data-dependent bandwidth and the fixed-sample nominal-size discrepancy. It is not a claim to originate high-dimensional distance linearization, joint Gaussian approximations, or the Student ratio.

## value

PASS

The question concerns calibration of a named published two-sample procedure in a natural different asymptotic regime. At four observations per group, a nominal one-sided 5% Gaussian cutoff has limiting null rejection about 18.24%; the theorem yields an exact replacement cutoff. The discrepancy is not a cosmetic Bessel correction: even correcting the variance does not turn a fixed-degree Student limit into a normal law. Applicability to non-Gaussian coordinates and common pooled bandwidth selection broadens the usefulness of the calibration boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
