# Independent mathematical audit

## correctness

PASS

Independent check by total variance: mass two stops with probability 2/3 at contrast −5, otherwise has contrast 4. The exact mean is 2,−2,0,...; the two exceptional means cancel in the sum over proper splits once n≥3 (for n=3 each proper split sums to zero). The variances at n=2,3,4,5 are 18,9,78/5,253/15. For n≥5, (n+1)V_n=2 sum_{i=1}^{n−1}V_i+16: four proper-split positions give conditional mean ±2 and all other positions give zero. Subtracting consecutive equations proves V_n/(n+2) is constant from n=5, so the claimed n≥6 is valid and conservative. An independent exact rational total-variance recurrence agreed through n=30. For an arbitrary linear contrast T_n, its mean from the first-moment recurrence is g(n+2) for n≥4, with g equal to the same linear combination of 1/6 and 1/15. For n≥8 its scaled conditional-mean variance G_n=(n+1)Var(E[T_n|first split]) is 2g²(n+2)²+4g²(n−7)+O(1), with an exactly constant remainder from the six boundary positions (child size 1,2,3). Hence the increment of Var(T_n)/(n+2) is (G_n−G_{n−1})/[(n+1)(n+2)]=4g²/n+O(n^−2). This independently gives the two leading variances, cross coefficient by polarization, and correlation tending to one. No limiting distribution is inferred.

## originality

PASS

The original stopping model and earlier size-one variance are background; the supported contribution is the joint two-terminal-size covariance structure and the exact residual contrast variance. No exact or governing stronger equivalent was found in the inspected evidence.

## value

PASS

The two counts distinguish fully resolved single units from unresolved two-unit chunks in the original stopping model. The theorem separates the common n log n variance mode from an exactly linear second mode and computes its coefficient. This gives information about fluctuations not recoverable from the marginals or from first-order concentration alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
