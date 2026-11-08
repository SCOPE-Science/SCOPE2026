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

# Reproduction and limitations

Run `python verify.py` with Python 3.10 or newer and no third-party dependencies. The bundled exact rational checks verify the BST distribution recursion through size 26, cumulant linearity through order eight for all accessible sizes, conditional split moments through order four, the two-leaf event and its monotonicity, and  all permutations for every size one through eight (46,233 total), computed independently by constructing insertion trees and comparing to local maxima.

The test output for the delivered program is `PASS: 93551 exact identities, including exhaustive independent insertion histories through n=8`. These finite calculations complement but do not replace the proof for unrestricted sizes and moment orders.

Self-review: passed. Independent audit: not yet performed.
