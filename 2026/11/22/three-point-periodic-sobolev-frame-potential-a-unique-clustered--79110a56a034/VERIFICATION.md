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

The proof in `RESULT.md` is analytic. The standalone standard-library script `VERIFY.py` checks exact rational kernel, Gram, stationary-polynomial, and benchmark identities and enumerates 487452 exact rational assertions, including all three-gap rational partitions of denominators 3 through 144. Execute `python3 VERIFY.py` to reproduce the checks. This enumeration is finite and does not establish the continuum theorem; boundary comparison and exhaustive Lagrange critical-point analysis supply that proof.

The reference comparison used public versions of arXiv:1403.7382, arXiv:1407.1663, and arXiv:1301.5288, and the dated arXiv:1210.5488 abstract. It does not exclude all unindexed historical results. No independent audit was performed.
