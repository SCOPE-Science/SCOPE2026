# Scientific review

## Correctness — PASS

The model is exactly specified by eighteen integer-labelled edges, three spin values, and the Hamiltonian in `RESULT.md`. Three disjoint triangles and a residual three-vertex path force the unique five-site independent set; its complement induces three disjoint edges. The size-six internal-edge bound and the cubic degree lower bound together prove every positive-field energy comparison, including the two exact crossings and the absence of intermediate sectors. Configuration counts 16, 32, 48 and the independence-polynomial evaluation 1377 are recomputed from explicit finite objects by `verify_frucht.py`, which checks all 531441 states and 4096 vertex sets. No thermodynamic-limit or finite-temperature assertion is made. Risk: implementation transcription, mitigated by direct mathematical decomposition and independent exact enumeration; a separate researcher has not audited the result.

## Originality — PASS on available evidence

Shrock and Xu, arXiv:1009.1182 (2010), provide a general field-dependent Potts model and graph-partition framework; their exact graph cases concern paths, cycles, trees, complete graphs, joins and related families, not the particular field-induced complementary occupation classes here. Their zero-temperature antiferromagnetic weighted chromatic polynomial enforces proper coloring, whereas the upper intermediate plateau here retains precisely three monochromatic edges. The Frucht graph description covers its asymmetry and independence number, not field-driven sitewise occupation inversion. Publicly indexed field calculations on the truncated tetrahedron, Grötzsch graph and line graphs concern different host graphs and do not contain a universal implication establishing the Frucht reversal. Search failure is not a uniqueness or historical-priority certificate. The original 1949 graph article was not read in full; an unindexed equivalent Frucht spin calculation is a residual risk.

## Mathematical value — PASS

This is not merely a ground-state count. An increasing *uniform* field causes the favoured-color indicator to decrease from one to zero **at every vertex in a five-site set**, while increasing at each complementary vertex, in a naturally distinguished cubic graph with no nontrivial graph automorphism. The exact reversal is explained by a unique maximum independent set and its induced matching complement. This gives a rigorously characterized failure of sitewise monotonicity for an antiferromagnetic spin system and two sharp field thresholds, including endpoint degeneracies. The value is finite-system and structural; no broader universality or minimum-graph-size claim follows.

## Closest work and limits

The closest archived primary source is Shrock and Xu (2010), https://arxiv.org/abs/1009.1182. The Frucht construction is referenced through the 1949 paper DOI https://doi.org/10.4153/CJM-1949-033-6 and MathWorld. Existing exact finite-graph Potts field tables on other twelve-site or nonbipartite graphs are not equivalent. Scope is precisely the graph and coupling conventions written in the theorem; historical priority is subject to further checking.

Self-review: passed. Independent audit: not yet performed.
