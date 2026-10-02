# Independent mathematical audit

## correctness

PASS

The final covariance formulas reconstruct directly from the canonical Hoeffding decomposition. For a fixed order r, each canonical term has pseudo-value coefficient r/C(n-1,r-1) when the deleted index is in the r-set and (1-r)/C(n-1,r) otherwise; orthogonality makes the variance and two-index cross-covariance finite combinatorial sums, yielding exactly [r(n-2)+1]/C(n-1,r) and -(r-1)/C(n-1,r). Positive-semidefinite Hoeffding covariance components then give the sign and iff-additive equality statement. In the scalar case the correlation is a nonnegative weighted average of the pure-order ratios, so the sharp interval and its endpoint constructions follow. Exchangeability and n^{-1}sum_i V_i=U_n give E Sigma_J-Var(U_n)=-Cov(V_1,V_2), and coefficient comparison gives the stated sharp inflation factor. The inspected exact-arithmetic verifier checks these identities and the Rademacher example, but the infinite statement is proved symbolically rather than inferred from the finite grid.

## originality

FAIL

The final claim is mechanically implied by earlier general jackknife theory once specialized to a complete U-statistic. Efron--Stein give an exact ANOVA/Hoeffding-type decomposition of a symmetric statistic and an exact positive expansion for the bias of the jackknife variance estimator, and they explicitly discuss the U-statistic specialization. For the exchangeable pseudo-values used here, the elementary identities Var(U_n)=[D+(n-1)C]/n and E Sigma_J=(D-C)/n convert that prior bias formula into C=-bias. Substituting the standard Hoeffding variance coefficients produces the submitted all-order cross-covariance coefficients; the scalar interval and matrix inflation factor are then immediate optimizations of those coefficients. Under the required implication bar, the fact that the earlier paper did not print the same pseudo-value formula verbatim does not preserve originality.

## value

PASS

As an exposition, the explicit sign, iff-additive criterion, correlation envelope, and exact connection to pseudo-value dependence are mathematically useful finite-sample facts. They clarify a misleading exact-uncorrelatedness reading in later applied work. The scientific rejection is originality-based, not because the formulas are valueless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
