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

The standalone `verify.py` uses only Python 3 standard library and asserts exhaustive coverage for every pair of total transition tables through order four, separate Burnside counts, and pairwise distinct joint counting-refinement signatures. It also checks the five-point counterexample against every bijection. `expected_output.txt` contains the reproducible deterministic output. The finite assertion is established by exhaustive enumeration; no claim is made beyond the proved first-collision bound or of independent validation.
