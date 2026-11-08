# Review of the finite-population neutral-corner theorem

## Correctness — PASS

For every \(N\ge3\) divisible by three, the per-agent Bernoulli implementation gives conditional triple output distributions \(\operatorname{Binomial}(3,a/3)\) and \(\operatorname{Binomial}(3,1-a/3)\) at the two corners. A uniform three-subset has exact mixed probability \(3k(N-k)/[N(N-1)]\). The law of total variance gives \(2k(N-k)/[3(N-1)]\); the quadratic disagreement observable is then an exact one-step eigenfunction with factor \(q_N\), and bounded martingale convergence proves the terminal probabilities. Survival estimates use only the exact finite-state bounds on that observable. Exact-rational transition enumeration for sizes \(N=3,6,9\) agrees with these formulas. A computation alone would not establish the all-size theorem; the analytic argument does.

## Originality — PASS (with residual literature risk)

The April 2026 source specifies ratio-dependent independent agent activations but studies a deterministic density map, not finite-population consensus waiting times. Toth–Galam's earlier group-decision local-flip paper explicitly identifies the identity-map point; that known map fact is not the novelty claim. The July 2026 microscopic paper analyzes eight-state irreversibility for uniform contrarians, not these two parameter corners and the exact multi-triple variance. Prior record and literature comparisons did not identify an implication covering the exact \(q_N\) and finite-state duality. General neutral-drift martingales are a close analogy; they do not by themselves determine the update-specific conditional variance. Unindexed equivalent results and alternative finite implementations remain live originality risks.

## Mathematical value — PASS

The density-map identity and involution are highly singular regimes in a recent sociophysics phase diagram. The new exact finite-size law resolves what actually happens under an explicitly specified stochastic population implementation: stochastic consensus despite density-level neutrality, a population-size dependent relaxation eigenvalue, and an alternating absorbing phase at the reversal point. This gives a precise baseline for finite-size modeling and for distinguishing independent individual opposition from common group flips. It is not a generic assertion that random systems fixate, nor a claim of global behavior at other parameter values.

## Scientific limits

The full all-size result depends on uniform independent reshuffling, independently activated choices for each agent in each triple, and population size divisible by three. The exact hitting-time distribution is not determined outside the special three-agent example, and no claim of a new deterministic identity/involution map is made.

Self-review: passed. Independent audit: not yet performed.
