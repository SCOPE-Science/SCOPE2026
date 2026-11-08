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

# Verification of the endpoint correlation law

The proof is given in `RESULT.md`; the separate executable `verify_meandric_endpoint.py` directly enumerates all configurations for small lengths, independently recomputes the finite-state and first-moment recurrences, numerically checks the mode sums, tests the Green function at every site through \(m=100\), and verifies half-integer cosine eigen-relations. Run using `python3 verify_meandric_endpoint.py`; the completed check produced `VERIFY_OK checks=21378`.

These checks are finite and cannot certify the asymptotic profile or novelty. The analytical arguments in `RESULT.md` establish the statements for all positive lengths and the indicated limit. The different sampling of an extra inert index in the public implementation is reflected in the explicit finite-time adjustment. Historical-priority concerns are detailed in `REVIEW.md`; no independent mathematical audit has been performed.
