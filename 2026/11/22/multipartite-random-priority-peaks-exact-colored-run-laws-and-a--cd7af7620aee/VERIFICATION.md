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

The package includes standalone `check.py`; run `python3 check.py`. The code uses exact `fractions.Fraction` arithmetic and exhaustive permutations and color assignments for small complete multipartite graphs, including the three-part case. Checks concern finite laws and identities. The Gaussian weak limit and variance limit are justified by conditional Berry–Esseen, uniform geometric tails, count concentration and the bounded-difference centering argument in `RESULT.md`; those infinite claims are not established by a finite enumeration. No independent validation has been performed.
