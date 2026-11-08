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
# Verification

The universally quantified proof is in `RESULT.md`. Its key steps are the commutator block rank identity, the unicyclic incidence-dependence criterion, the finite-field character count for constrained nonzero pairs, and the exceptional full-cycle correction. The constructive argument realizes all ranks from zero through the number of vertices.

Run `python verify.py` in a directory containing that standalone file. The expected output is `VERIFY_OK_UNICYCLIC 13`. The verifier builds the algebra multiplication table directly and does not use the proof's incidence-block matrix; it enumerates all elements, constructs every commutator linear map, and uses field-specific Gaussian elimination. Thirteen complete finite cases over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) include reversed arrow orientations, cycles with multiple tree attachments, and the characteristic-two extension field.

For example, the directed 3-cycle over F2 has exact rank frequencies `(2, 6, 32, 24)` for ranks zero through three; the directed 4-cycle over F2 has `(2, 8, 60, 106, 80)` for ranks zero through four. These computations are finite checks, not an exhaustive verification of all fields and dimensions. No independent audit was performed.
