# Review of the extremal-forest enumerator

## Correctness

PASS. The exact three cases of distance differences yield the sufficiency of positive degrees without single-edge components; empty-class and single-edge obstructions both exceed the claimed optimal size. A connected-component edge bound forces exactly \(q\) small tree components at equality; constructive bipartite star/path layouts prove attainability. Standard labelled tree enumeration then yields the coefficient formula. The standalone exact-arithmetic checker and direct distance tests support, but do not replace, the unrestricted proof.

## Originality

PASS, provisional historical priority. Fernández et al. (arXiv:2505.19642, full paper inspected) and Kumar (arXiv:2609.32161, full HTML inspected) establish the graph framework and threshold; the 2025 square-case proof already rules out one-edge components for optimum incidence graphs, a key mechanism reused here. A released mathematical resolution at trureturing.org already proves the full scalar minimum for the remaining rectangular cases, and its incidence and degree estimates strongly overlap the present proof. Those known claims are explicitly excluded. The assessed statement is the classification of **all** minimum bases by component-size profile together with an exact **labelled bivariate enumerator** for every stated parameter. Searches for these statements and their aliases did not disclose a covering formula. An equivalent unindexed enumeration or an implicit corollary of a prior classification remains a residual risk.

## Value

PASS. Minimum-basis enumeration is a natural refinement of the fully determined weak-metric dimension: knowing the minimum size does not yield the number or shapes of extremizers. The theorem gives an unrestricted structural census in the near-square range and computable exact counts that are large already at small orders, with a three-way residue-class transition.

## Scope and remaining risks

The statement concerns labelled row-column products in \(8\le n\le m\le2n-5\), not symmetry orbits or larger parameters. Historical novelty is not independent verification; the original scalar result is fully credited. The exact enumerative claim has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
