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

## Reproducibility
Run `python3 check.py` using Python 3 and the standard library. The exact-rational checker outputs `PASS 9728 exact-rational assertions`. It exercises the three branch formulas, checks first-return agreement with the rotation, computes least periods of sampled rational points, and verifies the band integration and normalization formulas for coprime \(p,q\) with \(2\le q\le8\).

## Scope
The finite program is a consistency check only. It does not prove the all-rational-parameter or irrational cases and does not certify novelty or publication priority. The proof in `RESULT.md`, especially the exact grid-phase count, size weighting and symbolic integration, supplies the unrestricted argument. There has been no independent audit.
