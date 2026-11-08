# Scientific review

## Correctness — PASS

The covariance formula follows by conditioning individually on a source vertex in the two-vertex and larger vertex classes. All affected directed-wedge contributions are explicitly counted, and unaffected edges remain independent. The second derivative of the sign polynomial is strictly negative for every integer \(b\ge3\); three exact rational supporting tangents rule out positive values for \(b=3,4,5\), while a rational witness and its strict increase in \(b\) give exactly two zeroes for every \(b\ge6\). The case \(b=2\) is handled directly. The packaged checker passed 645 exact enumerations or rational assertions. Finite tests supplement the analytic proof; no unproved step is inferred from sampling.

## Originality — PASS with residual priority risk

The closest accessible papers concern correlation of directed *connection events*: Linusson (arXiv:0905.2881), Alm–Janson–Linusson (arXiv:0906.0720), Aas (arXiv:1102.1711), and Narayanan (arXiv:1609.01003). Aas treats complete bipartite hosts but assumes uniform orientation and derives asymptotic reachability-event dependence, whereas the claim here treats exact finite-order source-count versus oriented-wedge-count moments under asymmetric bias. Narayanan permits biased orientations but still studies joint reachability, not counting variables. Inspected statements and sections do not imply the claimed classification directly. General older motif-count moment formulas may implicitly contain this special case; the record establishes a best-knowledge comparison, not certified priority.

## Value — PASS

Sources quantify where flow can originate in a directed network, while directed length-two paths count elementary flow opportunities. It is not automatic that their dependence changes sign more than once under orientation bias. The complete family classification gives a sharp smallest high-degree-side cutoff \(b=6\), two rigorously unique bias thresholds thereafter, and a nontrivial positive-covariance witness with exact rational value. This is a natural boundary for an interpretable biclique motif family, not an arbitrary numerical slice.

## Scope and uncertainty

The complete classification holds only for \(K_{2,b}\) with common direction probability and the given pair of statistics; no wider network sign law is asserted. The exact roots are implicit. The independent historical and scientific review is outstanding.

Self-review: passed. Independent audit: not yet performed.
