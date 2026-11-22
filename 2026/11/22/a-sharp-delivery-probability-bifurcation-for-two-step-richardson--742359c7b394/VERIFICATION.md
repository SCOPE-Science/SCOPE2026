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

Run `python3 artifacts/verify_bernoulli_richardson.py` with Python 3 and SymPy. The included recorded output reports `VERIFY_OK 1010`. The symbolic checks expand the precise global weighted-endpoint sum-of-squares certificate and the unequal-step perturbation identity to zero. Exact-rational examples exercise several condition numbers, success probabilities including the boundary, and two-step parameters. A separate rational convexity calculation verifies the explicit high-reliability improvement.

These computations are not a proof for infinitely many real inputs. That proof is in `RESULT.md`, relying on exact algebra and compactness. They check the identities used in it and a concrete numerical witness. Independent mathematical validation has not been performed.
