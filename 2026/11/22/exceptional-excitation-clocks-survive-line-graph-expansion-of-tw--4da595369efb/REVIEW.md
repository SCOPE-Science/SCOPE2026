# Scientific review: exceptional excitation clocks on line graphs

## Correctness — PASS
The claim is precisely about the line graphs of \(GP(5,1)\) and \(GP(5,2)\), each with fifteen labelled vertices and \(3^{15}\) labelled states. The update is specified unambiguously. Two complete, independent state-transition reconstructions agree on every nonempty period/entry histogram cell (46 and 37 cells). An exhaustive cycle classifier counts least periods and sharp depths, and a separate indegree-pruning algorithm corroborates them. A standard-library-only permutation checker enumerates all twenty and 120 automorphisms of the triangle-free cubic bases, which exactly recover the full line-graph automorphisms via their ten incidence-star triangles. It validates each exceptional cycle and obtains the claimed partitions. The proof includes the finite-map correctness argument. Remaining risk is undetected errors shared by code and problem formulation; no formal or external audit is claimed.

## Originality — PASS, qualified
Actual searches of indexed published mathematical records for one-contact Greenberg–Hastings dynamics on the Petersen line graph, pentagonal-prism line graph, and possible exceptional-period preservation found no equivalent indexed claim. The closest published ten-vertex generalized Petersen census has the *same periodwise non-three numbers* but on the original graphs; that fact alone does not determine the nonlinear dynamics of their fifteen-vertex line graphs. Gravner–Lyu–Sivakoff (2016) supply qualitative general circulation criteria, not exact line-graph transition counts. The published Tait-coloring theorem is for two-contact threshold and period three. We inspected the complete primary arXiv HTML theory and the full published-finding corpus `RESULT.md` for each close statement. Historical/unindexed stronger equivalent results remain a material priority risk. Search absence is not a uniqueness proof.

## Value — PASS
The pair is canonical (the two ten-vertex generalized Petersen graphs) and the line-graph operation is natural, increasing the graph from ten cubic sites to fifteen quartic sites. Exact non-three orbit populations survive this expansion in both pairs even as period-three orbits grow from 150 to 195250 and from 80 to 220810, and maximum first-entry times grow from eight to seventeen and six to twelve. The unusual conservation is a motivated exact comparison, not an arbitrary subcount, and the distinct geometric-class partitions show structural differences invisible to temporal counts. The complete finite orbit and basin tables are useful benchmarks for studying excitability under graph transformations, without implying a general theorem or physical causal interpretation.

## Closest sources and residual limits
- Gravner, Lyu, Sivakoff (arXiv:1610.07320v1, 2016-10-24), Theorem 3: qualitative global graph dynamics; no precise line-graph census.
- Published `Exact recurrence and basins on the two ten-vertex generalized Petersen graphs`: original cubic graphs; equivalent *numerical exceptional counts* but not coverage of the expanded graph dynamics.
- Published `Tait colourings as primitive-three excitation on cubic line graphs`: distinct excitation threshold and primitive period.
- Other exact finite-graph studies concern different graphs and do not imply this result. The finite calculation is complete for the stated two graphs but not independently externally audited, and wider priority remains uncertain.

Self-review: passed. Independent audit: not yet performed.
