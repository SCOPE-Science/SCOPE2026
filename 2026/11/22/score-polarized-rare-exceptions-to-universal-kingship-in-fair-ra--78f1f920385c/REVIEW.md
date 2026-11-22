# Self-review

## Correctness — PASS

The fixed-covering-pair conditional law follows by deleting exactly one forbidden two-edge orientation pattern independently at each other vertex, yielding probability \(\frac12(3/4)^{n-2}\) and an exact three-type multinomial. A pairwise-overlap sum for covering events gives relative rare-multiple-pair probability \(O(n(5/6)^n+n^2(3/4)^n)\); comparing the conditional law to its covering-pair size-biased version proves the total-variation claim. Binomial concentration for unmarked vertex scores yields strict degree extrema; the multinomial covariance yields the bivariate Gaussian limit. Exact verification passed 222 rational assertions for all labeled tournaments of orders 3–6. Finite tests do not establish infinite limits.

## Originality — PASS, qualified

Fey (2007) studies the typical size of tournament solution sets, with ordinary Copeland-score comparisons. Saile–Suksompong (2019) and Manurangsi–Suksompong (2022) study probability thresholds for kings and other tournament solutions. The closest inspected published 2026 theorem gives a refined first-/second-order failure probability and double-obstruction clustering; these are credited as prior knowledge. Its full published proof and conclusion do **not** state a complete conditional marking law, joint pair-score Gaussian asymptotics or a score-only recovery rule for exceptional vertices. These are independently formulated and proved. Related unlabeled score studies and older historical work leave a residual priority risk.

## Value — PASS

When universal kingship fails in a large random tournament, the theorem identifies the exclusion using just the minimum Copeland score and identifies the exceptional coverer using just the maximum score. The entire conditional edge pattern around the exceptional pair is described up to exponentially small total-variation error and the exceptional scores have an explicit nondegenerate joint fluctuation law. This replaces a purely rarity-based statement with structural information about what exceptional instances look like. A score-only diagnostic for a natural random social-choice obstruction, not a restatement of its probability, is the motivation.

## Closest literature and limits

The 2026 rare-obstruction analysis is especially close and dominates any assertion merely about the probability or number of covering pairs. The present claim deliberately excludes those established conclusions as novel. Independent edge orientations and the asymptotic regime are essential; numerical sharpness of the TV error and historical novelty beyond inspected works are unproved.

Self-review: passed. Independent audit: not yet performed.
