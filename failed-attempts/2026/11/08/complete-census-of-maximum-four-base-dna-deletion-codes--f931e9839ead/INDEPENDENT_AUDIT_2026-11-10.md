# Independent mathematical audit

## correctness

PASS

In the precise reverse-complement-closed, no fixed strands, one-deletion length-four DNA model, there are 120 candidate pairs of complementary orbits. Each pair is internally deletion compatible. Valid codes correspond bijectively to cliques in their 120-vertex graph with adjacency exactly disjoint deletion shadows (64 possible observed 3-mers). A rigorously bounded clique search proves no 12-clique and counts 44 11-cliques (22 codewords), with exactly nine alphabet-symmetry orbits of sizes 4 seven times and 8 twice and only universal representatives AAAA and CCCC. An independently implemented Python Bron–Kerbosch search over the actual definitions visited 3,867,602 calls and confirmed 44 maxima, nine orbit classes, and compulsory Watson–Crick pairs; its completeness follows maximal-clique enumeration plus an already bounded maximum. This proves a finite exact statement and does not extrapolate to other block lengths.

## originality

FAIL

Decisive prior publication 2026-11-02 already counts exactly 44 labeled optimal reverse-complement-closed length-four deletion codebooks under the same exclusion of self-complementary strands, and publishes a FULL 44-row optimal_rc22_no_self.tsv inventory. Nine symmetry orbits and the intersection of all codebooks are directly calculable from that published full inventory. The new package is therefore a recomputation and grouping of a known complete classification, irrespective of its independent algorithm and formal presentation.

## value

FAIL

The known full 44-codebook inventory already supplies a complete, searchable classification of the natural model. Its nine orbit sizes and common pairs are immediate small finite-table operations, rather than a newly motivated obstruction, new structural theorem, or unknown invariant. Reproducing an already published optimum and list has little independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
