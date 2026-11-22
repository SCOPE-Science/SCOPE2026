# Review of a matching-deletion law for dominant edge-metric generators

## Correctness — PASS

The statement is quantified over every integer \(m,n\ge3\) and every deleted matching size \(0\le t\le\min(m,n)\). Its proof is a complete classification: a vertex cover omits vertices in only one shore or precisely one removed matched pair; edge resolution of a one-shore omission is equivalent to omitting at most one unmatched vertex there. The necessity is witnessed by indistinguishable edges from two omitted unmatched vertices; sufficiency uses a matched partner as a distance-two-versus-one witness. The two shapes count to the exact polynomial, whose maximal omitted sets determine every inclusion-minimal generator and the minimum. The edge-distance assumptions hold for both the smallest permitted shores and the balanced full-deletion case. Two independently structured brute-force implementations agree with the polynomial coefficientwise for all \(71\) and \(108\) parameter cases in their respective finite bounds. Finite checks are not the proof.

## Originality — PASS (historical priority provisional)

Tavakoli et al., *The dominant edge metric dimension of graphs* (DOI: 10.5614/ejgta.2023.11.1.16), prove only the \(t=0\) scalar value \(m+n-1\) for this family, and present general corona, edge-corona and join formulas. A missing-matching biclique is not a join when \(t>0\), so those formulas do not cover the present graph family. Kelenc–Tratnik–Yero (arXiv:1602.00291) study the edge metric dimension without vertex-cover restrictions. Ikhlaq–Hayat–Siddiqui (arXiv:2211.09327) require vertex-edge domination rather than a vertex cover, and their complete-bipartite scalar value is different. Full scientific records were inspected for a complete vertex-resolving polynomial on matching-deleted bicliques (record 01c06d3fb257) and ordinary edge-metric bases of crown graphs (record b5b3c45f23e8). They use, respectively, vertex-pair distances without a cover and edge-pair distances without a cover, neither implying the present combined all-generator theorem. Absence of a covering result in the checked sources is not proof of global uniqueness.

## Value — PASS

The result extends the previously known single scalar on a complete bipartite graph to a complete cardinality distribution and full classification for every matching-deletion size. A local edge defect changes the optimal combined coverage-and-identification cost, while larger matching deletions create two distinct sizes of inclusion-minimal sensor sets separated by a gap growing with the defect size. The exceptional full balanced deletion endpoint and all optimum multiplicities follow from the same structural law, rather than from an arbitrary finite calculation.

## Limits

The graph has two shores of size at least three and only a matching of cross-edges removed. No assertion is made for arbitrary deletion graphs, edge-resolving sets without vertex-cover constraints, or other vertex-edge domination definitions. Publication priority is provisional and there has been no independent external mathematical validation.

Self-review: passed. Independent audit: not yet performed.
