# Self-review

## Correctness — PASS
The proof treats arbitrary finite nonempty graphs and every strict profile, with the zero-clique and one-colour boundaries stated. For the upper bound the new apex takes its favourite colour and hence has envy outdegree zero, while the remaining \(k\) colours admit a stable colouring on the original graph. For the lower bound the new colour is ranked last by original vertices and first by the apex. If the apex uses the new colour, its complement contradicts the obstructing original profile; otherwise an original vertex using the new colour creates a mutual-envy two-cycle, and using none leaves an obstructed stable colouring on the original palette. The induction and excess assertion are exact. `artifacts/verify.py` exhaustively checks small instances but is not needed as an infinite proof. No premise is based on a finite extrapolation.

## Originality — PASS (priority provisional)
The initiating primary paper [1] gives general bounds, subgraph monotonicity and specific families, not exact clique-coning additivity. In particular, its reachability estimate can be strictly larger than the stable chromatic number and does not imply equality after coning. The closest published matching-topic record [2] is a single \(K_{2,3,3}\) instance; full scientific text was compared, and it does not imply the identity for arbitrary base graphs. Actual searches for apex, cone, join, universal vertex, preference stability and equivalent forms uncovered no stronger covering theorem. Historical priority is not independently certified; unindexed equivalences remain possible.

## Mathematical value — PASS
This is an exact structural graph-operation law for a newly studied stability invariant, not a one-instance computation or a relabelling. The nontrivial direction holds against *every* profile and is proved by a transferable obstruction rather than an ordinary chromatic-number counting argument. It immediately determines preference-stable chromatic numbers of arbitrarily many cone families from any known base value, and it preserves the stability-versus-chromatic gap while increasing the ordinary chromatic number without bound. No paper-sized claim is made about arbitrary graph joins.

## Closest literature and limitations
[1] Koana, Oh, Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1 (2026-09-01); inspected definition, structural bounds, special-family results, and conclusion. [2] Published record *Stable chromatic number of the complete tripartite graph \(K_{2,3,3}\)* (October 2026); inspected full `RESULT.md`, one fixed-profile lower-bound example. The general theorem is exact, but literature priority remains provisional. Computational spot checks are not independent validation.

Self-review: passed. Independent audit: not yet performed.
