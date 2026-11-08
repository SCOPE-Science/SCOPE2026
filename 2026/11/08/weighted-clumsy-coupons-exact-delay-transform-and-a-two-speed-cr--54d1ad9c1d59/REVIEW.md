# Scientific review: weighted clumsy coupon completion

## Correctness — PASS

The finite transform rests on a conditional independence argument at the ordinary cover time, the explicitly checked stationary product law of random-scan refresh, the all-present return probability, and an exact first-hitting renewal identity. Differentiation produces the finite delay mean. The two Schur-convexity conclusions follow from opposite strict curvatures of the two logarithmic product integrands, with all selection weights strictly positive. For the two-speed limit, independent Poissonized coupon clocks yield the slow-class Gumbel law, while the exact finite delay transform yields the limiting Laplace transform by dominated convergence. A stationary two-class immigration–death process has that transform by the strong Markov renewal identity. Finite independence gives the independent-sum limit. The Jensen comparison proves a strict positive delay gap for distinct normalized speeds. The packaged `verify.py` passes 1,168 exact-rational/numeric finite checks; computations do not stand in for the infinite proof.

## Originality — PASS, with residual historical risk

Attrill and Garoni (arXiv:2605.14206v1, Theorem 4.10) state the critical law for uniform coupon selection only. Long (arXiv:2605.14511v1, Sections 3.6 and 4) treats unequal selection in a global-reset model, not in the clumsy single-type refresh model; his clumsy result uses uniform selection and fixed loss probability. Anceaume–Busnel–Sericola (arXiv:1402.5245, Theorem 5) optimize ordinary monotone coupon collection, not post-cover loss. Makowski's 2001 M/G/∞ queue theory covers important generic busy-period identities and comparisons, not a coupon critical limit with heterogeneous draw frequencies. The finite stationary hitting resolvent is an application of a standard renewal identity, not presented as an independently invented general principle. The joint finite-weight optimization and two-speed critical limit were not found in the inspected sources. Priority is provisional because a broader random-scan heat-bath or marked infinite-server theorem might imply parts of the result.

## Mathematical value — PASS

The source's critical nonmonotone collection law is exact but restricted to equal sampling rates. Unequal coupon popularity changes both the classical cover-time scaling and the subsequent defective-coupon dynamics: the slowest positive-mass class governs the Gumbel center while *both* classes contribute to the stationary emptying delay. Exact finite transforms make those contributions explicit, and strict Schur-convexity identifies uniform sampling as the optimal choice of rates for every finite population and common loss probability. The nonzero, quantified delay-heterogeneity gap is meaningful for sampling or update scheduling. This concerns a natural transition between coupon collection and finite-server/immigration–death asymptotics, not an arbitrary parameter slice.

## Closest published work and boundaries

- Attrill–Garoni, *The clumsy coupon collector's problem*, 2026, arXiv:2605.14206v1, Lemma 4.2 and Theorem 4.10: uniform-selection baseline.
- Long, *Clumsy and Careless*, 2026, arXiv:2605.14511v1, Sections 3.6 and 4: distinguish global-reset unequal sampling from clumsy uniform sampling.
- Anceaume–Busnel–Sericola, *New results on a generalized coupon collector problem using Markov chains*, 2014, arXiv:1402.5245, Theorem 5: ordinary monotone unequal coupon optimization.
- Makowski, *On a Random Sum Formula for the Busy Period of the M/G/Infinity Queue with Applications*, 2001, TR 2001-9, Sections 2–5: standard queue busy-period and convex-order background.

Limits: strictly positive fixed class rates and masses, common erasure parameter, and two fixed speed classes; no moment claim for the centered total time, no full-law stochastic-order claim, no independent mathematical or historical certification. The finite verifier tests identities but cannot establish weak convergence or exhaustive novelty.

Self-review: passed. Independent audit: not yet performed.
