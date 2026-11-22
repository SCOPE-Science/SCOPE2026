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

Run `python3 verify.py` using Python 3's standard library. The script generates all ternary words avoiding adjacent repeats of one or two letters for lengths 4 through 16. It reconstructs every single-coordinate substitution edge, traverses each component independently of the mathematical fiber classification, and tests the exact component multiplicities, independence numbers, and maximum-codebook counts. The completed execution printed `PASS` through length 16, where the graph has 5,922 vertices.

The symbolic all-length proof, including the interior-rigidity argument and the Fibonacci endpoint census, is in RESULT.md. This finite verification does not establish the infinite assertion on its own. No independent audit was performed.
