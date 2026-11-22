---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification procedure and limits

From this directory run:

```sh
python3 verify_stabilizers.py
python3 verify_orbit_cells.py
```

The first command prints `STABLE_KNESER_ORBIT_CHECK_OK` after regenerating all stable-pair independence faces for each cyclic length 8 through 12, checking 100 rotation/reflection actions, their invariant faces, signed Lefschetz traces and the subgroup arithmetic. The second command prints `STABLE_KNESER_HOMOTOPY_CHECK_OK` after building the barycentric-flag orbit CW structure, checking actual elementary free-face cancellations, contracting a spanning tree and simplifying triangular attaching words by reversible generator eliminations for both actions at lengths eight and nine.

Expected residual CW counts are `(12,35,24)` and `(18,56,40)` for the rotation quotients, and `(1,0,0)` and `(8,18,12)` for the dihedral quotients; the ordered coordinates are degrees zero, one and two. The nontrivial final attaching words are four copies of the surviving circle generator in the first rotation quotient and two triples of its inverse in the second. The dihedral length-nine quotient retains one nullhomotopic two-cell after eliminating all one-cells.

Finite calculations cannot establish the arbitrary-length theorem. The all-parameter proof uses Braun's established simple-connectivity result, the complete chord-family stabilizer classification, Armstrong's quotient fundamental-group theorem and the equivariant two-dimensional cell model. The character formula is credited to its previous mathematical source. No external or independent audit is asserted.
