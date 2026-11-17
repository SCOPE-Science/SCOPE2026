# Scientific review

## Correctness: PASS

The ordinary three-cut complex is defined by disconnected induced triples. Its Alexander dual consists exactly of vertex sets whose induced nonedge graph has maximum degree one. The signed equivariant Alexander-duality identity converts the unique top homology character into an augmented signed face trace. In the published stable shellability range, this identity is exact in all dimensions. Every nontrivial rotation orbit of order at least three contains two nonneighbors per vertex, while an antipodal half-turn permits only the empty face and individual antipodal pairs. Reflection-invariant sets decompose into vertex-axis and edge-axis orbit clusters; the former cancel by toggling their fixed vertex and the latter admit a finite binomial cancellation. This yields the three stated reflection formulas without extrapolating from numerical data. The invariant-rank formula is the direct character average.

Independent finite checks use a separate permutation-orbit enumeration of the dual, and a direct construction and simplicial trace of the original cut complex. The verifier recorded 165 dual-character comparisons, 122 direct comparisons, and 30 invariant-rank checks. This verifies samples and implementation details, not the infinite proof. The 2026 shellability theorem and the orientation twist remain mathematically indispensable.

## Originality: PASS against inspected sources

The 2023 cut-complex article supplies the basic construction and earlier equivariant examples. Its 2024 successor determines dihedral characters for unpowered cycles, not for cycle powers. The 2024 squared-cycle paper establishes homotopy dimensions without complete dihedral characters. The 2026 all-power shellability paper proves homology concentration and ranks but does not furnish the all-power reflection representation. A published prior result already determines every rotation for all powers; its complete public proof and explicit lack of reflection characters were inspected, and the result is incorporated with attribution. A preceding calculation covers reflections for the squared-cycle case and is explicitly excluded from the novel scope. Statement-level searches found no earlier consequence yielding the closed reflection formulas for all powers, especially every power at least three. Search failure is not an independence proof; unindexed literature is a residual risk.

## Value: PASS

This closes a natural representation-theoretic gap left by the all-power homotopy and cyclic-character theorems: the full dihedral character of an infinite, geometrically symmetric family. It distinguishes inequivalent vertex-axis and edge-axis reflections and yields a global vanishing criterion for invariant classes at every admissible length congruent to one modulo four. Such conclusions cannot be recovered from Betti numbers or from the rotation character alone. No unjustified integral or equivariant-homotopy consequence is asserted.

## Relationship to prior work and limitations

The exact sphere count and vanishing of other degrees are imported from Chauhan and Shukla (arXiv:2603.23155, Theorem 1.4). The rotation part and the squared-cycle special case are previously available, while the general reflection calculation is the present assertion. The result is rational and restricted to the established shellability range; it does not address smaller lengths or other cut parameters. The full proof is in RESULT.md; verification_output.txt records finite independent checks.

Self-review: passed. Independent audit: not yet performed.
