# Independent mathematical audit

## correctness

PASS

The v4 raw-input statistic has exactly the stated pair kernel and variance normalization. Writing h=( (x-y)^2-g )/2, with g=(x+y)|x-y|, cancels the empirical squared-difference term against the unbiased sample variance and the subtractive half; the remaining ratio is -U_g/(4 S_n^2). Sorted pairs give y^2-x^2, including ties, which yields the stated coefficients 2j-n-1. Joint reflection makes the population contrast zero, and square integrability from the fourth moment gives the first-order Hoeffding projection 2g_F(X) for U_g. Slutsky gives variance Var(g_F)/(4 sigma^4), permitting a point mass at zero. The statistic is only defined when S_n^2>0; that event has probability tending to one by consistency at positive variance. Independently, pairing Y with -Y gives g_F(x)=E[(x^2-Y^2)_+] for x>=0 and odd extension. This recovers 2x^3/3 on the unit half-interval and the stated normal projection by a truncated second-moment integral. Scale invariance and E[X^6]=1/7 for the unit uniform give nu_F=1/7. Separate bounded quadrature (`python /workspace/branches/926bb4dc-83e3-47e6-9d34-48c623c92778/independent_numeric_check.py`) reproduces nu_0=0.44233111437756269142… and limiting uniform rejection 0.000563036470104841576…. The normal limit is continuous at the positive critical value, so the result applies to consistent exact-null quantile calibration or the stated Gaussian cutoff; it does not assert equivalence for a fixed finite simulation bank.

## originality

PASS

Pass for the reflection obstruction of the cited scalar procedure, the normalized-statistic asymptotics for its blind class and the explicit uniform witness together. The parent test, general projection theory and other zero-bias tests are prior. The cited paper states the kernel and an order-statistic formula but does not establish these consequences in the located passages, and its variance expression differs materially for the ratio actually used.

## value

PASS

The obstruction changes the scientific interpretation of a published normality statistic: exact cancellation leaves every centered symmetric alternative on the null scale, even though many are plainly nonnormal. A continuous uniform example has limiting rejection far below nominal under correct null calibration, quantifying the practical consequence beyond noting parity or a normalization discrepancy. The result remains confined to the signed scalar test, not Stein's characterization or the squared-distance procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
