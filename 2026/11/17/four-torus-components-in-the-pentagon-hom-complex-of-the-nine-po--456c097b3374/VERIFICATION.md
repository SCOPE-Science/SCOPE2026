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

# Verification and reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. The script produces one JSON line equal to `certificate.json` when parsed. No external packages or downloaded data are used.

Checks are exhaustive for the nine-vertex target and five-vertex source: all 59,049 candidate vertex maps; both construction methods for all 4,680 product cells; signed boundary-squared identities; all 360 elementary free-face collapses with current maximality and uniqueness; connected components; all surviving edge-to-face counts; all 900 vertex links; integer orientation compatibility; and surface Euler characteristics. The four surviving surfaces each have cell vector \((225,495,270)\), all orientable, so each has genus one.

The verifier is a finite computation, but it is exhaustive for the exact finite claim. It is not evidence about other graph targets or cycles. An independent external audit has not been performed.
