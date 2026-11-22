# Scientific review: optimal regular covers of finite Kripke pretrees

## Correctness — PASS
The proof applies the bounded-morphism back condition to maximal-depth preimages of target clusters, forcing the exact branching and cluster-size feasibility thresholds. The lower bound counts distinct internal quotient preimages, and the construction pads only leaves of the internal target skeleton. Equality forces an internal skeleton isomorphism. Weighted inclusion-exclusion counts required adjacent leaves, and independent cluster surjections supply multiplicities. The extracted checker independently tests cone-image equality and direct finite set-function counts: `VERIFY_OK shapes 57 brute_tree_counts 24 cluster_brute 4 shape_rigidity 375 branch_obstruction 259`. Finite enumeration supports, but does not replace, the proof of all finite cases.

## Originality — PASS within inspected evidence
Wołoszyn (2026, Lemma 3.7) establishes existence of a regular cover using uniform replicated branches. The inspected published results on prescribed rooted-tree p-morphism images and multiplicities already give broad *fixed-source* decision and counting results. Their coverage is acknowledged: the unrestricted fixed-tree counting problem is not claimed as new. The optimized minimum over all regular pretrees, its unique internal-skeleton shape, and the weighted formula for target clusters are distinct statements requiring additional lower-bound and equality proofs. Full source readings are cited in AUDIT.json; semantic searches do not prove absolute novelty.

## Value — PASS
A construction used in finite Kripke-frame regularization is sharpened from unquantified existence to an exact linear-size optimum, complete extremal shape rigidity, and explicit optimal-map multiplicity. The parameter conditions and cluster weights are intrinsic rather than arbitrary. This gives a mathematically motivated, reusable quantitative finite-model-theory fact.

## Literature and limitations
The closest primary source is https://arxiv.org/html/2605.14182 ; relevant publicly accessible prescribed-tree p-morphism results are https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-finite-rooted-kripke-p-morphism-images-are-rooted-topological-mi--fec4b9aa3bee and https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-bounded-morphism-counting-between-arbitrary-finite-rooted--e532142d4dde. The special three-level target source is https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-bounded-morphism-census-and-sharp-branching-threshold-for--9537b2b1e958. The theorem does not address general preorders, infinite frames, nonuniform source clusters or inverse-back morphisms. Independent mathematical and historical-priority validation is absent.

Self-review: passed. Independent audit: not yet performed.
