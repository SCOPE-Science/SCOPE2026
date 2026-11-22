# Review

## Correctness — PASS

The fixed-opinion threshold model samples uniformly among discordant edges, then chooses either retained endpoint equally and samples a nonneighbor by positive similarity weights. With \(K_N/N\to\kappa<1\), a per-target bound \(O(1/N)\) gives \(o_{\mathbb P}(N)\) maximum degree over bounded time intervals; the target class law is uniformly \(U_{ac}+o_{\mathbb P}(1)\). The edge-count process has bounded jumps and martingale quadratic variation \(O(1/N)\), establishing the stated deterministic typed-edge ODE until discordance disappears. In the two-class case the uniform positive concordance success rate proves a stopped linear growth law. The three-class matching probabilities and their unequal limits are exact rational identities, independently enumerated by `check.py` for sizes \(3\le n\le34\). A numerical test alone is not the proof of convergence; the analytic coupling and martingale argument supplies it.

## Originality — PASS, literature-bounded

Nagel et al. (arXiv:2606.25872v1), especially their threshold-update steps and equations (21)–(26), and Appendix D, develop an approximate *scalar* graphon balance under a uniform-within-domain step ansatz. They explicitly do not supply a rigorous microscopic-to-graphon convergence proof (Appendix D). Their scalar closure does not imply a rigorous sparse-class fluid limit or the sharp two-versus-three-class universality boundary. Kan, Feng and Porter (2023) instead allow opinion coevolution; Chodrow and Mucha (2020) consider binary adaptive voter models with opinion updates and approximate moment closures. Cárdenas-Sabando et al. (arXiv:2511.15043) address fixed states and a related active-link mean-field, but only its abstract could be inspected; it remains a specific historical-priority risk. Searches for variants of 'lumpability', 'two versus three opinion classes', 'edge-type fluid' and 'homophily sparse closure' did not reveal an equivalent published claim. Absence from search results is not proof of priority.

## Value — PASS

The motivating 2026 model identifies global concordance as a useful collective variable. It matters mathematically whether this variable is a universal exact evolution coordinate or a successful approximate statistic for certain ensembles. This theorem identifies a natural sharp class-count boundary, supplies a rigorous sparse state-space reduction at the level of class-pair edges, and exhibits identical initial global concordance but genuinely different order-one macroscopic speeds. The distinction guides which additional coarse observables are needed when the opinion distribution is multimodal. The counterexample is not an assertion that the published approximation is inaccurate on the random-graph ensembles it studied.

## Closest literature and limitations

- Nagel et al. (2026), arXiv:2606.25872v1, Sections II.B, V.B and Appendix D: original stochastic model; step-graphon scalar approximation, not this exact sparse class-pair limit.
- Kan, Feng and Porter (2023), DOI 10.1093/comnet/cnac055: homophilic adaptive bounded-confidence opinion dynamics, but opinions coevolve.
- Chodrow and Mucha (2020), DOI 10.1137/18M1232346: binary adaptive voter moment closure with opinion updates; not this absorbing fixed-opinion threshold dynamics.
- Cárdenas-Sabando et al. (2025), arXiv:2511.15043: abstract-only source inspection, residual historical-priority risk.

The theorem is conditional on strictly positive affinities, all distinct classes separated by tolerance, finite class count, sparse bounded-average-degree graphs and initially sublinear maximum degree. The three-class obstruction is existential; no claim is made about all opinion distributions. Further independent literature review and proof checking remain desirable.

Self-review: passed. Independent audit: not yet performed.
