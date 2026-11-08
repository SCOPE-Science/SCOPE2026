# Review: birthday and complete-collection dependence

## Correctness — PASS

For iid uniform draws from exactly \(n\ge2\) labels, the independent geometric discovery-stage construction simultaneously represents cover time and the indicators of an all-distinct prefix. Conditioning on the first collision yields a strict first-order stochastic ordering of completion times, including the exceptional all-distinct terminal case. Linearity of covariance and the geometric identities give the displayed finite double sum. Uniform Gaussian domination of birthday survival probabilities proves the residual covariance constant, while moment bounds, the occupancy inclusion–exclusion Gumbel limit, and an explicit independent-stage coupling prove the correlation and joint limits. The finite independent checker verifies the exact formulas and conditional means, but finite enumeration is not a proof of the general statements.

## Originality — PASS, with historical-priority risk

The comparison target is the same-path bivariate first-repeat/first-complete-collection statistic, not marginal birthday or coupon waiting times. The 1987 report of Flajolet–Gardy–Thimonier develops the separate birthday and coupon methods; the inspected sections do not state the mixed stochastic order or covariance. The 2010 thesis of Pósfai supplies marginal geometric waiting stages and coupon-collector limits, not their joint covariance with the birthday time. Myers–Wilf (2003) study other collector variants and the comparison of independent collectors. A related 2008 generalized birthday/coupon article was accessible in abstract only, and earlier general multivariate enumerations may imply the identity implicitly. The lack of an exact search hit is not independent evidence of novelty; the inspected mathematical statements and their implications underpin this qualified assessment.

## Value — PASS

Both the first repeated coupon and the final missing coupon are canonical waiting-time milestones observed on the same sequence. Their conditional first-order stochastic ordering is stronger than a covariance sign; the exact all-size mixed moment and the residual \(\sqrt n\)-scale dependence explain why asymptotic independence of Rayleigh and Gumbel normalizations does not make their finite-sample association negligible on its natural covariance scale. These are motivated dependence properties, not a relabeling of either known marginal distribution.

## Limits

Equal sampling probabilities are essential. No independent external audit has been performed. The full text of the 2008 Inoue–Aki article was not accessible for a decisive comparison, and implicit derivability from classical multivariate coefficient formulas remains a priority risk. The new checker gives reproducibility, not infinite proof or independent certification.

Self-review: passed. Independent audit: not yet performed.
