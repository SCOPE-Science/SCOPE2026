# Independent mathematical audit

## correctness

PASS

The n+1 uniform spacings have constant density on the n-dimensional simplex. Conditioning on an internal D_k>t replaces the vector by t e_k+(1-t)Z and has probability (1-t)^n. The unbiased variance is the sum of squared pairwise differences divided by n(n-1). Its internal-spacing quadratic form has diagonal entry b=k(n-k)/[n(n-1)] and row sum nb/2, since the crossing pairs have average rank length n/2. The conditional mean is therefore (1-t)^2/12+t(1-t)nb/(n+1)+t^2b; subtracting the unconditional mean inside the probability factor gives (1). The sign bracket is increasing with endpoints nb/(n+1)-1/6 and b-1/12, giving the stated strict criterion and threshold, including the excluded endpoint zeros for k=1 at n=5,12. Summing b over internal gaps gives (n+1)/6 and the strictly positive Euler covariance. The Euler identity uses only internal gaps and with closed intervals merges at equality, matching the strict indicator. Substituting t=c/n gives the announced limit, and for k/n→u the limiting bracket determines the eventual sign away from its zero boundary.

## originality

PASS

The accepted claim is the full threshold-by-rank covariance with sample variance and its aggregate sign law, not the known uniform-simplex identity, a linear spacing covariance, or an Euler test calibration. Known exceedance corrections for separable spacing statistics use the same conditioning step but not the cross-rank variance quadratic form. Inspected distinct same-date statements concern other statistics; no priority inference was made from the date.

## value

PASS

The exact mixed moment quantifies dependence between standard dispersion and a canonical one-dimensional topology statistic at arbitrary finite-sample thresholds. It resolves behavior an aggregate cannot show: a positive total at every radius coexists with negative outer-rank contributions, and the first internal rank switches only in a finite, explicit sample-size window. This gives a meaningful baseline for comparing summaries of the same sample, without claiming an independence test or power improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
