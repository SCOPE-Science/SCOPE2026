# Scientific review: sharp two-compartment Haldane allocation law

## Correctness — PASS

The normalization \(s=\sqrt{K_sK_i}\,u\) has an explicitly positive multiplier and preserves maximizing assignments. The derivative factorization is reproduced with exact symbolic algebra by `verify_haldane.py`; the polynomial signs are proved for every positive parameter rather than sampled. Its strict convexity and the two endpoint signs yield either strict monotonicity or one interior maximum. The quadratic discriminant gives the precise optimizer. The implicit-function derivative and large-mean expansion prove both asymptotic statements. This includes the equality and fully concentrated boundary cases. The checker passed 10,667 checks but is not an infinite proof.

## Originality — PASS, provisional

The fixed-sum **independent** two-compartment objective and its complete threshold/optimizer/asymptotic classification were compared to published substrate-inhibition kinetics, bioavailability transport, serial bioreactors and related resource-allocation claims. The closest physically relevant full-text article, Gharasoo et al. (2015), computes a crossover between single-compartment inhibitory degradation kinetics and mass-transfer-limited kinetics. It does not maximize \(f(s_1)+f(s_2)\) under \(s_1+s_2\) fixed. Reed et al. (2010) discuss physiological functions of the single-site inhibition curve. Abu Reesh (2021) and Stacey–Shepherd (2022) study serial, flow-coupled reactors with a different objective. Published resource-allocation findings involving monotone Hill inhibition, Type-III predator functional responses, or dispersal do not imply the Haldane hump's exact allocation threshold from the inspected claims. Searches and scientific comparisons are documented in `AUDIT.json`. Main unresolved historical risk: a general nonconcave allocation or convex-envelope theorem might dominate the special two-point result; absence from search results alone is not uniqueness evidence.

## Value — PASS

Under substrate self-inhibition, a single site's growth-rate peak does not mark the onset of a benefit from unequal feeding. The theorem gives an exact, *higher* fixed-mean threshold and a fully specified global allocation for all positive kinetic parameters. It rules out complete substrate concentration as optimal, proves a square-root transition, and identifies the high-budget asymptote at the individual maximum-response concentration. This supplies a reference test for spatial substrate heterogeneity and two-site feeding heuristics; unlike a derivative-only exercise it classifies the entire feasible design set with boundary cases and a physically motivated invariant. The two-compartment idealization is explicit; neither clinical nor field validity is claimed.

Self-review: passed. Independent audit: not yet performed.
