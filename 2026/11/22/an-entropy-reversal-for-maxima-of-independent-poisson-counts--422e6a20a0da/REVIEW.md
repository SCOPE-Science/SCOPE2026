# Review: entropy reversal for independent Poisson maxima

## Correctness (C): PASS

For every fixed integer \(m\ge2\), the exact mass identity \(r_k=F_k^m-F_{k-1}^m=p_kA_{m,k}\) yields an exact entropy comparison. A small-intensity expansion isolates the zero/one masses and bounds the entire remaining entropy tail. At large intensity, expectation-controlled Stirling expansions and the probability-integral transform establish the stated Gaussian-maximum limit. Strict Gaussian Poincaré and the normal maximum-entropy inequality show the constant is negative. The continuity and intermediate-value arguments establish existence, not uniqueness, of a zero. Re-running the self-contained `checker.py` checks representative finite values and an exact two-sample constant, but finite computations are not used as the infinite proof.

## Originality (O): PASS (historical priority qualified)

Badiella, del Castillo and Puig (2023), DOI 10.1016/j.spl.2023.109900, prove ultra-log-concavity and underdispersion for Poisson order statistics; they do not compare the Shannon entropy of a maximum with its parent. Their complete four-page open-access paper, including the theorem and corollary, was inspected. Braiman et al. (2024), DOI 10.15388/namc.2024.29.35560, study Shannon and Rényi entropy of the *parent* Poisson law across intensity, not the maximum; their full open-access paper was inspected. Balakrishnan, Buono and Longobardi (2021), DOI 10.1007/s11009-021-09850-0, study distinct *cumulative entropy* functionals of continuous order statistics. Prior published calculations of two-Poisson-maximum variance transitions and Fano limits do not logically determine entropy comparison, which is a distinct functional, nor the family of exact Gaussian maximum-entropy constants. Searches for synonym formulations and dominating entropy theorems disclosed no established equivalent result, but this absence is not a proof of historical novelty.

## Value (V): PASS

The extreme observation is the statistic used when retaining the largest of replicated count measurements. Although order-statistic ultra-log-concavity and underdispersion are known, neither entails whether taking the maximum raises or lowers Shannon entropy compared with a single measurement. Showing opposite signs at two intensity regimes for *every* fixed sample size, and supplying the exact high-intensity information deficit, resolves a structural ambiguity that moment comparisons alone leave open. The result does not claim a unique crossover or a location for it.

## Limitations and risks

The proof addresses only iid common-rate Poisson maxima with fixed sample size. It does not establish the number of crossings or handle unequal rates, other order statistics, or growing sample size. The entropy constants for sample sizes above two are given by explicit convergent normal integrals. A historically earlier or unindexed equivalent entropy comparison could exist; independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
