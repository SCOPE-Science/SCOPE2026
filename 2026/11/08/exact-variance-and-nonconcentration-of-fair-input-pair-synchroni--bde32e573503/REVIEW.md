# Scientific review

## Correctness — PASS

All hypotheses and the initial pair are explicitly fixed. The key nonstandard computation is a second-moment recurrence on the odd-order unordered-pair automaton. The transition table is checked directly from the letters; the arc-sum identities reduce the full system to an inhomogeneous one-dimensional finite difference equation. Its exact polynomial sum yields the variance without extrapolating finite data. The claim that the normalized hitting time does not concentrate is supported separately by a uniform geometric-tail bound from maximum pair mean, giving fourth-moment uniform integrability. A standalone rational pair-chain solver agrees for five independent state sizes, and symbolic substitution verifies the polynomial identity. No claim is made about full-state synchronization or even state count.

## Originality — PASS (qualified)

Gusev [1], Theorem 3.1, is the decisive comparison because the model, initial pair, and random input are identical. It covers the mean, explicitly excluded from novelty, but its complete inspected Section 3 and conclusion do not supply the second raw moment or variance. Gonze–Jungers [2] addresses optimized synchronizing probabilities and deterministic triple-rendezvous, not iid pair absorption-time fluctuations. Semantic research-record queries about the fair-input Černý pair hitting time, variance, and second moments returned related deterministic bounds and general hitting-time records, but no identified implication of this result. Novelty therefore has residual risk from other unindexed or inaccessible equivalent work; a search result alone is not a novelty proof.

## Value — PASS

The previously known cubic mean quantifies average recovery time but says nothing reliable about relative uncertainty. The sharp sixth-degree variance shows relative fluctuations remain of constant order, and a separate moment-bound argument upgrades this into the operationally meaningful failure of concentration around the mean. The identity applies to an infinite natural family of classical synchronizing automata and can serve as a benchmark for stopping-time tails and prospective distributional limit theorems. It is not a simple change of variables or routine fixed-size enumeration.

## Closest sources and boundaries

[1] V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731, Section 3. Source date: 27 April 2014.

[2] F. Gonze and R. M. Jungers, *On the synchronizing probability function and the triple rendezvous time for synchronizing automata*, arXiv:1410.4034, Sections 1–3. Source date: 15 October 2014.

The work has not received an independent mathematical audit. A future extension could characterize the full scaled absorption-time distribution; no such result is asserted here.

Self-review: passed. Independent audit: not yet performed.
