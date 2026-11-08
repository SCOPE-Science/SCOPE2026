# Review of Sharp orientation extremizers for zero-product probabilities in radical-square-zero quiver algebras

## Correctness — PASS
The proof starts with explicit vertex and arrow multiplication, obtains the positive subgraph count and proves a sharp termwise maximum on bipartite graphs. On paths a selected edge subset decomposes into runs; the mixed/pure internal-vertex weight determines both strict extremizers. Two explicit transfer matrices give the recurrences, while a direct characteristic-polynomial comparison establishes the distinct leading exponential rates. The standalone `verify.py` was executed successfully against actual finite algebra multiplications. Finite tests corroborate but do not replace the algebraic proof.

## Originality — PASS relative to inspected sources
A pre-existing all-quiver right-annihilator spectrum formula gives every fixed-orientation zero-product count; the counting expansion is therefore treated as a supporting lemma, **not** as a new counting result. Earlier cycle-specific transfer laws also yield individual orientation contrasts, not this path optimization. The assessed new assertion is the complete source–sink maximization for all bipartite graphs, the exact unique extrema for every path, and the strict two-rate exponential separation. Shumyatsky–Vannacci (2023) treat structural probability consequences; Dolžan (2025) treats semisimple/local families; neither asserts the extremizers. Unidentified stronger weighted-graph orientation results remain a genuine priority risk.

## Mathematical value — PASS
Which orientation extremizes the probability of zero multiplication is a natural comparative invariant for quiver algebras having identical underlying undirected graph and algebra dimension. The classification over all path lengths and finite fields, together with two explicit asymptotic decay constants, is a substantive structural and asymptotic boundary rather than a restatement of finite count tables.

## Sources and limitations
Relevant source texts: Khasraw, arXiv:1810.13312v1; Vaso, arXiv:2105.05830v1; Shumyatsky–Vannacci, arXiv:2307.12633v1; Dolžan, arXiv:2504.12886v1; and the accessible abstract of Dolžan 2022 (DOI 10.1017/S0004972721001246). The earlier all-quiver annihilator-spectrum statement and oriented-cycle count must not be presented as newly discovered here. The path minimum is not asserted for general bipartite graphs. Unseen stronger literature could affect novelty. No independent mathematical validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
