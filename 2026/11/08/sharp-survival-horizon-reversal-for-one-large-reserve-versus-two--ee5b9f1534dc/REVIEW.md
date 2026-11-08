# Review of the reserve survival-horizon classification

## Correctness — PASS

The transient occupancy generator gives the exact two-exponential survival law, which is independently reconstructed from the resolvent. Its strictly increasing hazard yields at most one positive survival-curve crossing, and the tail exponent determines whether that crossing occurs. Exact mean integrations and symbolic threshold subtraction show a nonempty ranking-reversal interval for every positive area exponent. The `verify.py` checker completed 401 symbolic and high-precision numerical assertions, including independently generated Markov matrix exponentials. The analytic proof, not the finite tests, establishes the universal statement.

## Originality — PASS within inspected material, with residual priority risk

Etienne and Heesterbeek (2000) directly motivate equal-total-area reserve comparisons and consider \(R_0\) and mean extinction time, but their inspected full-text framework does not give the proposed exact full-distribution comparison. Nicol and Possingham (2010) optimize restoration policies at finite and infinite horizons; its complete main text and appendices could not be accessed, so a concealed special-case formula is not excluded. Helmstedt et al. (2014) focus on economic reserve-fencing cost rather than the stochastic occupancy survival distribution; complete text was also unavailable. Trouillier et al. (2023) compare viability criteria using simulated population trajectories, not this exact two-state threshold law. The finding does not claim the elementary two-state resolvent or the general idea of conflicting viability metrics as new. The claimed difference is the sharp one-vs-two, all-horizon crossing classification with the precisely \(e\)-wide gap between mean and tail thresholds. Search failure is not proof of absolute novelty; historical priority remains provisional.

## Value — PASS

In fixed-area habitat fragmentation, optimizing expected extinction time and requiring persistence at a long fixed deadline are both natural but different decisions. The theorem gives an exact, nonempty and all-exponent parameter region where these legitimate criteria recommend *opposite* configurations, not merely a numerical anecdote or tiny improvement. It supplies a benchmark separating extinction-tail risk from mean-lifetime gain in an explicitly defined minimal model.

## Scope and risks

The statement is proved only for two independent smaller patches initially occupied, local exponential extinction scaling as an inverse power of patch area, one-step recolonization at constant rate, and no immigration. It is not a full landscape or policy optimizer. The most material historical risk is partial access to Nicol and Possingham (2010), although the accessible abstract describes a distinct stochastic dynamic-programming intervention setting. Neither simulation checks nor partial literature access establish independent priority.

Self-review: passed. Independent audit: not yet performed.
