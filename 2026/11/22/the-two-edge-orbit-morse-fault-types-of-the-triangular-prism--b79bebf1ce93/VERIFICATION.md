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

# Independent reproducibility

The complete standard-library script `verify_faults.py` is supplied with this result. Run `python3 verify_faults.py` in the same directory. No network, package installation, external generated files, precomputed tables, or source downloads are necessary. It recomputes both graph cases from labeled edge lists, and terminates with `ALL CHECKS PASSED` only when every exact assertion succeeds.

## Expected independent checks

For the missing rung, the nonempty face vector is `(16, 98, 284, 381, 180)`, the acyclic Hasse matching has 463 pairs and critical cells in dimensions `(0:1,3:16,4:16)`, and the exact integer Morse differential has seven unit pivots and zero remaining entries. The original chain complex's mod-two boundary ranks are `(15,83,201,171)`.

For the missing triangle edge, the nonempty face vector is `(16, 98, 286, 397, 210)`, the acyclic Hasse matching has 491 pairs and critical cells `(0:1,3:4,4:20)`, and the exact integer Morse differential has four unit pivots and zero remaining entries. The original mod-two boundary ranks are `(15,83,203,194)`.

The script enumerates *all* `2**16` incidence subsets in each case, not selected samples, and checks Hasse acyclicity across 959 and 1007 nonempty simplices. From the one-vertex three-/four-dimensional Morse CW complexes and their integral unit degrees, the degree-three Hurewicz theorem upgrades these calculations to wedge-of-spheres homotopy equivalences.

## Limitations

The exact finite verification proves the two six-vertex graph cases; symmetry supplies all edge deletions of the triangular prism. It does not prove any classification for larger prism graphs or determine the inclusion maps to the intact graph. No independent external mathematical audit has been performed.
