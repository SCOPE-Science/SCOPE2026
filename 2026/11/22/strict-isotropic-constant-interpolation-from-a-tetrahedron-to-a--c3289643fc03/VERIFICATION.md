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

# Verification and limits

Run `python3 verify.py` in the extracted folder. This requires only Python 3's standard library. The script independently partitions the frustum into three tetrahedra and exactly integrates volumes, first moments, and second moments using barycentric integration; it recomputes the determinant and agrees at ten rational values of the truncation parameter. It passed 151 exact assertions. The derivative factorization, its sign for the entire open interval, and asymptotic endpoint expansions are proved analytically in `RESULT.md`; finite checks are not used to certify an unbounded continuum. The reported outcome is a self-review, not independent verification or a historical-priority certificate.
