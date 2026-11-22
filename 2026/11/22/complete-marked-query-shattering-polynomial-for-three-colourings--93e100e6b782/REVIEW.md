# Review of the complete marked-query double-star shattering polynomial

## Correctness — PASS

For every pair of positive integers \(a,b\), the theorem counts each shattered *vertex--colour query support* with its actual named colour targets. The key reduction is an exact equivalence between all leaf-answer traces and the centre-colour feasibility requirement: necessity uses the all-positive leaf pattern, and sufficiency independently fills every negative leaf with the remaining third colour. Four exhaustive centre-query cases produce the formula. The algebraic factors have direct enumerative meanings. The highest-degree statement follows both from those cases and an explicit witness. The one-coefficient graph-reconstruction corollary follows from a strictly decreasing exponential expression after fixing the total leaf count. The embedded Python script directly enumerates all \(256256\) marked supports across eleven trees, compares complete direct traces, and separately compares centre feasibility and polynomial coefficients. The unlimited conclusions rest on the proof, not the finite tests.

## Originality — PASS (with historical-priority risk)

The most direct prior double-star statement classifies which *vertex subsets* admit at least one assignment of colour targets and the topology of that projected support complex; it explicitly does not count all query-pair supports. That is weaker information. For example, the same three-vertex projected support can have a shattering assignment of target colours and another assignment that fails, so the projection cannot recover the number of valid marked assignments. Its scalar VC dimension is not newly claimed. The publicly available complete-bipartite proper-colouring theorem uses a different graph family, with extra edges, and does not imply the double-star support counts. The published small-tree obstruction result and path-colouring scalar theorem do not provide these coefficients. Walker's general tree-dimension theorem, Guingona et al.'s zero-set theorem, and Blanca et al.'s graph-structure-learning results also do not entail this closed two-parameter marked-query polynomial. Equivalent unindexed results remain possible; absence from searches is not a uniqueness proof.

## Value — PASS

The full query-pair shattering polynomial is a natural finer invariant for the precise Boolean concept class, not just a relabeling of the number of admissible vertex sets. It determines the count of every shattered rank for arbitrarily large and imbalanced double stars, and its *single highest coefficient*, together with graph order, recovers the unordered pair of hub leaf degrees. At six vertices the highest coefficients for two nonisomorphic double stars are \(78\) and \(60\), while both have the same scalar VC dimension. The exact all-parameter factorization and sharp reconstruction property make the refinement mathematically substantial even though general tree colouring shattering remains open.

## Closest results, limits, and verification

Primary publications reviewed by available full HTML: Blanca et al. (arXiv:1708.05118), Guingona et al. (arXiv:2109.04805), and Walker (arXiv:2203.12211). Closely related published full results reviewed: *The first branching obstruction to three-colouring shattering on trees* and *Exact shattering polynomial and palette transition for complete-bipartite proper colourings*. Historical priority for equivalent unindexed terminology is not certified. The proof assumes three named colours, positive leaf counts and binary equality queries. An independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
