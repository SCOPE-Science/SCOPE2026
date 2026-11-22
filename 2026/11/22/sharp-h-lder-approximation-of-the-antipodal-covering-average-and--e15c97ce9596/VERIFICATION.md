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

# Reproducibility and verification

The precise norm domain, the two-sheet distance transform and all parameter quantifiers are stated in `RESULT.md`. Four analytic components are checked: the concave transform is a metric, Kantorovich–Rubinstein duality identifies the operator defect with transport, the odd/even monodromy lower bounds hold for arbitrary continuous labelled maps, and the explicit single-label-flip constructions attain the bounds. The only finite-dimensional linear program is the two-sink integral assignment problem described in the proof.

Run the standalone, standard-library script using `python CHECK.py`. It performs explicit exact-vertex-enumeration transport comparisons at finite meshes for nine term counts and six cost functions, checks the glued endpoint condition, and prints `CONCAVE_CIRCLE_TRANSPORT_DIAGNOSTIC_OK 2799` on success. These computations are finite diagnostics, not a formal certificate for all term counts or all concave metric transforms. Bibliographic uniqueness is not independently established.

Independent audit: not performed.
