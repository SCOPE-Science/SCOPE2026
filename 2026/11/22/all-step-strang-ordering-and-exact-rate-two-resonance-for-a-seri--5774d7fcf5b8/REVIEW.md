# Scientific review

## Correctness — PASS

The theorem concerns a single exact exponential Strang step for two serial Markov transitions, with rates \(a,b>0\) and duration \(h>0\). Row-sum conservation reduces the total-variation distance for any initial probability \(p\) to \(p_0\) times a terminal-probability error. The exact terminal distribution is the two-exponential sum CDF; each Strang orientation has a rectangle-product CDF. The reflection of two cross quadrants in the \([0,h]^2\) waiting-time square proves the strict true-CDF-above-average inequality for any strictly decreasing positive waiting-time densities. The factorization of the two Strang CDFs orders them by rate. Exact signed differences are proportional to differences of the even strictly increasing-in-absolute-argument \(\operatorname{sinhc}\) function, fixing their signs and their only positive-rate zeros. These steps justify the all-time ordering, rate-two exactness, and stated large-time asymptotic. The actual `verify.py` program passed 3,937 supplementary high-precision cases, including independent stochastic matrix multiplication and rate-two identities. Finite checks are not treated as proofs.

## Originality — PASS (qualified)

Engblom, *Strong convergence for split-step methods in stochastic jump kinetics* (arXiv:1412.6292, 2014/2015), was inspected in the full available PDF, including §4.3.3 and the conclusions. The text sets out the symmetric splitting and analyzes stochastic strong/weak convergence, but does not give the present universal comparison of the two placements for a serial irreversible three-state chain or exact rate-two matrix coincidence. Mitra, Diddens and Heuer (2026, DOI 10.1007/s10910-026-01780-x), was inspected in open HTML including its three-state model and Appendix 1. It studies coupled reversible reaction/diffusion dynamics, different performance measures and corrected reaction probabilities, not the present two irreversible serial transitions with exact total-variation comparisons. Lukassen and Kiehl (2018, DOI 10.1002/pamm.201800026) address chemical splitting and stiffness; only their abstract was accessible, leaving a residual priority risk. Queried research records on Markov splitting concerned directed cycles, exact three-factor compositions for two-state generators, and extrapolation positivity, none of which logically implies this serial-chain result. Historical priority is not independently certified. Closely related full texts might still exist.

## Value — PASS

The model is the minimal serial reaction chain with a genuine choice between two Strang orders. The theorem supplies a uniform-in-step global rule in a meaningful matrix norm, rather than just a cubic-order local-error heuristic, and identifies a surprising exact whole-matrix resonance when the fast rate is twice the slow one. The strict sign diagram explains when the better orientation overshoots rather than undershoots, and the wrong order may have an exponentially larger long-step error. This exact benchmark can inform reaction subflow ordering and testing of splitting codes. It does not claim general-network transfer or a paper-scale numerical algorithm.

## Limitations and closest literature

The only stationary states of this chain are absorbing, so this is a transient single-step result, not an equilibrium or multiple-step approximation theorem. The strongest access limitation is the abstract-only 2018 Lukassen–Kiehl source. The Engblom PDF and 2026 open article are actual inspected primary material; their different objects/claims do not by themselves prove historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
