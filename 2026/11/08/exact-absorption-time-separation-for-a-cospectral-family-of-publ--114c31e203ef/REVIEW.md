# Mathematical review

## Correctness — PASS

The update rule at unit externality and all-zero initial activity is a monotone random maximal-independent-set process. The star has a direct coupon-collector hitting time. For the other graph, independent rate-one Poisson clocks establish the bipartite first-choice law, isolate completion time, and the identity between expected clock time and expected update counts. Integrating its exact exponential distribution gives a finite beta sum. Bonferroni and harmonic-number estimates give the stated unbounded \(m-2\log m+O(1)\) step gap. A separate, exact-rational recurrence checks orders \(m=2\) through \(8\), plus graph-state recursion for \(m=2,3\). The proof, not those tests, establishes arbitrary \(m\).

## Originality — PASS, with residual risk

Misiak and Dziubiński (arXiv:2602.15986v1, Sections 2 and 3.2.2) introduced the update model and already showed simulated different convergence rates on the five-node cospectral pair. Hence the existence of cospectral convergence distinctions is prior knowledge. The new claim provides exact hitting-time expectations for a natural infinite cospectral family and their rigorous asymptotic absolute gap. Krivelevich et al. (DOI:10.1002/rsa.21200) and the publicly available random-greedy independent-set results on complete multipartite and threshold graphs characterize terminal greedy sets rather than the count of repeated updates until equilibrium. Relevant full texts and claim-level searches found no covering calculation; equivalent waiting-time identities under random sequential adsorption remain a realistic indexing risk.

## Mathematical value — PASS

Exact expected convergence time matters for computational costs of decentralized public-good adjustment. The first nontrivial cospectral pair in the motivating paper becomes a computable infinite family with a growing, explicitly quantified step gap. This separates adjacency-spectral information from an actual hitting-time observable rather than solely terminal equilibrium counts. The difference is only order \(\sqrt N\), not a fixed fraction of the order \(N\log N\) convergence time; disconnected comparison graphs and the special endpoint are substantive limitations.

## Evidence and limits

Reproduction: run `python check_absorption.py` with Python 3 standard library. The proof applies to every integer \(m\ge2\); the checker covers finitely many values as corroboration. Source text and two nearby publicly available independent-set findings were compared at the level of claims, not just titles. The exact final statement is bounded by the stated initial condition, update protocol, externality and graph class.

Self-review: passed. Independent audit: not yet performed.
