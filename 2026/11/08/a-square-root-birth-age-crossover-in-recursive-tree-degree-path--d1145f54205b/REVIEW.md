# Scientific review

## Correctness — PASS

The exact covariance law follows by a parent-edge intervention and the independent expected descendant-subtree size \(n/j\). Finite harmonic-sum algebra yields the discrete first difference, and its sign gives a unique birth-label crossing. The Euler–Maclaurin expansion at \(i\asymp\sqrt{n/\log n}\) supplies the limiting critical scale. A standalone exhaustive enumeration of all recursive trees through nine vertices, separate harmonic identities through 150 vertices, and large-size diagnostics returned `VERIFY_OK 12134 exact/diagnostic assertions` (12,124 exact and 10 numerical). The computation is supplementary to the general analytic proof.

## Originality — PASS, qualified

The most directly overlapping published result establishes the exact root-attachment covariance with total path length and a root-specific stochastic order. The \(i=1\) specialization is therefore not claimed as new. Lodewijks (2022) develops joint degree and depth properties for labelled vertices, but the inspected main results do not concern a specified vertex's offspring covariance with the *sum* of all depths. Eslava (2016) treats degree and depth of high-degree vertices. Dobrow and Fill (1999) treat total path length without the positional offspring statistic in the available abstract. The present result gives a nonroot all-ranks covariance law, unique sign change, and \(\sqrt{n/\log n}\) crossover; these do not follow as stated from the root case or individual-vertex distribution theorems. A classical generating-function identity might nevertheless encode the same mixed moments. Full text of the 1999 paper was not inspected, so priority remains qualified.

## Value — PASS

A vertex's contribution to branching is a natural local predictor of total search cost in a growing tree. Its direction of dependence varies by birth age and the boundary lies at a mesoscopic rank, rather than a constant or linear fraction of the tree. The exact finite law, global sign structure, and sharp crossover explain a qualitative dependency reversal in a canonical model; they do not rely on arbitrary small-size slices or purely computational enumeration.

## Scientific limitations

The result addresses covariance and does not infer a full stochastic order for nonroot offspring count. It assumes independent uniform attachments and does not assert an analogous threshold for preferential-attachment models. Historical priority for the mixed first moment remains open to additional specialized literature checks.

Self-review: passed. Independent audit: not yet performed.
