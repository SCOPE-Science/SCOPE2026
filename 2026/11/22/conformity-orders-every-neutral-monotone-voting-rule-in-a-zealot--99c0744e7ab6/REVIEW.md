# Scientific review

## Correctness — PASS

The claim is exact for every finite electorate, positive source weight pair, stationary inertia \(\ell<1\), and every coordinatewise monotone self-dual binary aggregation rule. The full-vector beta-mixture representation follows from the cited source's unique, permutation-invariant stationary count law. Conditioning on the absolute beta deviation yields a sign probability independent of the common beta-shape shift. The absolute deviation has a strict decreasing likelihood-ratio ordering as that shift increases. For every permitted voting rule, the Bernoulli product expectation is strictly increasing, and self-duality yields exactly the required signed integrand. This proves all strict comparisons and the balanced and fair boundaries. Exact-rational checks in the included standalone program corroborate but do not replace the proof.

## Originality — PASS (literature-bounded)

The closest full text, Braha and de Aguiar, arXiv:2607.14288, proves the stationary beta–binomial law and different finite-size/asymptotic comparisons; it does not state or imply strict **conformity-parameter ordering uniformly over all monotone self-dual voting rules**. The public reading note at https://pith.science/paper/2607.14288 explicitly identifies a variable-conformity large-population beta limit. That is acknowledged prior material, excluded from the new claim. Berend–Sapir (2007) study monotonicity as committee size changes, and Arab–Oliveira–Wiklund (2021) compare beta law orderings and threshold probabilities, but their stated results are not the shared-additive-beta-shape aggregation order proved here. The latter paper's openly available sections on stochastic orders, main results and applications were inspected; Berend–Sapir's available abstract was inspected but not the full journal text. Consequently a historic equivalence not detected in the searches remains a residual priority risk, not a claim of independently established novelty.

## Value — PASS

The result resolves a natural finite-electorate sensitivity question left open by the primary paper's fixed-conformity results: is the accuracy ordering seen in simple majority tied to that particular rule or to the social influence mechanism? The answer is rule-uniform across the broad natural class of monotone label-neutral decisions, including unequal voter weights and hierarchical aggregation. The proof isolates the invariance of the conditional beta sign and a strict monotone-likelihood-ratio order, so it is structural rather than a numerical improvement. The reversed sign under wrong-side leader advantage is equally important when interpreting increased conformity.

## Closest literature, limitations and remaining risks

The most relevant source, arXiv:2607.14288, was inspected in its actual public full text including its model, Theorems 1, 3, 5, 6, and proofs. The other readings and the precisely scoped novelty comparisons are documented in AUDIT.json. The model assumes a stationary fully mixed population, positive exogenous leader weights, and a self-dual monotone rule; it asserts nothing general for nonneutral electoral rules, transient trajectories or heterogeneous social networks. Priority could be affected by inaccessible older dependent-jury literature. Computer checks are finite evidence only; no independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
