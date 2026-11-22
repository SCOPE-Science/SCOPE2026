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

`verify.py` uses only Python's standard library. Invoke `python3 verify.py` from the extracted folder. The output was independently generated from that exact source before packaging, saved verbatim as `verification_output.txt` and compared during package validation.

The test enumerates all independent faces, constructs augmented boundary maps over the field with two elements, and checks exact reduced Betti numbers. It covers 28 symmetry-reduced two-arm configurations, 20 three-arm configurations, 15 four-arm configurations and 7 four-to-six-arm stress cases, for 70 total. The two-arm instances are known-baseline checks outside the new theorem's claimed domain.

This is not a machine certificate of the infinite homotopy equivalence. The written argument establishes the integral statement by a complete double mapping-cone decomposition and path-inclusion homotopy equivalences. No independent scientific audit has been performed.
