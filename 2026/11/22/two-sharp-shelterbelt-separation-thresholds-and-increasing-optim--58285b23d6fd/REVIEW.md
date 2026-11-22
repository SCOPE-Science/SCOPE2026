# Scientific review

## Correctness — PASS

The wind-speed response is explicitly defined at every row, including coincidences. Formula (1) follows by integrating each exponential relaxation contribution. The exact derivatives in (2) uniquely maximize over the second row for fixed third-row position. The reduced function \(F_E(y)\) is strictly increasing, has \(F_E(E)<E\) and \(F_E(1)=a(2-a)\), and its crossing of \(E\) gives the unique global optimum. The second transition follows from a strictly monotone branch condition. The inequalities for three consecutive gaps follow from the two stationarity equations and \(a(2-a)<1\). All boundaries \(0<a<1\), \(0<E<1\) and equality cases are included. A standalone checker independently reproduced the integral and passed 83,416 assertions. Numerical sampling is corroboration, not proof.

## Originality — PASS (subject to historical priority)

The exact claim is the complete global optimizer for three sequential identical wind-speed barriers with exponential recovery over a finite field, including both horizon thresholds and strict increasing-gap ordering. The original 1953/1956 USDA-reprinted primary papers were read and concern measured wind-tunnel protection and empirically prescribed row spacings, not the stated analytic optimizer. The accessible 2002 Zhu–Jiang–Matsuzaki article abstract concerns physical porosity and threshold design; its full text was unavailable, leaving a specific historical risk. Full-text primary discussions from 2022 and 2024 are also based on field experiments, wind-speed thresholds, and large-eddy simulations, rather than the exact three-jump integrated criterion. Related exponential-decay spacing, runoff, and firebreak formulations have different state laws, horizons, or objectives and do not imply this statement. General impulse-control theory may contain an equivalent result; novelty is not independently certified.

## Value — PASS

An area-integrated measure of wind protection was scientifically motivated by early shelterbelt studies. This model's exact two critical field lengths distinguish three genuinely different placement regimes, demonstrate strict uniqueness, and refute naive equal-gap planning for a concrete exact example. The robust inequalities also identify where the idealization becomes physically misleading: some optimum rows coincide and the increasing gaps are not universal in atmospheric flows. This is a reusable analytical benchmark for comparing more realistic design models, not a calibrated forestry prescription.

## Closest literature and scientific limits

Woodruff–Zingg (1953), Woodruff (1956), Zhu–Jiang–Matsuzaki (2002), Sun and collaborators (2022), and Wang and collaborators (2024) are discussed with URLs in `RESULT.md`. The 1953 and 1956 lawful reprints were examined in full; 2002 was assessed from abstract and bibliography only. No empirical or independent proof audit has been performed.

Self-review: passed. Independent audit: not yet performed.
