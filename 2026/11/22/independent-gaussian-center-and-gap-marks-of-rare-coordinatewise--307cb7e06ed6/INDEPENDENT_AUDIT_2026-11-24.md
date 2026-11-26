# Independent mathematical audit

## correctness

PASS

Conditioning on a directed edge leaves iid coordinates with density 2 on 0<u<v<1. Triangle integration gives E[U^a V^b]=2/((a+1)(a+b+2)); the endpoint means are 1/3,2/3, variances 1/18 each and covariance 1/36. The centered sum and gap then have diagonal covariance (1/6,1/18), proving the product Gaussian limit by the multivariate CLT. An ordered pair meets 4n-6 indices including itself, with reciprocal probability zero and joint per-coordinate bounds 1/3 for a fork and 1/6 for a chain. These give b1=n(n-1)(4n-6)4^-d, b2 at most n(n-1)(4n-8)3^-d, and b3=0. The union bound over pairs gives the matching estimate. When the marks are split into any finite Borel partition, summing the category probabilities preserves b1, mutual exclusion inside each index contributes zero to b2, and the whole outside neighborhood remains independent. The materially checked marked process theorem therefore applies and projection by summation gives exactly the stated Poisson means and TV rate. At critical scale both error terms vanish. Bounded continuous nonnegative tests can be approximated uniformly by simple tests; the approximation error in their Laplace functionals is controlled by the bounded mean mass, and the exact mark laws are tight by their CLT. This proves the finite random measure limit. A void on the complement of a lower rectangle gives the stated extrema law; for finite thresholds with Gaussian rectangle factors a,b the joint probability divided by the product of the marginal limits is exp(lambda(1-a)(1-b)), not 1.

## originality

PASS

The sparse count and pair-neighborhood calculation already appear in closely related work; the general marked approximation is also prior. The supported distinct refinement is the joint full-coordinate fluctuations of the center and gap across rare ordered comparisons, with the explicit intensity and shared-count extrema. It is not a rediscovery of a fixed-dimensional vertex projection, a sparsity threshold or a Poisson approximation theorem.

## value

PASS

This identifies fluctuations of the locations and separations of the comparable pairs, rather than only whether pairs occur. Separation and center decorrelate jointly on each limiting atom even though the endpoint averages are correlated, while maxima of the two marks remain dependent through the common random atom count. The marked process and finite-parameter approximation answer this joint-statistic question; the isolated moment arithmetic, unmarked Poisson law and matching bound would not by themselves justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
