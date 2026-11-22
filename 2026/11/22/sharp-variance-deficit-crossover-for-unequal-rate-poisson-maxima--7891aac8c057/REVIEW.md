# Scientific review: Poisson maximum variance-deficit transition

## Correctness

PASS. The all-parameter proof starts with a Poisson size-bias identity, obtains an exact variance-deficit decomposition, and proves nonnegative covariance through the coordinatewise monotonicity of the maximum and residual sum. For two rates, the covariance identity is algebraic and uses only independence. The unequal-rate sharp coefficient follows from the Skellam series and Bessel fixed-order asymptotics, with a geometric summable dominant sequence justifying interchange of limits. The equal-rate linear limit follows from a uniformly integrable central limit theorem. Explicit code reproduces finite mass and asymptotic calculations. No numerical experiment is substituted for an infinite-domain proof.

## Originality

PASS, with residual priority risk. The 2023 order-statistics article proves underdispersion in identically distributed samples, not the unequal-rate, sharp-prefactor statement. General Poisson Poincaré and the Skellam formula already imply important parts of the setup; neither qualitative underdispersion nor the underlying Bessel function identity is presented as new. The published identical-rate two-sample Fano limit is also prior work. The proposed distinct contribution is the explicit, nonuniform \(\sqrt t\exp[-t(\sqrt a-\sqrt b)^2]\) deficit with the exact prefactor and its singular contrast with the equal-rate linear law. Related summaries on Poisson maxima, heterogeneity and curvature do not state that asymptotic; access to all potentially relevant complete articles was not obtained, so priority is provisional.

## Value

PASS. Equality and strict inequality of the two counting intensities lead to radically different variance deficits, even though the maximum is underdispersed in both regimes. The exact leading coefficient quantifies how quickly a heterogeneous maximum can become practically indistinguishable from an equidispersed Poisson count, and clarifies why conclusions based on the equal-rate model are not uniform in rate heterogeneity. This is a natural property of replicated counts rather than an arbitrarily selected parameter slice.

## Prior coverage and limitations

The source paper's identical-law preservation theorem and the classical Poisson Poincaré inequality cover the qualitative comparison with a Poisson variance. A previous identical-rate limit covers the \(1-1/\pi\) limiting Fano ratio. Neither such statement contains the unequal-rate sharp prefactor. The new equivalent is for fixed unequal positive rates, not for a coalescing-rate triangular array; no claim is made about intermediate-intensity shape or independent verification.

Self-review: passed. Independent audit: not yet performed.
