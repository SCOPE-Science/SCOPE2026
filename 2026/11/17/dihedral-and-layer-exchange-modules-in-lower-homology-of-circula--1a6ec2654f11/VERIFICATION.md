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

# Reproducibility

Run `python3 verify.py` in this directory. The script uses only the Python standard library, reads no external inputs, and terminates with `CIRCULAR_LADDER_EQUIVARIANT_CHECKS_PASS` if all assertions succeed. Its stdout is included in `verify_output.txt`.

The cycle-orbit calculation evaluates all rotation and reflection traces of the cycle independence-complex homology for \(n=6,12,18,24,30,36,42\), testing 336 group elements against the six-periodic character formula. For widths \(4,6,8,10\), complete enumeration of perfect matchings and simplicial faces independently checks the decomposition into the invariant base and two exceptional simplices and verifies the intersection complexes. At width six, full and base signed-Lefschetz numbers differ by the predicted relative character for every group element. At width twelve, a separate computation of the alternating relative simplicial traces on the exceptional faces gives the predicted character for all 48 group elements without using the orbit-graph independence-polynomial calculation.

The finite checks test particular widths and cannot independently prove an unrestricted classification. The all-width proof is contained in `RESULT.md` and uses the explicitly cited published graph-folding and matching-extension lemmas; the verification does not establish any integral equivariant lattice decomposition or external independent audit.
