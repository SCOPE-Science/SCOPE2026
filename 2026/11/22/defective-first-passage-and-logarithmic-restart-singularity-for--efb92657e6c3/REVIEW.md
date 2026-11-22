# Scientific assessment: geometric-counting telegraph first passage

## Correctness — PASS

The two reversal rates are independent exponential variables and remain fixed within each episode, exactly as required for mixed-Poisson geometric counting. Conditional first-passage transforms follow from the two backward equations and the unique bounded spatial eigenmode. Integrating the positive-part rate difference gives the exact nonhitting probability. The one-dimensional Gaussian-tail mixture gives the logarithmic small-discount singularity, with explicit estimates of the small and large difference regions; standard renewal conditioning then yields the reset mean and both sharp endpoint asymptotics. The existence (not uniqueness) of a finite positive mean-optimal rate follows from continuity and divergent endpoint costs. The numerical checker compares different integral representations and checks parameter scaling. Independent external validation is not asserted.

## Originality — PASS, subject to the identified coverage risk

The model paper by Di Crescenzo, Iuliano, Mustaro and Verasani (arXiv:2310.10231, pp. 5–9, 27) analyzes stationary, transient and moment properties, and explicitly proposes first passage as future work. Ratanov (arXiv:2102.04905, pp. 1–5) provides fixed-rate Markov telegraph first-passage results, but not the new exponential rate mixture or its logarithmic singularity. Cinque and Orsingher (arXiv:2010.02689, introductory and model sections) treat a single-rate asymmetric-speed telegraph maximum. A 2026 Bernoulli-reset telegraph model is not the Poisson-reset, mixed-Poisson-clock protocol. Database searches comparing alias phrases and stronger claims identified related resetting and telegraph studies but no result deriving the combined defect, logarithmic asymptotic and mean-reset characterization. Similar unindexed studies may remain; this review is not a publication-priority guarantee.

## Mathematical value — PASS

The original transport model explicitly motivates first-passage analysis for searches and foraging. The new result shows that equality of mean directional reversal rates does not ensure target accessibility, identifies the mechanism in a quenched drift mixture, and quantifies the exact singular cost of rare resets plus the competing exponential cost of frequent resets. The sharp logarithmic correction is structurally more informative than a generic reset-renewal identity or a single numerical optimization point. It gives a reproducible benchmark for anomalous persistent search.

## Scope and remaining limitations

Only symmetric speeds, equal mean exponential directional rate mixtures, complete renewal upon instantaneous Poisson resets, and rightward first contact are covered. The optimum is proved to exist, not to be unique. Generic first-passage or renewal identities are not claimed as new. The accepted theorem has not undergone independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
