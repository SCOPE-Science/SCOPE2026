# Scientific review — star coloring on four cubic girth-six graphs

## Correctness — PASS

The full constraints of proper vertex-star coloring were reconstructed from the no-bichromatic-four-vertex-path definition. The canonical restricted-growth enumeration is exhaustive up to global palette permutation because every coloring has a unique first-appearance normalization. Early pruning only excludes completed prohibited edges or completed forbidden paths and thus preserves all valid solutions. Independent original-order Python and BFS-order C++17 implementations enumerate the complete feasible sets, test nonexistence of every three-color solution, recover all 24 named permutations of each optimum, build all legal single-vertex recolorings, and identify all connected components. Python also checks the eight-cycle rim criterion for the nine-vertex grid components. The two standalone programs return identical detailed numbers; their recorded successful runs are included. Full finite enumeration, not a truncated sample, is the proof of the finite census. No independent scholarly assessment is implied.

## Originality — PASS, with priority risk

Actual searches of mathematical research records for star-coloring and the names of all four graphs, optimal partitions, frozen star colorings, and reconfiguration yielded no prior result implying the exact four component decompositions. The closest star-coloring theory gives generic subcubic upper bounds, not exact optimal-recoloring graphs; an indexed Heawood result instead concerns strong **edge** coloring, whose two-edge-color-path constraints differ. Published ordinary recoloring results permit intermediate colorings forbidden under the star constraint. No inspected statement covers the ordered combination of all four structures. No known table containing these component counts was located. Unindexed historical enumerations and papers not available in full are residual priority risks. This is a best-knowledge originality judgment, not proof of universal uniqueness.

## Value — PASS

The quartet is not a handpicked arbitrary induced subgraph: it comprises classical, highly symmetric cubic graphs of girth six. At the same optimal palette size, their exact recoloring components range from purely eight-vertex cubes to thousands of isolated states, with a nine-state grid structure at Desargues. This supplies a natural finite family of starkly differing obstructions to local recoloring under a no-bichromatic-four-path constraint; full shape identification and all optimizer counts make the statement stronger than isolated chromatic-number computations. The finite scope is explicit, and there is no claim of a broader asymptotic theorem.

## Sources and limitations

The primary dated archival source is Albertson et al., *Coloring with no 2-Colored P4's* (2004, DOI 10.37236/1779), with its published March 31, 2004 date. Fertin–Raspaud–Reed (2004, DOI 10.1002/jgt.20029), Karthick–Subramanian (2013, DOI 10.7151/DMGT.1672), and standard recoloring literature were compared for generic coverage. Historical graph-specific numerical tables may be unindexed. The classification is a machine-reproducible finite result and has not undergone independent scholarly audit.

Self-review: passed. Independent audit: not yet performed.
