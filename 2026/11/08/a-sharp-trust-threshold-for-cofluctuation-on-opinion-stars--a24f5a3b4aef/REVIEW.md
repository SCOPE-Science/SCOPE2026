# Scientific assessment: sharp trust threshold for opinion-star cofluctuations

## Correctness — PASS

The statement specifies independently activated one-sided averaging on an undirected star, two distinct stubborn opinions, and strictly positive homogeneous trust. The centre and each flexible leaf have the same stationary mean because the leaf-to-centre balance is harmonic and the centre's stubborn inputs fix the common mean. After centring, the full stationary quadratic-generator balance reduces by exchangeability to four moment types, and its three nonredundant equations are written in RESULT.md. Direct elimination gives exact rational variances and off-diagonal covariance. The difference between sizes \(k\) and \(k+1\) has numerator \(-q\theta^2[h\theta^2-(2h+4)\theta+4]\), with strictly positive denominators. This proves a unique trust threshold simultaneously for every \(k\) and both stubborn camp sizes. Individual variance and Pearson-correlation signs follow by separate exact subtraction. The large-\(k\) limit is an ordinary ratio of leading coefficients. The standalone checker derives all *labelled* stationary moment equations separately and verifies the formulas in 608 exact rational and symbolic assertions. This is a proof for all sizes and trust values, not an extrapolation from sampled computations.

## Originality — PASS within inspected evidence, provisional

Acemoglu–Como–Fagnani–Ozdaglar, *Opinion fluctuations and disagreement in social networks* (arXiv:1009.2653, first submitted 2010-09-14; published 2013), contains a general stationary second-moment linear system, so the covariance calculation is implicitly obtainable from prior theory. Their explicit star/tree examples in Section 5 analyze means for partial trust and variances at full copying, not the sharp sign of a size increment under arbitrary partial trust. The exact simultaneous results (an invariant off-diagonal moment, a trust threshold depending only on the number of stubborn leaves, and correlation increasing even when covariance decreases) require the additional specialized elimination and comparison shown here. Yildiz et al. (2013) treat binary voter copying, not general partial trust. A separate earlier exact star specialization remains possible. The near-domain prior findings on a four-agent gossip *path* and on deterministic equilibrium opinions of a *cycle* do not yield this all-size star criterion. Full-text comparative access was strongest for the original Acemoglu manuscript; the complete Yildiz paper was not obtained. This is not an independent historical-priority determination.

## Value — PASS

How the number of ordinary agents alters ensemble disagreement under fixed competing opinion leaders is a natural comparative-static question in social network dynamics. The exact threshold yields a qualitative reversal that is invisible to the mean opinion and missed by the full-copying boundary case. It also distinguishes raw covariance from normalized correlation: increasing the flexible periphery raises leaf correlation under every trust level, while decreasing the actual covariance for low trust. The result includes a complete sharp all-size classification and a persistent-common-fluctuation limit, both useful as analytic benchmarks for stochastic opinion simulators. It does not claim empirical calibration or extend to arbitrary networks or symmetric averaging.

## Closest literature and limitations

- Acemoglu, Como, Fagnani and Ozdaglar (2010 preprint; 2013 journal): general moment equations and full-copying tree case, not the explicit partial-trust size-comparison law.
- Yildiz et al. (2013): binary stochastic voter model and fixed agents, overlapping only the full-copying boundary.
- Xing and Johansson (2022 preprint): transient two-community gossip under a different update topology, not the stationary star comparison.

Residual risk: General second-moment theory already contains an implicit computational specification of these specialized covariances; another source may have solved and compared them. Verification is internal to the proof and checker; no external review or certification has occurred.

Self-review: passed. Independent audit: not yet performed.
