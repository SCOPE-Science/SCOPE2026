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

The theorem is established by the all-dimensional symbolic argument in `RESULT.md`. The separate `verify.py` reconstructs each signed-independent-set vertex support, exact rational John/Löwner coefficients and complementary-slackness equations for `n=3,...,16`, and independently optimizes 18 log-determinant problems with SciPy for `n=3,...,11`. The numerical programs test finite ranks only; they neither certify the all-rank proof nor independent validation. Reproduce with `python3 verify.py` in the extracted package directory; expected token: `FENCE_EXTREMAL_ELLIPSOIDS_PASS`.

Sources and limits: Ohsugi–Tsuchiya provides signed-chain facets (Proposition 6.1 of their 2020 paper); the other prior full-texts and exact historical comparisons are detailed in `REVIEW.md` and `AUDIT.json`. Graph-entropy aliases leave a residual priority risk. The claim is specific to the standard Euclidean coordinate embedding.
