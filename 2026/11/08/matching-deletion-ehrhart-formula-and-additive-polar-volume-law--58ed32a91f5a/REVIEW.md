# Scientific review

## Correctness — PASS

For each integer dilation, normalize lattice potentials by their minimum. Their range is either at most the dilation or has a uniquely oriented missing matching pair as its minimum and maximum; the other coordinates form an independent interval whose width is below the dilation. The disjoint cases yield a complete polynomial count for all nonnegative dilations, including zero. Summing the generating function gives the displayed \(h^*\), and the standard Eulerian gamma recurrence proves nonnegativity. The continuous integration uses the same unique-extrema partition, with a directly computed Jacobian of \(1/\sqrt n\). Small exact-enumeration and independent hull computations support, but do not replace, the proofs. No unproved step is needed for the stated all-parameter formulas.

## Originality — PASS, historical priority provisional

The closest direct primary paper [D'Alì, Juhnke-Kubitzke, Koch, 2023, Proposition 5.1] gives a general bijection between bounded cuts and polar lattice points; it does **not** evaluate the closed \(K_n\) minus matching count, Eulerian numerator, or independent-length volume. Higashitani–Jochemko–Michałek (2018) give complete-multipartite **primal facet** results; D'Alì–Delucchi–Michałek (2019) give polar lattice-point structure and a planar first-dilation count, not this full Ehrhart series for all \(n,k\). Previous available matching-related results concern inradii/facets, the single-pair scalar polar-volume special case, and the isolated scalar \(K_{2,2}\) polar-volume endpoint at \(n=4,k=2\). None evaluates the full stated matching-family Ehrhart or independent-distance volume expressions. Existing classical Eulerian gamma positivity and the complete-graph baseline are explicitly credited. Residual priority risks include differently indexed general weighted metric-polytope or bounded-cut formulas, which were not exhaustively surveyed.

## Mathematical value — PASS

The problem is the full lattice-point enumeration and polar volume of the natural dense graph family \(K_{2,\ldots,2,1,\ldots,1}\), not an arbitrary finite slice. It determines every Ehrhart coefficient via a concise Eulerian expression and a structured \(\gamma\)-positive numerator for arbitrarily large dimension. The independent-parameter volume additivity is a geometric separation phenomenon: no mixed terms survive, even though the defining inequalities share most vertices. The exact small relative-volume correction quantifies robustness of the complete-graph polar under disjoint deletions.

## Sources and residual limitations

Primary sources: arXiv:1910.05193v1, arXiv:2307.04933v1, arXiv:1807.07678v1, arXiv:1608.06848. Published records concerning matching-relaxed metric facet classifications and the accessible related one-edge polar-volume statement were compared by mathematical implication. The primary claims are proven for a deleted matching of size at least two and distances in the stated range only. The review does not establish universal historical priority, and external mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
