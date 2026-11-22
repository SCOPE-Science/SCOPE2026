# Scientific review: Universal inverse-distance germination penalty in a heterogeneous habitat corridor

## Correctness — PASS

The exact formula follows from a geometric first-step identity at each unsuitable patch and at the suitable target. Logarithmic differentiation gives a strictly decreasing positive stationarity function, with endpoint limits of infinity and zero, hence a unique global maximum. Appending a patch adds a strictly positive summand and strictly raises optimal dormancy. A habitat-specific policy maximizes every traversing factor and target germination separately. Uniform Taylor bounds for \(A_j\le1-\varepsilon\) establish \((1-q_n)K_n\to1\) and the exact relative factor \(1/[e(1-s_0)K_n]\). The singular target-survival boundary is treated separately. A standalone standard-library script independently tests finite-horizon recursions and analytical formulas on many heterogeneous examples; it cannot replace proof of infinite claims.

## Originality — PASS on inspected evidence

A publicly posted March 2021 preprint (Szojka and Germain) and its March 2024 journal version motivate transport of dormant seeds through unsuitable matrix habitat, but their empirical findings do not establish the corridor-wide unique optimizer, patch-append monotonicity, or heterogeneous inverse-distance cue penalty. The inspected Satterthwaite (2009), Chen et al. (2020) and Pausas et al. (2022) primary texts concern dormancy fitness, trait covariation and cue strategies without this hitting-probability law. The Venable–Lawlor (1980) abstract concerns escape in space and time; its full text was inaccessible, so historical priority remains provisional and full-document noncoverage is not asserted. Standard absorption and geometric-series calculations are explicitly credited as prior methods. Searches of related seed-bank growth optimization, absorbing-chain first passage and spatial dispersal results found no demonstrated covering implication; search absence is not a novelty certificate.

## Value — PASS

The exact distinction between germination based on habitat cues and one common germination fraction is biologically motivated by dormant seeds traversing unsuitable landscape matrices. The theorem supplies a complete finite-length strategy classification and a genuinely heterogeneous asymptotic: even when patch transport/survival vary arbitrarily within a natural bounded-retention class, inability to recognize the target adds the sharp \(e^{-1}/K_n\) inverse-distance penalty to an already decaying establishment probability. This quantifies a previously qualitative landscape-connectivity mechanism, while leaving field prediction and population-level fitness outside scope.

## Closest literature and limits

Szojka and Germain: https://doi.org/10.1101/2021.03.22.436493 (public preprint 23 March 2021) and https://doi.org/10.1002/ecs2.4814 (2024 journal article); Satterthwaite: https://doi.org/10.1007/s11258-009-9696-y; Venable and Lawlor: https://doi.org/10.1007/BF00540137; Chen et al.: https://doi.org/10.1111/ele.13595; Pausas et al.: https://doi.org/10.1111/nph.18436.

The proof does not include backwards dispersal, reproduction during crossing, adaptive site sensing beyond the stated comparison, environmental correlations, a deadline, or evolutionary optimality. Full-text historical priority comparison is incomplete, and independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
