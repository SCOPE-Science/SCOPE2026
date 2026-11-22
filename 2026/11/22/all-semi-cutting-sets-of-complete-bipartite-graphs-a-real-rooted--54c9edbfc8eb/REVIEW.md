# Review: semi-cutting sets of complete bipartite graphs

## Correctness — PASS
The proof exhausts all shortest terminal-terminal paths in a complete bipartite graph, including singleton shores and one-shore terminal sets. These constraints partition the edge set into four independent blocks, producing the exact polynomial. Local admissibility proves that inclusion-minimal solutions are precisely minima, and the direct subtraction identity gives the equality-case classification. Root claims follow from explicit linear/monomial factors. An independent checker enumerates all edge-deletion subsets and recomputes terminal distances by breadth-first search in 92 small parameter profiles. Risks: computation corroborates only bounded cases, so all-size correctness relies on the all-case proof; no weighted or noncomplete graph claim is made.

## Originality — PASS with historical-priority caveat
The directly motivating full primary preprint (Bosek, Serra and Vena, arXiv:2611.20287v1, 15 November 2026) proves the universal inequality and expressly poses equality cases and minimum structures as future directions. It does not count semi-cutting edge sets of complete bipartite graphs, prove their root law, or classify equality among bicliques. Searches across indexed mathematical research and accessible prior claims did not locate equivalent edge-deletion results. Distinct indexed biclique domination or geodesic-cover records do not imply the semi-cutting statement. Risk: historical research not covered by available indexing might contain equivalent results; some related records were accessible only as indexed summaries.

## Value — PASS
The motivating general theorem explicitly asks for equality conditions and minimum-edge configurations. The result supplies a complete all-terminal-layout answer on a central nontrivial dense graph family. The exact polynomial describes *all* feasible deletions and reveals real-rootedness, strict fixed-size purity of inclusion-minimal solutions, an explicit optimizer census and connected reconfiguration, beyond a single scalar lower bound. The sharp distinction between stars and genuine bicliques clarifies where equality is structurally possible. These are meaningful natural invariants, not arbitrary finite slices.

## Limitations
The classification is restricted to finite unweighted complete bipartite graphs; no independent audit or priority guarantee is asserted. Some related papers were readable as indexed summaries only.

Self-review: passed. Independent audit: not yet performed.
