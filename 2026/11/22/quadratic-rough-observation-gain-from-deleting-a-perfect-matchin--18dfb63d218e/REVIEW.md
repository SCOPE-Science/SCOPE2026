# Review: quadratic rough-observation gain on crown graphs

## Correctness — PASS

For each integer \(n\ge3\), the explicit closed-neighborhood membership test reduces the rough pair to two complementary upper-coverage profiles. Classification of all nonfull profiles gives exactly \(2^{n+1}+n^2-n-3\) such values. Only \(2n\) subsets have both complementary profiles nonfull. Counting the two one-full orientations, those exceptional profiles and the central pair proves \(4\cdot2^n+2n^2-5\). A binomial count of inverse fibers and the independent total mass \(4^n\) establish the rest. Boundary cases \(n=1,2\) are treated separately. A source-code checker independently enumerates inputs and verifies both observations and every fiber for \(3\le n\le9\). Neither experiments nor the simple mass-balance identity is being treated as a replacement for the structural proof.

## Originality — PASS within inspected evidence

The closest exact published normal form for complete multipartite tolerances gives \(4\cdot2^n-5\) for *unmodified* \(K_{n,n}\). Because the crown graph's nonadjacency does not partition into equivalence classes at \(n\ge3\), that prior theorem cannot be specialized to the deleted-matching case. A separate exact Tutte evaluation applies to dual-incidence *posets*, which have a different underlying relation and cardinality problem. A contemporary 2026 rough-graphs paper was read in its available PDF text: its definitions concern partition- and covering-based rough *subgraphs*, not the exact count and inverse fibers of vertex-subset rough observations. The 2026 categorical rough-set paper concerns equivalence-based categorical structures. A 2020 neighborhood paper was only partially accessible and remains a publication-priority risk. Searches of the research records and accessible prior work found no exact crown formula or table, but search failure does not establish uniqueness. The previously recorded closed-neighborhood path census concerns paths, not this crown family.

## Value — PASS

The exact number of attainable rough approximations, and the source-fiber distribution, are natural invariants of a tolerance: they distinguish observable data from indistinguishable inputs. Removing a perfect matching from a balanced biclique increases the exact observation count by \(2n^2\) and exposes a sharply structured collision census. These are motivated quantitative boundaries for nontransitive tolerance models, not mere examples or recomputations of the known undeleted case. No algorithmic or applied significance beyond the established exact structural calculation is asserted.

## Closest sources and residual risks

Syau, Liau and Lin (2026), DOI:10.3390/math14020369; Hafez et al. (2026), DOI:10.5206/mase/23201; Järvinen and Radeleczki, arXiv:1303.6332; complete multipartite-tolerance and graph-incidence-poset exact-result records listed in `RESULT.md`. The 2020 neighborhood systems primary paper was inspected only in available public preview, so a hidden equivalent specialization remains possible. Broader historical literature has not been comprehensively audited. Publication priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
