## Correctness — PASS

The proof reconstructs every single-pass, critical-energy, initially periodic configuration from its unique firing times. The conserved chip total forces equality in each pre-first-firing eligibility constraint, hence prohibits simultaneous firing across an edge. The complete bipartite structure and next-round eligibility then force alternating nonempty shore blocks, including across the cyclic boundary. Conversely, two ordered shore partitions and a starting shore construct a unique periodic configuration; degree-threshold verification supplies the exact sequence, and a proper subperiod contradicts a unique firing per vertex. The count and orbit division follow without appealing to computer sampling. Two independent standard-library finite tests reproduce all checked cases; see `VERIFICATION.md`.

## Originality — PASS, with residual historical risk

Jiang (2010) gives the allowed period set for complete bipartite graphs and constructs samples (Proposition 3.9), but not the entire minimal-mass single-pass per-period count. Jiang, Scully and Zhang (2012) characterize admissible binary firing patterns; their result does not present the specified chip-mass census. A later paper studies higher chip-density bands. Existing accessible period-two and period-four enumerators cover corresponding lower-period special cases, which are *not* offered as novel. The substantive new part is the structural bijection and the full family of exact period-six-and-higher counts. A related paper by Goles and Prisner (2000) was only accessible as abstract/metadata; equivalence through source-reversal theory remains a documented uncertainty. Absence of indexed results is not assumed to certify absolute priority.

## Mathematical value — PASS

The counting problem is a natural finite-energy refinement of the known period-length classification of parallel chip firing. It resolves a complete infinite two-parameter period census in a precise dynamical sector and yields a nontrivial Stirling-number profile and exact maximal-period orbit populations, rather than a routine example of the existence theorem. The constraints defining the sector are essential and are explicitly retained; no claims are made about the unrestricted critical-energy recurrent set.

## Literature and limitations

Primary full text inspected: Jiang (2010), Sections 1–3; Jiang, Scully and Zhang (2012), Sections 1 and 6–7; Ji, Li and Wang (2024), abstract/introduction and chip-mass statements. The related Goles–Prisner (2000) source-reversal work was available only bibliographically and as an abstract. The classification is restricted to already-periodic states at mass \(mn\) with one firing per vertex per least period; neither fixed points, multiple-firing states nor transient attraction basins are counted.

Self-review: passed. Independent audit: not yet performed.
