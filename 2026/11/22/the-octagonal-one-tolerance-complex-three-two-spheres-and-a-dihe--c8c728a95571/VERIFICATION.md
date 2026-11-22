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

# Reproducibility and limits

Execute `python3 check.py` in this directory with `collapse_certificate.json` in the same directory. This checks the exact defining face oracle on all nonempty subsets, the 40 ordered elementary collapses (including uniqueness of each free face's coface at the moment of removal), the terminal f-vector, two modular second-boundary ranks, and all signed fixed-simplex Lefschetz traces. All sixteen dihedral permutations and the derived rational quotient ranks are covered. The scientific proof of simple connectivity, torsion-free integral homology and the wedge decomposition appears in `RESULT.md`. The executable enumerations are finite and establish only the specified eight-vertex instance; no other-instance extrapolation is claimed.

An independent matrix calculation over the integers for the terminal boundary map gave Smith diagonal entries equal to one with multiplicity thirteen; this is corroboration, not an assumption used in the homotopy proof. No independent mathematical audit has been performed.
