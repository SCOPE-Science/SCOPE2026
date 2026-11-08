# Scientific review: exact planar Gaussian XNysTrace risk and calibration

## Correctness — PASS

The claim is restricted to the unnormalized two-probe leave-one-out definition (Epperly–Tropp–Webber, equations (8)–(9)); the independent standard Gaussian probes, matrix positivity, ambient dimension, and posterior squared-error normalization are explicit. Diagonalization and the exact rank-one Nyström residual reduce the two basic errors to Gaussian radial factors and uniform angles. The covariance is computed, not assumed zero; the angular Poisson-kernel coefficient at frequency four is the critical step. Exact symbolic polynomial factorizations show both global bounds and their equality conditions. The standalone verifier reproduces the factorization, five independent angular integrations and five independent direct-estimator simulations. No finite numerical enumeration substitutes for the general proof. The small-dimension and normalized-algorithm distinctions are stated.

## Originality — PASS, with residual risk

Closest primary source: Epperly, Tropp and Webber, arXiv:2301.07825, full accessible text inspected at equations (7)–(9), Proposition 2, Sections 2.3, 5.3 and 5.6. It defines the estimator and provides general variance bounds and a correlation-based posterior-calibration identity; it does not evaluate the planar two-probe Gaussian covariance or state the sharp \(5/3\) and \(5/8\) spectral boundaries. Persson, Cortinovis and Kressner, arXiv:2109.10659, full text inspected at Sections 1 and 2, treat a different fixed-split Nyström++ procedure. Relevant prior mathematical results concerning one-column planar Nyström residual means and Hutch++ variances do not determine this joint covariance. Targeted searches for two-probe XNysTrace variance and error-estimator calibration, together with comparisons of accessible prior scientific claims, did not identify an equivalent or stronger statement. This is provisional literature-led originality, not a universal uniqueness certificate; obscure or subsequent work may contain the same formula.

## Mathematical value — PASS

The posterior error estimator is part of the source algorithm and informs adaptive stopping. The exact nonzero covariance of its two leave-one-out corrections produces a systematic underreporting factor with a complete sharp spectrum-dependent upper boundary; general correlation identities do not quantify it. The exact variance supplies a sharp fixed-Gaussian-probe baseline benchmark. This is a natural complete planar classification, not an arbitrary parameter substitution. The two-by-two case is deliberately a stress test: two matvecs already permit full matrix reconstruction, and the optional normalized scheme can be exact. Thus the result informs reliability analysis of the basic baseline variant rather than claiming practical optimality.

## Literature and verification limitations

No independent audit or expert validation was performed. Stronger undiscovered specialist work may contain the same formulas. The later Epperly (2025) thesis, arXiv:2512.15929, has a related scope, but only its metadata/abstract could be retrieved; its full text was not compared. The optional normalized variant, complex arithmetic, semidefinite singular cases, higher dimensions, and non-Gaussian probes are excluded. The exact source date is the first arXiv posting, January 19, 2023, not the 2024 journal date.

Self-review: passed. Independent audit: not yet performed.
