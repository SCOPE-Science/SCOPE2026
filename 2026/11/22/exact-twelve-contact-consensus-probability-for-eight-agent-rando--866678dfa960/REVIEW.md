# Scientific review: eight-agent shortest-time consensus probability

## Correctness — PASS

The general-position condition makes the event of consensus equivalent to obtaining the constant stochastic coefficient matrix. Sum of eight row entropies increases by at most two bits per pair contact and has final value 24 bits; equality at twelve contacts forces disjoint row supports. Reverse analysis of a uniform output forces each parent row to be uniform on a disjoint equal-sized half-support, inductively giving the exact state-transition rule. Conversely twelve such transitions saturate total entropy and therefore reach consensus. Thus counting these transitions is exhaustive, not a finite sample of a larger unproved search space. Two integer dynamic programs independently yield 2,528,870,400, and an unrelated rational-matrix exhaustive test on four agents reproduces the literature's 1/54. Limits: the theorem is for eight agents only and the computational integer arithmetic must be run with the provided verifier for independent reproduction.

## Originality — PASS on inspected evidence, with residual risk

The 2012 original study and its 2014 MTNS version prove the universal minimum interaction length and provide constructive optimal schedules, but do not enumerate twelve-event words in the eight-agent random model. The 2025 paper studies the **same** uniform compromise model; its Section IV explicitly identifies the minimal hitting probability as unknown beyond four agents. The new result gives its first open eight-agent case, not merely a restatement of the minimal-length theorem. Search against semantically similar published findings returned synchronous matching averages, full-horizon spectral contraction, and unrelated voter and finite-peer consensus models, without an implication of this count. General unindexed enumerations and later work are residual priority risks; absence from an index is not a proof of uniqueness.

## Value — PASS

The exact 8-agent fastest-time probability is a natural operational statistic in finite-time distributed averaging, rather than a numerically arbitrary invariant: it measures the rare-event likelihood of achieving the proven theoretical latency optimum under an uncoordinated uniform pair selector. It fills a specific explicitly identified four-to-eight-agent knowledge gap, validates the combinatorial mechanism through a complete count, and benchmarks random gossip against deterministic shortest schedules. The value claim does not require a general closed-form recurrence for all powers of two.

## Sources and limits

Shi et al. (2012, arXiv:1206.0992), full-text Introduction and Section 2; Shi et al. (2014, MTNS conference PDF), main theorem and MSC 90B10; Krapivsky–Plakhov (2025, arXiv:2509.01024), full-text Sections III–V and explicit probability gap. Limitations include no noisy communications, no multi-pair synchronous rounds, no sixteen-agent count, and possible unindexed exact enumerations. Self-review does not constitute external review.

Self-review: passed. Independent audit: not yet performed.
