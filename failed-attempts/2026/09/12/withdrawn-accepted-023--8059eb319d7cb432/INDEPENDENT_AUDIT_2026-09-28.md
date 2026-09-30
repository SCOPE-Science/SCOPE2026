# Independent Audit — 2026/09/12/023

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `7cf00364e6b15e29bd7531c071bc5346db4ea602`  
**Disposition:** **FAILED**

## Correctness

The zero colour-frequency gap follows exactly from symmetry. Reflection R(x,y)=(y,x) preserves the regular Ammann-Beenker octagonal window, swaps the two diagonal half-windows, and permutes the eight star offsets; therefore the star acceptance domain D is R-invariant and D+ and D- have equal area. This alone falsifies any conjunction requiring a strictly positive symmetric-star gap. The numerical clipping script is only a consistency check; the proof is exact.

## Originality

Patch frequencies of regular model sets are standardly computed as areas of acceptance domains in internal space, and the Ammann-Beenker window has the dihedral symmetries used here. Once the colour split is chosen along a symmetry diagonal and the patch itself is reflection-invariant, equality of the two colour areas is an immediate symmetry consequence rather than a new aperiodic-order phenomenon.

## Scientific value

The observation is useful for rejecting an overstrong target, but it does not establish a new diffraction theorem, a new inflation invariant, or a nontrivial patch-frequency classification. It is a one-line symmetry obstruction for one deliberately symmetric patch/split, so it is better retained as target triage than as a standalone validated finding.

## Limitations

- The audit conclusion is only about the symmetric 8-star and the y=x diagonal split.
- No conclusion is drawn about asymmetric patches, other colour-window cuts, or independent Bragg-contrast clauses once the conjunction has already failed.
- The repository's floating polygon calculation is not needed for the exact equality and is treated only as a numerical cross-check.

## Evidence

- [Baake–Grimm, Homometric model sets and window covariograms](https://arxiv.org/abs/math/0610411): Uses regular model-set window geometry and covariograms in diffraction/homometry, providing the standard internal-space framework in which window symmetries control frequencies.
- [Jagannathan–Duneau, Properties of the Ammann-Beenker tiling and its square approximants](https://arxiv.org/abs/2308.07701): Reviews the octagonal cut-and-project geometry of the Ammann-Beenker tiling; the relevant dihedral window symmetry is standard.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `7cf00364e6b15e29bd7531c071bc5346db4ea602`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
