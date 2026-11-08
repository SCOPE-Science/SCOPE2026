# Self-review

**Finding:** Entropy-barrier selection and exponential consensus latency in two-layer coordination games.

## Correctness — PASS

For \(1\le a<b\le N-2\), a focal person's payoff difference under the two coordination games is the number \(j\) of \(A\)-neighbors minus \(a\) or \(b\). Inside \(a+1\le i\le b\), environment selection exactly resamples a random player as a Bernoulli-\(p\) action, and outside the interval the population moves monotonically to unanimity. The harmonic resistance formula, Green kernel, and coupon-collector cleanup means solve the finite problem without omitted boundary cases. Stirling's formula and bounds on the positive Green sum prove the logarithmic consensus-time and rare-winner exponents. The activity crossover has exactly one root because the difference of the two binary relative entropies is strictly decreasing. An independent labeled-state transition enumerator established 33,270 Bellman equalities over 249 rational parameter cases. Finite enumeration does not establish the theorem; the written proof does.

## Originality — PASS, with residual priority risks

The initiating two-layer game [1] defines the asynchronous update and discusses its fully overlapping configuration, but its inspected main article reports numerical BR outcomes rather than these finite probability formulas and large-deviation selection law. General robust-consensus results [2] imply qualitative agreement in appropriate regimes but do not supply the winner probabilities, exponential consensus-time law, or sharp relative-activity threshold. Classical urn theory [3] supplies known reversible-chain methods; these generic techniques are expressly not claimed as novel. Search comparisons for aliases (heat bath, Ehrenfest, switching thresholds, metastability, coordination games) and indexed public scientific records found no equivalent or stronger covering statement. The separate supplementary material to [1] could not be read, and a matching unindexed result cannot be ruled out.

## Value — PASS

The precise question is motivated by the literature's long-lived mixed outcomes when contexts favor opposite conventions. Although either fixed environment alone reaches unanimity in at most a harmonic coupon-collector mean \(NH_N\), their random switching creates exponential expected latency. The result determines how long this effect persists as population grows, supplies exact finite-N benchmark probabilities, and identifies when a small change in the frequency of one context causes asymptotically almost-sure selection of the opposite convention. Complete layer overlap and complete connectivity are explicit structural assumptions; the result is not extrapolated to arbitrary graphs. The unique activity threshold is mathematically and substantively meaningful for the source model.

## Closest literature and limits

[1] Raducha–San Miguel, arXiv:2212.08877v1 (2022), full readable main article arXiv:2212.08877v2.

[2] Arditti–Como–Fagnani–Vanelli, arXiv:2109.12685 (2021), qualitative robust consensus.

[3] Xin–Cui–Zhao–Yao, arXiv:1810.04219 (2018), generic Ehrenfest hitting times.

[4] Raducha–San Miguel, arXiv:2110.10036 (2021), related single-layer coordination.

The theorem excludes partial overlap, sparse layers, nonlinear imitative rules, non-independent context switching, and general time-varying clocks. The supplemental PDF of [1] was inaccessible and has not been used to assert noncoverage. The case where the two entropy barriers coincide is not assigned a universal limiting winner probability; subexponential details matter.

Self-review: passed. Independent audit: not yet performed.
