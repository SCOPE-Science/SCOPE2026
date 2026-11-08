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

Run `python3 verify.py` with Python 3 and its standard library. The executed script returned `PASS: 252 rational parameter triples, 50904 exact symbolic-formula/word-evaluation checks, and rational witness.` It forms \(U\), \(V\), and \(W\) from rational rank-one projections; checks the analytic trace and determinant of the two-step error-moment difference; independently enumerates four equally likely ordered samples for twenty-five initial integer error vectors per parameter triple; and checks all three fractions of the explicit witness. This verifies exact arithmetic at the sampled points, not the universal theorem.

The universal two-step statement follows from the algebraic identity for \(D\) and the signs of its trace and determinant proved in RESULT.md. The source's relaxation rule was checked in the October 8, 2026 arXiv HTML article. Historical originality is assessed against the inspected sources with the access limitations recorded in AUDIT.json. No independent expert validation or external audit has been performed.
