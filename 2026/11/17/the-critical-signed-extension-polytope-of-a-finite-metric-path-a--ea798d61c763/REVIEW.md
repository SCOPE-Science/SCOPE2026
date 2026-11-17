# Scientific review

## Correctness — PASS
For every finite weighted path with positive edges and equidistant one-point attachment \(R\ge D/2\), the edge-sign dual computation gives exactly \(N_j=\sum_{i<j}\ell_i|F_i|+\sum_{i\ge j}\ell_i|F_i-1|\), including signed weights. The endpoint triangle inequality and endpoint-average witness certify the global optimum \(1\). At \(R=D/2\), saturation of both endpoint inequalities forces \(0\le F_i\le1\) and the weighted mean equation; substituting these into all other norms is logically equivalent to the displayed prefix inequalities. Relative-interior and negative-coefficient constructions are explicit and cover boundary dimensions, including \(m=1\) and \(m=2\). For unit edges the cyclic rotation argument gives \(1/m\) of the central cube section, and the sorted chamber gives \(1/m!\); their ratio is \(1/(m-1)!\). All formula normalizations were checked. The standalone rational checker independently evaluates dual edge-sign potentials.

## Originality — PASS with historical risk
Relevant exact source inspections: Bruè--Di Marino--Stra, arXiv:1801.07533, Theorem 4.1 (2018); Ambrosio--Puglisi, arXiv:1609.01450, Theorems 2.14--2.15 (2016); Godard, arXiv:0904.3178, Theorem 3.2 (2009); and Marichal--Mossinghoff, arXiv:math/0607715, Theorem 4 (2006). General extension existence, tree \(L_1\) representation, and cube-section volume are acknowledged prior work. Searches of published mathematical-record summaries and the primary literature identified no stated theorem classifying this precise *signed* critical path extension equality polytope and giving its factorial positivity fraction. The standard cyclic-maximal-partial-sum argument is not separately claimed new. Residual historical risk: an equivalent Chebyshev-center or continuous-ballot-polytope formulation may have been published under another terminology.

## Mathematical value — PASS
The question of *all* optimal linear extensions is not answered by an existence theorem or a norm estimate. Here the equality locus is explicitly solved for arbitrary positive edge lengths, its dimension and the first possible signed optimum are sharp, and in the canonical unit case a factorial fraction quantifies how atypical the positive optimizers become. These are natural invariants of a basic finite-tree extension problem and distinguish positive random projections from unrestricted signed operators. Their determination is more than evaluating a single extremal value or merely restating a known cube section.

## Limits
Finite exact enumeration supports but does not prove the infinite-parameter result; analytic proofs are supplied in the result. The historical novelty assessment is qualified, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
