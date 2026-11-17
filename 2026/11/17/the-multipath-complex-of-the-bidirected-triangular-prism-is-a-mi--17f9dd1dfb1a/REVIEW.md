# Scientific review: bidirected triangular-prism multipath complex

## Correctness — PASS

The graph is specified by its nine undirected edges and eighteen directed arcs. `verify.py` enumerates all \(2^{18}\) selected-arc subsets, gives 686 nonempty faces, and verifies every face deletion. The 326 ordinary face pairs are acyclic across all 2,256 directed cover incidences and leave critical cells \(1,5,22,6\) in dimensions \(0,2,3,4\). Exact signed Morse boundary reductions vanish over the integers; mod-two boundary ranks \((17,91,164,54)\) independently agree. The five integral two-cocycles form a full rational cohomology basis, and each of the 25 ordered degree-two cup products is an exact rational coboundary. Because integral fourth cohomology is free, these products vanish integrally. Hurewicz and Hilton–Milnor arguments then rule out every degree-three and degree-four attachment, proving the **homotopy type**, not just Betti numbers. Potential calculation risk is bounded by the fully reproducible exhaustive code; the homotopy-theory deduction has not been independently peer reviewed.

## Originality — PASS (best knowledge)

The closest primary result, Caputi–Collari–Smith (arXiv:2601.05670), studies bidirected paths and simple polygons, not their triangular-prism graph assembly. Caputi–Collari–Di Trani–Smith (arXiv:2208.04656) treat several directed graph families including small linear grids, but the fully bidirected prism does not satisfy the identified grid hypotheses. Deshpande–Sawant (arXiv:2602.14936) define the same complex under a directed-linear-forest alias, but their quoted decomposition theorems require different orientations/underlying graph families. Related indexed homotopy results on bidirected double-stars are for trees. Other indexed prism records concern **different simplicial complexes** (ordinary discrete Morse matching, Rips, Čech and total-cut). The actual alias and implication comparisons are recorded in `AUDIT.json`; absence of a search hit does not prove priority. Unindexed equivalent sources remain possible.

## Mathematical value — PASS

The triangular prism is a canonical first multiply cyclic prism graph, materially different from the already studied bidirectional polygons. Its multipath complex exhibits simultaneous nonzero homotopy in dimensions two, three and four. The nontrivial issue is not just computing three ranks: degree-four cells may attach by Hopf or Whitehead elements, and the exact cup-product calculation proves that they do not. The result supplies an exact, standalone, testable case for theories of directed path-forest complexes. It does not purport to classify arbitrary prisms or all orientations.

## Limitations

Finite six-vertex graph only; no family-wide extension, symmetry representation, or independence from all possible unpublished work is claimed. Only self-review have been made.

Self-review: passed. Independent audit: not yet performed.
