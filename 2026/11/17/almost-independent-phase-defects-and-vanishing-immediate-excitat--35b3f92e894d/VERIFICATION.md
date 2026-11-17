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

The included `tools/defect_check.py` uses Python standard-library integer and rational arithmetic and exhaustive enumeration for Boolean cube dimensions 1, 2, and 3. It checks the direct three-step update against the local contact criterion, exact first two moments, and all available distance-one and distance-two joint probabilities. Its captured standard output is `data/defect_check_output.txt`.

Run `python3 tools/defect_check.py` from the package root. The program terminates with `ALL_CHECKS_PASS` on a successful execution. Finite enumeration alone does not establish the claim for arbitrarily large cube dimension; the general proof uses disjoint neighborhood reasoning and the published Chen–Stein bounds. No independent audit or external certification is claimed.
