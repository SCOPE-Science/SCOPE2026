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

# Reproducibility and scope

Execute `python3 verify.py` with Python 3 standard library. The verifier constructs the grounded path Laplacian from its edges, independently inverts the matrices by exact Gauss–Jordan elimination, and compares the direct inverse-trace changes against the proposed closed-form gain. It also checks positive/negative/tied adjacent gain differences and exact global maximizers at the full rational threshold set. The executed run reported 60,096 passing exact identities and limiting sanity checks.

Finite checks do not prove the statement for every chain length or every real edge weight; the proof in `RESULT.md` establishes those claims symbolically. Continuous-time noise normalization follows the independent unit-Brownian diffusion convention, making the stationary covariance half the grounded inverse. The source comparison includes an uninspected relevant 2026 preprint's full text; priority is not externally certified.
