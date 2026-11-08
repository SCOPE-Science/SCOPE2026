# Scientific assessment

## Correctness — PASS

The single claim comprises the exact conditional distribution of missing successor-colored neighbors and its biased-color Poisson critical window, together with equivalence to time-zero primitive period three on connected graphs. The proof identifies disjoint sets of random edges for distinct source-vertex deficiency events. It then uses a uniform multinomial concentration bound, rare-Bernoulli Poisson approximation, and a direct random-graph connectivity union bound. The exact finite probability formula follows by conditioning. All quantifiers and boundaries, including \(n\ge1\), fixed positive color masses, and the connected/disconnected distinction, are explicit. Two standalone programs reproduce the ten exact finite probability cases and the critical-window simulation outputs. Finite checks do not replace the general proof.

## Originality — PASS, qualified

The closest inspected primary source is Gravner–Lyu–Sivakoff (2016), arXiv:1610.07320v1, especially Theorem 6 and its Erdős–Rényi proof. It studies eventual oscillation for \(p=\Theta(1/n)\), not the initial-period-three event at \(p=\Theta((\log n)/n)\), and does not state the conditional independent-binomial decomposition or biased-color Poisson parameter. Search comparisons considered the aliases cyclic neighbor domination, random three-color successor saturation, and isolated-vertex Poisson limits. No explicit covering mathematical claim was located. This is not proof of global priority: equivalent bipartite isolated-vertex results may specialize to the probabilistic part, and indexed coverage may omit older manuscripts.

## Mathematical value — PASS

The theorem identifies two distinct random-network scales: eventual nontrivial activity from cycles at \(p=\Theta(1/n)\) in prior work versus immediate primitive-three activity at \(p=\Theta((\log n)/n)\). The exact independent-binomial law and rarest-color coefficient exhibit how asymmetry in neuron-state frequencies shifts a dynamical threshold, an effect not visible from uniform-color heuristics. Both the finite law and the limiting window are reusable quantitative invariants of random excitable networks. No claim is made about quenched concentration or other periodicities.

## Closest work and uncertainty

Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), Sections 1–2 and 4, is the primary comparison. Generic Poisson approximation and random-graph isolated-vertex threshold arguments supply mathematical ingredients, not a documented statement of the full Greenberg–Hastings claim. The main residual originality risk is equivalence to an unindexed cyclic-domination or bipartite isolation theorem.

Self-review: passed. Independent audit: not yet performed.
