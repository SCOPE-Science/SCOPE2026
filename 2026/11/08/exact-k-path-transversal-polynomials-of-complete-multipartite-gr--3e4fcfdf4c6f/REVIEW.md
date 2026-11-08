# Mathematical review of the complete-multipartite \(k\)-path transversal theorem

## Correctness — PASS
The full-scope proof establishes the longest-path occupancy characterization \(\ell(S)=\min(|S|,2(|S|-\max_i |S\cap V_i|)+1)\), then proves both directions of the inclusion-maximal classification. The potential boundary when the whole graph is \(P_k\)-free is included, and the coefficient sums count only unique dominant parts. The complement map establishes minimal path covers without a separate assumption. A direct adjacency-and-path checker tested 557 parameter instances and 320576 vertex subsets, independently agreeing with both polynomials. The even/odd bipartite coefficient identities and the fixed-parameter asymptotic expansion are exact algebraic consequences.

## Originality — PASS (provisional publication priority)
The closest directly overlapping work concerns minimum \(k\)-path vertex-cover *numbers* on complete bipartite graphs (Li–Zuo 2018, as quoted in Tu 2022, Theorems 37–38), and the full accessible Bujtás–Jakovac–Tuza 2021 paper concerns general degree/chordal bounds. Known longest-path constructions in multipartite graphs imply the feasibility lemma, and known \(\(k=3\)\) dissociation enumerators cover that excluded boundary, but none of the accessible inspected results gives the complete cardinality census of inclusion-minimal covers for all \(k\ge4\) and part-size vectors. The partial-access Li–Zuo source remains a meaningful residual risk, not a claim of checked whole-document absence.

## Value — PASS
The complete enumeration concerns a standard path-transversal problem, not an arbitrary slice. It simultaneously determines all minimal-solution sizes and multiplicities for an infinite class with arbitrary part-size profiles and all path orders \(4\le k\le N\). On balanced bicliques it proves a sharp parity-dependent well-coveredness analogue and unbounded gaps; for fixed odd path order almost every minimal cover is asymptotically about twice the minimum size. These statements refine previously known scalar optimum values and identify the structure of non-optimal minimal solutions.

## Limitations
The graph class is complete multipartite; paths are subgraphs rather than induced paths. Primary publisher access to Li–Zuo 2018 was incomplete. No independent mathematical audit or priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
