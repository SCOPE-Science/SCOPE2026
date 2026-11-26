---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of finite periodic Fourier interpolation

The proof in RESULT.md uses the unitary length-\(m\) transform across cells, exact parity decomposition of a real \(3\times3\) Gram matrix, and an analytic sign test for the unique interior crossing. It applies for every \(m\ge1\), including the endpoint with repeated nodes. The collision calculation serves as a check against the already known leading law for a symmetric three-source cluster.

Run `python3 checker.py` with the Python standard library only. Its recorded run passed 88 full-matrix spectral moment comparisons and the supplementary transition and collision checks. These finite floating-point checks do not certify an infinite-domain assertion. The results concern the specified equal weights, consecutive frequencies, and three-periodic sampling pattern only.
