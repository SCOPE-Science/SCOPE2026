# Review of the matched-equilateral variance theorem

## Correctness — PASS

All quantifiers, normalizations, and exceptional parameter endpoints were reconstructed. Strict convexity of uniform variance modulo constants restricts maximizers to vertices of the Lipschitz polytope. Tight-edge incidence rank proves the six possible states for each shortened pair. The explicitly computed expected-variance improvement from replacing two split pairs is strictly positive for every \(k\ge2\) and \(0<\lambda<1\), so maximizers have at most one split. Discrete finite differences select the unique optimal remaining count, and direct subtraction gives the stated rational threshold. The standalone checker independently enumerated the full tight-tree extremal set at four small rational instances and agreed with the candidate variance and optimizer family at 22 instances. The finite tests do not prove the unbounded family; the analytic proof does.

## Originality — PASS (qualified)

The classical complete-graph spread is known (Addario-Berry, Janson and McDiarmid, arXiv:0902.1156). The general Lipschitz-polytope tight-edge geometry is also prior work (Gordon and Petrov, arXiv:1608.06848). The closest indexed result, *Facet enumeration for equilateral metrics with independently shortened pairs*, explicitly **does** establish the six-state extreme-point classification for this entire matching family; this geometric classification is not claimed new. It does **not** derive sharp uniform variance, eliminate all but one split pair among variance maximizers, or determine the exact optimizer transition. A separate equilateral Banach--Mazur result treats the unshortened norm comparison and does not imply the contracted-matching profile. No covering variance theorem appeared in the targeted source searches and full-text inspections. Unindexed equivalent formulations remain possible.

## Mathematical value — PASS

The problem measures the sharp Lipschitz-to-centered-\(L^2\) norm under a controlled metric contraction. It captures a genuine parity obstruction (matching-pair count), a nontrivial stability plateau, and a sharp quadratic transition with complete localization of the defect on one pair. The structural elimination lemma reduces exponentially many extreme potentials to two meaningful families and identifies exactly how variance recovers toward the equilateral benchmark. This is a motivated infinite parameter family rather than an arbitrary finite table.

## Boundaries and residual risks

Equal matched distance and uniform atomic mass are essential to the symmetric sharp formula. The matching metric ceases to have the same extremizers at \(\lambda=1\). The argument does not address unequal shortenings, arbitrary other short-edge patterns or nonuniform probability. Priority relative to unindexed literature is not proven, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
