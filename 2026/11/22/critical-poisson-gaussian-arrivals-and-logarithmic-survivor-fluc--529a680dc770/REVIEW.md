# Self-review

## Correctness — PASS

The scope specifies independent Brownian motions with generator \(D\partial_x^2\), fixed initial source distance, independent exponential killing and \(q_N=\log N+c\). The analytic proof reconstructs the established defective hitting density and its normalization, changes variables to the exact successful-arrival mark density, and derives an **integrated** Edgeworth expansion with exponentially controlled tails. This yields the explicit \(0.3775032500\ldots\) first-order single-mark total-variation constant. A binomial–Poisson count coupling and the event of exactly one mark in the sign-positive density region give two-sided, process-level total-variation bounds. Finally an exact conditional-binomial formula for the population still diffusing at the first success, followed by uniform concentration on tight arrival-time windows, establishes the joint logarithmic-survivor limit. The independent numerical checker exercises 239 finite consistency conditions; none is used as proof of a limit.

## Originality — PASS, qualified

Meerson–Redner (2015) is the decisive same-model predecessor: it gives the one-particle hitting density, the full success probability, the threshold of mortal redundancy, conditional moments and finite-population success formula, which are all **prior inputs**. Paquin-Lefebvre–Delbreil–Holcman (2026) gives general finite-population first-exit and surviving-population identities, especially their Section 2.3; these identities include the exact conditional-survivor binomial mechanism and are credited. Skorski (2023) already gives standardized inverse-Gaussian normal approximation of total-variation order \(q^{-1/2}\). A published-finding corpus paper on continually *recruited* mortal searchers gives a different immigration arrival process with a distinct critical exponential waiting law. No examined full text or targeted published-finding corpus comparison stated the combined synchronized critical marked-arrival law, its **exact single-mark total-variation coefficient and sharp whole-cloud order**, or the perfectly coupled first-arrival/logarithmic-survivor limit. These new claims are not a reassertion of the known success threshold or of standard qualitative normal/Poisson approximation.

The principal originality risk is that the new asymptotic may be implicit in the strong classical *finite-parameter* formulas and standard rare-event/normal-approximation machinery, or in an unlocated work. The absence of a matching search result is not proof of novelty. No independent literature or scientific audit has been performed.

## Value — PASS

The critical window is motivated by the competing particle-number and mortality scales at which the expected number of successful arrivals stays finite. In this physically natural regime, conditional first-arrival time alone hides the population-level randomness: the newly identified log survivor-count fluctuation is deterministically the **negative** of the limiting first-arrival mark. The sharp process-level total-variation order provides a quantitative approximation for **all** successful arrival order statistics at a finite population, while the explicit \(C_*\) is a reference normalization. This closes a distribution-level and population-response gap left by fixed-killing large-population formulas, without asserting robustness to interactions, heterogeneous killing or measurement noise.

## Closest sources and scientific boundaries

- Meerson and Redner (2015), *Mortality, Redundancy, and Diversity in Stochastic Search*, DOI:10.1103/PhysRevLett.114.198101 — same geometry, known exact single-particle and survival data.
- Paquin-Lefebvre, Delbreil and Holcman (2026), arXiv:2611.14375v1 — general finite-\(N\) flux, survivor distribution and fixed-killing asymptotics; the motivating new work is restricted to a different joint scaling.
- Skorski (2023), *Normality of Inverse Gaussian* — established order of qualitative Gaussian approximation in total variation.
- *Sharp mortality–recruitment threshold for first arrivals of independent Brownian searchers* (2026), published-finding corpus — distinct continuous recruitment process with almost-sure eventual arrival.

No stability, robustness, empirical validation, or higher-dimensional extension is claimed. An implicit prior equivalent remains possible; independent publication-priority evaluation is necessary.

Self-review: passed. Independent audit: not yet performed.
