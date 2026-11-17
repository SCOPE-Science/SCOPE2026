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

Run `python3 check_trend_bv.py` from the extracted files with Python 3. The code uses only the standard library and exact `fractions.Fraction` arithmetic; it does not call an external optimizer. For every \(2\le n\le8\), it enumerates \(2^{n-2}\) subsets of zero-curvature rows, computes exact orthogonal projector matrices with rational Gaussian elimination, and tests every single-jump indicator cut. The exhaustive algorithm relies on the mathematically proved face/cut reduction in `RESULT.md`.

Expected rational constants in order: \(1,1,6/5,4/3,7/5,28/19,11/7\). It also checks that each projector fixes constants, explicitly verifies the four-site primal-dual witness, and tests the analytically derived all-length lower-bound identity for \(4\le n\le25\). The latter finite range is not an infinite proof; the analytic argument proves the formula for all \(n\ge4\).

The self-review documents correctness, prior-work comparison and value. No independent audit was performed. No assertion is made that searches establish absolute historical priority.
