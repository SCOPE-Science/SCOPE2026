# Scientific review: A sharp storm-concentration crossover in periodic surface-pollutant wash-off

## Correctness — PASS

The two-stage affine return map has strict contraction factor \(s_1s_2<1\), since each cycle has positive total rainfall. Solving its fixed point and integrating the two dry intervals gives \(\overline B=(aT/4)(1+s_1)(1+s_2)/(1-s_1s_2)\), which exactly specializes to the claimed hyperbolic means. For \(c=2^{p-1}>1/2\), \(G_p(x)=\coth(x/2)/\coth(cx)\) is strictly decreasing because \(\sinh z/z\) strictly increases. With endpoint limits \(2^p\) and \(1\), all parameter cells and equality boundaries follow. The \(p=2\) threshold reduces exactly to \(\cosh^2x-\cosh x-1=0\). Replaying the supplied standard-library checker reports 38,553 supplemental assertions; they are numerical cross-checks, not the infinite proof.

## Originality — PASS on inspected evidence

The closest fully inspected research includes the stormwater decision-support model in Vinck et al. (2023) and the published mathematical results *Sharp three-stage stormwater exposure ordering with continued pollutant supply*, *Periodic leaching minimizes stationary salt mass: a renewal convex-risk law*, and *Two sharp patch-allocation transitions for a generalized Type III feeding response*. Their actual hypotheses respectively concern empirically simulated buildup/wash-off, fixed-rate order permutations and exported exposure, renewal event timing at fixed retention, and Hill-type prey allocation. None states or implies the fixed-total-rain, event-depth-dependent, stationary-mean crossover by mere parameter restriction. Source title matching is not used as a novelty test; the comparison is by objects, quantifiers and implications. The motivating Mao et al. (2024) primary text was unavailable beyond its bibliographic abstract, so this finding's historical priority is provisional, not independently certified. See AUDIT.json for query strings, source inspection material and residual risks.

## Value — PASS

The sharp distinction between sublinear/linear and superlinear rain-dose responses identifies the precise mechanism under which concentrating a fixed rain quantity can outperform splitting it. The explicit analytic crossover, and the special quadratic golden-ratio value, give a complete structural comparison for two canonical periodic storm patterns rather than a single computed point. The result is a motivated conceptual benchmark for hydrological surface-wash modeling; it is not a proven operationally optimal rain schedule and has no field-calibrated parameters.

## Limits of this review

One claim is reviewed across all three criteria. No independent audit was performed. The theorem concerns retained surface burden, not total washed-off pollutant mass; conservation makes the latter equal to \(aT\) per period for either pattern. The model ignores event duration, variable deposition and physical sediment dynamics, and the most closely matching 2024 paper's full article and appendices could not be inspected. A possible earlier mathematical equivalence remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
