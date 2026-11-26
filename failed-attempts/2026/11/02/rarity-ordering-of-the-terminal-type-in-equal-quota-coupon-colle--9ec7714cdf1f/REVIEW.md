# Independent mathematical audit

## correctness

PASS

The multinomial enumeration at t-1 requires exactly q-1 copies of the terminal label, at least q of the others, and arbitrary null count; this gives the labeled coefficient formula, with strictly positive masses for all t>=mq. For a pair i,j, the shared coefficient sequence is log-concave with interval support, including the point mass when m=2 and p_0=0. Its Toeplitz minors are nonnegative by decreasing ratios; convolution follows by finite Cauchy–Binet. For p_i>p_j, the two remaining coupon columns have strictly positive minors in the stated order on indices r,s>=q. For adjacent output rows n,n+1, the choice r=n-h, s=r+1 at the first supported index h makes the Toeplitz minor exactly a_h^2>0. Thus the ordering is strict, and time normalization does not alter the odds. Counting a single extra draw gives the displayed mq+1 posterior. Exchangeability and those first two posteriors give the independence criterion. Pairwise odds comparisons imply strict decrease of the mean of any strictly increasing g(p_J) when rates differ; the independent-copy covariance identity gives the sign. Finally, conditional on exactly q-1 copies of i before completion, the remaining quotas are met with probability tending to one, leaving the slowest factor (1-p_i)^(t-q) for minimal rates. Ties are exchangeable. Independent exact word enumeration for q=3 and probabilities (1,3,4)/8 gave posteriors (1/3,1/3,1/3), (7/16,5/16,1/4), (160/303,88/303,55/303), verifying the successive minors in that case.

## originality

FAIL

A distinct earlier indexed record states exactly the strict adjacent-time likelihood-ratio theorem for common positive quotas, heterogeneous required rates and optional null draws. It also supplies the exact labeled coefficient law, shortest-time uniformity and asymptotic odds. The additional first-step and covariance observations are direct consequences; no substantive distinct theorem remains.

## value

FAIL

A sharp terminal-label ordering across all times would be a useful structural result. Here that ordering is already stated for the full model, and the extra mq+1 expression, independence and covariance are elementary consequences of the same exact law and ordering. The record does not resolve another meaningful gap beyond the known theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
