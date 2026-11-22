# Self-review

**Correctness — PASS.** The claim is finite and exactly specified. The disjoint excited/refractory-mask transition follows directly from the three-state update. Two distinct exhaustive methods reproduce all twelve histogram cells across \(2\cdot3^{16}\) initial states: full ternary-code enumeration and independently weighted initial/next-excitation-mask grouping. The latter has an exact multiplicity proof. Explicit witnesses establish sharpness, while independently enumerated affine graph automorphisms give the eight Shrikhande extremal symmetry classes. `sh verify.sh` has passed using sources included with this finding.

**Originality — PASS, qualified.** The closest published same-graph result (*Four-cycle excitation clocks distinguish the Shrikhande and rook graphs*) uses the different threshold-one update and does not imply the three-contact extinction census. The earlier half-degree period-three theorem and general triangle-cover result concern existence/absence of recurrence, not exact first-extinction-time distributions or the eight maximal-shell orbits. Gravner–Lyu–Sivakoff and Doba also use the single-neighbor rule. Targeted searches found no matching threshold-three census. Equivalent unindexed work remains possible.

**Value — PASS.** The two graphs are the canonical nonisomorphic strongly regular pair with identical parameters and spectrum, making them a natural controlled test of what spectral data can determine about nonlinear dynamics. A genuine sharp four-versus-five relaxation separation, and the explicit rare 1,088-state final shell split into eight symmetry types, adds useful dynamical information beyond the known universal-extinction fact. These are complete natural invariants, not arbitrary parameter slices.

**Limitations and risk.** This is a two-graph finite computation, not an infinite-family theorem; the priority check is best-knowledge, and independent external audit is not performed. The general extinction principle is not separately claimed as original.

Self-review: passed. Independent audit: not yet performed.
