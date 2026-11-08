# Self-review: optimal Rayleigh triangle hitting law

## Correctness — PASS

The deterministic bound \(a(G)\le4e(G)/3\) is established by complete connected-component cases and is attained by disjoint copies of \(P_4\). The conditional hazard bound is valid for every adaptive strategy, including randomized strategies. The constructive strategy counts exactly one new reserved \(P_4\) for every three productive, previously unused offers. Nonproductive offers have expected count at most \(j(j-1)/n\) on survival, giving \(O_L(n^{-1/2})\) loss compared with the product lower bound. Finite exhaustive and seeded tests corroborate the graph inequality and construction. The proof explicitly retains distinct edges and permits repeat-edge choices, so no false simple-graph assumption is imposed on other strategies.

## Originality — PASS, with residual historical-priority risk

The fully adaptive process is already defined in Ben-Eliezer et al. (arXiv:1805.02259). Their Theorems 1.10–1.11 and Claim 5.1 establish the \(\sqrt n\) hitting-time order and an upper bound based on at most \(2j\) potentially incident vertices, but neither the sharp \(4j/3\) active-vertex extremum nor the Rayleigh limiting quantile. Akhmejanova–Kupavskii (arXiv:2610.33854v1), Theorem 3 and Section 4.1, prove analogous order of growth across candidate-set sizes and a growing-multiplier high-probability construction, not an exact fixed-probability first-triangle limit. Gao–Koerts, DOI:10.1002/jgt.23202, address pre-/post-positional comparison at the order-of-growth level. Relevant independently indexed previous-claim search and accessible earlier own claims found no statement logically covering the asserted sharp distribution. This is a best-knowledge originality assessment; a historical source not located could still cover the result.

## Value — PASS

The finding identifies the first exact optimal fixed-probability threshold profile for a natural small subgraph in the fully adaptive random-vertex process, including its sharp constant. The \(4/3\) exposure bound is a structural optimization inequality and the constructive \(P_4\) packing proves it achievable despite adaptive random offers. The result converts a high-probability \(\Theta(\sqrt n)\) scale into an exact limiting distribution for every quantile, directly useful for analyzing optimal construction budgets.

## Reproducibility and limits

Execute `python verify.py` with the Python standard library. This replays 6,228 exhaustive labeled triangle-free graph checks up to six vertices, the \(P_3\)/\(P_4\) boundary values, and seeded simulation checks. The mathematical theorem is proved analytically and does not depend on empirical evidence. No independent mathematical audit or comprehensive historical-priority certification was performed.

Self-review: passed. Independent audit: not yet performed.
