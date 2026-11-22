# Scientific review

## Correctness — PASS

The matching conditional law follows exactly from permutation transitivity and counting matchings containing prescribed disjoint edges. The circle representation uses the normalized independent-exponential spacing law; its local-minimum correlations yield the stated finite variance. Total covariance gives the exact positive covariance between shared-replicate overlap counts. Joint Poisson factorial moments have a controlled vertex-collision/repeated-edge error, and the conditional moments combine with the bounded-dependent Gaussian limit. `verify.py` passed 75 independent exact-rational assertions for finite matching and circular cases. Fixed replicate count is essential; neither convergence rates nor growing replicate regimes are proved.

## Originality — PASS (qualified)

One-sample reciprocal-nearest-neighbor means, variances and CLTs are previously established (Enns–Ehlers–Misi; Bahadır–Ceyhan). A general Poisson overlap for a uniform perfect matching against sparse graphs is established in later matching literature (Deng, 2025). Those facts are excluded from the novelty claim. The specific combination of exact size-conditioned distribution-free *partial*-matching calibration, a simultaneous Gaussian–Poisson independent-replicate law, and exact finite positive covariance of overlapping replicate comparisons is not given in the checked sources or nearest published-record comparisons. General matching identities or statistical permutation-test treatments could implicitly cover the conditional formula; bibliographic priority is not certified.

## Value — PASS

Repeated labelled point-cloud comparisons require a null distribution for persistence of reciprocal-neighbor pairings. The complete finite conditional polynomial permits exact tests even when geometric density and dimension are unknown, while the simultaneous limit gives joint rather than separately marginal calibration for several replicates. The positive finite covariance quantifies the residual dependence hidden by the independent limiting Poisson law. These conclusions address a natural inferential quantity rather than an arbitrary parameter slice.

## Sources and limitations

Material inspected includes the accessible primary arXiv HTML material from Bahadır–Ceyhan (arXiv:1605.01940, particularly its nearest-neighbor representation and moment/CLT sections) and Deng (arXiv:2505.13799, especially its introduction, main matching-overlap theorem and generating-function approach), together with the accessible one-dimensional cluster study of Enns–Ehlers–Misi. Public record searches for conditional matching overlaps, repeated reciprocal-neighbor matching intersections, and shared-replicate covariance did not find an exact matching statement. Residual historical risk: the conditional polynomial follows from classical matching counts and might occur in an unindexed reference; the marginal Poisson component is substantially anticipated by general sparse matching results. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
