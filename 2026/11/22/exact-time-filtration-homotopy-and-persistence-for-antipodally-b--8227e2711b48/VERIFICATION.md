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

Run `python3 verify_filtration.py` using Python 3.10 or newer with no external dependencies. Its `stage_complex_check` enumerates every nonempty face of the 4-element translated firing simplex and independently tests its actual intersection with all earlier faces, including the four-row corner cases. It checks the specified previously appearing cone triangles, and `dynamics` directly implements synchronous chip transfer for full periods. The `barcode` function constructs and reduces the complete mod-two simplicial boundary matrix in filtration-compatible simplex order. All assertions must pass and the terminal output match `filtration_verification_output.txt` byte-for-byte.

Proved all-parameter statements rely on the symbolic residue intersection table and explicit triangle cones in `RESULT.md`; finite tests neither extend the theorem nor certify it independently. The computations over \(\mathbb F_2\) corroborate but do not establish the integral decomposition. No independent mathematical audit has been performed.
