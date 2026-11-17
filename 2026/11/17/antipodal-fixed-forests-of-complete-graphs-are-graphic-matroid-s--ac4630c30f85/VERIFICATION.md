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
The proof reduces orbit-admissibility to the forest property of a named multigraph and then applies standard matroid shellability and exact labeled-tree enumeration. The accompanying Python script reconstructs both graph models separately and compares all \(2^{m^2}\) selections of edge-orbits for \(m=1,2,3,4\). It checks face vectors and alternating Euler values and contains no third-party dependencies. Run `python3 proof/verify_antipodal.py`; the expected stdout is embedded in `proof/verify_output.txt`.

This finite enumeration does **not** prove the all-parameter result by itself. That result relies on the double-cover tree-component argument. The homotopy classification relies on established shellability of matroid independence complexes. No independent audit or external formal certification is asserted.
