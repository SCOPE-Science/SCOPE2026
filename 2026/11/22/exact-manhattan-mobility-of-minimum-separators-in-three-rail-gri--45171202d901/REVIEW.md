# Scientific assessment

## Correctness — PASS

The claim is an all-length theorem for a specifically defined three-rail grid and fixed middle-row terminals. Three disjoint terminal paths force the cardinality-three lower bound, while an internal column realizes it. The possible row coordinates are characterized both by explicit detours outside the bounds and a left/right cut partition inside the bounds. All and only legal slides change one feasible triple coordinate by one. A no-cycle blocking argument supplies monotone geodesics and the exact Manhattan metric. Optimizing the explicitly proved eccentricity formula yields the stated radius and diameter. Independently written, standalone checkers confirm every cut and every pairwise distance in directly enumerated graphs through nine columns, then confirm the full coordinate geometry through 24 columns. The computations are corroboration, not proof of the infinite claim.

## Originality — PASS, qualified

The primary 2023 minimum-separator reconfiguration paper proves a general shortest-slide algorithm and canonical-path confinement, which we explicitly credit: pathwise displacement is not claimed as an algorithmic novelty. It does not identify the three-row middle-terminal separator space, prove its global connectivity, or calculate its state count, edge count, eccentricities, radius, and diameter. The 2020 precursor treats broader (not necessarily minimum) separator reconfiguration and graph-class algorithms; accessible text does not identify the exact target family. Searches for aliases involving 3-by-\(n\) grids, strip vertex cuts, Cartesian products and the exact formulas, together with relevant indexed-record searches, yielded no covering result. This is evidence of originality, not a proof of global priority. The 2020 full document was not materially inspected, and unindexed or differently named prior calculations remain possible.

## Value — PASS

A three-rail rectangular grid is a natural small-width planar network in which the terminals have three internally disjoint routes. The theorem classifies every minimum failure set and proves that local reconfiguration never requires temporary loss of minimum-cut optimality. The exact \(3n-5\) worst-case relocation length and all-configuration eccentricity formula make a quantitatively sharp benchmark for shortest separator rearrangement, supplementing general complexity/algorithmic results. The statement is not an arbitrary finite slice: it is uniform across the entire length parameter. It does not claim a general downstream theorem or applications not proved by this model.

## Closest sources and limitations

- Gomes et al., *Minimum Separator Reconfiguration*, arXiv:2307.07782 (first public 2023-07-15), sections on canonical paths, forward-motion and shortest token slides: https://arxiv.org/abs/2307.07782
- Gomes, Nogueira and dos Santos, *Some Results on Vertex Separator Reconfiguration*, arXiv:2004.10873 (first public 2020-04-22): https://arxiv.org/abs/2004.10873

The claim is restricted to middle-row terminal endpoints and minimum-cardinality cuts under token sliding. There is no assertion about arbitrary terminals, more rows, or token-jump geodesics. Independently performed review is not claimed.

Self-review: passed. Independent audit: not yet performed.
